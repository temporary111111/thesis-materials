# MASTER HANDOFF V2 — PicAIsso Thesis Project
## Complete continuity document for another AI

**Last updated:** August 9, 2026  
**Project:** Undergraduate Computer Science Thesis 1  
**Proposal status:** Already submitted to professor  
**Working title:**  
**PicAIsso: Cross-Detector Reliability Prediction from Ordered Mobile-Degradation Response Curves for Selective AI-Generated Image Detection**

---

# 1. READ THIS FIRST — SIMPLE VERSION

If you are the next AI, this is the most important context.

The user is developing a Computer Science thesis called **PicAIsso**.

The thesis does **not** primarily try to make a new AI-generated-image detector.

Instead, it asks:

> **Can we tell when an existing AI-image detector is probably wrong by observing how its output score changes when the image is progressively degraded?**

And the most important research question is:

> **Can a reliability model learned from some AI-image detectors still work on another detector that was not used to train that reliability model?**

Example:

An AI-image detector originally outputs:

\[
0.95
\]

Then the same image is progressively processed:

\[
0.95
\rightarrow
0.88
\rightarrow
0.62
\rightarrow
0.41
\]

PicAIsso studies whether that score behavior can indicate:

> “The original detector prediction may be unreliable.”

The system then either:

- accepts the detector's original AI/real answer; or
- returns **Inconclusive**.

It does **not** use the transformed versions to automatically change the original AI/real prediction.

---

# 2. CURRENT OVERALL VERDICT

After several independent and intentionally adversarial literature-research passes:

## Exact duplicate found?

**No exact duplicate was located.**

## Are all individual ideas novel?

**No.**

Almost every broad component has prior art:

- transformed-image confidence estimation;
- black-box error prediction;
- test-time augmentation confidence;
- sequential/composed degradation;
- degradation response trajectories;
- AI-image detector reliability;
- selective classification/abstention;
- output-score changes under perturbations;
- generic architecture-agnostic failure prediction.

## Does the thesis still appear to have a research gap?

**Yes.**

The strongest surviving research gap is:

> **Whether the stage-by-stage output-score behavior of a frozen AI-generated-image detector under cumulative, label-preserving mobile-style degradations contains a correctness signal that can be learned from other detectors and transferred unchanged to a held-out detector without using detector-internal features or labeled target-detector errors.**

## Recommendation

**KEEP THE TOPIC.**

But:

- revise the novelty wording;
- improve several experimental controls;
- reconsider or soften the detector-architecture-diversity claim;
- run the planned pilot before locking the final experiment.

---

# 3. IMPORTANT NOTE ABOUT CERTAINTY

The user has strong concerns about accidentally choosing a thesis that already exists.

Do not provide fake certainty.

No literature search can prove:

> “Nobody anywhere has ever done this.”

Possible unseen work includes:

- unpublished theses;
- papers under review;
- unindexed manuscripts;
- internal research;
- papers published after the search date.

The correct statement is:

> **After several aggressive literature searches, no located primary work appears to subsume the complete PicAIsso experiment.**

That is the appropriate standard.

---

# 4. WHAT THE THESIS ACTUALLY PREDICTS

For detector \(d\):

\[
s_{d,0}=f_d(x)
\]

where \(x\) is the original image.

The detector produces its original class:

\[
\hat y_d.
\]

The dataset has ground truth:

\[
y.
\]

The PicAIsso reliability target is:

\[
z_d =
\begin{cases}
1,& \hat y_d=y\\
0,& \hat y_d\neq y
\end{cases}
\]

Therefore PicAIsso predicts:

\[
P(z_d=1)
\]

or conceptually:

> **Probability that the detector's original answer is correct.**

It is **not directly another**

\[
P(\text{AI-generated})
\]

classifier.

This distinction must always be preserved.

---

# 5. ORIGINAL SYSTEM BEHAVIOR

The web prototype is intended to:

1. accept one still-image upload;
2. validate and decode it;
3. send the original image to a frozen AI-image detector;
4. save the detector's original continuous score and original class;
5. generate controlled diagnostic image versions;
6. query the same detector on those versions;
7. analyze the resulting score behavior;
8. estimate whether the original detector prediction is reliable;
9. either:
   - show the original result; or
   - output **Inconclusive**.

Suggested wording:

- “Likely AI-generated according to the tested detector”
- “Likely camera-captured according to the tested detector”
- “Inconclusive”

The system must not claim:

- authenticity;
- fraud;
- truth of the depicted event;
- legal proof;
- forensic certainty.

---

# 6. BLACK-BOX / OUTPUT-ONLY RULE

