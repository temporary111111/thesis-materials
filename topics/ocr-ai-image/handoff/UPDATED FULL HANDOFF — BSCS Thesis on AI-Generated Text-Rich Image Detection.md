# UPDATED FULL HANDOFF — BSCS Thesis on AI-Generated Text-Rich Image Detection

## 0. PURPOSE OF THIS HANDOFF

You are taking over an ongoing Bachelor of Science in Computer Science thesis-planning conversation.

Do **not restart the brainstorming from zero**.

Continue from the exact state documented here.

The student is working on **CS 124 – Thesis 1 at Bicol University**.

The broad thesis area has already been narrowed to:

> **Artificial Intelligence / Computer Vision / AI-generated image detection**

The student’s main priority is:

> **Graduate efficiently with a thesis that is feasible, defendable, has a clear Computer Science contribution, and does not require unnecessarily difficult datasets or computing resources.**

The student is **not trying to maximize theoretical novelty at all costs**.

The optimization priority is roughly:

1. High probability of finishing the thesis.
2. Clear Computer Science contribution.
3. Defendable research gap.
4. Public/easily obtainable dataset.
5. Manageable training and implementation.
6. Clear evaluation metrics.
7. Reasonable novelty for an undergraduate CS thesis.
8. Avoid unnecessary complexity.

If two topics are equally defendable, choose the **simpler one**.

---

# 1. OFFICIAL THESIS MATERIALS PROVIDED BY THE USER

The user originally uploaded:

1. **Thesis_Domains_CS.pdf**
2. **Topic_Proposal_Template_CS.pdf**
3. **Thesis_1_Course_Introduction_Sy.pptx**

If this conversation is being continued in another AI/session, ask the user to **re-upload these three files before drafting the actual proposal/manuscript**.

These materials should be treated as the primary institutional requirements.

Do not replace their requirements with generic thesis advice.

---

# 2. CENTRAL UNIVERSITY RULE

The most important institutional rule is:

> A Computer Science thesis must contain a substantial computing contribution.

A normal application/system is not sufficient.

The official guide identifies acceptable computing components such as:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Computer Vision
- Image Processing
- Natural Language Processing
- Data Analytics
- Predictive Modeling
- Algorithms
- Optimization
- Intelligent Systems
- Recommender Systems
- Cybersecurity
- IoT Intelligence
- Human-Computer Interaction
- Computational Modeling
- Emerging Computing Technologies

The software/application is supposed to serve only as the **vehicle for implementing and evaluating the computational contribution**.

Therefore, never make the thesis primarily:

> “Development of an AI Image Detection Website.”

The website is secondary.

The actual contribution should involve something like:

- evaluation,
- enhancement,
- optimization,
- algorithm/model implementation,
- controlled computational experimentation,
- robustness/generalization analysis,
- feature representation,
- model comparison with a research question,
- or another measurable computing contribution.

The institutional guide explicitly allows:

> **development, evaluation, enhancement, or application of computational methods**

It does **not** require the students to invent an entirely new algorithm.

This is important.

The thesis can be an empirical enhancement/evaluation study if the contribution is clearly defined.

---

# 3. RELEVANT APPROVED CS DOMAIN

The current topic belongs primarily to:

## Artificial Perception

Relevant areas:

- Computer Vision
- Image Processing
- Pattern Recognition

It can also overlap with:

## Machine Learning and Artificial Intelligence

Relevant areas:

- Machine Learning
- Deep Learning
- potentially Explainable AI, but explainability is not currently the chosen research contribution.

---

# 4. SIX ITEMS THE UNIVERSITY EXPECTS IN A TOPIC PROPOSAL

The official thesis-domain guide expects every topic proposal to explicitly identify:

1. **CS Domain**
2. **Computing Contribution**
3. **Bicol University Research Agenda**
4. **Sustainable Development Goal**
5. **Beneficiary**
6. **Expected Innovation**

These are **not fully finalized yet**.

Current provisional state:

### CS Domain
Artificial Perception — Computer Vision / Artificial Intelligence

### Computing Contribution
Still being validated experimentally.

Current leading form:

> evaluation and possible enhancement of lightweight AI-generated text-rich image detection using OCR-derived page-level spatial/layout cues.

Do not finalize the other four fields until the technical direction passes the proof-of-concept test.

---

# 5. UNIVERSITY TITLE EXPECTATION

The proposal guide recommends a title structure approximately like:

> **[Computing Technique/Approach] + [Problem Being Solved] + [Application Domain]**

Therefore the final thesis title should make the computational contribution visible.

Avoid:

> AI Image Detector

or:

> AI-Generated Image Detection System

