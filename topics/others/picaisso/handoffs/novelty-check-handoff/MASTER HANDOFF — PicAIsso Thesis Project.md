# MASTER HANDOFF — PicAIsso Thesis Project
## For continuation by another AI if the original conversation is lost

**Handoff date:** August 9, 2026  
**User:** Undergraduate Computer Science student  
**Project stage:** Thesis 1 / proposal already submitted to professor  
**Primary concern:** Novelty, research gap, collision with existing literature, methodological defensibility, and whether the topic is safe enough to “lock in” before substantial implementation begins.

---

# 0. INSTRUCTIONS TO THE NEXT AI

Treat this document as the accumulated state of a long, adversarial thesis-review conversation.

Do **not** restart from generic advice such as “search Google Scholar” or “AI-generated image detection is a growing field.”

The user already asked the previous AI to perform several independent deep-research passes specifically because the user has a **high need for verification before committing to the topic**. The previous AI intentionally tried to invalidate the proposal rather than merely confirm it.

The user values:

- evidence over reassurance;
- deep research over speed;
- direct admission of weaknesses;
- adversarial novelty checking;
- precise distinction between what is actually novel and what is prior art;
- primary research papers and official repositories over blog summaries;
- explicit methodological attacks that a thesis panel could make;
- willingness to revise or abandon a claim if evidence contradicts it.

Do **not** reassure the user simply because the proposal sounds sophisticated.

If performing new research, actively try to **kill the novelty claim**. Search using synonyms, adjacent fields, new 2026 papers, unpublished/preprint literature, citation neighborhoods, official code repositories, and methods that may use different terminology for the same idea.

Because this is a fast-moving AI-generated-image-detection field, **recheck current literature instead of assuming this handoff is permanently current.**

Use primary sources wherever possible:

- peer-reviewed papers;
- arXiv/preprints;
- CVPR/ICCV/ECCV/ICLR/NeurIPS/ACM proceedings;
- official OpenReview papers;
- official GitHub repositories of the authors;
- official dataset pages.

Do not claim literal “100% certainty that nobody anywhere has done this.” That level of negative proof is impossible because of unindexed theses, private manuscripts, papers under review, unpublished work, and future publications.

The correct standard is:

> “No prior work located after an aggressive literature search appears to subsume the complete proposed experiment.”

If a new paper is discovered that actually performs the same central experiment, **tell the user immediately**. Do not protect the previous conclusion.

---

# 1. ORIGINAL THESIS TITLE

**PicAIsso: Cross-Detector Reliability Prediction from Ordered Mobile-Degradation Response Curves for Selective AI-Generated Image Detection**

The proposal was already submitted to the professor.

The thesis is **not supposed to build yet another real-vs-AI image detector**.

Instead, it wraps already-existing frozen AI-generated-image detectors and tries to estimate whether their **original prediction is trustworthy**.

---

# 2. CORE PROBLEM THE PROPOSAL IS TRYING TO SOLVE

An AI-image detector may output:

> AI-generated — confidence 0.94

but that detector may still be wrong.

Standard confidence does not necessarily equal probability of correctness, especially under:

- unseen generators;
- resizing;
- JPEG compression;
- WebP conversion;
- cropping;
- screenshot/repost-like processing;
- distribution shift.

PicAIsso therefore asks:

> Can the way a frozen AI-image detector's output score changes as the same image passes through controlled cumulative mobile-style degradations reveal whether the detector's **original prediction** was correct?

And more importantly:

> Is that failure signal sufficiently reusable that a reliability model trained using other detectors can work on a detector it never saw during reliability training?

This second question is the strongest part of the research.

---

# 3. IMPORTANT DISTINCTION: THIS IS A CORRECTNESS MODEL, NOT ANOTHER AI DETECTOR

For a frozen detector \(d\):

\[
s_{d,0}=f_d(x)
\]

The detector predicts:

\[
\hat y_d =
\mathbb{I}[s_{d,0}>\tau_d].
\]

Dataset ground truth is:

\[
y.
\]

PicAIsso's target is:

\[
z_d =
\mathbb{I}[\hat y_d=y].
\]

Therefore the reliability model predicts:

\[
P(z_d=1)
\]

rather than directly predicting:

\[
P(y=\mathrm{AI}).
\]

That distinction must be preserved in all future explanations.

The original detector's AI-vs-real class remains unchanged.

PicAIsso only decides whether to:

**accept the detector's original answer**

or

**abstain / return Inconclusive.**

The transformed copies are diagnostic probes.

They are **not supposed to vote and flip the original detector label**.

---

# 4. ORIGINAL SYSTEM DESIGN FROM THE PROPOSAL

The proposed web prototype receives one still image.

It:

1. validates and decodes the image;
2. queries a selected frozen AI-image detector;
3. stores the detector's original score and original class;
4. generates controlled transformed copies in memory;
5. queries the same frozen detector on those copies;
6. extracts trajectory/response features;
7. feeds those features into a lightweight correctness estimator;
8. estimates whether the original prediction is likely correct;
9. either releases the original detector class or returns **Inconclusive**.

Suggested output wording from the proposal:

- “Likely AI-generated according to the tested detector”
- “Likely camera-captured according to the tested detector”
- “Inconclusive”

The prototype must not claim:

- authenticity;
- fraud;
- factual truth of the depicted event;
- legal admissibility;
- forensic proof.

---

# 5. BLACK-BOX / OUTPUT-ONLY CONTRACT

The intended reliability wrapper may only:

\[
\text{submit RGB image}
\rightarrow
\text{receive continuous detector score}.
\]

It must not inspect:

- detector weights;
- gradients;
- embeddings;
- intermediate feature maps;
- internal losses;
- detector training data.

This constraint is important because several close prior works use internal features.

The intended scientific question is partly whether useful reliability information can be extracted from **observable detector behavior alone**.

---

# 6. ORIGINAL PROPOSED DIAGNOSTIC PATHS

The proposal describes three cumulative, platform-agnostic paths.

Exact final parameters were intended to be frozen after a pilot.

Approximate initial design:

## Path A — resize/recompression

Original

→ long-side resize

→ JPEG Q85

→ second JPEG Q65

## Path B — low-bandwidth path

Original

→ downsample/up-sample

→ WebP Q80

→ JPEG Q70

## Path C — crop/repost path

Original

