# ZGJ Style Guide

## Evidence Base

This guide was distilled from sampled Gongjian Zhou coauthored IEEE/TAES/TSP/TITS/JSEE/letter papers in the local `zgj` folder, including work with Zhuanhua Zhang and Keyi Li on heading constraints, range-squared coordinates, and track-before-estimate, plus related work on revisit interval uncertainty, spatiotemporal bias compensation, coherent integration, track-before-detect, DOA and sparse arrays, deep-learning radar detection, and switch-constrained multiple-model smoothing.

## High-Level Pattern

Use a fixed, rigorous progression:

1. State the application background or established method.
2. Point out the uncertainty, limitation, mismatch, or practical violation.
3. Define the exact problem being investigated.
4. State the proposed method in a conservative passive, paper-subject, or method-noun construction.
5. Explain key formulation steps in the order they occur.
6. State experiments and results without overstating novelty.

For abstracts, use this stricter template:

1. Problem/background: state the estimation, detection, filtering, or modeling problem.
2. Limitation: introduce the difficulty using "However, ..." or "This ... makes ..."
3. Paper action: use "In this paper, ..." or "To address this limitation, ..."
4. Method details: use passive/third-person constructions, such as "is formulated", "is constructed", "is derived", "is incorporated", and "is analyzed".
5. Results: end with "Simulation results show/demonstrate ..." or "Numerical experiments are conducted to ..."

Typical opening structures:

- "The problem of ... is considered/investigated."
- "This paper/article/letter proposes/presents/investigates/develops ..."
- "In this paper/article, ... is investigated, and ... is presented."
- "To deal with ..., a ... method is proposed/presented."
- "To address this limitation, ..."
- "Based on ..., the ... problem is converted into/formulated as ..."
- "Simulation/Numerical results demonstrate/validate/illustrate ..."

## Sentence-Order Rules

ZGJ-style prose is strict about English order and does not favor free rearrangement.

- Put the technical topic first: problem, method, model, measurement, state vector, filter, or experiment.
- Then state the operation: is formulated, is derived, is augmented, is incorporated, is solved, is utilized.
- Then state the purpose/result: to handle nonlinearity, to improve accuracy, to produce estimates, to validate effectiveness.
- Put discourse connectors at the beginning of the sentence when possible: "Therefore, ...", "However, ...", "To address this limitation, ...", "Then, ...", "Moreover, ...", "Furthermore, ...", "In addition, ...". Avoid more flexible inserted forms such as "... and, therefore, ..." or "... is therefore ..." unless they are needed for grammar.
- Prefer impersonal or paper-subject subjects over author subjects. Rewrite unnecessary "we propose", "we can see", and "we assume" as "a ... is proposed", "It can be seen that ...", and "It is assumed that ...". Keep occasional "we" only when it is already part of the manuscript's local exposition and replacing it would make the sentence more awkward or less precise.
- Use method-noun subjects with fixed verbs: "a method is proposed", "two pseudo-measurements are constructed", "an augmented system is derived", "the role of ... is analyzed", and "simulation results show ...".
- Use paper-subject active voice as a corpus-consistent alternative: "This paper proposes ...", "This article presents ...", "This letter investigates ...", and "This work develops ...".
- Avoid sentences that begin with abstract evaluation words, broad rhetorical phrases, or creative hooks.
- Avoid excessive participial openings unless they are standard: "Based on ...", "According to ...", "Compared with ...".

Prefer:

- "The measurement equation is formulated as a function of both target states and sensor biases."
- "A bias fusion approach with feedback is presented to improve the compensation performance."
- "This article presents a systematic solution to the state prediction and filtering problem."
- "Therefore, the conventional filtering method cannot be directly applied."
- "To address this limitation, a pseudo-measurement-based filter is proposed."
- "Then, the pseudo-measurement is incorporated into the filtering framework."
- "Moreover, the computational cost is analyzed."
- "It is important to note that the revisit interval is not necessarily constant."

Avoid:

- "By cleverly fusing feedback, the algorithm unlocks better compensation."
- "Accurate compensation becomes possible through an elegant feedback design."
- "The conventional filtering method, therefore, cannot be directly applied."
- "We note that the revisit interval is not necessarily constant."
- "We revisit the modeling of the constraint."
- "The boundary information is embedded explicitly in the filtering model."
- "The method combines the boundary information more robustly."
- "It retains a computation time close to ..."