A better title should reveal:

- the computational technique,
- the exact detection problem,
- and the narrowed application domain.

---

# 6. OFFICIAL PROPOSAL STRUCTURE

According to the provided template, the Background of the Study should eventually cover:

1. Context and relevance
2. Sustainable Development Goals / BU Research Agenda
3. Existing challenges and research gaps
4. Opportunities and proposed computing approach
5. Discussion of computing components
6. Concluding synthesis

The proposal must emphasize the **computing contribution**, not merely the software.

The final project should also generally follow:

## Objective 1
Dataset acquisition/preparation.

## Objective 2
Algorithm/model/computational technique implementation.

## Objective 3
Prototype/system development.

## Objective 4
Evaluation and assessment.

Potential algorithm metrics for the current problem:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Potential later system evaluation:

- ISO/IEC 25010
- SUS
- user evaluation

But system evaluation should come only after the actual research model is established.

---

# 7. USER’S MAIN PRACTICAL GOAL

The student originally said that the most important thing is:

> feasibility, something that can be defended, and a clear contribution, with the practical goal of graduating quickly.

The user chose AI-generated images because:

- public datasets appear easier to obtain,
- the area is Computer Vision,
- the user already knows a little Computer Vision,
- the project can potentially avoid difficult manual dataset collection.

This remains the correct high-level strategy.

---

# 8. BROAD TOPIC DECISION

The broad topic has survived repeated review:

> **AI-generated image detection**

is still considered a viable Computer Science thesis area.

However:

> **basic Real-vs-AI detection is not enough as a thesis contribution.**

A title such as:

> “AI-Generated Image Detection Using CNN”

is considered too basic and too easy for a panel to challenge with:

> “What is new?”

---

# 9. RESEARCH DIRECTIONS PREVIOUSLY CONSIDERED

Many possible sub-directions were investigated.

These included:

- JPEG/compression robustness
- blur/resize robustness
- cross-generator detection
- unseen-generator generalization
- lightweight models
- quantization
- resource-efficient detection
- few-shot adaptation
- continual adaptation
- test-time adaptation
- calibration
- uncertainty estimation
- selective classification / abstention
- foundation-model features
- CLIP-based detection
- explainability / Grad-CAM
- frequency/spectral detection
- localized AI edits
- generator attribution
- text-rich AI-generated image detection
- OCR/text/layout-based detection

Repeated novelty auditing eliminated or downgraded many of these.

---

# 10. DIRECTIONS THAT SHOULD NOT BE USED AS THE MAIN NOVELTY

## A. Basic CNN detection

Example:

> AI-Generated Image Detection Using CNN

### Status
DROP.

Reason:

Already extremely established.

---

## B. Transfer learning model comparison only

Example:

> Comparative Analysis of ResNet and MobileNet for AI-Generated Image Detection

### Status
Weak.

The panel could reasonably ask:

> “So you only trained several models?”

Comparison needs a deeper research question.

---

## C. JPEG / blur / resize robustness

### Status
DROP as main contribution.

Recent benchmark/challenge work has already heavily investigated degraded AI-generated image detection.

Compression, resizing, blur, cropping, etc. can remain **secondary stress tests**, but should not be the thesis novelty.

---

## D. Grad-CAM / explainability alone

### Status
DROP as main contribution.

Explainable AI-generated image detection has already been explored in multiple studies.

Grad-CAM may be used later for analysis, but not as the core innovation.

---

## E. Calibration

### Status
DROP as main contribution.

Recent 2026 work already investigates post-hoc calibration, quality-aware calibration, and other calibration strategies for distribution shift.

---

## F. Selective classification / “uncertain” output

### Status
DROP as main contribution.

Recent studies already investigate rejection/uncertainty mechanisms for AI-generated image detection.

---

## G. Few-shot adaptation

### Status
Downgraded heavily.

Recent 2025–2026 work already directly studies few-shot adaptation to unseen generators.

Potentially valid but increasingly crowded.

---

## H. Test-time adaptation

### Status
Not recommended for graduation-first strategy.

It is an active current research area and adds algorithmic complexity.

---

## I. Foundation-model/frozen-feature detection alone

Examples:

- CLIP features
- DINO-style frozen features
- lightweight linear classifier

### Status
Too crowded as the only contribution.

These may still be used as components, but not as novelty.

---

## J. Frequency/spectral detection alone

### Status
Crowded.

Numerous methods already use frequency-domain forensic cues.

---

# 11. PREVIOUS LEADING BACKUP — RESOURCE-EFFICIENT / QUANTIZED DETECTION

A previous leading idea was approximately:

> **Cross-Generator Robustness and Computational Efficiency of Quantized Lightweight Models for AI-Generated Image Detection**

The idea:

- train lightweight detector,
- test known vs unseen generators,
- quantize model,
- compare accuracy/F1/model size/latency.

This looked attractive because it is easy to implement.

However, deeper novelty review found surrounding work already studying:

- lightweight AI-generated image detectors,
- accuracy-efficiency tradeoffs,
- efficient detectors,
- low-power/edge deployment,
- compact cross-generator detection.

The exact controlled question:

> FP32 vs INT8 quantization effect on unseen-generator generalization

may still be somewhat distinct, but the surrounding research territory is crowded.

### Current status
**Backup only.**

### Advantages
Very easy implementation.

### Weakness
Harder to defend as meaningful research rather than deployment optimization.

---

# 12. CURRENT LEADING AREA — TEXT-RICH AI-GENERATED IMAGES

Repeated searches identified a more recent problem:

> **AI-generated text-rich images**

Examples:

- receipts
- tables
- infographics
- UI screenshots
- commercial posters
- academic posters
- other document-like or structured images containing substantial text.

Modern multimodal image generators can now produce increasingly realistic readable text and structured layouts.

Recent 2026 benchmark studies show that existing AI-generated image detectors still have difficulty with these image types.

This creates a strong **problem gap**.

Important distinction:

> The problem is clearly under active development and not solved.

However:

> The exact method novelty still needs careful framing.

---

# 13. IMPORTANT RECENT BENCHMARK — TEXTRICH

The current core dataset candidate is:

> **TextRich**

The latest version discussed in the research contains approximately:

- 12,095 total images
- 6,109 AI-generated
- 5,986 real

Across six categories:

1. Tables
2. Receipts
3. Infographic Charts
4. UI Screenshots
5. Commercial Posters
6. Academic Posters

Approximately 2,000 images per category.

Its synthetic samples are generated using **GPT-Image-2**.

This makes it very convenient for an undergraduate project because:

- dataset already exists,
- classes are nearly balanced,
- six application categories are available,
- no manual annotation is required.

However:

### Limitation
Synthetic data come from one primary generator family.

Therefore:

> Do not claim universal AI-image detection.

The thesis should stay bounded to the evaluated datasets.

---

# 14. IMPORTANT DATASET SHORTCUT RISK

A methodological issue was noticed in TextRich.

The generated and real images may originate from different file/storage pipelines.

For example, generated samples may be PNG while some real datasets contain JPG/JPEG.

If the experiment is careless, a model could learn:

> “PNG = AI”

rather than meaningful authenticity cues.

Therefore the experimental pipeline should normalize all images before training:

> decode pixels  
> convert to RGB  
> strip metadata through re-encoding  
> standardize output format/preprocessing

This is not the thesis novelty.

It is necessary experimental hygiene.

---

# 15. SECOND IMPORTANT TEXT-RICH BENCHMARK — TEXTFAKE

Another recent benchmark is:

> **TextFake**

It contains approximately:

- 20,000 text-rich images
- multiple languages
- multiple recent image generators

Its studies found substantial detector difficulty.

A key reported phenomenon is:

> **Text Density Curse**

Meaning:

as text density increases, conventional AI-generated image detectors can become less reliable.

This is very important for the current research direction.

However:

TextFake may require academic/non-commercial dataset access approval.

Therefore:

> Do not make thesis completion depend on TextFake.

Potential strategy:

### Core dataset
TextRich

### Optional external validation
TextFake, if access is successfully obtained.

---

# 16. ORIGINAL TEXT-RICH IDEA

The first text-rich idea was:

> visual features + text features

or:

> visual model + OCR.

Repeated novelty review showed this was too broad.

Why?

Because recent studies already use:

- text-region features,
- semantic text representations,
- visual + textual fusion,
- multimodal reasoning,
- OCR information.

Therefore:

> “We use OCR.”

is NOT novelty.

> “We combine text and images.”

is NOT novelty.

> “We use text regions to improve AIGI detection.”

is also not safe as a novelty claim.

---

# 17. IMPORTANT CLOSEST PRIOR WORK — TIQA / ANTIQA

A recent study named TIQA/ANTIQA was found to have an AI-generated image detection experiment.

Their approach roughly:

1. detect text regions,
2. crop text regions,
3. encode each text crop using a learned text-quality representation,
4. pool those representations,
5. combine them with a global AI-image detector representation,
6. classify Real vs AI.

This is a very important overlap.

Therefore the thesis must not claim:

> text-region fusion with a visual detector is new.

The remaining distinction is narrower.

TIQA focuses more on:

