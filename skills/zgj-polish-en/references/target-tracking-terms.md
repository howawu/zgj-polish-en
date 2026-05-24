# Target Tracking And Pseudo-Measurement Terms

Use this reference when polishing target tracking, constrained filtering, pseudo-measurement, range-Doppler, range-squared coordinate, IMM/MM, track-before-estimate, or radar measurement-model text. The patterns are distilled mainly from local ZGJ papers coauthored with Zhuanhua Zhang and Keyi Li, plus closely related ZGJ tracking papers.

## General Rule

Preserve technical nouns more strictly than ordinary style. In this domain, synonym variation often changes the object:

- "state" is not always interchangeable with "estimate".
- "filter", "estimator", "algorithm", "method", "model", and "approach" should match the source object.
- "measurement", "pseudo-measurement", "converted measurement", "monopulse ratio measurement", and "observation" should not be swapped for variety.
- "base state vector", "augmented state vector", "pseudostate vector", and "target state vector" denote different constructions.
- "incorporate", "augment", "formulate", "construct", "derive", "convert", "initialize", and "integrate into" are preferred technical verbs.

Do not replace repeated technical nouns with pronouns if the antecedent may become unclear.

## Pseudo-Measurement And Constrained Filtering

Preferred fixed patterns:

- "state estimation with equality constraints"
- "the equality-constrained filtering problem"
- "constrained estimates"
- "the constraint surface"
- "the heading constraint imposed by the road/linear road segment/circular road segment"
- "the constraint is formulated as ..."
- "the constraint relationship is rewritten to construct a pseudo-measurement"
- "pseudo-measurements are constructed to incorporate the constraint into the estimator"
- "the measurement vector is augmented with/by the pseudo-measurement"
- "the pseudo-measurement is augmented into the measurement vector"
- "the constrained filtering problem is converted into a regular/common filtering problem"
- "the physical measurements are uncorrelated with the pseudo-measurements"
- "the pseudo-measurement is noise-free" or "the pseudo-measurements are equal to zero"
- "the measurement noise covariance matrix is augmented accordingly"

Use "pseudo-measurement" for one constructed constraint equation and "pseudo-measurements" for multiple equations. Do not change it to "pseudo observation", "virtual measurement", "fake measurement", or "auxiliary signal" unless the manuscript defines a different term.

Prefer:

- "A pseudo-measurement is constructed according to the equality constraint."
- "The pseudo-measurement is used to augment the original measurement vector."
- "In this manner, the state estimation problem with the heading constraint is converted into a regular filtering problem."
- "The EKF is utilized to deal with the nonlinearity in the state-to-measurement relationship."

Avoid:

- "The constraint is embedded explicitly in the filter."
- "A fake observation is added to the filter."
- "The constraint is injected into the algorithm."
- "The method leverages the road boundary in a robust way."

## State Augmentation And Constraint Formulation

For Zhang/Keyi Li style constrained tracking text, preserve these distinctions:

- "base state vector"
- "augmented state vector"
- "state augmentation"
- "parameter augmentation"
- "the states at the past time step are used to augment the base state vector"
- "the y-intercept of the constraint straight line is augmented into the state vector"
- "the heading constraint is formulated by the elements of the augmented state vector"
- "the direction of the target trajectory is known in advance" or, when imitating the corpus closely, "is prior known"
- "only part of the trajectory information is available"
- "the conventional constrained estimation methods cannot be used"

Use "augment ... into the state vector" and "augment the state vector by/with ..." carefully:

- "the parameter is augmented into the state vector"
- "the base state vector is augmented by the parameter"
- "the measurement vector is augmented with the pseudo-measurement"

Do not blur "state augmentation" and "measurement augmentation". The state vector is augmented to formulate unknown parameters or past states; the measurement vector is augmented to incorporate pseudo-measurements.

## Target Tracking Fixed Terms

Preferred terms and collocations:

- "target state estimation"
- "target tracking"
- "maneuvering target tracking"
- "tracking performance"
- "estimation accuracy and consistency"
- "state prediction and filtering update"
- "state transition equation"
- "measurement equation"
- "state vector at time step k"
- "process noise" and "measurement noise"
- "zero-mean white Gaussian process/measurement noise"
- "known covariance"
- "range and azimuth measurements"
- "range-Doppler (R-D) estimates"
- "Cartesian coordinates", "polar coordinates", and "sensor coordinates"
- "nearly constant velocity (NCV)"
- "nearly constant acceleration (NCA)"
- "nearly coordinated turn (NCT)"
- "constant turn (CT)"
- "interacting multiple model (IMM) estimator"
- "multiple-model (MM) method"

Preferred result patterns:

- "Simulation results demonstrate the effectiveness of the proposed method."
- "Numerical experiments are conducted to evaluate the performance of the proposed method."
- "The proposed method achieves superior estimation accuracy and consistency."
- "The performance of the proposed method is superior to that of ..., and comparable with that of ..."

## Range-Squared Coordinate And R-D Estimation

For Keyi Li range-squared coordinate papers, preserve the technical vocabulary:

- "range-squared (RS) coordinate"
- "range-Doppler (R-D) measurements/estimates"
- "pseudostate vector"
- "linear time-evolution equations of pseudostate"
- "motion modeling in the RS coordinate"
- "converted measurement Kalman filter (CMKF)"
- "decorrelated unbiased converted measurement (DUCM)"
- "scaled unscented transformation"
- "the pseudostate estimate is converted into the R-D plane"
- "the propagation of nonlinearity approximation errors"
- "the observability of the pseudostate is guaranteed/verified"
- "the motion model accurately describes the time-evolution of pseudostate"

Prefer:

- "Pseudostate vectors are defined in the RS coordinate, and linear pseudostate equations are derived."
- "The motion models are incorporated into the CMKF to extract R-D estimates from converted measurements."
- "The conversion is performed outside the estimation recursions to avoid the propagation of nonlinearity approximation errors."

Avoid turning "pseudostate" into "pseudo-state" unless the manuscript already uses that spelling.

## Revisit Interval And Space-Time Joint Processing

For rotating radar tracking text, use:

- "revisit interval"
- "prior known revisit interval" when closely imitating the corpus; otherwise "revisit interval known in advance"
- "antenna scanning period"
- "mechanically steered rotating radar"
- "the revisit interval depends on the antenna rotation and target states"
- "the state transition with revisit interval uncertainty"
- "state prediction and filtering operations"
- "space-time joint processing (STJP)"
- "Newton-Raphson iteration"
- "the revisit interval and predicted state are calculated simultaneously"
- "the UKF is utilized/adopted to deal with the nonlinear filtering problem"
- "the antenna scanning period is approximated as the revisit interval"

Do not use loose alternatives such as "refresh time", "radar revisit time" or "scan gap" unless the source defines them.

## Track-Before-Estimate And Multipath

For Keyi Li/ZGJ low-elevation target tracking with multipath:

- "track-before-estimate (TBE)"
- "track-after-estimate strategy"
- "low-elevation target tracking"
- "multipath effect"
- "specular reflection assumption"
- "monopulse ratio"
- "monopulse ratio measurement"
- "elevation angle measurement"
- "angle discrimination curve"
- "reflection coefficient"
- "the real and imaginary parts of the monopulse ratio"
- "an accurate measurement equation is established"
- "the relationship between the monopulse ratio and the Cartesian state"
- "the filter initialization issue"
- "one monopulse ratio measurement may correspond to multiple initial height estimates"
- "a multiple subfilter strategy is proposed"
- "the bisection method is utilized to find possible height estimates"

Preferred contrast pattern:

- "The monopulse ratio is employed rather than the elevation angle as the measurement in the tracking process."
- "This enables the transformation from the traditional track-after-estimate strategy to the track-before-estimate strategy."

Avoid calling the monopulse ratio an "angle" when the text distinguishes the ratio from the elevation angle estimate.

## Multiple-Model And Maneuvering-Parameter Terms

For IMM/MM and maneuvering target tracking papers:

- "motion-mode uncertainty"
- "maneuvering parameter"
- "maneuvering parameter jumps"
- "mode jumps"
- "model set"
- "model-conditioned estimates"
- "elemental filters"
- "state mixing process" or "mixing process"
- "maneuver sojourn segments"
- "model matching"
- "matching coverage"
- "parameter initialization"
- "Gaussian mixture"
- "partial state interaction strategy"
- "models with the same structure"
- "models of different structures"
- "the best-initialized filter"
- "state components common to all models"
- "maneuvering-parameter-specific state components"

Prefer:

- "The model set is designed to cover the possible maneuvering parameter space."
- "The partial state interaction strategy prevents the best-initialized filter from being affected by false maneuvering parameter estimates."
- "The maneuvering parameter is initialized using a Gaussian pdf/Gaussian mixture."

Avoid:

- "the best model is protected from bad models"
- "the parameter jumps randomly everywhere"
- "models talk to each other"

## Article And Preposition Checks

These papers are sensitive to small article/preposition choices. Prefer:

- "incorporated into the estimator/filtering framework"
- "augmented into the state vector"
- "augmented with/by the pseudo-measurement"
- "formulated as a function of ..."
- "converted into a regular filtering problem"
- "in the framework of the UKF/IMM"
- "with respect to ..."
- "corresponding to ..."
- "in terms of estimation accuracy and consistency"
- "compared with ..."
- "superior to that of ..."
- "comparable with that of ..."

Check "only" placement:

- Use "used to update only the posterior mean" when the restriction is on what is updated.
- Use "only the direction of the target trajectory is known in advance" when the restriction is on available trajectory information.

## Conservative Rewrite Examples

Loose:

"We add a pseudo measurement so the filter can use the road constraint."

ZGJ-style:

"A pseudo-measurement is constructed to incorporate the road constraint into the filtering framework."

Loose:

"The state is expanded by old states, and then the filter handles it."

ZGJ-style:

"The states at the past time step are used to augment the base state vector, and the corresponding pseudo-measurement is constructed to convert the constrained filtering problem into a regular filtering problem."

Loose:

"The RS model avoids nonlinear errors."

ZGJ-style:

"The linear pseudostate model in the RS coordinate avoids the propagation of nonlinearity approximation errors between filtering recursions."

Loose:

"The monopulse ratio gives better tracking under multipath."

ZGJ-style:

"The monopulse ratio is employed as the measurement in the tracking process to avoid incorporating elevation angle estimation errors arising from the multipath effect."
