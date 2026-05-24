# ZGJ Polish En

An unofficial Codex skill for polishing English academic paper prose in a rigorous, conservative IEEE-style writing pattern associated with ZGJ-style manuscript revision.

The skill is intended for radar, target tracking, constrained estimation, and related engineering papers where the preferred style is formal, detail-oriented, and based on fixed technical sentence patterns rather than free literary rewriting.

## What It Does

- Polishes English academic paragraphs, abstracts, introductions, methods, experiments, conclusions, captions, and reviewer-response text.
- Prefers conservative IEEE-style sentence order.
- Uses explicit sentence-initial logical connectors such as `However`, `Therefore`, `To address this limitation`, `Then`, and `Moreover`.
- Rewrites frequent `we + verb` constructions into passive or third-person forms when appropriate.
- Checks sensitive fixed usages such as `be equal to`, `be incorporated into`, and `used to update only ...`.
- Preserves fixed target-tracking terms such as `pseudo-measurement`, `base state vector`, `augmented state vector`, `range-Doppler (R-D)`, and `range-squared (RS) coordinate`.
- Preserves technical meaning, notation, claims, assumptions, and comparison scope.

## Repository Layout

```text
.
+-- skills/
|   +-- zgj-polish-en/
|       +-- SKILL.md
|       +-- agents/
|       |   +-- openai.yaml
|       +-- references/
|           +-- style-guide.md
|           +-- target-tracking-terms.md
+-- scripts/
|   +-- validate_skill.py
+-- .github/
|   +-- workflows/
|       +-- validate.yml
+-- CONTRIBUTING.md
+-- LICENSE
+-- README.md
```

## Installation

Install with the Codex skill installer from this GitHub repository:

```bash
python C:/Users/Administrator/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo howawu/zgj-polish-en --path skills/zgj-polish-en
```

After installation, restart Codex so the skill can be discovered.

## Usage

Invoke the skill explicitly:

```text
Use $zgj-polish-en to polish this abstract in a rigorous ZGJ-style IEEE paper tone.
```

Or ask naturally:

```text
Polish this paragraph for a strict supervisor who prefers fixed IEEE sentence patterns and conservative wording.
```

## Design Principles

This skill is deliberately not a general "make it native-like" English polisher. It follows a narrower style:

- Prefer fixed technical expressions over creative alternatives.
- Prefer passive or third-person method statements over frequent first-person writing.
- Prefer explicit logical connectors at the beginning of sentences.
- Prefer technical precision and stable terminology over stylistic variation.
- Prefer domain-specific target-tracking and pseudo-measurement terminology over broad synonyms.
- Avoid changing scientific meaning for the sake of style.

## Validation

Run the bundled validator:

```bash
python scripts/validate_skill.py
```

The validator checks the skill frontmatter, required files, metadata, and basic reference links.

## Status

This is an unofficial writing-style helper. It is not affiliated with, endorsed by, or maintained by any journal, institution, or named researcher.