## Detail-Oriented Revision Checklist

Apply this checklist before final output:

- Verify every acronym is introduced or already known in the supplied text.
- Keep notation, capitalization, and hyphenation stable: "state vector", "time stamp", "revisit interval", "pseudo-measurement", "range-Doppler", "space-time joint processing".
- Do not change "filter", "estimator", "algorithm", "method", "model", and "approach" interchangeably unless the source clearly allows it.
- Check whether "which" modifies the intended noun.
- Prefer explicit antecedents over vague "this".
- Ensure "respectively" matches parallel listed items exactly.
- Ensure "based on" attaches to the correct object.
- Avoid stacked nouns if they obscure the relation; keep common IEEE compounds if they are standard in the field.
- Keep comparison conditions precise: "compared with existing methods", "compared with the standard UKF", "in terms of estimation accuracy and consistency".
- Do not introduce claims such as optimality, robustness, online capability, real-time capability, or low complexity unless they are in the source.
- Check sensitive fixed usages:
  - Prefer "be equal to a deterministic constant/value" over "equal a deterministic constant".
  - Prefer "be directly incorporated into recursive Bayesian filtering" over "incorporate directly into recursive Bayesian filtering".
  - Prefer "used to update only the posterior mean" over "used only to update the posterior mean" when the intended restriction is on the object updated.
  - Prefer "the computational time of the proposed filter" or "the computation time of the proposed filter" over "a computation time".
  - Prefer "that of ..." for parallel comparisons: "close to that of the projection-based filter and lower than that of UKF-LMI".
  - Prefer a stable noun phrase over a pronoun if "it" can refer to more than one object.
- Apply a corpus-quality filter: stable patterns repeated across journal papers are stronger evidence than isolated awkward phrases from conference papers or early drafts.
- Do not convert every active "This paper/article ..." sentence into passive voice. If the paper-subject construction is clear and standard, it is already compatible with the style.

## Preferred Fixed Expressions

Problem and motivation:

- "The problem of ... has been studied/investigated in recent years."
- "This paper/article considers/investigates ..."
- "However, in practical applications, ..."
- "Therefore, ..."
- "This assumption may be violated in real systems."
- "In this case, the conventional ... methods cannot be directly used."
- "To overcome the aforementioned shortcomings, ..."
- "To address this limitation, ..."
- "To deal with ..., ..."
- "It is important to notice/note that ..."
- "It can be seen that ..."
- "It is clear that ..."
- "It is assumed that ..."

Method statement:

- "It is assumed that ..."
- "A ... method/algorithm/filter is proposed/presented."
- "This paper/article/letter proposes/presents a ... method/algorithm/filter."
- "A ... pseudo-measurement is constructed."
- "An augmented ... system/model/equation is derived."
- "The ... is formulated as ..."
- "The ... is augmented in the state vector."
- "The ... is incorporated into the estimator by constructing pseudo-measurements."
- "The ... is solved using ..."
- "The ... is utilized/adopted to handle the nonlinearity."

Contribution statement:

- "The main contributions of this work are summarized as follows."
- "The contributions of this paper/article can be summarized as follows."
- "First, ... is formulated/derived."
- "Second, ... is presented/developed."
- "Third, ... is integrated/embedded into ..."

Experiment statement:

- "Numerical experiments are conducted to evaluate the performance of the proposed method."
- "Simulation results demonstrate the effectiveness of the proposed method."
- "Simulation results show that ..."
- "Experimental results illustrate the superiority of the proposed method."
- "The proposed method achieves superior estimation accuracy and consistency."
- "The performance of ... is superior to that of ..., and comparable with that of ..."

## Abstract-Specific Rewrites

Free or polished:

"Existing methods therefore often rely on auxiliary procedures."

ZGJ-style:

"Therefore, existing methods often rely on auxiliary procedures."

Free or polished:

"We revisit the modeling of interval constraints and show that interval feasibility can be represented by an equality relation."

ZGJ-style:

"In this paper, the modeling of interval constraints is revisited, and interval feasibility is represented by an equality relation."

Also acceptable when the paper-subject style is more direct:

"This paper revisits the modeling of interval constraints and represents interval feasibility by an equality relation."

Free or polished:

"We construct a noise-free pseudo-measurement and augment it with the original measurement."

ZGJ-style:

"A noise-free pseudo-measurement is constructed and augmented with the original measurement."

Free or polished:

"We then analyze the role of the pseudo-measurement in the UKF."

ZGJ-style:

"Then, the role of the pseudo-measurement in the UKF is analyzed."

Free or polished:

"A monotonic pseudo-measurement is therefore developed to combine the two-sided boundary information more robustly."

ZGJ-style:

"To address this issue, a monotonic pseudo-measurement is developed, so that the contributions from the two boundaries are accumulated rather than canceled."

Free or polished:

"It retains a computation time close to projection-based filtering and more than two orders of magnitude lower than UKF-LMI."

ZGJ-style:

"The computational time of the proposed filter is close to that of the projection-based filter and is more than two orders of magnitude lower than that of UKF-LMI."

Paper organization:

- "The rest of this paper/article is organized as follows."
- "Section II presents/states ..."
- "Section III introduces/derives ..."
- "Simulation results are presented in Section IV."
- "Finally, Section V concludes this paper/article."

## Common Rewrites

Loose:

"We design a new method to solve the problem, and it works better in simulations."

ZGJ-style:

"To solve this problem, a new method is proposed. Numerical simulation results demonstrate that the proposed method achieves better performance than the existing methods."

Loose:

"We therefore formulate the problem as a filtering problem."

ZGJ-style:

"Therefore, the problem is formulated as a filtering problem."

Loose:

"We can see that the interval is time-varying."

ZGJ-style:

"It can be seen that the interval is time-varying."

Loose:

"We assume that the radar is located at the origin."

ZGJ-style:

"It is assumed that the radar is located at the origin."

Loose:

"The sensor timestamps are unreliable, so fusion becomes hard."

ZGJ-style:

"When the time stamps cannot be used as reliable time references, proper fusion of multisensor measurements becomes difficult, and the problem of temporal bias should be considered."

Loose:

"Our algorithm uses UKF because the model is nonlinear."

ZGJ-style:

"The UKF is adopted to handle the nonlinearity in the state transition and measurement update."

Loose:

"We propose a filter and test it in simulations."

ZGJ-style:

"In this paper, a filter is proposed and evaluated by numerical simulations."

Also acceptable:

"This paper proposes a filter and evaluates it by numerical simulations."

Loose:

"The technique is fast and robust."

ZGJ-style:

"The proposed method reduces the computational burden while maintaining the integration performance."

Loose:

"The constraint is hard to incorporate directly into the filter because it does not equal a deterministic value."

ZGJ-style:

"The constraint is difficult to be directly incorporated into the filter because it is not equal to a deterministic value."

## What To Avoid

- Do not rewrite into highly polished but unfamiliar native-speaker prose if it departs from fixed IEEE phrasing.
- Do not use marketing verbs, metaphors, rhetorical questions, or strong adjectives without evidence.
- Do not vary technical terms for style.
- Do not favor smooth expressions over fixed technical patterns. Expressions such as "On this basis", "embedded explicitly", "more robustly", "statistical cancellation", and "retains a computation time close to" should be checked and replaced when a more direct technical construction is available.
- Do not compress away important conditions, assumptions, or comparison baselines.
- Do not replace all passive constructions with active voice.
- Do not normalize sentence-initial "Therefore/However/Furthermore/In addition" into more flexible mid-sentence connector placement.
- Do not introduce frequent "we" subjects unless the existing manuscript explicitly adopts first-person style.
- Do not treat occasional "we" in sampled papers as permission to rewrite abstracts or contribution lists in a first-person style.
- Do not remove standard "This paper/article/letter ..." subjects merely to maximize passive voice.
- Do not imitate isolated awkward expressions such as "quite rigorous", "extant", or unnatural article/preposition choices if a conservative IEEE expression is available.
- Do not make every sentence short; ZGJ-style often uses carefully structured compound sentences.