The intended reliability wrapper may use only:

\[
\text{image input}
\rightarrow
\text{continuous detector output score}.
\]

It should not inspect:

- weights;
- gradients;
- embeddings;
- intermediate feature maps;
- training losses;
- detector training data.

This matters because some close prior works use internal detector features.

---

# 7. ORIGINAL DIAGNOSTIC PATH IDEA

The proposal suggested approximately three cumulative paths.

## Path 1 — resize/recompression

Original

→ resize

→ JPEG 85

→ JPEG 65

## Path 2 — low-bandwidth style

Original

→ downsample/up-sample

→ WebP 80

→ JPEG 70

## Path 3 — crop/repost style

Original

→ approximately 90% crop

→ resize

→ JPEG 70

Together with the identity/original image, around **10 views per root image** were proposed.

These paths must be described as:

> **platform-agnostic mobile/reposting-style processing paths**

and not exact Facebook, Messenger, WhatsApp, etc. simulations unless actual platform measurements support such claims.

---

# 8. STAGE-RESOLVED CUMULATIVE TRAJECTORY

This is now the preferred conceptual framing.

Start with:

\[
x_0=x
\]

Then:

\[
x_1=T_1(x_0)
\]

\[
x_2=T_2(x_1)
\]

\[
x_3=T_3(x_2).
\]

The frozen detector returns:

\[
s_0=f(x_0)
\]

\[
s_1=f(x_1)
\]

\[
s_2=f(x_2)
\]

\[
s_3=f(x_3).
\]

PicAIsso therefore has access to:

\[
[s_0,s_1,s_2,s_3].
\]

The important idea is **not simply that transforms are composed**.

The potentially useful information is:

> **the detector's intermediate score evolution throughout the cumulative path.**

Preferred terminology:

> **stage-resolved cumulative degradation-response trajectory**

instead of relying heavily on:

> “ordered transformations.”

---

# 9. POSSIBLE TRAJECTORY FEATURES

Original proposal included:

- original score margin;
- stage-to-stage change;
- normalized change;
- slope;
- curvature;
- area;
- worst margin;
- first class reversal;
- number of reversals;
- monotonicity violations;
- recovery after confidence drop;
- disagreement among degradation paths.

Important terminology correction:

For mixed operations such as:

crop → resize → JPEG,

do not imply that “slope” and “curvature” are physical continuous derivatives.

Use:

> **first-order finite difference along the fixed processing path**

and:

> **second-order finite difference along the fixed processing path**

where appropriate.

“Path area” should be described as an ordinal/path-index summary.

---

# 10. PROPOSED RELIABILITY MODELS

Primary:

- L2-regularized logistic regression;
- shallow XGBoost.

Possible exploratory model:

- small MLP.

The thesis novelty is **not XGBoost**.

The core contribution is the reliability representation, transfer hypothesis, and experimental protocol.

---

# 11. MAIN DATASET

Primary:

**GenImage**

Planned approximately:

- 12,000 root images;
- ~6,000 generated;
- ~6,000 real.

Generator-disjoint split concept:

- 5 generator subsets for development;
- 1 generator subset for validation;
- 2 generator subsets for untouched final testing.

Exact assignments should be fixed before examining final results.

Data hygiene:

- exact SHA-256 duplicate detection;
- perceptual duplicate screening;
- related real images grouped;
- original image and all derivatives kept in one partition;
- metadata excluded;
- filenames excluded;
- folder paths excluded;
- EXIF excluded;
- file-extension shortcuts excluded.

Experimental unit:

> **root image**

not transformed derivative.

---

# 12. EXTERNAL AUDIT

Planned:

**Synthbuster**

with

**RAISE / RAISE-1k real photographs.**

Each generated-source subset should preferably be evaluated separately with the real reference collection rather than falsely treating repeated reuse of the same real images as statistically independent evidence.

Potential optional extensions:

- NTIRE;
- AncesTree;
- ReWIND;
- newer degradation benchmarks.

---

# 13. ORIGINAL DETECTOR PLAN

The proposal preferred:

1. UniversalFakeDetect
2. NPR
3. SAFE

This detector selection needs special attention.

---

# 14. IMPORTANT DETECTOR ARCHITECTURE FINDING

A later code-level review found:

## UniversalFakeDetect

Uses a CLIP/ViT-family representation.

This is clearly structurally different from the other two.

## NPR

Uses neighboring-pixel residual preprocessing and a ResNet-style CNN detector.

## SAFE

Uses frequency/DWT/transformation-oriented preprocessing but also uses a closely related ResNet-style CNN architecture.

Therefore:

> **NPR and SAFE are different forensic mechanisms, but they should not casually be described as two completely unrelated architecture families.**

This creates a problem for a strong claim such as:

> “three architecturally different detectors.”

Recommended options:

### Better option

Replace either NPR or SAFE with a public detector from a genuinely different architecture family.

### Even better if compute permits

Add a fourth detector.

### If keeping all three

Use cautious wording:

> **“three detector mechanisms, including a CLIP/ViT-based detector and two CNN/ResNet-family forensic detectors.”**

Or:

> **“cross-detector transfer, including at least one clear cross-architecture-family held-out condition.”**

Do not overclaim architectural diversity.

---

# 15. CROSS-DETECTOR EXPERIMENT

For detectors A, B, C:

Train reliability estimator using:

\[
A+B.
\]

Then test the unchanged reliability estimator on:

\[
C.
\]

Repeat:

\[
A+C\rightarrow B
\]

and:

\[
B+C\rightarrow A.
\]

Ideally run all three leave-one-detector-out folds.

Do not select only successful folds.

Within-detector comparisons may also be reported:

\[
A\rightarrow A
\]

\[
B\rightarrow B
\]

\[
C\rightarrow C.
\]

These act as an upper bound/reference.

---

# 16. THE MOST IMPORTANT RESEARCH QUESTION

The thesis can be summarized as:

> **Does degradation-response error geometry transfer between frozen AI-generated-image detectors?**

More understandable version:

> **Can the way an AI-image detector reacts while an image is progressively degraded tell us when that detector is wrong, and can that learned pattern still work for another unseen detector?**

---

# 17. WHAT DEEP RESEARCH ROUND 1 FOUND

The first major literature review established that the broad idea:

> transformed versions → classifier outputs → prediction correctness

already exists.

The key paper was:

**Bahat & Shakhnarovich (2018), Confidence from Invariance to Image Transformations.**

They already use transformed classifier responses to learn whether an original classifier prediction is correct.

Therefore PicAIsso cannot claim:

> “First method to predict classifier correctness using transformed outputs.”

Round 1 also found existing synthetic-image reliability/selective-classification work.

Examples:

- ReSIDe;
- DACOM;
- Maier & Riess;
- Yumlembam et al.

Therefore PicAIsso cannot claim:

> “First uncertainty-aware AI-image detector.”

or

> “First abstaining AI-image detector.”

However, the exact cross-detector transfer setup still appeared unresolved.

---

# 18. WHAT DEEP RESEARCH ROUND 2 FOUND

Round 2 intentionally searched for papers that could destroy the novelty.

It found strong prior art for:

- sequential degradation;
- progressive processing;
- repeated reposting-like transformations;
- model self-awareness using degradation.

Therefore this broad novelty claim was rejected:

> “PicAIsso is novel because it uses sequential/cumulative degradation.”

Sequential degradation itself is not new.

---

# 19. WHAT DEEP RESEARCH ROUND 3 FOUND

Round 3 searched adjacent terminology such as:

- failure prediction;
- correctness estimation;
- perturbation response;
- response trajectory;
- degradation fingerprint;
- cross-model confidence;
- transferable error prediction.

It found existing work using:

- response curves;
- trajectory features;
- area/change/knee descriptors;
- output changes under perturbation;
- generic model-agnostic failure prediction.

Therefore these broad claims were also rejected:

> “First response-curve method.”

> “First use of score changes as reliability.”

> “First architecture-agnostic failure predictor.”

Still, the exact AIGI cross-detector correctness-transfer experiment was not located.

---

# 20. WHAT FINAL DEEP RESEARCH FOUND

The final research pass was deliberately adversarial.

Its conclusion was:

> **Nearly every individual ingredient of PicAIsso has prior art, but the complete combination still appears unresolved.**

The surviving combination is:

1. frozen AI-generated-image detector;
2. output-score-only black-box interface;
3. controlled label-preserving degradation;
4. cumulative path;
5. intermediate score stages preserved;
6. target is whether the original detector prediction is correct;
7. reliability model learned from other detectors;
8. same reliability model deployed unchanged on held-out detector;
9. no detector-internal features;
10. no labeled target-detector errors under strict transfer;
11. selective accept/abstain rather than changing the original class.

No exact primary work performing the whole combination was located.

---

# 21. BAHAT 2018 — FUNDAMENTAL PRIOR ART

**Confidence from Invariance to Image Transformations**

This is one of the most important papers for the thesis.

Broad structure:

\[
\text{transformed copies}
\rightarrow
\text{classifier outputs}
\rightarrow
\text{predict correct/error}.
\]

Therefore do not hide or minimize this paper.

