from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "zgj-polish-en"
SKILL_MD = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"
STYLE_GUIDE = SKILL_DIR / "references" / "style-guide.md"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def require(path: Path) -> None:
    if not path.exists():
        fail(f"missing required file: {path.relative_to(ROOT)}")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def main() -> None:
    require(SKILL_MD)
    require(OPENAI_YAML)
    require(STYLE_GUIDE)

    skill_text = SKILL_MD.read_text(encoding="utf-8")
    fields = parse_frontmatter(skill_text)
    if fields.get("name") != "zgj-polish-en":
        fail("frontmatter name must be zgj-polish-en")
    if not fields.get("description"):
        fail("frontmatter description is required")
    if "Gongjian Zhou" not in fields["description"] or "fixed English sentence patterns" not in fields["description"]:
        fail("description should preserve the intended trigger coverage")
    if "references/style-guide.md" not in skill_text:
        fail("SKILL.md should point to references/style-guide.md")

    yaml_text = OPENAI_YAML.read_text(encoding="utf-8")
    if "default_prompt:" not in yaml_text or "$zgj-polish-en" not in yaml_text:
        fail("agents/openai.yaml must include a default prompt with $zgj-polish-en")

    guide_text = STYLE_GUIDE.read_text(encoding="utf-8")
    required_patterns = [
        "Therefore,",
        "To address this limitation",
        "used to update only",
        "be equal to",
        "passive",
    ]
    missing = [pattern for pattern in required_patterns if pattern not in guide_text]
    if missing:
        fail(f"style guide is missing expected guidance: {', '.join(missing)}")

    print("zgj-polish-en skill project is valid")


if __name__ == "__main__":
    main()