> how the generated text visually/perceptually looks

rather than:

> explicit global page-level spatial geometry of all OCR-detected text regions.

---

# 18. OCR LAYOUT GEOMETRY IS ALSO NOT NEW GENERALLY

Repeated red-team novelty auditing found older document-forensics research using:

> OCR bounding boxes + geometric/spatial relationships

for detecting manipulated documents.

Other recent document-forgery systems also use:

- OCR masks,
- OCR-guided text regions,
- document layout,
- layout-aware representations.

Therefore:

> “Using OCR bounding boxes to detect fake documents is new”

would be false.

This must NEVER be used as the novelty statement.

---

# 19. WHAT EXACT DISTINCTION STILL SURVIVES

After repeated targeted searching, no direct duplicate was found whose central experiment is exactly:

> **Does explicit page-level OCR-derived spatial layout geometry provide complementary authenticity information to a lightweight visual detector for fully AI-generated multi-domain text-rich images?**

Important:

> “No direct match found” does NOT prove that nobody has ever done it.

Do not make “first-ever” claims.

The safest contribution framing is:

> **controlled computational evaluation and possible enhancement using OCR-derived page-level spatial-layout cues as complementary forensic information for lightweight detection of AI-generated text-rich images.**

This is an incremental undergraduate research contribution.

That is acceptable under the official CS guide because evaluation and enhancement are recognized CS thesis contributions.

---

# 20. CURRENT STATUS OF TEXT-RICH OCR/LAYOUT IDEA

### Broad problem
Strong.

### Method novelty
Moderate.

### Dataset feasibility
High.

### Compute feasibility
High.

### Defense feasibility
Good if framed conservatively.

### Risk
Layout information may not actually improve detection.

### Current verdict
**KEEP / MODIFY / EMPIRICALLY VALIDATE**

It is NOT locked as the final thesis yet.

---

# 21. CURRENT WORKING RESEARCH QUESTION

The most defensible current research question is approximately:

> **To what extent can OCR-derived page-level spatial-layout representations improve a lightweight visual classifier for detecting AI-generated text-rich images across structured image domains?**

A possible secondary question:

> **Which text-rich image categories benefit most from explicit layout information?**

Potential categories:

- Tables
- Receipts
- Infographics
- UI Screenshots
- Commercial Posters
- Academic Posters

---

# 22. POSSIBLE STRONGER RESEARCH QUESTION

Because TextFake reports a Text Density Curse, a more specific future enhancement could be:

> **Can OCR-derived spatial-layout information compensate for visual-detector degradation as text density increases?**

This could lead to:

> **text-density-aware visual-layout fusion**

However:

Do **not** commit to this before the initial proof-of-concept confirms that layout signal is actually useful.

The preferred progression is:

1. test whether layout has signal,
2. test whether layout improves visual detection,
3. only then design adaptive/density-aware fusion if justified.

---

# 23. CURRENT WORKING TITLE

Not final.

Most conservative version:

> **Evaluating OCR-Derived Spatial Layout Cues for Lightweight Detection of AI-Generated Text-Rich Images**

A more enhancement-oriented future version:

> **Text-Density-Aware Visual–Layout Fusion for Lightweight AI-Generated Text-Rich Image Detection**

But the second title should only be used if empirical evidence supports it.

Do not freeze either title yet.

---

# 24. WHY THE TITLE SHOULD SAY “EVALUATING”

Using:

> Evaluating

is currently safer than:

> Novel Visual–Layout Architecture

because the novelty is mainly:

> empirical investigation of a specific complementary forensic cue in a recent unsolved text-rich detection setting.

The thesis does not need to pretend the use of OCR/layout is unprecedented.

---

# 25. MOST IMPORTANT CURRENT STEP — PROOF OF CONCEPT

Before writing Chapter 1 or finalizing the title:

> **Run a small proof-of-concept experiment.**

Purpose:

> Determine whether OCR-derived spatial layout actually contains useful authenticity information.

If it does not:

> drop the idea immediately.

This prevents investing weeks in a weak proposal.

---

# 26. PILOT HYPOTHESES

## H1

> OCR-derived page-level spatial-layout information contains discriminative signal for distinguishing real from AI-generated text-rich images.

## H2

More important:

> OCR-derived layout information provides useful complementary signal beyond a lightweight visual classifier.

H2 is the thesis-critical hypothesis.

If layout-only works but visual + layout does not improve visual-only, the thesis direction becomes weaker.

---

# 27. PILOT DATASET SIZE

Do NOT begin with all ~12,000 images.

Use approximately:

> **2,400 images**

Balanced across six categories.