It should be treated as a mandatory conceptual baseline.

---

# 22. BAHAT 2020 — MAJOR FINAL-PASS CORRECTION

**Classification Confidence Estimation with Test-Time Data-Augmentation**

Important discovery:

Bahat 2020 already includes transformations that are applied **consecutively/compositionally**.

Therefore this statement is unsafe:

> “Other work uses independent transformations; ours uniquely composes them.”

The real PicAIsso distinction is narrower:

Bahat may use:

\[
T_3(T_2(T_1(x)))
\]

as one transformed version.

PicAIsso explicitly retains:

\[
f(x)
\]

\[
f(T_1(x))
\]

\[
f(T_2(T_1(x)))
\]

\[
f(T_3(T_2(T_1(x))))
\]

and models the **intermediate evolution**.

Therefore future novelty wording should emphasize:

> **stage-resolved cumulative response**

not merely:

> **composition.**

---

# 23. ReSIDe 2026

ReSIDe already performs:

- selective classification;
- synthetic-image detector reliability;
- abstention;
- AURC/risk-coverage evaluation;
- post-hoc confidence estimation.

But it relies on:

> **intermediate detector-layer features/confidences.**

That is different from the PicAIsso black-box requirement.

Therefore ReSIDe is a close white-box comparison, not an exact duplicate.

---

# 24. DACOM 2026

DACOM estimates how trustworthy a forensic detector is under distortions.

It uses:

- detector-internal forensic features;
- image-quality descriptors;
- distortion features.

Important distinction:

Its multi-detector setup equips detectors with detector-specific DACOM confidence models.

It does not appear to demonstrate:

\[
R_{A+B}\rightarrow C
\]

using one unchanged correctness model on a new detector.

Thus the PicAIsso transfer question remains different.

---

# 25. QuAD 2026

QuAD studies real-world quality/degradation and repeated image versions in AI-generated-image detection.

It includes degradation/reposting behavior such as:

- resizing;
- cropping;
- recompression.

Therefore:

> “reposting-style progressive degradation is novel”

is false.

However, QuAD primarily improves/calibrates the **real-vs-AI decision itself**, rather than predicting whether another frozen detector's original decision is correct.

---

# 26. GlobalForge / RealDeg-Bench 2026

GlobalForge includes:

> **multi-step compound degradation chains**

for robust AI-generated-image detection.

Therefore compound/sequential degradation alone is not PicAIsso's novelty.

---

# 27. Diffusion Snap-Back

This work studies progressive response trajectories for AI-generated-image detection.

It already uses trajectory-style quantities such as:

- area under curve;
- change across stages;
- knee/threshold behavior.

Therefore these ideas cannot be claimed as newly invented by PicAIsso.

But Snap-Back directly predicts:

\[
\text{real vs AI}
\]

rather than:

\[
\text{correct vs incorrect prediction of another frozen detector}.
\]

---

# 28. GenRes / GenRes++

Recent work also studies relationships between original and transformed samples for generalized AIGI detection.

Again:

> transformation response itself is not novel.

But it builds a detector for real-vs-generated classification rather than an output-only correctness estimator around arbitrary frozen detectors.

---

# 29. 2026 OUTPUT-LOGIT RESPONSE STUDY

A recent study examined detector-logit changes after controlled image purification across several detectors.

Important finding:

> detector response behavior can be highly detector-specific.

This creates an important risk for PicAIsso.

The assumption:

\[
P(\text{wrong}\mid\phi_A)
\approx
P(\text{wrong}\mid\phi_B)
\]

may not hold for detector C.

This is not evidence that the thesis is already done.

It shows the main hypothesis is genuinely uncertain.

---

# 30. MetaErr 2026

MetaErr predicts whether a DNN will succeed or fail.

Therefore generic:

> “architecture-agnostic failure prediction”

is not a safe novelty claim.

However, MetaErr does not appear to demonstrate the exact:

\[
A+B\rightarrow C
\]

base-detector transfer setup proposed by PicAIsso.

---

# 31. CLAIMS THAT MUST NOT BE USED

Do not claim any of the following:

### ❌ “First transformation-based confidence method.”

Existing.

### ❌ “First black-box correctness predictor.”

Existing.

### ❌ “First selective AI-generated-image detector.”

Existing.

### ❌ “First uncertainty-aware AI-generated-image detector.”

Existing.

### ❌ “First sequential degradation method.”

Existing.

### ❌ “First composed/cumulative transformation confidence method.”

Unsafe.

### ❌ “First AIGI response-curve method.”

Unsafe.

### ❌ “First to use score changes under transformations.”

Existing.