→ approximately 90% crop

→ resize to fixed long side

→ JPEG Q70

Together with identity, approximately **10 detector views per root image** were proposed.

Important:

These are **not to be described as exact Facebook/WhatsApp/Messenger/etc. simulations** unless independently measured.

They are platform-agnostic, controlled, label-preserving mobile/reposting-style diagnostic paths.

---

# 7. FORMAL CONCEPT OF A STAGE-RESOLVED CUMULATIVE TRAJECTORY

Let:

\[
x_0=x.
\]

A cumulative path produces:

\[
x_1=T_1(x_0)
\]

\[
x_2=T_2(x_1)
\]

\[
x_3=T_3(x_2)
\]

etc.

The frozen detector produces:

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

The trajectory is:

\[
[s_0,s_1,s_2,s_3,\ldots].
\]

The reliability representation may include the raw vector and/or derived descriptors.

---

# 8. ORIGINAL PROPOSED FEATURES

The proposal suggested features such as:

- original margin;
- stage-to-stage score change;
- normalized first difference;
- second difference;
- path area;
- worst margin;
- first class reversal;
- number of reversals;
- monotonicity violations;
- recovery after earlier confidence drop;
- cross-path disagreement.

Important correction from the research audit:

Do not imply that “slope” and “curvature” are physical derivatives over a universal continuous degradation scale when the path is:

crop → resize → JPEG.

For heterogeneous operations, safer terminology is:

**first-order finite difference along a fixed ordinal processing path**

and

**second-order finite difference along a fixed ordinal processing path.**

Likewise “path area” should be understood as an ordinal/path-index summary, not an integral over a physically universal degradation variable.

---

# 9. RELIABILITY LEARNERS

Primary proposed reliability heads:

- L2-regularized logistic regression;
- shallow XGBoost.

Potential exploratory:

- small MLP.

The proposal deliberately avoids using a large neural meta-model as the central contribution.

The main novelty should **not** be presented as XGBoost or feature engineering.

The central contribution is the experimental question / representation-transfer framework.

---

# 10. DATASET PLAN FROM THE PROPOSAL

Primary dataset:

**GenImage**

Approximately:

- 12,000 root images total;
- around 6,000 AI-generated;
- around 6,000 real;
- balanced;
- deduplicated.

Generator partitions were intended to be disjoint:

- 5 generator subsets for reliability development;
- 1 generator for threshold/validation;
- 2 generators for final unseen-generator testing.

Exact assignment should be frozen before final results are inspected.

Dataset hygiene includes:

- SHA-256 exact duplicate detection;
- perceptual near-duplicate screening;
- grouping repeated real images;
- grouping root image and all transformed derivatives in the same partition;
- no leakage through EXIF;
- no filename leakage;
- no folder-name leakage;
- no extension/provenance shortcut in primary reliability model.

Statistical unit:

**root image**, not each transformed derivative.

---

# 11. EXTERNAL AUDIT

Proposal intends a locked external audit using:

**Synthbuster**

plus

**RAISE / RAISE-1k real photographs**

for balanced evaluation.

Each Synthbuster generator should ideally be evaluated as a separate real-vs-generated subset rather than pretending repeated use of the same real collection creates independent pooled observations.

Possible extension only if practical:

- NTIRE benchmark;
- AncesTree;
- ReWIND;
- other modern degradation datasets.

---

# 12. ORIGINAL DETECTOR TRIO

Preferred proposal detectors:

1. **UniversalFakeDetect (UFD)**
2. **NPR**
3. **SAFE**

The intended claim was cross-detector / cross-architecture transfer.

However, a major issue was discovered during the final audit.

---

# 13. IMPORTANT DETECTOR-DIVERSITY ISSUE DISCOVERED

Official implementation inspection suggested:

## UniversalFakeDetect

Uses a **CLIP ViT-L/14** representation with a learned detector head.

It is structurally quite different from the other two.

## NPR

Uses neighboring-pixel residual preprocessing followed by a **ResNet-style CNN detector**.

## SAFE

Uses transformation/frequency/DWT-oriented preprocessing followed by a closely related **ResNet-style CNN implementation**.

Working conclusion:

**NPR and SAFE represent different forensic mechanisms, but they are not ideal evidence for three completely independent architecture families.**

Therefore future documents should not casually say:

> “three architecturally distinct detectors”

unless the architecture distinction is independently justified.

Safer wording if retaining them:

> “three distinct detector mechanisms, including a CLIP/ViT-based detector and two CNN/ResNet-family forensic detectors.”

Even better:

**replace either NPR or SAFE with a genuinely different architecture family, or add a fourth detector**, if compatibility and compute permit.

A replacement should have:

- public checkpoint;
- reproducible preprocessing;
- continuous output score;
- stable threshold or decision mapping;
- architecture meaningfully different from the existing detectors;
- feasible compute.

Do not choose a replacement based only on paper claims. Inspect official code/checkpoints first.

---

# 14. ORIGINAL CROSS-DETECTOR EXPERIMENT

For three detectors A, B, C:

Train the same reliability model on response records from:

\[
A+B
\]

then deploy unchanged on:

\[
C.
\]

Repeat:

\[
A+C \rightarrow B
\]

and:

\[
B+C \rightarrow A.
\]

Ideally report **all three leave-one-detector-out folds**.

Do not cherry-pick only successful folds.

Within-detector models can be included as an upper-bound/reference:

\[
A\rightarrow A
\]

\[
B\rightarrow B
\]

\[
C\rightarrow C.
\]

The scientific question is whether:

\[
R^{A,B}
\]

still meaningfully predicts correctness on:

\[
C
\]

without fitting a new:

\[
R^C.
\]

---

# 15. STRICT TRANSFER CONDITION — IMPORTANT NORMALIZATION ISSUE

The proposal originally allowed detector-oriented normalization using the target detector's documented threshold and possibly its unlabeled output distribution.

The audit identified a conceptual distinction that should be made explicit.

Recommended evaluation tiers:

## Tier 1 — Source-only / strongest inductive transfer

Use only information intrinsic/documented for detector C:

- score direction;
- documented threshold;
- fixed analytical transformation such as threshold-relative margin.

No target test-distribution statistics.

## Tier 2 — Unlabeled target calibration

Allow statistics from a **separate unlabeled calibration pool** for target detector C.

Examples:

- median;
- quantiles;
- scale normalization.

Do not compute these from the locked final test and then call the condition completely zero-shot.

## Tier 3 — Light labeled calibration

Permit a small labeled validation set to calibrate scale/threshold but **do not retrain the reliability learner**.

Report this separately.

The user should not hide target-domain access.

---

# 16. PRIMARY EVALUATION METRICS

Primary endpoint in proposal:

**Area Under the Risk-Coverage Curve (AURC)**

Lower is better.

Also strongly recommended:

**Excess AURC**, because base detectors may have different overall error rates.

Supporting metrics:

- selective risk at 70% coverage;
- selective risk at 80%;
- 90%;
- 95%;
- coverage at fixed empirical risk;
- error-prediction AUROC;
- error-prediction AUPR;
- balanced accuracy of accepted set;
- false-AI rate;
- false-real rate;
- Brier score;
- negative log-likelihood;
- Expected Calibration Error;
- per-generator analysis;
- per-class risk/coverage;
- behavior on initially high-confidence errors;
- latency;
- throughput;
- RAM;
- GPU memory;
- query count;
- overhead over ordinary one-pass detector inference.

Statistical uncertainty:

paired/stratified bootstrap, preferably using root image or source cluster as the resampling unit.

Proposal mentioned 10,000 bootstrap resamples.

---

# 17. PROPOSED BASELINES

The thesis will be weak if PicAIsso is only compared with raw detector confidence.

Mandatory or highly recommended baselines include:

- original confidence;
- entropy;
- temperature-scaled confidence;
- Bahat & Shakhnarovich 2018 transformation-invariance correctness estimator;
- Bahat & Shakhnarovich 2020 TTA-confidence approach;
- mean transformed score;
- transformed score variance;
- flip rate;
- simple instability threshold;
- ordinary test-time augmentation aggregation;
- unordered/same-view representation;
- raw normalized stage-score vector;
- endpoint-only composed transformation;
- independent-from-root transformation probes.

Where feasible:

- ReSIDe;
- DACOM;

but those should be labeled white-box/internal-feature methods and only implemented if detector compatibility allows fair comparison.

---

# 18. MOST IMPORTANT PRIOR ART: BAHAT & SHAKHNAROVICH 2018

Paper:

**Confidence from Invariance to Image Transformations**

arXiv:1804.00657

This is a fundamental collision.

They already demonstrate the broad concept:

\[
\text{query transformed copies}
\rightarrow
\text{observe classifier outputs}
\rightarrow
\text{learn whether original classification is correct}.
\]

Therefore PicAIsso **cannot claim**:

> “We are the first to predict classifier correctness from transformed black-box outputs.”

That is false/unsafe.

This paper should be treated as one of the most important baselines, not buried in RRL.

---

# 19. BAHAT & SHAKHNAROVICH 2020 — EVEN MORE IMPORTANT CORRECTION

Paper:

**Classification Confidence Estimation with Test-Time Data-Augmentation**

arXiv:2006.16705

Important final-audit finding:

The paper's appendix includes **consecutively composed transformations**.

Therefore PicAIsso also should not claim:

> “Prior work only applies independent transformations, while ours uniquely chains transforms.”

Too broad / unsafe.

A composed transformation may already look conceptually like:

\[
T_3(T_2(T_1(x))).
\]

PicAIsso's narrower potential distinction is:

**It records and models the detector's intermediate outputs at every stage:**

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

rather than merely treating the final composition as one TTA view.

This led to the preferred terminology:

> **stage-resolved cumulative degradation-response trajectory**

rather than simply:

> “ordered transformations.”

---

# 20. CRITICAL CORRECTION TO THE ORIGINAL PROPOSAL'S NOVELTY PARAGRAPH

The proposal approximately argued:

> existing transformation-confidence methods generally treat transformed copies as a set, while PicAIsso models ordered trajectories.

This distinction is too weak / potentially misleading.

Do **not** preserve that sentence unchanged in the final thesis or defense.

Preferred replacement idea:

> Prior transformation-based confidence methods establish that classifier responses to transformed inputs can reveal prediction errors, and prior work also includes composed transformations. PicAIsso therefore does not treat transformation response or transform composition itself as novel. Instead, it investigates whether the stage-by-stage evolution of a frozen synthetic-image detector's output along cumulative, label-preserving processing paths contains correctness information that remains useful when the reliability estimator is transferred unchanged to a different held-out detector.

---

# 21. CLOSE PRIOR ART — ReSIDe 2026

Paper:

**Post-hoc Selective Classification for Reliable Synthetic Image Detection**

Zheng & Seidman, 2026

arXiv:2605.08574

ReSIDe is an important near-neighbor.

It already tackles:

- synthetic-image detection;
- reliability;
- selective classification;
- abstention;
- risk/coverage;
- frozen detectors.

Therefore PicAIsso must not claim:

> “first selective/reliability framework for AI-image detection.”

ReSIDe differs because it uses **intermediate detector-layer confidence/features** and combines detector-internal evidence.

Its aggregation/tuning uses labeled hold-out validation.

Therefore it is more detector-specific / white-box than PicAIsso's intended output-only black-box interface.

---

# 22. CLOSE PRIOR ART — DACOM 2026

Paper concept:

**Enabling Your Forensic Detector Know How Well It Performs on Distorted Samples**

ICLR 2026

OpenReview identifier mentioned in proposal:

Jz5SA2KoFt

DACOM is extremely relevant.

It estimates per-sample detector confidence under distortion and supports selective rejection.

It uses:

- forensic internal features;
- image-quality descriptors;
- distortion information.

Important distinction discovered:

In its multi-detector study, individual forensic detectors are equipped with their corresponding DACOM confidence models.

It does **not appear to establish**:

\[
R_{A+B}
\rightarrow C
\]

where the same reliability model is deployed unchanged on unseen detector C.

Therefore DACOM does not appear to subsume PicAIsso's strongest transfer question.

---

# 23. CLOSE PRIOR ART — QuAD 2026

Paper:

**Quality-Aware Calibration for AI-Generated Image Detection in the Wild**

arXiv:2604.15027

Important because it includes realistic/reposting-like degradation behavior.

Its associated AncesTree-style evaluation includes progressive degradation processes involving things like:

- recompression;
- resize;
- crop;
- repeated transformations.