Suggested pilot subset:

| Category | Real | AI |
|---|---:|---:|
| Tables | 200 | 200 |
| Receipts | 200 | 200 |
| Infographic Charts | 200 | 200 |
| UI Screenshots | 200 | 200 |
| Commercial Posters | 200 | 200 |
| Academic Posters | 200 | 200 |
| Total | 1,200 | 1,200 |

This is only a proof-of-concept.

The final thesis sample may use more data.

---

# 28. IMAGE NORMALIZATION BEFORE PILOT

Before any modeling:

1. Load every image.
2. Decode to pixels.
3. Convert to RGB.
4. Re-encode using a consistent process.
5. Remove metadata through clean re-save.
6. Use consistent preprocessing.

Purpose:

reduce trivial file-format/source shortcuts.

Do this before model training.

---

# 29. OCR REQUIREMENT

For the first experiment:

> **OCR recognition is not required.**

We do not need to know the words.

We only need:

> text-detection bounding boxes.

Example:

Instead of reading:

> “TOTAL ₱550”

we only need to know:

> a text box exists at normalized location X,Y with width W and height H.

This keeps the project much simpler.

A lightweight OCR text detector such as PaddleOCR can provide bounding boxes.

---

# 30. TWO PROPOSED LAYOUT REPRESENTATIONS

Use at least two simple representations so failure of one representation does not immediately kill the hypothesis.

## Representation A — Geometric feature vector

Possible simple features:

- number of detected text regions
- total text-region area
- text coverage ratio
- mean box width
- mean box height
- width variance
- height variance
- mean aspect ratio
- horizontal spread
- vertical spread
- average gap
- alignment statistics
- box density

Use a simple classifier:

- Logistic Regression
- or a small MLP

Purpose:

determine whether simple layout statistics alone have discriminative signal.

---

## Representation B — Layout map

Convert OCR boxes into a normalized binary image, e.g.:

> 64 × 64 layout mask

Example:

Original:

- title at top
- table in center
- totals at bottom

Layout map:

only rectangles/regions showing where the text exists.

This preserves:

- structure
- density
- alignment
- relative placement

while discarding:

- actual words
- texture
- fonts
- semantic content.

Then use a tiny CNN on the 64×64 map.

---

# 31. VISUAL BASELINE

Use only **one lightweight visual model** for the first experiment.

Recommended pilot candidate:

> **MobileNetV3-Small**

Reason:

- lightweight,
- pretrained weights available,
- low compute,
- enough for concept validation.

Do NOT compare many models yet.

The goal is not to find the best architecture.

The goal is to test whether layout adds information.

---

# 32. FOUR CORE PILOT EXPERIMENTS

## Experiment A — Visual only

Image  
→ MobileNetV3  
→ classifier  
→ Real / AI

Purpose:

baseline.

---

## Experiment B — Layout statistics only

OCR boxes  
→ geometric feature vector  
→ Logistic Regression or small MLP  
→ Real / AI

Purpose:

test simple page-geometry signal.

---

## Experiment C — Layout map only

OCR boxes  
→ 64×64 layout mask  
→ tiny CNN  
→ Real / AI

Purpose:

test learned spatial structure.

---

## Experiment D — Visual + layout

Image  
→ MobileNetV3  
→ visual embedding

Layout map  
→ tiny CNN  
→ layout embedding

Concatenate embeddings  
→ small MLP  
→ Real / AI

This is the most important experiment.

---

# 33. PILOT SPLIT

Suggested initial split:

> 70% train  
> 15% validation  
> 15% test

Stratify by:

- class: Real/AI
- image category

For 2,400 images:

approximately:

- 1,680 training
- 360 validation
- 360 test

Save exact filenames for all splits.

The same image must belong to the same split in:

- visual experiment,
- layout experiment,
- fusion experiment.

---

# 34. PILOT METRICS

Primary classification metrics:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Most important:

> F1 and per-category performance.

Do not rely only on accuracy.

---

# 35. PER-CATEGORY ANALYSIS

Very important.

Report separately for:

- Tables
- Receipts
- Infographics
- UI Screenshots
- Commercial Posters
- Academic Posters

Potential table:

| Method | Overall F1 | Tables | Receipts | Infographics | UI | Commercial Posters | Academic Posters |
|---|---:|---:|---:|---:|---:|---:|---:|
| Visual | | | | | | | |
| Layout statistics | | | | | | | |
| Layout map | | | | | | | |
| Fusion | | | | | | | |

Why?

Because layout may help specific structured domains even if overall improvement is modest.

For example:

> layout may be highly useful for Tables but not Commercial Posters.