### ❌ “First architecture-agnostic error predictor.”

Unsafe.

### ❌ “Previous transformation methods only treat views as unordered sets.”

Too weak/inaccurate as a universal statement.

### ❌ “UFD, NPR and SAFE are three completely unrelated architectures.”

Likely inaccurate.

---

# 32. CURRENT STRONGEST NOVELTY STATEMENT

Preferred:

> **PicAIsso investigates whether stage-resolved output-score trajectories generated by cumulative, label-preserving mobile-processing probes can serve as transferable per-instance correctness representations across heterogeneous frozen AI-generated-image detectors. The reliability estimator is trained using source detectors and applied unchanged to a held-out detector without detector-internal features or labeled target-detector errors, and its usefulness is evaluated through selective risk against confidence and transformation-based alternatives.**

Safer academic opening:

> **“To our knowledge, prior work does not establish whether…”**

Do not unnecessarily claim “first ever.”

---

# 33. SIMPLE NOVELTY EXPLANATION FOR THE USER

The user may prefer this explanation:

Existing research already knows that:

> transformations can reveal something about confidence.

Existing research also knows that:

> sequential degradation affects AI detectors.

Existing research even uses:

> response curves and score changes.

What PicAIsso is trying to newly test is:

> **Can the entire stage-by-stage degradation behavior be learned as a detector-error pattern that still works when transferred to another unseen AI-image detector?**

That is the important novelty.

---

# 34. MOST IMPORTANT REQUIRED EXPERIMENT #1
## Stage-resolved trajectory vs endpoint-only composed transform

Because composed transforms already exist in prior work, PicAIsso needs to prove that the intermediate stages add useful information.

Example:

\[
x_0=x
\]

\[
x_1=T_1(x)
\]

\[
x_2=T_2(T_1(x))
\]

\[
x_3=T_3(T_2(T_1(x))).
\]

PicAIsso sees:

\[
[s_0,s_1,s_2,s_3].
\]

Endpoint baseline sees only something equivalent to:

\[
[s_0,s_3].
\]

Question:

> Does knowing the entire journey improve prediction of detector errors?

Desired result:

\[
AURC_{\text{trajectory}}
<
AURC_{\text{endpoint}}.
\]

This is now considered extremely important.

---

# 35. MOST IMPORTANT REQUIRED EXPERIMENT #2
## Cumulative vs independent-from-root

Cumulative:

\[
T_1(x)
\]

\[
T_2(T_1(x))
\]

\[
T_3(T_2(T_1(x))).
\]

Independent:

\[
T_1(x)
\]

\[
T_2(x)
\]

\[
T_3(x).
\]

Use the same or closely matched operations/query budget.

Question:

> Does processing history actually matter, or is ordinary transformation diversity enough?

Desired:

\[
AURC_{\text{cumulative}}
<
AURC_{\text{independent}}.
\]

---

# 36. IMPORTANT CONTROL #3
## History vs endpoint severity

Example:

\[
JPEG65(JPEG85(x))
\]

versus:

\[
JPEG65(x).
\]

Both may end with nominal JPEG 65, but one has prior compression history.

This helps determine whether the model learns:

> cumulative processing history

rather than merely:

> final quality/severity.

---

# 37. IMPORTANT BASELINE #4
## Raw stage-score vector

Do not only use engineered features.

Compare:

\[
[s_0,s_1,s_2,\ldots,s_K]
\]

against:

\[
[\text{finite differences},\text{area},\text{reversals},\ldots].
\]

If raw stage scores work better:

The contribution remains viable, but the story becomes:

> **stage-resolved trajectory representation**

rather than:

> “our handcrafted curve features are the innovation.”

---

# 38. DETECTOR-IDENTITY LEAKAGE TEST

Train a simple classifier:

\[
\phi(x)\rightarrow \text{detector identity}.
\]

If detector identity is extremely easy to predict from trajectory features, then the representation may encode detector-specific signatures.

This does not automatically invalidate cross-detector transfer.

But the result should be reported and discussed.

---

# 39. IMPORTANT TARGET-NORMALIZATION DISTINCTION

Do not mix all target-detector access into a single “strict transfer” claim.

Recommended three levels:

## Level 1 — Source-only transfer

Only use:

- known score direction;
- documented threshold;
- analytical threshold-relative normalization.

No target-distribution statistics.

## Level 2 — Unlabeled target calibration

Use a separate unlabeled target calibration pool.

Can estimate:

- median;
- variance;
- quantiles;
- scale.

Do not calculate these from the locked final-test set.

## Level 3 — Light labeled calibration

Allow a small labeled target validation set for score/threshold calibration.