Therefore PicAIsso cannot claim:

> “first sequential/reposting-style degradation study for AI-image detection.”

QuAD uses multiple image versions / quality-aware aggregation to improve authenticity classification.

Its goal is not:

> predict whether another frozen detector's original decision is correct and transfer that correctness model across detectors.

---

# 24. CLOSE PRIOR ART — GlobalForge / RealDeg-Bench 2026

arXiv:2607.14684

Important contribution:

**multi-step compound degradation chains**

for AI-generated-image detection robustness.

Therefore:

> “multi-step compound degradations are novel”

is false.

GlobalForge primarily concerns robust/generalizable AIGI detection under realistic degradation.

It does not appear to implement the same per-detector correctness-transfer framework.

---

# 25. CLOSE PRIOR ART — DIFFUSION SNAP-BACK

Paper:

**Detecting AI-Generated Images via Diffusion Snap-Back Reconstruction**

arXiv:2511.00352

Important because it uses progressive response trajectories.

It calculates trajectory-style descriptors involving things such as:

- area under response;
- stage-to-stage change;
- knee/threshold behavior;

and can feed those descriptors into logistic regression for real-vs-AI classification.

This means PicAIsso cannot claim:

> “first AIGI method using trajectory/curve shape.”

The distinction is that Snap-Back's trajectory concerns reconstruction/perceptual behavior and directly predicts:

\[
\text{real vs AI}
\]

whereas PicAIsso's target is:

\[
\text{base detector correct vs incorrect}.
\]

---

# 26. CLOSE PRIOR ART — GenRes / GenRes++

Paper:

**Do Transformations Reveal the Truth? Generative Residual Learning for Generalized AI-Generated Image Detection**

arXiv:2607.08674

Published July 2026.

It explores relational behavior between an image and transformed samples.

Important because it reinforces:

> “behavior under transformations is an AIGI signal”

is already active prior art.

But the method learns real-vs-generated classification representations.

It is not an output-score-only correctness model around arbitrary frozen detectors.

---

# 27. CLOSE PRIOR ART — 2026 IMAGECLEF / OUTPUT-LOGIT RESPONSE STUDY

arXiv:2607.25842

The previous research pass identified a July 2026 study that measures **raw detector-logit shifts after controlled image purification** across several AIGI/deepfake-related detectors.

Importance:

It establishes that:

\[
\Delta \text{detector output after transformation}
\]

is itself not a wholly new observable.

It also reportedly finds the usefulness of response behavior to be **strongly detector-dependent**.

This is important evidence against assuming transfer will automatically work.

It makes PicAIsso's hypothesis both:

- riskier;
- more scientifically non-trivial.

---

# 28. ADJACENT PRIOR ART — DeYO

arXiv:2403.07366

This work uses changes in classifier prediction/confidence after a deliberately destructive transformation as a useful adaptation/confidence cue.

Therefore:

> “prediction change after transformation as reliability information”

is broadly established outside AIGI.

Again, PicAIsso's novelty cannot rely merely on Δscore.

---

# 29. ADJACENT PRIOR ART — SELF-AWARE OBJECT DETECTION VIA DEGRADATION MANIFOLDS

2026

arXiv:2602.18394

Important because it uses **sequentially composed degradations** for model self-awareness/reliability monitoring.

However, it reportedly emphasizes that its goal is not per-instance prediction correctness but recognition of degradation/distribution behavior.

Therefore it is conceptually adjacent, not an exact duplicate.

---

# 30. ADJACENT PRIOR ART — MetaErr 2026

arXiv:2604.23289

MetaErr trains a meta-model to predict whether a base DNN prediction will succeed or fail.

It describes the mechanism as architecture/training-parameter agnostic at the interface level.

Therefore PicAIsso cannot safely claim:

> “first architecture-agnostic failure predictor.”

But the important distinction is that MetaErr does not appear to demonstrate PicAIsso's exact setting:

\[
\text{train reliability model from base detectors A+B}
\rightarrow
\text{deploy unchanged on unseen base detector C}.
\]

That remains the relevant unresolved question.

---

# 31. OTHER BROAD PRIOR ART TO REMEMBER

The proposal already cites or discusses:

### Maier & Riess 2024

Reliable out-of-distribution recognition of synthetic images.

Shows uncertainty for unseen generators/post-processing is established.

### Yumlembam et al. 2025

Combines uncertainty measures with rejection.

Shows synthetic-image detection + uncertainty + rejection is existing.

### Guo et al. 2017

Calibration of modern neural networks.

### Geifman & El-Yaniv 2017

Selective classification.

### Shanmugam et al. 2021

Better aggregation in test-time augmentation.

### GenImage 2023

Major benchmark demonstrating generator generalization and degraded-image conditions.

### NTIRE 2026 challenge

Further emphasizes broad generators and transformation robustness.

Therefore none of these broad concepts should be marketed as PicAIsso inventions.

---

# 32. CLAIMS THAT ARE NOW CONSIDERED UNSAFE / FALSE

The next AI should actively prevent the user from making any of the following claims unless entirely new evidence changes the landscape.

Do not claim:

> “First method to use transformed images to estimate confidence.”

Existing.

Do not claim:

> “First black-box correctness predictor.”

Existing.

Do not claim:

> “First uncertainty-aware AI-generated-image detector.”

Existing.

Do not claim:

> “First selective/abstaining AI-generated-image detector.”

Existing.

Do not claim:

> “First method using sequential degradation.”

Existing.

Do not claim:

> “First method using cumulative/composed transformations.”

Existing or at minimum unsafe.

Do not claim:

> “Previous transformation confidence always treats transforms as unordered sets.”

Not robust enough.

Do not claim:

> “First AI-image detector using response trajectories.”

Unsafe.

Do not claim:

> “First method using curve AUC/slope/change for AIGI.”

Unsafe.

Do not claim:

> “First method to use output changes under perturbation.”

Existing.

Do not claim:

> “First architecture-agnostic failure predictor.”

Unsafe.

Do not claim:

> “NPR, SAFE and UFD are three completely unrelated architectures.”

Likely inaccurate / oversimplified.

---

# 33. CURRENT STRONGEST NOVELTY CLAIM

Preferred scientific formulation:

> **PicAIsso investigates whether stage-resolved output-score trajectories generated by cumulative, label-preserving mobile-processing probes can serve as transferable per-instance correctness representations across heterogeneous frozen AI-generated-image detectors. The reliability estimator is trained using source detectors and applied unchanged to a held-out detector without internal-feature access or labeled target-detector errors, and is evaluated through selective risk against confidence and transformation-based alternatives.**

Do not overstate this as “definitely first ever.”

A more defensible phrase is:

> **“To our knowledge, prior work does not establish whether…”**

---

# 34. EVEN SHORTER CORE RESEARCH QUESTION

If the user, adviser or panel asks:

> “Ano talaga ang thesis ninyo?”

Answer conceptually:

> **Does degradation-response error geometry transfer between frozen AI-generated-image detectors?**

More explicit version:

> **Can the stage-by-stage output behavior of a frozen AI-image detector under cumulative mobile-style degradation predict whether its original decision is wrong, and can that correctness signal transfer to an unseen detector?**

---

# 35. THE “RESIDUAL GAP” THAT SURVIVED ALL RESEARCH PASSES

After removing everything already covered by prior art, the remaining experimental intersection is approximately:

\[
\boxed{
\begin{array}{c}
\text{Frozen AI-generated-image detector}\\
+\\
\text{output-score-only black-box interface}\\
+\\
\text{controlled label-preserving cumulative degradation}\\
+\\
\text{stage-by-stage intermediate scores retained}\\
+\\
\text{target = correctness of original detector decision}\\
+\\
\text{reliability model trained using other detectors}\\
+\\
\text{unchanged reliability model on held-out detector}\\
+\\
\text{no labeled target-detector errors in strict condition}\\
+\\
\text{selective accept/abstain rather than class replacement}
\end{array}}
\]

The previous AI did **not locate a primary paper that performs this complete combination** after several adversarial search passes.

That is the current basis for keeping the topic.

---

# 36. MOST IMPORTANT NEW EXPERIMENT — STAGE TRAJECTORY VS COMPOSED ENDPOINT

Because Bahat 2020 already permits consecutively composed transformations, the thesis needs to prove that **retaining the intermediate states matters**.

Example:

\[
x_1=T_1(x)
\]

\[
x_2=T_2(x_1)
\]

\[
x_3=T_3(x_2).
\]

PicAIsso sees:

\[
[s_0,s_1,s_2,s_3].
\]

Construct an endpoint/composed baseline that sees essentially:

\[
[s_0,s_3]
\]

or treats:

\[
T_3\circ T_2\circ T_1
\]

as one ordinary composed transformation.

Then compare selective performance.

A strong result would be:

\[
AURC_{\text{stage-resolved}}
<
AURC_{\text{endpoint-only}}.
\]

This demonstrates that the **path evolution**, not merely the final degraded copy, contains useful correctness information.

This experiment is considered close to mandatory.

---

# 37. SECOND CRITICAL EXPERIMENT — CUMULATIVE VS INDEPENDENT-FROM-ROOT

Using the same operations and approximately matched query budget:

## Cumulative

\[
x_1=T_1(x)
\]

\[
x_2=T_2(T_1(x))
\]

\[
x_3=T_3(T_2(T_1(x))).
\]

## Independent-from-root

\[
x_1'=T_1(x)
\]

\[
x_2'=T_2(x)
\]

\[
x_3'=T_3(x).
\]

Compare the resulting correctness models.

Desired evidence:

\[
AURC_{\text{cumulative}}
<
AURC_{\text{independent}}.
\]

Without this control, a panelist could reasonably argue that ordinary transformation-diversity/error prediction explains everything.

---

# 38. THIRD IMPORTANT CONTROL — HISTORY VS ENDPOINT SEVERITY

There is another confound.

Suppose:

\[
x_2 = JPEG65(JPEG85(x)).
\]

Compare to:

\[
x_2'=JPEG65(x).
\]

Both have the same final nominal codec setting, but one has processing history.

If detector responses differ in a correctness-informative manner, this provides more evidence that the model is learning cumulative history rather than simply “lower quality = unreliable.”

Where possible, build endpoint-matched comparisons.

---

# 39. RAW SCORE VECTOR BASELINE IS REQUIRED

Suppose engineered features are:

\[
[\text{finite differences},\text{area},\text{reversals},...].
\]

Also train the same reliability learner directly on:

\[
[s_0,s_1,\ldots,s_K].
\]

Why?

Otherwise a panelist can ask:

> “Are the engineered slope/curvature features actually useful, or would the raw stages perform just as well?”

Possible outcomes:

### Handcrafted wins

Good evidence the representation helps.

### Raw vector wins

Still a useful thesis, but frame the contribution as:

> stage-resolved response trajectory

rather than handcrafted curve geometry.

### Both fail vs confidence/Bahat

Then the proposed signal is weak and should be revised during the pilot.

---

# 40. DETECTOR-IDENTITY LEAKAGE TEST

Potential problem:

A reliability learner trained across detectors might learn:

> “this trajectory looks like detector NPR”

rather than:

> “this trajectory indicates a mistake.”

Recommended diagnostic:

Train a simple classifier to predict detector identity from normalized trajectory features.

If detector identity is trivially recoverable with very high accuracy, discuss whether the representation is truly detector-agnostic.

This does not automatically invalidate transfer, but it is an important interpretability check.

---

# 41. ROOT-IMAGE LEAKAGE MUST BE PREVENTED

A root image may generate:

- original image;
- multiple transformed images;
- records from detector A;
- records from detector B;
- records from detector C.

When splitting reliability-model records, **all records associated with the same root image must remain in one partition**.

Do not let detector A's record for image X appear in training while detector B's record for the same root image X appears in validation/test, unless the specific experimental design explicitly requires it and leakage implications are addressed.

This can otherwise cause content-level leakage.

---

# 42. GENERATOR SPLITTING

Generator-disjoint evaluation is important because the system could otherwise learn generator artifacts rather than general detector-failure behavior.

Recommended:

- source-generator development;
- held-out generator validation;
- untouched unseen-generator test;
- external Synthbuster audit.

No final generator test should influence:

- feature selection;
- path selection;
- severity;
- thresholds;
- XGBoost tuning;
- normalization choices.

---

# 43. CROSS-DETECTOR CLAIM MUST MATCH THE ACTUAL EVIDENCE

If all three original detectors remain:

Avoid universal wording such as:

> “detector-independent”

unless evidence is extraordinarily strong.

Preferred:

> “cross-detector transfer across the tested detector families.”

If only one clear architecture-family jump is available:

> “including a held-out cross-architecture-family condition.”

If transfer fails:

> “the procedure is detector-specific and requires detector calibration.”

The proposal already contains language allowing this downgrade.

That is a strength.

---

# 44. POSITIVE, PARTIAL AND NEGATIVE OUTCOMES ARE ALL INTERPRETABLE

## Best case

\[
R_{A+B}\rightarrow C
\]

works significantly better than calibrated confidence and Bahat-style baselines.

Interpretation:

> Some degradation-response error structure is reusable across tested detector mechanisms.

## Intermediate case

Within-detector:

\[
R_A\rightarrow A
\]

works strongly, but cross-detector:

\[
R_{A+B}\rightarrow C
\]

fails.

Interpretation:

> Cumulative trajectories contain useful correctness information, but the relation is detector-specific.

Still scientifically meaningful.

## Weakest case

Trajectory methods do not beat strong transformation-confidence or calibrated-confidence baselines.

Interpretation:

> The chosen mobile degradation trajectories do not provide sufficient additional correctness information.

That is why a pilot is necessary before opening the final test.

---

# 45. GO-OR-REVISE PILOT

Original proposal planned a pilot on approximately:

**1,000–2,000 root images**

before final experiment.

This is strongly supported.

The pilot must not consume the locked final detector/generator test.

Questions the pilot should answer:

- Do transformations produce nontrivial score variation?
- Do incorrect predictions behave differently from correct ones?
- Does cumulative beat independent?
- Does stage-resolved beat endpoint-only?
- Do raw stage vectors or handcrafted features work better?
- Does logistic regression work?
- Does XGBoost add meaningful value?
- Is cross-detector transfer above confidence baseline?
- Do paths cause excessive class-label-changing damage?
- Is compute practical?

If no signal exists, revise paths or thesis claim **before unlocking final test data**.

---

# 46. DEFENSE SCRIPT IF A PANELIST SAYS “EXISTING NA IYAN”

Recommended substance:

> “Yes, transformation-based confidence estimation and selective classification already exist, and we do not claim otherwise. Bahat and Shakhnarovich already demonstrated that transformed classifier outputs can help predict errors, while recent synthetic-image work such as ReSIDe and DACOM directly addresses reliability. Our narrower question is whether the stage-by-stage output trajectory produced when a frozen AI-image detector is subjected to cumulative mobile-style processing contains a correctness signal that can transfer to another detector excluded from reliability-model training. We therefore test the contribution against transformation-confidence, confidence-calibration, independent transformation, endpoint-only composition, same-view unordered baselines, and leave-one-detector-out evaluation.”

Do not sound defensive about prior art.

Showing awareness of close prior work makes the thesis more credible.

---

# 47. DEFENSE SCRIPT IF ASKED “ANO ANG NOVELTY?”

Short answer:

> “The novelty is not using transformations or abstention by themselves. The study tests whether stage-resolved degradation-response behavior can serve as a transferable correctness representation across different frozen AI-image detectors using only their output scores.”

Longer answer:

> “Existing methods already use transformations for confidence estimation and synthetic-image detection, and recent methods already address selective reliability. What remains underexplored is whether a reliability estimator trained on the cumulative output-score response of source detectors can be applied unchanged to an unseen detector without using its internal features or labeled errors. PicAIsso is designed specifically to test that transfer hypothesis.”

---

# 48. DEFENSE SCRIPT IF ASKED “WHY CUMULATIVE?”

Good answer:

> “We are not assuming cumulative processing is automatically better. It is an empirical hypothesis. Reposting and mobile-processing histories are inherently sequential, so we test whether intermediate score evolution contains additional information beyond independent transformed views or the final composed transformation. Those alternatives are explicit baselines.”

This is better than asserting cumulative is inherently novel.

---

# 49. DEFENSE SCRIPT IF ASKED “WHAT IF IT FAILS?”

> “A failure of cross-detector transfer is still informative because it would show that degradation-based error signatures are detector-specific rather than reusable. We separately report within-detector reliability models as an upper-bound condition. If even within-detector trajectories do not improve over strong confidence and transformation baselines during the pilot, the proposed signal will be revised before the locked final experiment.”

---

# 50. CURRENT LOCK-IN JUDGMENT

After multiple separate novelty/research-gap passes and a final adversarial audit:

**Exact duplicate located:** No.

**Broad components already existing:** Yes, almost all of them.

**Central combination apparently subsumed by prior work:** No primary paper located so far.

**Undergraduate CS research gap:** Defensible.

**Novelty strength:** Moderate-to-strong if narrowly framed.

**Novelty strength if framed as “ordered transformations are new”:** Weak / unsafe.

**Greatest scientific strength:** cross-detector correctness-transfer hypothesis.

**Greatest scientific risk:** that the transfer signal may not exist.

**Greatest protocol concern discovered:** insufficient architectural diversity between NPR and SAFE.

**Recommendation:** KEEP TOPIC, but revise novelty framing and strengthen detector-selection / ablation design before methodology lock.

---

# 51. WHY THE PREVIOUS AI RECOMMENDED KEEPING THE TOPIC

Not because PicAIsso invented all its ingredients.

Actually the opposite.

The literature search found prior art for:

- transformation-confidence estimation;
- black-box correctness prediction;
- TTA confidence;
- composed transformations;
- progressive degradations;
- AIGI degradation benchmarks;
- selective classification;
- distortion-aware detector confidence;
- trajectory descriptors;
- output-logit perturbation responses;
- generic architecture-agnostic failure prediction.

Despite deliberately finding those collisions, the exact question:

\[
\boxed{
\text{Can degradation-response error geometry transfer between frozen AIGI detectors?}
}
\]

still appeared unanswered.

That is a much more credible novelty position than saying:

> “We searched briefly and nobody has done transformations before.”

---

# 52. CURRENT RECOMMENDED TITLE DIRECTION

The existing title can still work:

**PicAIsso: Cross-Detector Reliability Prediction from Ordered Mobile-Degradation Response Curves for Selective AI-Generated Image Detection**

However, the word **“Ordered”** may overemphasize the weakest novelty distinction.

Potential future refinements worth considering, without changing the core project:

**PicAIsso: Cross-Detector Reliability Prediction from Stage-Resolved Mobile-Degradation Response Trajectories for Selective AI-Generated Image Detection**

or

**PicAIsso: Transferable Error Prediction from Stage-Resolved Degradation Responses of AI-Generated Image Detectors**

No title change has yet been formally decided.

Do not silently rename the project without user approval.

---

# 53. CURRENT RECOMMENDED RESEARCH-GAP PARAGRAPH

Use as conceptual basis, not necessarily final manuscript wording:

> Prior work has independently established black-box confidence estimation from transformed classifier outputs, transformation-responsive synthetic-image detection, robustness testing under sequential image degradation, and post-hoc selective reliability for synthetic-image detectors. These studies show that neither transformed-image probing, degradation chains, uncertainty estimation, nor abstention is individually new. What remains underexplored is whether the stage-by-stage output response of a frozen synthetic-image detector along cumulative, label-preserving processing paths contains prediction-correctness information that remains useful across detector boundaries. PicAIsso therefore investigates whether a correctness estimator learned from source-detector response trajectories can be transferred unchanged to a held-out detector without detector-internal features or labeled target-detector errors, and whether this representation improves selective risk beyond calibrated confidence and strong transformation-based alternatives.

---

# 54. WHAT THE NEXT AI SHOULD RESEARCH NEXT IF ASKED

Do not simply do another generic novelty search.

Highest-value future research tasks are:

### A. Search for exact collision using new terminology

Try combinations involving:

- transferable failure prediction;
- cross-model error prediction;
- cross-detector uncertainty;
- black-box detector reliability;
- behavior-based error prediction;
- response signature;
- perturbation signature;
- score trajectory;
- confidence trajectory;
- degradation fingerprint;
- model failure fingerprint;
- cross-model selective classification;
- meta-confidence transfer;
- transferable confidence estimator;
- detector-independent reliability;
- transformation response meta-learning;
- failure transfer;
- sequential perturbation confidence.

### B. Search theses and repositories

Potentially:

- ProQuest;
- institutional repositories;
- master's theses;
- undergraduate capstones;
- OpenReview submissions;
- arXiv;
- HAL;
- Semantic Scholar;
- Google Scholar.

A thesis may use different terminology from journal papers.

### C. Citation-neighborhood search

Start from:

- Bahat 2018;
- Bahat 2020;
- ReSIDe 2026;
- DACOM 2026;
- QuAD 2026;

and inspect:

- papers citing them;
- papers they cite;
- related-work clusters.

### D. Verify detector diversity

Inspect official implementations of candidate detector replacements.

Need genuine architecture/mechanism diversity and public continuous scores.

### E. Search very recent papers

The field moved significantly even during 2026.

Always verify literature newer than this handoff date.

---

# 55. WHAT HAS NOT YET BEEN DONE

The next AI must not assume these tasks are already complete.

No actual PicAIsso experiment has been reported in this conversation.

No empirical evidence yet proves:

- cumulative beats independent;
- stage-resolved beats endpoint-only;
- handcrafted features beat raw score vectors;
- transfer works;
- target-detector normalization is sufficient;
- UFD/NPR/SAFE checkpoints all work reliably in one inference pipeline;
- compute is manageable;
- the 12,000-image sample is statistically optimal;
- chosen degradation severities are label-preserving;
- the web prototype has been implemented.

No final replacement detector has been selected.

No actual compatibility pilot has yet been conducted.

No final RRL rewrite has yet been approved.

No final title change has been approved.

The final experiment must not be described as successful before actual measurements exist.

---

# 56. SYSTEM/ENGINEERING SCOPE TO PRESERVE

Planned stack:

- Python;
- PyTorch;
- Pillow and/or OpenCV;
- scikit-learn;
- XGBoost;
- pandas;
- PyArrow;
- FastAPI;
- React.

Privacy/security intentions:

- decode uploads transiently;
- transform in memory where practical;
- do not retain user images by default;
- no user-upload training by default;
- ignore/strip EXIF;
- avoid logging filename/image content;
- file-size limits;
- pixel-count limits;
- MIME/decode validation;
- HTTPS when remotely deployed.

The system is a **research prototype**, not a production forensic service.

---

# 57. EXCLUDED SCOPE

The thesis does not target:

- video deepfakes;
- audio deepfakes;
- partial-image manipulation localization;
- face swaps;
- generator attribution;
- reverse-image search;
- factual verification of depicted claims;
- C2PA verification;
- watermark verification;
- social-media scraping;
- continuous online learning;
- retraining from user uploads;
- legal authenticity judgments.

Binary experimental scope:

**fully AI-generated still image**

versus

**camera-acquired still image.**

Partially generated/edited images are excluded because labels become ambiguous.

---

# 58. LIMITATIONS THAT SHOULD BE ADMITTED

Transformation stability is not correctness.

A detector may be:

\[
\text{confidently wrong at every stage}.
\]

PicAIsso cannot guarantee catching such cases.

Cross-detector transfer may fail because of:

- incompatible calibration;
- output saturation;
- different score ranges;
- different decision thresholds;
- different preprocessing;
- different feature mechanisms;
- architecture-specific sensitivity to JPEG/crop/resize;
- training-data differences.

Dataset limitations:

- GenImage is historically bounded;
- Synthbuster generators are also bounded;
- transformations cannot represent every social platform;
- 3–4 detectors cannot justify universal detector-independence;
- approximately 12k images cannot represent all image content/generators.

Compute limitation:

Approximately 10 views × several detectors creates large inference overhead.

A CLIP ViT-L/14 model may be difficult on a 4 GB GPU.

Cloud T4-class GPU or equivalent may be required for offline response extraction.

---

# 59. EXPECTED SCIENTIFIC CONTRIBUTION IF SUCCESSFUL

A successful thesis would provide:

1. a reproducible stage-resolved output-score trajectory representation;

2. evidence about whether degradation-response failure structure transfers across detectors;

3. a leave-one-detector-out evaluation protocol;

4. comparison against strong output-only transformation-confidence baselines;

5. selective risk/coverage evidence under held-out generators and external datasets;

6. an output-only reliability wrapper that can abstain without modifying the underlying detector;

7. a practical web research prototype demonstrating the method.

Do not claim universal authenticity detection.

---