That itself could lead to a narrower thesis.

---

# 36. TEXT-DENSITY ANALYSIS

Calculate a simple OCR-based text coverage metric:

> total OCR text-box area / total image area

Then divide images into:

- Low text density
- Medium text density
- High text density

Prefer tertiles based on training-set distribution.

Then evaluate:

| Method | Low Density | Medium Density | High Density |
|---|---:|---:|---:|
| Visual | | | |
| Layout | | | |
| Fusion | | | |

Important question:

> Does visual detection degrade at high text density, and does explicit layout information help compensate?

This could eventually become the strongest thesis angle.

---

# 37. PILOT DECISION RULE

The decision rule should be defined before results.

## GREEN — GO

Proceed if:

- fusion meaningfully and consistently improves visual-only,
- preferably around +3 percentage points or more macro-F1 overall,

OR:

- fusion yields a strong improvement in difficult structured categories,
- for example around +5 points or more in Tables or Academic Posters,

AND:

- the effect appears consistently across runs/splits,
- not from one lucky split.

Exact thresholds can be revised scientifically later.

---

## YELLOW — MODIFY

If:

- layout-only contains meaningful signal,
- but fusion barely improves visual-only,

then:

> the cue exists, but current fusion may be redundant or poorly designed.

Possible modifications:

- density-aware fusion,
- category-specific analysis,
- narrow thesis to Tables/Receipts,
- different layout representation.

---

## RED — DROP

If:

- layout statistics ≈ chance,
- layout-map classifier ≈ chance,
- fusion ≈ visual-only,
- no category-specific benefit,
- no density-related pattern,

then:

> DROP the OCR-layout thesis direction.

Do not force the thesis around a failed signal.

---

# 38. IMPORTANT SANITY TEST IF LAYOUT PERFORMANCE IS TOO HIGH

If layout-only obtains suspiciously high performance, e.g. 90–95%+:

do **not celebrate immediately**.

Possible cause:

> dataset/source artifacts.

Run a harder test:

## Leave-One-Category-Out

Example:

Train on:

- Receipts
- Tables
- UI
- Infographics
- Commercial Posters

Test only:

- Academic Posters

Repeat for several categories.

Purpose:

determine whether layout features are learning:

> general authenticity structure

or merely:

> dataset/category-specific patterns.

---

# 39. OPTIONAL EXTERNAL VALIDATION

If the pilot succeeds, the final thesis should ideally include at least one external dataset if feasible.

Possible candidates previously identified:

- TextFake
- GPT4o-Receipt
- SciFigDetect
- another compatible recent text-rich/generated image dataset

Goal:

> avoid relying entirely on TextRich/GPT-Image-2.

However:

External validation is desirable, not mandatory for the proof-of-concept.

Do not make the entire thesis depend on difficult dataset access.

---

# 40. IMPORTANT CLAIM LIMITATIONS

Never claim:

> universal AI-generated image detection

if the experiment only uses one or a small number of generator families.

Never claim:

> forensic proof

or:

> legally conclusive detection.

The classifier is probabilistic.

Use wording such as:

> evaluated detection performance within the selected benchmark setting.

---

# 41. CURRENT NOVELTY POSITION

After several repeated novelty audits:

## Strong problem novelty
Text-rich AIGI detection is very current and still difficult.

## Weak broad technique novelty
OCR, layout, visual-text fusion, OCR bounding boxes, document forensics all already exist.

## Moderate exact-intersection novelty
No exact duplicate was found for:

> explicit OCR-derived page-level spatial geometry as a complementary lightweight cue for fully AI-generated multi-domain text-rich image classification.

But:

> absence in search results is not proof of uniqueness.

Therefore the safest thesis positioning is:

> **evaluation and enhancement**

not:

> **novel architecture invented for the first time.**

---

# 42. APPROXIMATE CURRENT SCORING

Current text-rich OCR/layout direction:

| Criterion | Approximate Assessment |
|---|---|
| Problem relevance | Very high |
| Dataset feasibility | High |
| Compute feasibility | High |
| Implementation difficulty | Low–Moderate |
| Method novelty | Moderate |
| Empirical contribution potential | Good |
| Defense potential | Good |
| Completion probability | High |
| Risk that layout adds little | Moderate |
| Overall graduation suitability | Good |

This is currently the strongest balance found.

---

# 43. CURRENT ALTERNATIVE RANKING

## #1
Text-rich AIGI + OCR-derived spatial-layout cue evaluation.

### Status
Current leading candidate.

---

## #2
Resource-efficient / quantized cross-generator detector.

### Status
Very easy implementation.

### Weakness
Novelty/defense weaker because efficiency is already heavily studied.