Do not retrain the reliability estimator.

Report separately.

---

# 40. ROOT-IMAGE GROUPING IS CRITICAL

All records derived from the same root image must stay together when required by the split.

This includes:

- transformed copies;
- detector A responses;
- detector B responses;
- detector C responses.

Otherwise:

> training may indirectly see the same image content that appears in validation/test.

That would weaken the results.

---

# 41. PRIMARY METRIC

Main:

**AURC — Area Under the Risk-Coverage Curve**

Lower is better.

Also strongly recommended:

**Excess AURC**

because detector base error rates differ.

Other metrics:

- risk at fixed coverage;
- coverage at fixed risk;
- error-prediction AUROC;
- error-prediction AUPR;
- Brier score;
- NLL;
- ECE;
- accepted-set balanced accuracy;
- false-AI;
- false-real;
- per-generator analysis;
- per-class analysis;
- high-confidence-error rejection;
- latency;
- memory;
- throughput;
- query overhead.

---

# 42. KEY BASELINES

At minimum compare against:

- original confidence;
- entropy;
- calibrated confidence;
- temperature scaling;
- Bahat 2018;
- Bahat 2020;
- mean score;
- score variance;
- flip rate;
- simple instability;
- ordinary TTA;
- unordered same-view representation;
- raw stage-score vector;
- independent transforms;
- endpoint-only composed transform.

If practical:

- ReSIDe;
- DACOM;

as white-box/internal-feature comparators.

---

# 43. GO-OR-REVISE PILOT

Planned:

**approximately 1,000–2,000 root images.**

This pilot is extremely important.

It should answer:

1. Do the degradations produce meaningful but label-preserving score changes?
2. Are wrong detector predictions behaviorally different from correct predictions?
3. Does cumulative outperform independent?
4. Does stage-resolved outperform endpoint-only?
5. Do handcrafted features outperform raw stage scores?
6. Does logistic regression work?
7. Does XGBoost materially improve it?
8. Does any signal survive held-out-detector transfer?
9. Is the compute cost practical?

Do not inspect the locked final generator/detector test during this phase.

If central signal is absent:

> revise the method before final evaluation.

---

# 44. WHAT IF CROSS-DETECTOR TRANSFER WORKS?

Suppose:

\[
R_{A+B}\rightarrow C
\]

significantly beats confidence and transformation baselines.

Interpretation:

> **Some detector-error structure revealed by degradation response is reusable across the tested detector mechanisms.**

This would be the strongest possible result.

---

# 45. WHAT IF CROSS-DETECTOR TRANSFER FAILS?

Suppose:

\[
R_{A+B}\rightarrow C
\]

fails, but:

\[
R_A\rightarrow A
\]

works.

Then the thesis can conclude:

> **Degradation trajectories contain useful detector-specific correctness information, but the relationship is not transferable enough across detector families.**

Still meaningful research.

Do not fake a universal result.

---

# 46. WHAT IF EVERYTHING FAILS?

If:

\[
AURC_{\text{PicAIsso}}
\geq
AURC_{\text{confidence/Bahat}}
\]

then:

> the selected degradation trajectories do not provide meaningful additional correctness information.

That would weaken the proposed method.

This is exactly why the pilot exists.

---

# 47. DEFENSE ANSWER — “EXISTING NA YAN”

Recommended:

> “Yes, transformation-based confidence estimation and selective classification already exist, and we do not claim otherwise. Bahat and Shakhnarovich already showed that transformed classifier outputs can reveal errors, while recent synthetic-image work such as ReSIDe and DACOM addresses detector reliability. Our narrower research question is whether the stage-by-stage output trajectory produced by cumulative mobile-style processing contains a correctness signal that can be transferred unchanged to another detector excluded from reliability-model training.”

---

# 48. DEFENSE ANSWER — “ANO NOVELTY?”

Short:

> **“We test whether stage-resolved degradation-response behavior can serve as a transferable correctness signal across different frozen AI-image detectors using only their output scores.”**

Longer:

> “The novelty is not transformations, degradation, response curves or abstention individually. The study tests whether a correctness estimator learned from the stage-by-stage degradation behavior of source detectors can still identify unreliable predictions on a held-out detector without accessing its internal representations or training on its labeled errors.”

---

# 49. DEFENSE ANSWER — “BAKIT CUMULATIVE?”

> “We do not assume cumulative processing is automatically better. It is an empirical hypothesis. Real reposting and mobile-processing histories can be sequential, so we test whether the intermediate detector-score evolution contains information beyond independent transformed views and beyond the final composed image. Both alternatives are explicit baselines.”

---