# 60. EXPECTED SCIENTIFIC CONTRIBUTION IF CROSS-DETECTOR TRANSFER FAILS

Possible thesis conclusion:

> Stage-resolved mobile-degradation response trajectories provide useful correctness information within a detector but fail to form an invariant correctness representation across the tested detector families.

That is still valuable.

It tells future researchers:

> reliability heads may require detector-specific calibration.

This negative finding aligns with concerns raised by recent output-response studies showing detector-specific response behavior.

---

# 61. EXPECTED SCIENTIFIC CONTRIBUTION IF THE ENTIRE RESPONSE-CURVE IDEA FAILS

If calibrated confidence/Bahat-style baselines perform as well or better:

Possible conclusion:

> Under the tested mobile-processing paths and detectors, stage-resolved degradation trajectories do not provide sufficient incremental correctness information beyond established transformation-based confidence estimation.

That is weaker but still scientifically legitimate if:

- protocol was frozen;
- baselines were strong;
- negative results were honestly reported.

The proposal's pilot exists specifically to avoid wasting the untouched final test on a nonfunctional mechanism.

---

# 62. IMPORTANT ATTITUDE FOR THE NEXT AI

The user has anxiety about accidentally choosing a thesis that “already exists.”

Do not respond with empty reassurance such as:

> “Don't worry, your idea is unique!”

Instead separate:

### Novelty question

Does an exact or subsuming method exist?

Current evidence:

**No exact prior work located.**

### Empirical question

Will the method work?

Current evidence:

**Unknown. Needs pilot.**

### Scope question

Are some claims already existing?

Current evidence:

**Yes. Many broad components are prior art.**

This distinction was very important in the original conversation.

---

# 63. SOURCE CHECKLIST FOR FUTURE RESEARCH

At minimum, re-open/re-verify these when doing another novelty audit:

### Transformation confidence / error prediction

- Bahat & Shakhnarovich (2018), **Confidence from Invariance to Image Transformations**, arXiv:1804.00657
- Bahat & Shakhnarovich (2020), **Classification Confidence Estimation with Test-Time Data-Augmentation**, arXiv:2006.16705
- Shanmugam et al. (2021), **Better Aggregation in Test-Time Augmentation**

### Calibration / selective classification

- Guo et al. (2017), **On Calibration of Modern Neural Networks**
- Geifman & El-Yaniv (2017), **Selective Classification for Deep Neural Networks**

### Synthetic-image reliability

- Maier & Riess (2024), **Reliable Out-of-Distribution Recognition of Synthetic Images**
- Yumlembam et al. (2025), uncertainty + rejection
- ReSIDe / Zheng & Seidman (2026), arXiv:2605.08574
- DACOM / Li et al. (ICLR 2026), OpenReview Jz5SA2KoFt

### AIGI degradation / transformation response

- QuAD (2026), arXiv:2604.15027
- GlobalForge / RealDeg-Bench (2026), arXiv:2607.14684
- Diffusion Snap-Back, arXiv:2511.00352
- GenRes / GenRes++, arXiv:2607.08674
- 2026 ImageCLEF/output-logit response study, arXiv:2607.25842
- FOSID/RASID line of work

### Adjacent reliability/error-prediction

- DeYO, arXiv:2403.07366
- Self-Aware Object Detection via Degradation Manifolds, arXiv:2602.18394
- MetaErr, arXiv:2604.23289

### Base detector / benchmark papers

- Ojha et al. (2023), UniversalFakeDetect
- Tan et al. (2024), NPR
- Li et al. (2025), SAFE
- Zhu et al. (2023), GenImage
- Bammey (Synthbuster)
- NTIRE 2026 robust AIGI challenge

Always re-check publication dates and exact titles.

---

# 64. FINAL STATE TO CARRY FORWARD

The topic has **not been rejected**.

The previous AI's final recommendation after repeated adversarial research was:

> **Proceed with PicAIsso, but narrow and strengthen the novelty framing before locking the methodology.**

Most important changes before final protocol freeze:

1. Stop treating “ordered/cumulative transformations” themselves as the novelty.

2. Define the core novelty as:

   **stage-resolved cumulative output response → per-instance correctness prediction → unchanged held-out-detector transfer.**

3. Add:

   **stage-resolved vs endpoint-only composed-transform baseline.**

4. Add:

   **cumulative vs independent-from-root baseline.**

5. Where feasible add:

   **endpoint-matched history/severity controls.**

6. Compare:

   **raw normalized stage-score vector vs handcrafted features.**

7. Test:

   **detector-identity leakage.**

8. Report:

   **all leave-one-detector-out folds.**

9. Separate:

   **source-only transfer, unlabeled-target normalization, and light labeled calibration.**

10. Improve the detector trio's architecture diversity or soften the architecture claim.

11. Keep generator-disjoint and root-image-grouped splits.

12. Do the 1k–2k root-image go/revise pilot before touching the locked final test.

---

# 65. ONE-PARAGRAPH ULTRA-COMPACT STATE SUMMARY

PicAIsso is an undergraduate CS thesis proposal already submitted to the professor. It wraps frozen AI-generated-image detectors and tries to estimate whether each detector's **original real-vs-AI classification is correct**, using only the detector's output scores on the original image and on intermediate stages of cumulative, mobile-style label-preserving transformations. It then accepts the original label or abstains. Multiple adversarial literature searches found extensive prior art for transformation-based correctness prediction, TTA confidence, composed transformations, sequential degradation, AIGI response trajectories, uncertainty/selective classification, output-logit perturbation behavior, and generic architecture-agnostic failure prediction. Therefore none of those broad ideas is novel individually. However, no located primary work has yet clearly subsumed the exact experiment of learning a stage-resolved degradation-response correctness model from source AI-image detectors and transferring the same reliability model unchanged to a held-out detector without detector-internal features or labeled target-detector errors. That narrow cross-detector transfer question is the current defensible research gap. The main methodological corrections are to compare stage trajectories against endpoint-only composed transforms and independent-root probes, test raw score vectors and detector-identity leakage, separate levels of target-detector calibration, and improve detector diversity because NPR and SAFE appear to use closely related ResNet-family backbones while UFD is CLIP/ViT-based. Current recommendation: **keep the topic, revise the novelty wording and experimental controls, then run the planned pilot before locking the final experiment.**

---

# END OF HANDOFF