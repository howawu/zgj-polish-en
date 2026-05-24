---
name: zgj-polish-en
description: Polish, revise, translate, or rewrite English academic paper text in Gongjian Zhou's rigorous IEEE-style writing habits. Use when Codex is asked to polish English LaTeX/manuscript paragraphs for Zhou Gongjian, zgj, Gongjian Zhou, or a supervisor who is strict about details, fixed English sentence patterns, conservative word order, sentence-initial logical connectors, passive, paper-subject, or third-person method statements, radar tracking, target tracking, pseudo-measurement methods, constrained filtering, multiple-model tracking, radar signal processing, DOA/array processing, IEEE TAES/TSP/TITS/JSEE/letter style, abstracts, introductions, methods, experiments, captions, contributions, or reviewer-response prose.
---

# ZGJ English Paper Polishing

## Core Principle

Polish toward rigorous, conservative IEEE paper prose. Prefer correctness, fixed usage, and traceable logic over stylistic freedom. Do not make the text sound creative, idiomatic at all costs, or rhetorically varied if that weakens the expected fixed sentence pattern.

Style imitation is subordinate to technical fidelity. Do not over-ZGJ-ize a sentence if the rewrite changes the claim, hides the actor, breaks a standard IEEE construction, or makes the English unnaturally rigid.

When a requested edit involves a substantial paragraph, first read `references/style-guide.md`.

When the text concerns target tracking, pseudo-measurements, constrained state estimation, range-Doppler estimation, range-squared coordinates, interacting multiple model methods, or track-before-estimate/track-before-detect methods, also read `references/target-tracking-terms.md`.

## Workflow

1. Identify the role of the text: abstract, introduction, problem formulation, method description, experiment analysis, conclusion, caption, or response.
2. Preserve the technical meaning, symbols, claims, assumptions, and comparison scope. Do not add unprovided advantages, limitations, datasets, or results.
3. Convert loose wording into fixed academic patterns:
   - problem/background -> limitation/gap -> proposed method -> implementation detail -> validation;
   - "This paper/article/letter proposes/presents/investigates/develops ...";
   - "is investigated", "is proposed/presented", "is formulated", "is derived", "is utilized/adopted", "is demonstrated";
   - "It is ... that ...", "It can be seen that ...", "It is important to note that ...", "It is assumed that ...";
   - "Simulation/Numerical results demonstrate/validate/illustrate...";
   - "The rest of this paper/article is organized as follows..."
4. Make sentence order conservative. Put the known topic or problem first, then the action, method, and result. Put discourse connectors such as "Therefore", "However", "To address this limitation", "Then", "Moreover", "Furthermore", and "In addition" at the beginning of the sentence by default. Treat this as a strong preference for main logical transitions, not as a mechanical rule for every adverb or local modifier.
5. Tighten detail consistency:
   - keep notation names and hyphenation stable;
   - keep singular/plural and article usage precise;
   - preserve domain terms such as "pseudo-measurement", "base state vector", "augmented state vector", "state transition equation", "measurement equation", "range-Doppler (R-D)", and "range-squared (RS) coordinate";
   - check whether each "this/these/the proposed method" has a clear antecedent;
   - check fixed prepositions and complements such as "be equal to", "be incorporated into", and "the computational time of";
   - place "only" close to the word it modifies, e.g., "used to update only the posterior mean";
   - align "method/approach/algorithm/filter/estimator/model" with the actual object.
6. Prefer moderate-length sentences with explicit logical connectors. Split only when needed for clarity; do not create choppy prose.
7. Return polished text directly. If meaning is ambiguous, include a short note after the text, not before it.

## Style Targets

- Tone: serious, restrained, detail-oriented, and technically exact.
- Voice: passive, paper-subject active, or impersonal active is acceptable. First person is usually avoided in abstracts, contributions, and result claims, but occasional "we" may remain in assumptions or explanatory method text when the manuscript already uses it and a rewrite would become awkward.
- Subject choice: prefer "This paper/article/letter ...", "It is ...", "The problem/method/model/filter/result ...", and passive constructions over unnecessary "we".
- Structure: for abstracts, follow the template "problem/background -> limitation -> In this paper/To address this limitation -> method details -> Simulation results show/demonstrate ...". For other sections, define the problem early; state what is investigated or proposed; then describe how it is formulated/solved; finally state experiments or organization.
- Word choice: prefer established tracking/radar wording over synonyms invented for variety.
- Claims: use "improve", "enhance", "reduce", "achieve", "obtain", "produce", "handle", "deal with", "incorporate", "formulate", "derive", "validate"; avoid inflated verbs such as "revolutionize", "unlock", "empower", or "seamlessly".
- Detail behavior: when unsure, make the sentence more explicit and less elegant.

## Fixed Habits To Respect

- Keep repeated technical nouns repeated when repetition avoids ambiguity. Do not replace every repeated term with synonyms.
- Use conservative connectors: "However", "Therefore", "Furthermore", "In addition", "Specifically", "Based on", "According to", "Compared with".
- Use these connectors mostly sentence-initially. In particular, avoid mid-sentence "therefore" when the sentence can be rewritten as "Therefore, ...". Prefer explicit transition openings such as "However, ...", "To address this limitation, ...", "Then, ...", and "Moreover, ...". Do not force connector movement if it changes scope or makes the sentence less grammatical.
- Prefer "It is ..." patterns when making assumptions, observations, or cautionary statements.
- Treat "This paper/article/letter proposes/presents/investigates/develops ..." as a normal ZGJ-compatible construction, not as a less formal alternative to passive voice.
- Prefer "prior known" only when imitating the local ZGJ corpus; otherwise "known in advance" is safer. Do not alternate both forms within one paragraph.
- Prefer "the proposed method/algorithm/filter" rather than casual "our method" unless the manuscript already uses first person.
- Prefer "the problem of ... is investigated" for problem statements.
- Prefer "a/the + method noun + is proposed/constructed/derived/presented" for contributions and method steps.
- Prefer "simulation results demonstrate/validate/illustrate the effectiveness/superiority" for experimental conclusions.
- Replace polished-but-indirect expressions with hard technical sentence patterns when needed: "embedded explicitly" -> "incorporated into"; "more robustly" -> state the concrete mechanism; "retains a computation time close to" -> "the computational time of ... is close to that of ...".
- Avoid free, literary, marketing-like, or highly native-speaker idioms.
- Do not imitate isolated awkward or erroneous corpus phrases. Give priority to repeated journal-paper patterns over one-off conference-paper wording.

## Output Discipline

For short polish requests, output only the revised paragraph.

For larger edits, output:

1. Revised text.
2. Minimal notes only for changed technical assumptions, unresolved ambiguity, or terms that need the user's confirmation.

Do not over-explain grammar unless the user asks.