# 50. DEFENSE ANSWER — “WHAT IF IT DOESN'T WORK?”

> “A failure of cross-detector transfer would still show that degradation-response reliability is detector-specific rather than transferable. We separately evaluate within-detector correctness models. If even within-detector response trajectories do not improve over strong confidence and transformation baselines during the pilot, the method will be revised before the locked final experiment.”

---

# 51. CURRENT THESIS TITLE ISSUE

Current:

**PicAIsso: Cross-Detector Reliability Prediction from Ordered Mobile-Degradation Response Curves for Selective AI-Generated Image Detection**

Potential concern:

The word **“Ordered”** may imply that ordering itself is the novelty.

Possible future title:

**PicAIsso: Cross-Detector Reliability Prediction from Stage-Resolved Mobile-Degradation Response Trajectories for Selective AI-Generated Image Detection**

Or:

**PicAIsso: Transferable Error Prediction from Stage-Resolved Degradation Responses of AI-Generated Image Detectors**

No title change has yet been approved.

Do not change it automatically.

---

# 52. CURRENT PREFERRED RESEARCH-GAP PARAGRAPH

> Prior work has independently established black-box confidence estimation from transformed classifier outputs, transformation-responsive synthetic-image detection, robustness testing under sequential image degradation, and post-hoc selective reliability for synthetic-image detectors. These studies show that transformed-image probing, transformation composition, degradation chains, uncertainty estimation, and abstention are not individually new. What remains underexplored is whether the stage-by-stage output response of a frozen synthetic-image detector along cumulative, label-preserving processing paths contains prediction-correctness information that remains useful across detector boundaries. PicAIsso therefore investigates whether a correctness estimator learned from source-detector response trajectories can be transferred unchanged to a held-out detector without detector-internal features or labeled target-detector errors, and whether this representation improves selective risk beyond calibrated confidence and strong transformation-based alternatives.

---

# 53. CURRENT TRAFFIC-LIGHT ASSESSMENT

## Overall topic

🟢 **KEEP**

## Exact duplicate risk based on completed searches

🟢 **Low**

## “Transformations improve reliability” as novelty

🔴 **Not novel**

## Sequential degradation as novelty

🔴 **Not novel**

## Response curves as novelty

🔴 **Not novel by itself**

## Selective abstention as novelty

🔴 **Not novel**

## AI-image detector reliability as novelty

🔴 **Not novel**

## Stage-resolved detector score trajectory for correctness

🟡🟢 **Underexplored / interesting**

## Same reliability model transferred to held-out AI detector

🟢 **Strongest research gap**

## Current UFD/NPR/SAFE architectural diversity claim

🟡 **Needs revision or cautious wording**

## Guaranteed positive experimental result

🔴 **No**

## Suitable undergraduate CS thesis

🟢 **Yes**

---

# 54. WHAT HAS NOT YET BEEN PROVEN

No experiment has yet demonstrated that:

- PicAIsso works;
- cumulative beats independent;
- trajectory beats endpoint-only;
- engineered features beat raw scores;
- cross-detector transfer works;
- output normalization works;
- UFD/NPR/SAFE all integrate cleanly;
- chosen transforms remain label-preserving;
- 12k images are optimal;
- latency is practical.

The project is still at the **proposal / methodological validation stage**.

Do not describe hypothetical results as actual results.

---

# 55. IMPLEMENTATION STACK FROM THE PROPOSAL

Planned:

- Python
- PyTorch
- Pillow/OpenCV
- scikit-learn
- XGBoost
- pandas
- PyArrow
- FastAPI
- React

Engineering/privacy:

- transient processing;
- no training from user uploads;
- strip/ignore EXIF;
- do not store image content by default;
- MIME validation;
- pixel limits;
- file-size limits;
- HTTPS if deployed remotely.

---

# 56. EXCLUDED SCOPE

Not included:

- video;
- audio deepfakes;
- localization of partial manipulation;
- face swap detection;
- generator attribution;
- reverse-image search;
- claim verification;
- C2PA;
- watermark verification;
- social-media scraping;
- continuous learning;
- user-upload retraining;
- legal authenticity declaration.

Experimental binary scope:

\[
\text{fully AI-generated still image}
\]

versus

\[
\text{camera-acquired still image}.
\]

---

# 57. IMPORTANT LIMITATIONS

A detector can remain:

> confidently wrong under every transformation.

Therefore:

> stability ≠ correctness.

The system cannot catch every error.

Cross-detector transfer may fail due to:

- calibration differences;
- saturated logits;
- threshold differences;
- preprocessing differences;
- detector-specific artifacts;
- architecture differences;
- different training distributions.