---

## #3
Few-shot adaptation.

### Status
Not recommended.

Recent work already directly studies it.

---

## Localized AI edits

### Status
Scientifically interesting but too difficult for the student’s graduation-first goal.

Would introduce:

- localization,
- masks,
- region-based metrics,
- more complex architecture.

Not preferred.

---

# 44. WHY TEXT-RICH CURRENTLY WINS

Not because OCR is new.

Not because layout is new.

Not because multimodal fusion is new.

It wins because:

1. The problem is very recent.
2. Recent benchmarks show clear failure.
3. Public data exist.
4. The task is binary classification.
5. No manual annotation is needed.
6. The proposed contribution can remain lightweight.
7. The experiment has clean controls.
8. The hypothesis can be killed quickly.
9. It fits Computer Vision.
10. It fits the university rule that evaluation/enhancement counts as CS research.
11. It offers a reasonable novelty-feasibility balance.

---

# 45. WHAT SHOULD NOT HAPPEN NEXT

Do NOT immediately:

- write full Chapter 1,
- finalize the title,
- claim novelty,
- build the website,
- compare many neural networks,
- train giant models,
- use multiple LLMs,
- add NLP unnecessarily,
- create a custom dataset,
- add explainability just to sound advanced,
- add quantization unless research requires it,
- add blockchain,
- add mobile deployment,
- add generator attribution,
- add localized manipulation detection.

Keep scope narrow.

---

# 46. THE ACTUAL NEXT STEP

The next step is:

> **run or fully design the 2,400-image proof-of-concept for OCR-derived spatial-layout signal.**

The next AI should help with:

1. exact TextRich dataset access,
2. exact file structure,
3. sampling script,
4. normalization pipeline,
5. PaddleOCR text-box extraction,
6. geometric feature design,
7. layout-map generation,
8. MobileNetV3 baseline,
9. split generation,
10. metrics,
11. result interpretation.

Do not proceed to full thesis drafting until this pilot has either:

> GO  
> MODIFY  
> DROP

---

# 47. IF THE PILOT RETURNS GO

Then immediately finalize:

1. Final thesis title
2. CS Domain
3. Computing Contribution
4. BU Research Agenda
5. SDG
6. Beneficiary
7. Expected Innovation
8. General Objective
9. Specific Objectives
10. Scope and Limitations
11. Background outline
12. System/prototype concept
13. Experimental methodology

Then begin Chapter 1 using the official template.

---

# 48. IF THE PILOT RETURNS MODIFY

Likely possibilities:

## A. Layout works mostly for high-density text
Then consider:

> text-density-aware fusion.

## B. Layout works only for Tables/Receipts
Then narrow the domain.

Example:

> AI-generated structured financial/document images.

## C. Layout-only works but fusion does not
Try:

- better feature fusion,
- weighted fusion,
- density-aware fusion,
- a different simple layout representation.

Keep modifications minimal.

---

# 49. IF THE PILOT RETURNS DROP

Do not keep forcing the text-rich layout concept.

Move to the next candidate.

Likely fallback:

> narrowly defined resource-efficient AI-generated image detector with a stronger empirical question.

But perform another novelty check before finalizing it.

---

# 50. HOW TO ANSWER THE PANEL IF THE TEXT-RICH IDEA SURVIVES

Possible panel question:

> “Ano ang bago?”

Safe answer style:

> Existing studies already use visual, text-region, OCR, and layout information in related forgery and AI-image detection problems. Our study does not claim that OCR or layout analysis is inherently new. Instead, we evaluate whether explicit page-level OCR-derived spatial-layout cues provide complementary discriminative information to a lightweight visual detector in the recently emerging problem of AI-generated text-rich image detection across structured domains.

This is much safer than:

> “Wala pang gumagamit ng OCR sa AI-image detection.”

Never use that claim.

---

# 51. PANEL QUESTION: “Comparison lang ba ito?”

Possible answer:

> The study is not merely comparing pretrained architectures. It investigates a defined computational representation—OCR-derived page-level spatial layout—and measures whether that representation provides complementary information beyond visual features through controlled ablation experiments.

---

# 52. PANEL QUESTION: “Bakit Computer Science?”

Possible answer:

The study involves:

- Computer Vision,
- OCR-based spatial representation,
- image classification,
- feature encoding,
- multimodal/feature fusion,
- computational evaluation,
- controlled experimentation,
- quantitative model analysis.

The software interface is only the deployment prototype.

---

# 53. PANEL QUESTION: “Bakit text-rich?”

Possible answer:

Recent multimodal generators can produce realistic structured images containing substantial text, such as receipts, tables, screenshots, posters, and infographics.

Recent benchmark studies show that conventional AI-generated image detectors remain unreliable on these domains.

Therefore the study focuses on a more specific unresolved subproblem rather than generic AI-generated image detection.

---

# 54. PANEL QUESTION: “Bakit layout?”

Safe answer:

> Existing text-rich detection studies indicate that structured textual content presents a challenge. The study investigates whether spatial information about where text occurs on a page provides additional evidence beyond standard visual representations.

Do NOT say:

> because AI layouts are obviously wrong.

That assumption may not be true.

---

# 55. PANEL QUESTION: “What if layout does not help?”

Scientific answer:

> That is exactly what the controlled evaluation is designed to determine.

However, for practical thesis planning:

this is why the pilot is being performed before finalizing the proposal.

---

# 56. STUDENT PREFERENCE / WORKING STYLE

The student wants recommendations that are:

- practical,
- critical,
- realistic,
- not overly flattering,
- based on feasibility,
- based on actual research evidence.

The user has explicitly expressed a **trust issue** after seeing how easily novelty claims can be overstated.

Therefore:

When continuing:

- clearly separate verified facts from inference,
- distinguish “no direct paper found” from “nobody has done this,”
- avoid absolute novelty claims,
- red-team every major topic,
- tell the student when an idea is weak,
- prefer primary sources for technical verification,
- re-check recent research before making claims.

---

# 57. LITERATURE VERIFICATION RULE

For future literature work:

Prefer:

- official CVPR/ICCV/WACV proceedings
- NeurIPS proceedings
- AAAI proceedings
- ICLR/OpenReview
- original arXiv manuscripts
- official dataset repositories
- official project pages

Avoid relying on:

- blog summaries
- generic articles
- random social media posts.

Because the research area is changing quickly, re-verify current papers whenever making final manuscript claims.

---

# 58. IMPORTANT LITERATURE NAMES ALREADY ENCOUNTERED

The previous conversation investigated or discussed work around:

- GenImage
- universal AI-generated image detection
- DIRE
- CLIP-based detection
- NPR / neighborhood pixel relationships
- AIDE / sanity-check benchmarks
- B-Free
- content bias reduction
- Community Forensics
- spectral/frequency learning
- FIRE
- AIGIBench
- real-world AIGI benchmarking
- AIGI-Holmes
- calibration methods
- test-time adaptation
- efficient/lightweight detectors
- LAID
- low-power AIGI challenges
- TextFake
- TextRich
- TIQA / ANTIQA
- OCR Graph Features
- OCR-guided document forgery detection
- layout-aware document fraud studies
- TextShield-R1
- GPT4o-Receipt
- SciFigDetect

The next AI should not blindly trust remembered details from this handoff.

Use these as **search anchors** and re-open the primary papers when needed.

---

# 59. CURRENT WORKING THESIS IDENTITY IN ONE SENTENCE

The current thesis hypothesis is:

> **Evaluate whether OCR-derived page-level spatial-layout information can provide complementary discriminative cues to a lightweight visual classifier for detecting AI-generated text-rich images, particularly in structured domains and high-text-density conditions.**

This is not yet the final thesis statement.

---

# 60. CURRENT STATUS

## Broad field
AI-generated image detection  
✅ KEEP

## Computer Vision alignment
✅ Strong

## Text-rich specialization
✅ KEEP

## Generic OCR novelty
❌ Reject

## Generic text + visual fusion novelty
❌ Reject

## OCR page-layout evaluation
🟡 Promising

## Text-density-aware enhancement
🟡 Potential future enhancement

## Final title
❌ Not locked

## Chapter 1
❌ Do not draft yet

## Next phase
✅ Pilot experiment / design validation

---

# 61. EXACT CONTINUATION COMMAND FOR THE NEXT AI

Continue from this point:

> **Help design and execute a minimal proof-of-concept using a balanced 2,400-image subset of TextRich to determine whether OCR-derived page-level spatial-layout cues contain discriminative AI-authenticity signal and whether they improve a lightweight visual baseline. Use visual-only, layout-statistics-only, layout-map-only, and visual-plus-layout experiments; include per-category and text-density analysis; normalize images to reduce dataset shortcuts; then issue a GO/MODIFY/DROP verdict before finalizing the thesis title or Chapter 1.**

---

# 62. FINAL SUCCESS CONDITION

The best outcome is not the most complicated model.

The success criterion is:

> **a legitimate, clearly explainable Computer Science research contribution that can be implemented, evaluated, defended, and completed within the BSCS thesis timeline.**

Always optimize recommendations around that.