Dataset limitations remain.

Three or four detectors cannot justify universal claims.

The correct wording is:

> **“across the tested detector families/mechanisms.”**

---

# 58. SOURCE CHECKLIST FOR FUTURE AI

Reverify these important works before making new novelty claims:

### Transformation confidence

- Bahat & Shakhnarovich 2018
- Bahat & Shakhnarovich 2020
- Shanmugam et al. 2021

### Calibration/selective prediction

- Guo et al. 2017
- Geifman & El-Yaniv 2017

### AIGI reliability

- Maier & Riess 2024
- Yumlembam et al. 2025
- ReSIDe 2026
- DACOM 2026

### Degradation / trajectory AIGI work

- QuAD 2026
- GlobalForge 2026
- Diffusion Snap-Back
- GenRes / GenRes++
- FOSID/RASID
- recent output-logit response studies

### Generic failure prediction

- DeYO
- MetaErr
- degradation-manifold/self-aware detection work

### Base detectors

- UniversalFakeDetect
- NPR
- SAFE

### Datasets

- GenImage
- Synthbuster
- RAISE
- NTIRE-related benchmarks

Because the field is rapidly changing, search for papers newer than August 9, 2026 if the date is later.

---

# 59. IF DOING ANOTHER NOVELTY SEARCH

Do not search only:

> “AI generated image detection confidence.”

Use terminology such as:

- transferable failure prediction;
- cross-detector error prediction;
- meta-confidence transfer;
- perturbation-response reliability;
- degradation signature;
- degradation fingerprint;
- confidence trajectory;
- correctness trajectory;
- score trajectory;
- output-response signature;
- cross-model confidence estimation;
- detector-independent selective classification;
- black-box reliability transfer;
- behavioral failure prediction;
- reliability head transfer.

Also inspect:

- citation graphs;
- institutional repositories;
- theses;
- OpenReview;
- arXiv;
- recent conference proceedings.

---

# 60. FINAL STATE THAT MUST BE CARRIED FORWARD

The previous AI conducted several deep-research passes and eventually reached a **narrower but stronger conclusion**.

The thesis should not be defended as:

> “We invented using transformations to check reliability.”

That is wrong.

It should not be defended as:

> “We invented cumulative transformations.”

Also wrong/unsafe.

It should not be defended as:

> “We invented response curves.”

Also unsafe.

The thesis should be defended as:

> **A test of whether stage-resolved degradation-response behavior contains prediction-error information that transfers across frozen AI-generated-image detectors.**

The strongest empirical test is:

\[
\text{train reliability estimator on detectors A+B}
\]

then:

\[
\text{apply same estimator unchanged to detector C}.
\]

No labeled correctness records from C should be used in the strict condition.

The methodology should include:

1. stage trajectory vs endpoint-only composition;
2. cumulative vs independent transforms;
3. endpoint-matched history controls where feasible;
4. raw score-vector baseline;
5. detector-identity leakage analysis;
6. all leave-one-detector-out folds;
7. clear target-calibration tiers;
8. stronger detector architecture diversity or weaker wording;
9. root-image grouped splits;
10. generator-disjoint evaluation;
11. 1k–2k pilot before locked final evaluation.

---

# 61. ONE-PARAGRAPH EMERGENCY HANDOFF

If the next AI only has time to read one paragraph:

> PicAIsso is an undergraduate CS thesis proposal about estimating whether a frozen AI-generated-image detector's original prediction is correct by observing only its output-score behavior across stage-by-stage cumulative mobile-style degradations, then accepting the original class or abstaining. Multiple adversarial literature searches found extensive prior art for transformed-image confidence, black-box error prediction, TTA, composed transformations, sequential degradation, response trajectories, selective AIGI reliability, output perturbation behavior, and generic model-agnostic failure prediction, so none of those broad concepts should be claimed as novel. However, no located primary work has yet clearly subsumed the exact experiment of training one correctness estimator from stage-resolved degradation trajectories of source AI-image detectors and applying that same estimator unchanged to a held-out detector without internal features or labeled target-detector errors. That cross-detector correctness-transfer hypothesis is the current strongest research gap. The main required improvements are stage-trajectory vs endpoint-only and cumulative-vs-independent baselines, raw-score and detector-identity checks, careful target-calibration tiers, and stronger detector diversity because NPR and SAFE appear to belong to closely related ResNet-style architecture families while UniversalFakeDetect is CLIP/ViT-based. Current recommendation: **keep the topic, refine the novelty framing, strengthen the protocol, then validate the signal in the planned pilot before locking the final experiment.**

---

# END OF MASTER HANDOFF V2