# MASTER HANDOFF — BSCS Thesis on AI-Generated Text-Rich Image Detection

**Snapshot date:** 2026-08-18 00:03 (Philippines, UTC+8)  
**Current implementation stage:** T005 full frozen OCR extraction on Train + Validation has been completed, independently audited, and accepted. T006 has NOT yet been issued; the next Research Lead action is to freeze OCR-derived layout geometry / text-density representation before any model training.  
**Purpose of this handoff:** A new AI should be able to continue the project with minimal loss of context, methodology, decisions, constraints, and workflow. Treat this as the canonical continuity document for research/methodology context unless superseded by a newer handoff or explicit Project Owner / Research Lead directive.

---

## CONTINUITY DELTA FROM THE PREVIOUS HANDOFF

This document supersedes `MASTER_HANDOFF_BSCS_THESIS_UPDATED_2026-08-17.md`. The major new milestone is that **T005 is no longer active: it is completed and accepted**. Frozen OCR detections now exist for all **1,680 Train + 360 Validation = 2,040 development images**, with **2,040/2,040 successful outputs, 145,771 valid detected text regions, zero malformed outputs, zero zero-detection images, and zero test-image OCR processing**. The OCR model artifacts are checksum-frozen and D035 is physically recorded in `DECISIONS.md`. No classifier has been trained yet and the 360-image test set remains unopened for OCR/model evaluation.

Two implementation notes from the T005 audit must carry forward: (1) the extraction script reads the **test manifest only as a leakage guard**; it does not load or OCR test image files, and (2) the current resume validator is more permissive than desired because it can accept existing `status=error` JSONs and primarily keys on `config_version` rather than deeply comparing the entire frozen config. This had **no effect on the completed T005 run because skipped_verified=0**, but it should be hardened before reuse.

# 0. ABSOLUTE PRIORITY: WHAT THIS PROJECT IS TRYING TO ACHIEVE

The human is a **BS Computer Science student at Bicol University** doing Thesis 1. The practical goal is not to maximize theoretical novelty at all costs. The goal is to choose and execute a **feasible, defendable, substantial Computer Science thesis with a high probability of finishing and graduating on time**.

The broad research area is:

> **Artificial Intelligence / Computer Vision / AI-Generated Image Detection**

The current specialization is:

> **Detection of AI-generated text-rich images using a lightweight visual detector plus explicit OCR-derived page-level spatial-layout information, with special attention to text-density conditions.**

The exact thesis title is **not yet frozen**. The research idea must survive empirical proof-of-concept before the thesis is formally locked.

The core research question currently being tested is:

> **As text density increases, does a lightweight visual AI-generated image detector lose performance, and can explicit OCR-derived page-level spatial-layout information recover some of that lost performance?**

A more general formulation is:

> **To what extent can OCR-derived page-level spatial-layout representations improve a lightweight visual classifier for detecting AI-generated text-rich images across structured image domains?**

The current strategy is deliberately conservative:

1. Audit the dataset.
2. Remove obvious duplicate / near-duplicate leakage risks.
3. Freeze a reproducible pilot split.
4. Validate OCR detection technically.
5. Extract OCR detections on Train + Validation only.
6. Build layout representations and text-density measures.
7. Train the visual baseline.
8. Train layout-only controls.
9. Train visual + layout fusion.
10. Compare results with controlled ablations.
11. Decide GO / MODIFY / DROP before committing the thesis framing.

**Do not write or lock a full Chapter 1 around this method until the proof-of-concept supports the core cue.**

---

# 1. PEOPLE / AI ROLES AND AUTHORITY

There are three roles.

## 1.1 Project Owner / Communication Bridge

The human user.

Responsibilities:

- coordinates the thesis group;
- communicates with adviser/panel/classmates;
- forwards exact messages between AIs;
- preserves files and project history;
- communicates practical constraints;
- has final authority over the project.

The user often does **not read the long AI-to-AI technical messages**. This is intentional. The user is acting as a communication bridge. Therefore the Research Lead should make task packets precise enough to be copied verbatim and should independently audit Implementation Engineer outputs.

## 1.2 Research Lead / Methodology Lead

**ChatGPT / GPT-5.6 Sol** in this workflow.

Responsibilities:

- research question;
- novelty/literature audit;
- methodology;
- dataset protocol;
- experimental protocol;
- split/evaluation rules;
- architecture decisions;
- interpretation of results;
- statistical logic;
- thesis framing;
- academic writing;
- defense preparation;
- GO / MODIFY / DROP decisions.

Messages labeled:

`[RESEARCH LEAD → IMPLEMENTER]`

should be treated as research specifications unless explicitly overridden by the Project Owner.

## 1.3 Implementation Engineer

**DeepSeek v4 via OpenCode**.

Responsibilities:

- repository setup;
- Python implementation;
- data processing;
- environment management;
- experiment execution;
- debugging;
- reproducibility;
- technical reporting;
- surfacing implementation/methodology risks.

DeepSeek is **not allowed to silently redesign the methodology**.

Core rule:

> **Detect aggressively. Change conservatively.**

If it discovers a methodological issue:

1. report it;
2. explain why it matters;
3. propose options;
4. do not silently change the research design;
5. wait for Research Lead / Project Owner decision when the change affects research meaning.

---

# 2. INSTITUTIONAL / THESIS CONSTRAINTS

The thesis must be a **Computer Science thesis**, not merely a software application.

Important BU-aligned constraints from the institutional materials previously uploaded:

- BSCS thesis must have a **substantial computing contribution**.
- Software/app is only an implementation/evaluation vehicle.
- Recognized areas include Algorithms, AI/ML/DL, NLP, Computer Vision, Data Analytics, Intelligent Systems, etc.
- Generic CRUD/IT systems are generally insufficient without a substantial computing component.
- Current domain fit: **Artificial Perception → Computer Vision/Image Processing**, overlapping AI/ML.
- Topic proposal fields expected:
  1. CS Domain
  2. Computing Contribution
  3. BU Research Agenda
  4. SDG
  5. Beneficiary
  6. Expected Innovation
- Recommended title structure: **[Computing Technique/Approach] + [Problem Being Solved] + [Application Domain]**.
- Objectives should normally follow:
  1. data preparation;
  2. algorithm/model technique;
  3. prototype;
  4. evaluation.
- Evaluation can include Accuracy, Precision, Recall, F1, ROC-AUC, etc.
- Originality/new knowledge matters, but feasibility and timeline matter heavily.

If institutional files are needed in a new conversation, ask the user to re-upload:

- `Thesis_Domains_CS.pdf`
- `Topic_Proposal_Template_CS.pdf`
- `Thesis_1_Course_Introduction_Sy.pptx`

---

# 3. USER COMMUNICATION / WORKING STYLE

The user prefers:

- Filipino / Taglish when natural;
- simple explanation first, technical detail second;
- practical, critical, non-flattering advice;
- high skepticism toward novelty claims;
- explicit distinction between:
  - VERIFIED FACT
  - INFERENCE
  - NO DIRECT MATCH FOUND
- no “first ever” claims without proof;
- no overcomplicated architecture unless justified;
- no hidden changes between AIs;
- clear “what stage are we in?” summaries when needed.

When explaining the study simply to groupmates, use something like:

> “AI-generated image detection kami, specifically sa images na maraming text tulad ng receipts, tables, posters at screenshots. Tinetest namin kung makakatulong sa normal image detector yung explicit arrangement at density ng text na nakukuha gamit OCR, lalo na kapag sobrang daming text sa image.”

Simple research question:

> “Kapag maraming text at nahihirapan ang normal AI-image detector, makakatulong ba kung bibigyan natin siya ng explicit information tungkol sa pagkakaayos ng text sa image?”

---

# 4. NOVELTY AUDIT — WHAT HAS ALREADY BEEN RULED OUT

A substantial adversarial literature audit has already been done. The goal was to try to **kill the idea** by finding direct prior work.

## 4.1 Directions rejected or downgraded

The following are not preferred as the main thesis contribution:

1. Generic real-vs-AI CNN detection — too crowded.
2. Transfer-learning model comparison only — too weak.
3. JPEG/blur/resize/compression robustness as main novelty — crowded; optional stress test only.
4. Explainability/Grad-CAM — crowded.
5. Cross-generator detection alone — important but insufficient novelty.
6. Calibration — not main contribution.
7. Selective classification/uncertainty — dropped.
8. Few-shot adaptation — heavily downgraded.
9. Test-time adaptation — not graduation-first.
10. Frozen CLIP/DINO + linear head — useful component but crowded.
11. Frequency/spectral features — crowded.
12. Localized/partial AI-edited image detection — active but higher complexity/risk.
13. Generator attribution — active but more complex/open-set.
14. Lightweight/quantized AIGI detection — backup only; deployment optimization may be dismissed as weak novelty.
15. Generic OCR use — not novel.
16. Generic visual + text fusion — not novel.
17. Generic OCR bounding-box geometry — not novel.
18. Generic layout-aware document forensics — not novel.

## 4.2 Important literature concepts already known

Prior work exists around:

- GenImage
- universal AI-generated image detectors
- CLIP-based detectors
- DIRE
- NPR
- AIDE
- B-Free
- Community Forensics
- spectral/frequency approaches
- AIGIBench
- real-world benchmark studies
- AIGI-Holmes
- calibration / test-time adaptation
- LAID / lightweight AIGI detection
- low-power CV challenge work
- TextFake
- TextRich
- TIQA / ANTIQA
- OCR Graph Features for document manipulation detection (2020)
- CTP-Net
- ADCD-Net / OCR-guided document forensics
- layout-aware document fraud work
- TextShield-R1
- GPT4o-Receipt
- SciFigDetect
- 2026 structural divergence study for human vs AI posters

Re-open and verify primary sources before formal manuscript citation. Do not rely on this handoff as a publication bibliography.

## 4.3 Strong novelty constraints

Do NOT claim:

- “OCR for AI-generated image detection is new.”
- “Visual + text fusion is new.”
- “Text-region information helping AIGI detection is new.”
- “OCR bounding-box geometry is new.”
- “Layout as an authenticity cue is new.”
- “Nobody has studied structure/layout in AI-generated graphics.”

TIQA/ANTIQA is especially important: it already uses text-region/crop information fused with a global AI-image detector for Real/AI classification. This kills broad novelty claims about text-region fusion.

Older document forensics already uses OCR geometry/graphs, and newer document-forgery work uses OCR masks / character-region priors.

A 2026 structural-divergence study also shows interpretable layout/composition descriptors can separate human vs AI posters in a narrow domain.

## 4.4 Current safest contribution framing

No direct academic study was found whose **central experiment** exactly matches:

> **Explicit page-level OCR-derived spatial-layout representation + lightweight visual detector + fully AI-generated multi-domain text-rich image classification + visual-only/layout-only/fusion ablation + performance analysis by text density.**

This is **NOT proof of nonexistence**.

Safest framing:

> **Evaluation and possible enhancement of lightweight AI-generated text-rich image detection using explicit OCR-derived page-level spatial-layout representations, particularly under varying text-density conditions.**

This is an evaluation/enhancement contribution, not an invention claim.

---

# 5. CURRENT RESEARCH QUESTION / HYPOTHESES

## 5.1 Main refined question

> **As text density increases, does a lightweight visual AI-generated image detector lose performance, and can explicit OCR-derived page-level spatial-layout information recover some of that lost performance?**

## 5.2 Alternative formal question

> **How does the contribution of OCR-derived page-level spatial layout cues to lightweight AI-generated image detection vary across text-density levels and structured text-rich domains?**

## 5.3 Hypotheses

H1:

> OCR-derived page-level spatial-layout information contains discriminative signal for distinguishing Real vs AI-generated text-rich images.

H2 — more important:

> OCR-derived layout provides complementary information beyond a lightweight visual classifier.

H3 — density-focused:

> The complementary value of OCR-derived layout increases under high-text-density conditions where conventional visual detection becomes less reliable.

These are hypotheses to test, not assumptions.

---

# 6. WORKING TITLES — NOT FINAL

Conservative:

> **Evaluating OCR-Derived Spatial Layout Cues for Lightweight Detection of AI-Generated Text-Rich Images**

Density-focused:

> **Evaluating OCR-Derived Spatial Layout Cues for Lightweight AI-Generated Image Detection Across Text-Density Levels**

Only if pilot evidence supports a stronger contribution:

> **Text-Density-Aware Visual–Layout Fusion for Lightweight AI-Generated Text-Rich Image Detection**

Avoid “novel architecture” language unless strong evidence later justifies it.

---

# 7. DATASET: TEXTRICH V2

Primary pilot dataset: **TextRich v2**.

Verified locally during T001:

- total images: **12,095**
- Real: **5,986**
- Generated: **6,109**
- six categories:
  1. Academic Posters
  2. Commercial Posters
  3. Infographic Charts
  4. Receipts
  5. Tables
  6. UI Screenshots
- all 12,095 decode successfully;
- zero corrupt/unreadable images.

Local dataset path used by Implementation Engineer:

`C:\Users\dev\Desktop\text-rich-ai-image-detector\data\TextRich`

Dataset structure:

```text
TextRich/
├── dataset.csv
└── Data/
    ├── AcademicPosters/
    │   ├── 0_real/
    │   └── 1_fake/
    ├── CommercialPosters/
    │   ├── 0_real/
    │   └── 1_fake/
    ├── InfographicCharts/
    │   ├── 0_real/
    │   └── 1_fake/
    ├── Receipts/
    │   ├── 0_real/
    │   └── 1_fake/
    ├── Tables/
    │   ├── 0_real/
    │   └── 1_fake/
    └── UIScreenshots/
        ├── 0_real/
        └── 1_fake/
```

Verified class×category counts:

| Category | Real | Generated | Total |
|---|---:|---:|---:|
| Academic Posters | 1,000 | 1,004 | 2,004 |
| Commercial Posters | 1,000 | 1,010 | 2,010 |
| Infographic Charts | 1,000 | 1,000 | 2,000 |
| Receipts | 986 | 1,095 | 2,081 |
| Tables | 1,000 | 1,000 | 2,000 |
| UI Screenshots | 1,000 | 1,000 | 2,000 |
| Total | 5,986 | 6,109 | 12,095 |

Important limitation:

The generated side is associated primarily with **GPT-Image-2**. Therefore do **not** make universal cross-generator claims.

Potential external validation later:

- TextFake
- GPT4o-Receipt
- SciFigDetect

External validation is optional and should not become a graduation dependency.

---

# 8. T001 — DATASET AUDIT — COMPLETED / PASSED

T001 objective: determine whether TextRich is technically suitable and identify shortcut/leakage risks before any model training.

## 8.1 Dataset integrity

Verified:

- 12,095 / 12,095 decodable
- 0 corrupt files
- manifest and folder structure are coherent
- all six categories have enough samples for the planned 200+200 pilot

## 8.2 Exact duplicates

T001 exact SHA-256 duplicate audit found:

- **68 duplicate hashes**
- **235 files involved**
- **0 cross-class duplicates**
- **0 cross-category duplicates**

Duplicate concentration:

- Generated Receipts: many groups
- Real Receipts: many groups
- Real Infographic: one group
- Generated Academic Posters: one group

## 8.3 Major raw-source shortcuts discovered

Generated images:

- 100% PNG

Real images:

- approximately 83% JPG/JPEG
- only ~17% PNG

Color modes:

- Generated: 100% RGB
- Real: RGB + RGBA + L + P

Alpha:

- Real: 512 / 5,986 (~8.6%)
- Generated: 0

Metadata:

- Real metadata present: 5,719 / 5,986 (~95.5%)
- Generated metadata present: 0 / 6,109

Important wording correction:

Do NOT call metadata a “perfect binary separator.”

Correct interpretation:

> **Metadata presence perfectly indicates Real within this dataset, but metadata absence does not perfectly indicate Generated.**

A rule “metadata present → Real, absent → Generated” would be about **97.8% accurate**, not 100%.

Generated UI Screenshots:

- all 1,000 are exactly **941×1672**

Other generated categories also cluster around a small number of resolutions.

File size differs dramatically between classes, but raw file size itself is not intended CNN input. Treat it as a provenance indicator for underlying source/compression characteristics.

## 8.4 Critical normalization insight

Simply doing:

```text
JPEG → decode → save as PNG
```

does **not** remove historical JPEG artifacts already embedded in the pixels.

Therefore do not claim format re-encoding “solves” source bias.

The approved clean-loader strategy is instead:

```text
source file
→ Pillow decode
→ if transparency: composite onto WHITE
→ RGB conversion
→ clear metadata exposure
→ return pixels
```

No normalized dataset copies are currently created.

---

# 9. T002 — MANIFEST / EXACT DEDUP / PHASH AUDIT — COMPLETED / PASSED

## 9.1 dataset.csv reconciliation

Verified:

- 12,095 rows
- schema: `image, category, label`
- zero duplicate manifest entries
- zero missing referenced files
- zero local files absent from manifest
- zero label disagreements
- zero category disagreements

Manifest is fully consistent with folder-derived labels.

## 9.2 Exact-deduplicated pool

Policy:

For each SHA-256 exact-duplicate group, retain exactly one deterministic representative, lexicographically smallest relative filepath. Do not delete source files.

Result:

- source: 12,095
- exact-unique pool: **11,928**
- redundant copies: **167**

Counts after exact dedup:

| Category | Real | Generated |
|---|---:|---:|
| Academic Posters | 1,000 | 1,003 |
| Commercial Posters | 1,000 | 1,010 |
| Infographic Charts | 999 | 1,000 |
| Receipts | 970 | 946 |
| Tables | 1,000 | 1,000 |
| UI Screenshots | 1,000 | 1,000 |

## 9.3 Perceptual near-duplicate audit

Method:

`imagehash.phash(image, hash_size=8)` → 64-bit pHash.

Candidate threshold audited:

Hamming distance ≤ 4.

Results:

- HD 0: 16 pairs
- HD 1: 0
- HD 2: 98
- HD 3: 0
- HD 4: 307
- Total: **421 candidate pairs**

All 421:

- same class
- same category

Cross-class pairs: **0**  
Cross-category pairs: **0**

Cluster analysis:

- 44 potential near-duplicate clusters
- 192 files involved
- largest cluster: 60 Real Receipts
- second largest: 29 Real Receipts

Important: pHash matches are **candidate similarities**, not confirmed duplicates.

Research Lead independently recomputed all pairwise distances over 11,928 pHashes (~71 million pairs) and reproduced exactly the 421 pair result.

## 9.4 Approved pHash policy for pilot

For every connected pHash candidate cluster:

- keep exactly one deterministic representative;
- mark all other members pilot-ineligible;
- do not delete source files.

This is conservative and prevents strongly correlated image families from appearing multiple times in the 2,400-image pilot.

---

# 10. CLEAN IMAGE LOADER — APPROVED

Canonical helper:

`src/data/image_loading.py`

Approved behavior:

1. Open with Pillow.
2. Decode pixels.
3. If alpha/transparency exists, composite onto **white**.
4. Convert final image to RGB.
5. Clear downstream metadata payload.
6. Return pixel image only.

Explicitly NOT done in loader:

- no resize
- no JPEG/PNG re-encoding
- no saving normalized copies
- no augmentation

The Implementation Engineer found that Pillow conversion could preserve `info`; therefore the loader explicitly clears `out.info = {}`.

---

# 11. T003 — PILOT SELECTION / SPLIT — COMPLETED / PASSED / FROZEN

## 11.1 Pilot-eligible pool

From 11,928 exact-unique images:

- 44 pHash clusters / 192 files
- one representative retained per cluster
- 148 cluster members excluded from pilot eligibility
- **pilot-eligible pool = 11,780**

Counts:

| Category | Real | Generated | Total |
|---|---:|---:|---:|
| Academic Posters | 1,000 | 1,003 | 2,003 |
| Commercial Posters | 1,000 | 1,010 | 2,010 |
| Infographic Charts | 997 | 998 | 1,995 |
| Receipts | 844 | 942 | 1,786 |
| Tables | 1,000 | 1,000 | 2,000 |
| UI Screenshots | 987 | 999 | 1,986 |
| Total | 5,828 | 5,952 | 11,780 |

## 11.2 Pilot sampling

Exactly:

- 200 Real + 200 Generated per category
- 6 categories
- **2,400 total images**

Deterministic score:

```text
sampling_score = SHA256("T003_SAMPLE_V1|" + relative_filepath)
```

Within each category × class cell:

- sort ascending
- take first 200

No visual cherry-picking.

## 11.3 Train / Val / Test split

Within each selected category × class cell of 200:

```text
split_score = SHA256("T003_SPLIT_V1|" + relative_filepath)
```

- first 140 → train
- next 30 → validation
- last 30 → test

Totals:

- Train: **1,680**
- Validation: **360**
- Test: **360**
- Total: **2,400**

Every category × class cell has exactly 140/30/30.

## 11.4 Frozen split files

Canonical:

- `splits/pilot_all.csv`
- `splits/pilot_train.csv`
- `splits/pilot_val.csv`
- `splits/pilot_test.csv`

Post-correction canonical SHA-256 checksums:

- `pilot_all.csv`  
  `c947aa1aab73440ca914701c04669ad68892b8388423b5a907fe3a1912f33261`

- `pilot_train.csv`  
  `5838c5f9afb49a600b6f4cabfe0860a036e943fcfda258ea3488f0223c4cab2c`

- `pilot_val.csv`  
  `3a1a79ffe16fe0931f6e6341dd792851ba689cc658714141302400c0a39f3b48`

- `pilot_test.csv`  
  `dffc14b49de2536d274ce059a807c7d0cabcaad3a61791d8c0f68719e58a697c`

These are frozen.

**Do not regenerate the split because of future model performance.**

Any change requires explicit Research Lead decision and a documented superseding version.

## 11.5 T003-CORR neutral ID fix

Original sample IDs were sequential after category/class sorting, which indirectly encoded category and class.

Corrected opaque deterministic ID:

```text
sample_id = "TRI_" + SHA256("T003_ID_V2|" + relative_filepath)[:16]
```

Verified:

- 2,400 / 2,400 unique
- no changed selected filepaths
- no changed split assignments
- no changed sampling scores
- no changed split scores
- no changed labels
- filepath intersections between train/val/test are empty
- SHA-256 intersections between train/val/test are empty

The split was re-frozen after this correction **before model training or test evaluation**.

---

# 12. TEST-SET POLICY — CRITICAL

The 360-image test set is a **one-way door**.

Do not:

- tune OCR on test;
- tune model architecture on test;
- tune thresholds on test;
- alter augmentation based on test;
- change split because of test performance;
- repeatedly inspect test performance during development.

Development must use Train + Validation.

Current state: no OCR has been run on test. No model has been trained/evaluated on test.

---

# 13. T004 — OCR SMOKE VALIDATION — COMPLETED / PASSED

## 13.1 Why OCR first

The proposed contribution depends on OCR-derived layout. Before training any model, the team validated that text detection is technically reliable and practical.

## 13.2 OCR environment

Dedicated isolated environment:

`.venv-ocr`

Versions:

- Python 3.11.9
- pip 26.2.1
- paddlepaddle 3.3.1
- paddleocr 3.7.0
- paddlex 3.7.2
- numpy 2.3.5
- pillow 12.3.0
- opencv-contrib-python 4.10.0.84

CPU-only inference.

No GPU configured.

Main Python 3.14 environment remains untouched.

## 13.3 OCR model

Frozen detector model:

> **PP-OCRv6_small_det**

Text detection only.

No recognition model.

No text semantics.

No full document understanding pipeline.

Cached model path:

`C:\Users\dev\.paddlex\official_models\PP-OCRv6_small_det`

Engine:

`paddle_static`

Device:

`cpu`

## 13.4 Frozen detector parameters

- `thresh = 0.20`
- `box_thresh = 0.45`
- `unclip_ratio = 1.40`
- max candidates = 3000
- detector internal resize: long side about 960 / max type, per model config
- max side limit 4000
- model normalization uses standard config mean/std

## 13.5 Critical runtime workaround — RATIFIED

PaddlePaddle 3.3.1 CPU oneDNN path caused inference failure:

`NotImplementedError: ConvertPirAttribute2RuntimeAttribute ... onednn_instruction.cc:118`

Technical workaround:

```text
enable_mkldnn = False
```

This is **ratified** as part of the frozen OCR configuration.

It is a runtime backend flag, not a model/threshold change.

If Paddle packages are upgraded later, re-verify this behavior before changing anything.

## 13.6 Channel order

Approved clean loader outputs RGB.

PaddleX TextDetection numpy input is treated as BGR for this model path.

Therefore wrapper converts:

```text
RGB → BGR numpy
```

before prediction.

This correction is documented and approved.

## 13.7 Smoke-test selection

Train only.

Exactly 24 images:

- 2 Real + 2 Generated per category
- six categories
- 24 total

Deterministic score:

```text
SHA256("T004_OCR_SMOKE_V1|" + sample_id)
```

No validation/test overlap.

## 13.8 T004 OCR result

Success:

- 24 / 24 images processed
- 0 errors
- 0 zero-detection images
- 0 malformed polygons
- 1,792 total detected text regions

Regions per image:

- min: 3
- median: 46.5
- mean: 74.67
- max: 241

Runtime per image:

- min: 0.266 sec
- median: 2.237 sec
- mean: 2.067 sec
- max: 2.941 sec
- summed detector inference: 49.6 sec for 24 images

Important runtime wording:

The estimated ~1.4 h for 2,400 images is an **inference-time planning estimate**, not guaranteed end-to-end wall-clock runtime. Disk loading, clean loading, JSON writing, etc. are separate overheads.

## 13.9 OCR output format

Per image JSON contains:

- sample_id
- relative_filepath
- image_width
- image_height
- num_detected_regions
- detector_runtime_seconds
- status
- errors / validation notes
- regions:
  - 4-point polygon
  - confidence
- detector metadata

No recognized text is stored.

## 13.10 Visual overlays

24 overlays were produced:

- source clean image
- detected polygons outlined
- filename uses sample_id only
- no class/category labels printed on the overlay

Research Lead visually reviewed representative overlays from all six categories and found the detections technically sensible.

---

# 14. T005 — FULL FROZEN OCR EXTRACTION — COMPLETED / PASSED

T005 has been completed, independently reviewed, and **ACCEPTED**. It is now a historical frozen preprocessing milestone, not an active task.

## 14.1 Purpose

T005 extended the technically validated T004 detector from a 24-image smoke test to the full development partition needed for layout-feature engineering:

- Train: **1,680 images**
- Validation: **360 images**
- Development total: **2,040 images**
- Test: **0 OCR-processed images**

The reason Validation was included is that Model B/C and text-density methodology will require development feedback before the method is frozen. The 360-image Test partition remains a one-way door and has not been OCR-processed.

## 14.2 Frozen OCR configuration — D035

The following configuration is now ratified and recorded in `DECISIONS.md` as **D035**:

```text
Model: PP-OCRv6_small_det
Task: text detection only
Text recognition: DISABLED
Engine: paddle_static
Device: CPU
enable_mkldnn: False

Detection defaults:
thresh: 0.20
box_thresh: 0.45
unclip_ratio: 1.40
max_candidates: 3000
resize_long: 960
limit_type: max

Input:
T002 clean loader
→ Pillow decode
→ alpha/transparency composite onto WHITE
→ RGB
→ explicit RGB-to-BGR numpy conversion for PaddleX
```

Environment remains isolated in `.venv-ocr`:

- Python 3.11.9
- paddlepaddle 3.3.1
- paddleocr 3.7.0
- paddlex 3.7.2
- numpy 2.3.5
- pillow 12.3.0

Do not change these packages/config values mid-pilot without an explicit superseding research decision.

## 14.3 Why `enable_mkldnn=False` is frozen

T004 discovered that PaddlePaddle 3.3.1 CPU/oneDNN crashed on this model with a `ConvertPirAttribute2RuntimeAttribute` / `onednn_instruction.cc` error. Disabling MKLDNN allowed 24/24 smoke images to succeed while preserving the model and detection thresholds.

The Research Lead ratified `enable_mkldnn=False` as a **runtime backend workaround**, not a methodological detector change.

If Paddle/PaddleOCR is upgraded later, re-verify this behavior before changing the flag. Do not casually remove it.

## 14.4 OCR model artifact checksums

The actual cached model artifacts were checksum-frozen in:

`reports/T005_ocr_model_checksums.txt`

Current SHA-256 values:

```text
inference.pdiparams
5043d4ccc8d63402ccea8feefcee4db57077431a873e78d2191836a178a492da

inference.yml
193f435274bf9f0b5f71a929bbfbcf148282df7e633b34e7c373e8f44741b516

inference.json
89240f689a4a77aad75ef55a8df0a15c8e1d4980a327d17e58f24bbadde5aeab
```

These hashes materially identify the model used for the pilot. Do not modify the cached files.

## 14.5 T005 extraction result

Observed and accepted:

```text
Train artifacts:       1,680
Validation artifacts:    360
Total artifacts:        2,040
Test OCR artifacts:         0

Successful:             2,040 / 2,040
Errors:                     0
Zero detections:             0
Malformed outputs:           0
Total text regions:    145,771
```

All **145,771 polygons** passed the technical validation used in the task:

- exactly four vertices;
- finite coordinates;
- coordinates within source-image bounds;
- finite confidence scores;
- nothing clipped/repaired silently.

Every JSON carries `config_version=FROZEN_T005_V1` and the frozen OCR metadata.

## 14.6 Detection-count statistics

Across 2,040 Train + Validation images:

```text
Min regions/image:      2
Median:                48.0
Mean:                  71.46
Max:                  498
High-count flags:      15 images with >=300 regions
```

Technical total regions by category:

- Academic Posters: **60,819**
- Tables: **35,239**
- Receipts: **18,017**
- Infographic Charts: **15,942**
- UI Screenshots: **10,553**
- Commercial Posters: **5,201**

These are **technical coverage statistics only**. They must not yet be interpreted as Real-vs-Generated evidence.

### High-count-image decision

Do **not** remove or alter the 15 high-count images merely because they contain many detections. Their polygons are valid and no failure occurred. Removing them after observing their counts could introduce selection bias. They remain part of the frozen development data unless a future independently justified rule is approved.

## 14.7 Runtime

Observed:

```text
Per-image detector runtime:
min     0.141 s
median  2.094 s
mean    2.095 s
max     7.461 s

Summed detector inference:
4,273.9 s = 71.2 min

Reported end-to-end wall clock:
4,522.4 s = 75.4 min
```

Important wording nuance: the implementation notes say wall-clock timing starts after detector construction in the extraction script, even though the report describes it as including detector build. Treat **75.4 min as the observed extraction wall-clock for the run**, not a universal benchmark. Do not overclaim exact end-to-end runtime across environments.

CPU throughput is practical for the 2,400-image pilot. There is no current need to introduce GPU complexity.

## 14.8 T005 outputs

Produced and accepted:

- `reports/T005_ocr_model_checksums.txt`
- `reports/T005_ocr_inventory.csv` — 2,040 rows
- `reports/T005_full_ocr_audit.md`
- `artifacts/ocr/frozen/train/<sample_id>.json` — 1,680
- `artifacts/ocr/frozen/val/<sample_id>.json` — 360
- `artifacts/ocr/frozen/T005_summary.json`
- `scripts/run_frozen_ocr_extraction.py`
- `DECISIONS.md` with D035

The Research Lead also received an archive of the 2,040 JSONs (`frozen.zip`) and directly audited the artifact counts/metadata.

## 14.9 Test-set status after T005

Critical distinction:

- The extraction script **may read `splits/pilot_test.csv` only to construct a leakage/overlap guard**.
- It must **not load, decode, OCR, inspect, or derive image features from any test image file**.
- T005 produced **zero test OCR artifacts**.

Safe wording:

> “The test manifest was consulted only for leakage protection; no test image was loaded or OCR-processed.”

Do not say “the script never reads pilot_test.csv,” because the guard does read manifest paths.

## 14.10 Resume-validator issue found during Research Lead audit

The completed first run processed all 2,040 artifacts fresh (`skipped_verified=0`), so the following issue had **no effect on T005 results**.

However, `verify_existing()` in `scripts/run_frozen_ocr_extraction.py` is currently more permissive than desired:

- it accepts statuses including `error` as potentially “complete”;
- it chiefly checks `config_version`, sample ID, and region-count consistency;
- it does not deeply compare every material frozen-config field/model checksum before skipping.

Before this script is reused for test extraction or a future resumed production run, harden the validator so that:

1. `status="ok"` is required for a normal skip, unless a deliberate separate policy exists for known zero-detection cases;
2. the full material frozen configuration is compared, not merely `config_version`;
3. sample path/split and model artifact identity are also validated where practical;
4. malformed/error artifacts are reprocessed or escalated, never silently skipped.

Do **not** rerun T005 simply to fix this code issue; current accepted artifacts were produced from a clean run.

## 14.11 What T005 did NOT do

T005 did not:

- OCR any test image;
- perform text recognition;
- use word semantics;
- compute final text-density values/bins;
- create B1 layout statistics;
- create B2 layout maps;
- train Model A/B/C;
- compare Real vs Generated OCR statistics as a hypothesis test;
- tune OCR thresholds;
- change the frozen pilot split.

## 14.12 Final T005 verdict

> **FULL TRAIN+VAL OCR EXTRACTION READY — PASSED**

The project can now proceed to the representation-engineering stage.

# 15. PLANNED MODEL / EXPERIMENT STRUCTURE

The thesis uses controlled ablation, not a pretrained-model tournament.

## 15.1 Model A — Visual Only

Concept:

```text
Original Image
    ↓
Clean Loader
    ↓
Model-specific resize/normalization
    ↓
MobileNetV3-Small
    ↓
Visual embedding
    ↓
Classifier
    ↓
Real / Generated
```

Current provisional backbone:

> **MobileNetV3-Small, ImageNet pretrained**

Do not change backbone without Research Lead approval.

Purpose:

> Establish the lightweight visual baseline.

A sees all pixels: colors, typography, textures, objects, artifacts, etc.

## 15.2 Model B1 — Layout statistics only

OCR boxes → interpretable geometric features.

Potential features:

- detected box count
- total text coverage
- mean/variance of box width
- mean/variance of box height
- aspect ratio stats
- horizontal spread
- vertical spread
- spacing/gap stats
- alignment proxies
- text density

Classifier:

- Logistic Regression or small MLP

No original pixels.

No recognized words.

Purpose:

> Determine whether page-level text arrangement itself carries authenticity signal.

## 15.3 Model B2 — Layout map only

OCR boxes → normalized binary/grayscale page-layout map, provisionally 64×64.

Preserves:

- global text positions
- rough region sizes
- global text structure

Discards:

- words
- font identity
- original colors
- textures
- background

Tiny CNN → layout embedding → classifier.

## 15.4 Model C — Visual + Layout Fusion

Concept:

```text
                         ORIGINAL IMAGE
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
         VISUAL BRANCH                  LAYOUT BRANCH
                │                             │
       MobileNetV3-Small                    OCR
                │                             │
       Visual embedding                 Bounding boxes
                                              │
                                        Layout map
                                              │
                                           Tiny CNN
                                              │
                                       Layout embedding
                │                             │
                └──────────────┬──────────────┘
                               │
                         Concatenate
                               │
                           Small MLP
                               │
                         Real / Generated
```

Important:

> Model C is NOT two models voting.

The two branches produce features first; the final classifier decides after feature fusion.

Initial fusion strategy:

> simple concatenation + small MLP

Do not introduce attention/gating unless the basic cue survives and a later decision authorizes it.

## 15.5 Main comparison

Primary research comparison:

> **A vs C**

Question:

> Does explicit layout information add useful complementary information beyond the visual representation?

B1/B2 are controls that help explain why C succeeds or fails.

---

# 16. TEXT DENSITY — PLANNED, NOT YET FROZEN

Text density is expected to become a central analysis variable.

Candidate definition:

> OCR text-region area / total image area

But exact computation is not yet frozen.

Important issue:

- OCR boxes may overlap.

Therefore likely prefer **union area of text boxes/polygons** rather than naive summed area, but this must be formally decided before implementation.

Potential density bins:

- Low
- Medium
- High

Likely use **training-distribution tertiles**, not arbitrary hand-picked thresholds.

Do not choose thresholds after seeing which creates the strongest effect.

Core density hypothesis:

> Visual-only detector performance may degrade as text density rises, while explicit layout information may provide increasing complementary value.

---

# 17. MODEL EVALUATION PLAN

Initial classification metrics:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Important:

- Macro-F1 for major comparisons
- per-category metrics across six categories
- confusion matrix
- save per-image predictions

Per-image prediction output should eventually include:

- sample_id
- true label
- predicted label
- predicted probability/score
- category
- text-density value
- split

Possible later statistical reliability:

- multiple seeds
- confidence intervals
- bootstrap comparisons
- statistical tests

Do not prematurely complicate the pilot. First determine whether the effect exists.

---

# 18. PILOT GO / MODIFY / DROP LOGIC

The exact final statistical criterion is not frozen, but practical screening logic exists.

## GREEN / GO

Layout fusion meaningfully and consistently improves visual-only baseline.

Rough screening examples previously discussed:

- about +3 percentage points macro-F1 overall
- or about +5 points in important high-density/hard categories

These are screening heuristics, not final inferential thresholds.

## YELLOW / MODIFY

Layout has some signal but fusion barely improves.

Possible future modifications:

- density-aware fusion
- category narrowing
- alternate simple layout representation

Do not jump immediately to complex architectures.

## RED / DROP

- layout-only near chance
- fusion ≈ visual-only
- no meaningful category/density pattern

Then drop the OCR-layout thesis framing instead of forcing a positive result.

Fallback topic:

> resource-efficient / quantized AI-generated image detection, after a fresh novelty audit.

---

# 19. DATASET BIAS LIMITATIONS — MUST REMAIN VISIBLE

TextRich has serious source-domain confounds that are manageable for a controlled pilot but must not be hidden.

Known limitations:

- Real images come from multiple public source datasets.
- Generated images come from a different generation pipeline.
- Historical JPEG artifacts may remain in Real pixels.
- Generated images have different resolution patterns.
- All generated UI screenshots are fixed at 941×1672.
- File format distributions differ strongly.
- Alpha/color-mode distributions differ.
- Source-specific rendering/resampling/compression differences may remain after clean loading.

Balanced sampling does **not** eliminate source bias.

Re-encoding does **not** erase historical compression artifacts.

Do not claim the model is a universal AI-image detector.

Possible later robustness/sanity tests:

- leave-one-category-out evaluation
- external dataset validation

Only add these after the core pilot is stable and if timeline allows.

---

# 20. NO-SILENT-CHANGE RULE — VERY IMPORTANT

DeepSeek / Implementation Engineer must not silently change any of the following:

- dataset membership
- class labels
- sample removal
- class balancing
- train/val/test split
- random/deterministic seeds/salts
- image normalization policy
- alpha handling
- resize policy
- augmentation
- pretrained weights
- visual backbone
- loss function
- OCR model
- OCR thresholds
- OCR confidence threshold
- OCR recognition / semantics
- OCR runtime backend flags
- layout features
- metrics
- decision thresholds
- hyperparameter optimization
- dropping failed runs
- package/model upgrades
- dataset substitution

If implementation convenience conflicts with research meaning, escalate.

---

# 21. RESULT-CHASING RULE

If Model C loses to Model A:

> **Report it.**

Do not automatically:

- change architecture
- tune until C wins
- change split
- increase epochs only because C lost
- add hidden augmentations
- alter OCR thresholds
- swap backbone
- remove difficult samples

Research Lead must first determine whether:

- hypothesis failed;
- implementation has a real bug;
- design needs an approved modification.

Negative result is scientifically valid.

---

# 22. EXPERIMENT IDs / ARTIFACT STRUCTURE

Suggested experiment IDs:

- `EXP-A001` — visual-only baseline
- `EXP-B101` — layout statistics
- `EXP-B201` — layout-map CNN
- `EXP-C001` — visual + layout fusion

Suggested experiment directory:

```text
experiments/EXP-A001/
├── config.yaml
├── metrics.json
├── predictions.csv
├── training_log.csv
├── notes.md
└── artifacts/
```

Every run should record:

- random seed
- Python version
- library versions
- hardware
- model/pretrained weights
- split file/checksum
- training config
- exact command
- metrics

No fabricated results.

If not run:

`NOT RUN`

If unverified:

`UNVERIFIED`

If blocked:

`BLOCKED`

---

# 23. REPOSITORY SOURCE OF TRUTH

Recommended repo structure:

```text
thesis-project/
├── PROJECT_CONTEXT.md
├── RESEARCH_PROTOCOL.md
├── DECISIONS.md
├── TASKS.md
├── README.md
├── data/
├── splits/
├── src/
├── scripts/
├── experiments/
├── artifacts/
├── reports/
└── docs/
```

The following three canonical files were already created and placed in repo root:

- `PROJECT_CONTEXT.md`
- `RESEARCH_PROTOCOL.md`
- `DECISIONS.md`

These files are intended to let DeepSeek recover context after a reset.

---

# 24. DECISIONS LOG — CURRENT KNOWN STATE

The repo `DECISIONS.md` has been received through **D035**, and D035 was verified as physically present after T005.

Summary:

- D001 Broad Research Area — APPROVED
- D002 Generic AI Detection as contribution — REJECTED
- D003 Text-Rich Specialization — APPROVED
- D004 OCR as novelty — REJECTED
- D005 Layout as broad novelty — REJECTED
- D006 Generic visual+text fusion novelty — REJECTED
- D007 Current candidate contribution — PROVISIONAL
- D008 Text density — PROVISIONAL
- D009 TextRich dataset — originally provisional; local audit passed and dataset is in active use
- D010 External dataset later — PROVISIONAL
- D011 Pilot before Chapter 1 commitment — APPROVED
- D012 Pilot size ~2,400 — originally provisional; concretely realized and frozen
- D013 Model A = lightweight visual baseline / MobileNetV3-Small — PROVISIONAL pending model-protocol freeze
- D014 Model B concept — APPROVED
- D015 Model C concept — APPROVED
- D016 Main comparison A vs C — APPROVED
- D017 Role of Model B — APPROVED
- D018 OCR recognition rejected for initial pilot — APPROVED restriction
- D019 Initial simple fusion — PROVISIONAL
- D020 Image normalization principle — APPROVED
- D021 Fixed splits — APPROVED
- D022 No test-set tuning — APPROVED
- D023 No silent research changes — APPROVED
- D024 Negative results accepted — APPROVED
- D025 Thesis title — NOT DECIDED
- D026 Initial task T001 dataset audit — historical
- D027 Exact-duplicate reduction policy — APPROVED
- D028 pHash audit scope — APPROVED
- D029 Clean image loading behavior — APPROVED
- D030 No category-specific UI augmentation — APPROVED
- D031 pHash cluster representative policy — APPROVED
- D032 Deterministic pilot sampling/split scores — APPROVED
- D033 Frozen pilot split — APPROVED
- D034 Opaque sample-ID scheme + explicit intersection checks — APPROVED
- **D035 Frozen OCR configuration — APPROVED / PHYSICALLY RECORDED**

D035 freezes:

```text
PP-OCRv6_small_det
paddle_static
CPU
enable_mkldnn=False
text recognition disabled
model-default detection thresholds
T002 clean RGB loader → explicit BGR numpy conversion
Python 3.11.9 OCR environment with pinned versions
model artifact checksums recorded in T005_ocr_model_checksums.txt
```

No D036 has been approved yet as of this handoff. T006 must not invent a new research decision without explicit Research Lead authorization.

# 25. COMMUNICATION PACKET FORMAT

Research Lead → Implementer:

```text
[RESEARCH LEAD → IMPLEMENTER]

TASK ID:
TITLE:

OBJECTIVE:

CONTEXT:

RESEARCH CONSTRAINTS / REQUIREMENTS:

DO NOT:

REQUIRED OUTPUTS:

ACCEPTANCE CRITERIA:
```

Implementation Engineer → Research Lead:

```text
[IMPLEMENTER → RESEARCH LEAD]

TASK ID:
STATUS: COMPLETED / PARTIAL / BLOCKED

1. What implemented
2. Files created/changed
3. Commands executed
4. Results
5. Assumptions made
6. Deviations from specification
7. Issues/risks discovered
8. Exact errors
9. Open questions
10. Recommended next action
```

The user should copy-paste these messages verbatim rather than paraphrasing whenever possible.

---

# 26. SAFE PANEL / DEFENSE CLAIMS

## “What is new?”

Safe answer:

> Existing studies use visual, text-region, OCR, and layout information in related problems. We do not claim OCR or layout itself is new. We evaluate whether explicit page-level OCR-derived spatial-layout cues provide complementary discriminative information to a lightweight visual detector in AI-generated text-rich image detection, particularly across text-density conditions.

## “Comparison lang ba?”

Safe answer:

> It is not simply a comparison of pretrained models. The study evaluates a defined computational representation through controlled ablations: visual-only, layout-only, and fused representations, including category and text-density analysis.

## “Why Computer Science?”

Safe answer:

> The work involves Computer Vision, OCR spatial representation, image classification, feature encoding/fusion, controlled computational experiments, and quantitative evaluation.

## “Why text-rich?”

Safe answer:

> Modern image generators can produce receipts, tables, screenshots, posters and infographics with readable text, while recent benchmark work indicates conventional AI-image detectors can still struggle in text-rich conditions.

## “Why layout?”

Safe answer:

> We do not assume layout works. The study evaluates whether the spatial organization of detected text regions provides complementary evidence beyond the visual image representation.

## “What if layout does not help?”

Safe answer:

> A negative result is scientifically valid. The pilot is deliberately designed as a kill-test so the group does not invest the whole thesis in a weak cue.

---

# 27. IMPORTANT FILES PRODUCED SO FAR

## Canonical context / protocol

- `PROJECT_CONTEXT.md`
- `RESEARCH_PROTOCOL.md`
- `DECISIONS.md` — through D035

## T001

- `scripts/audit_textrich.py`
- `reports/T001_dataset_audit.md`
- `reports/T001_image_inventory.csv`
- `reports/T001_exact_duplicates.csv`
- `reports/T001_invalid_images.csv`

## T002

- `reports/T002_manifest_verification.md`
- `reports/T002_exact_unique_pool.csv`
- `reports/T002_exact_redundant_files.csv`
- `reports/T002_phash_inventory.csv`
- `reports/T002_near_duplicate_candidates.csv`
- `reports/T002_near_duplicate_audit.md`
- `src/data/image_loading.py`
- `scripts/build_exact_unique_pool.py`
- `scripts/compute_phash_inventory.py`
- `scripts/search_near_duplicates.py`
- `scripts/sanity_check_image_loading.py`

## T003 / T003-CORR

- `reports/T003_pilot_eligible_pool.csv`
- `reports/T003_phash_cluster_exclusions.csv`
- `reports/T003_sampling_split_audit.md`
- `splits/pilot_all.csv`
- `splits/pilot_train.csv`
- `splits/pilot_val.csv`
- `splits/pilot_test.csv`
- `scripts/create_pilot_split.py`

Current post-correction canonical split hashes:

```text
pilot_all.csv
c947aa1aab73440ca914701c04669ad68892b8388423b5a907fe3a1912f33261

pilot_train.csv
5838c5f9afb49a600b6f4cabfe0860a036e943fcfda258ea3488f0223c4cab2c

pilot_val.csv
3a1a79ffe16fe0931f6e6341dd792851ba689cc658714141302400c0a39f3b48

pilot_test.csv
dffc14b49de2536d274ce059a807c7d0cabcaad3a61791d8c0f68719e58a697c
```

## T004

- `src/ocr/text_detector.py`
- `scripts/run_ocr_smoke_test.py`
- `reports/T004_ocr_environment.md`
- `reports/T004_ocr_smoke_audit.md`
- `reports/T004_ocr_smoke_manifest.csv`
- `reports/T004_ocr_requirements_freeze.txt`
- `artifacts/ocr/T004/<24 sample jsons>`
- `artifacts/ocr/T004/T004_summary.json`
- `artifacts/ocr/T004/overlays/<24 pngs>`

## T005 — completed

- `reports/T005_ocr_model_checksums.txt`
- `reports/T005_ocr_inventory.csv` — 2,040 rows
- `reports/T005_full_ocr_audit.md`
- `artifacts/ocr/frozen/train/*.json` — 1,680
- `artifacts/ocr/frozen/val/*.json` — 360
- `artifacts/ocr/frozen/T005_summary.json`
- `scripts/run_frozen_ocr_extraction.py`
- `DECISIONS.md` with D035

Research Lead also received:

- `frozen.zip` containing the frozen OCR artifact tree for review.

## Master continuity artifact

This file:

- `MASTER_HANDOFF_BSCS_THESIS_UPDATED_2026-08-18_POST_T005.md`

supersedes the prior 2026-08-17 handoff.

# 28. CURRENT TIMELINE STATUS

Current stage summary:

```text
T001 Dataset audit                           ✅ PASSED
T002 Manifest / exact dedup / pHash audit    ✅ PASSED
T003 Pilot sample + frozen split              ✅ PASSED
T003-CORR Neutral IDs / overlap fix           ✅ PASSED
T004 OCR smoke validation                     ✅ PASSED
T005 Full frozen OCR extraction Train+Val     ✅ PASSED
T006 Layout geometry / density representation ⏭️ NEXT — NOT YET ISSUED
```

Current factual state:

- Dataset is locally complete and audited.
- Pilot is fixed at **2,400 images**.
- Train = **1,680**.
- Validation = **360**.
- Test = **360**.
- Train+Validation OCR is complete for **2,040/2,040** images.
- **145,771** valid OCR text polygons are available for representation engineering.
- Test images have **not** been OCR-processed.
- Test images have **not** been model-evaluated.
- No classifier has been trained yet.
- No final text-density formula/bins have been frozen yet.
- No B1 geometric feature table exists yet.
- No B2 64×64 layout map dataset exists yet.
- No Model A/B/C experiment exists yet.

The project is now transitioning from **dataset/OCR infrastructure** into **feature-representation and experimental-model development**.

# 29. NEXT TASK — T006, THEN T007–T011 ROADMAP

T005 is accepted. The next Research Lead task should be **T006**, but its exact packet has not yet been sent as of this handoff.

Do not jump directly to training before freezing the layout/density representation.

## T006 — OCR-derived geometry / text-density / layout representation freeze

Primary goal:

> Convert frozen OCR polygons into reproducible, non-semantic page-layout representations while defining text density in a way that cannot be tuned after observing class separation.

Likely T006 components:

### A. Harden reusable OCR artifact validation

Before consuming T005 JSONs broadly, fix the known resume/verification weakness in `run_frozen_ocr_extraction.py` for future use. This is a code-quality correction; do not rerun T005 solely because of it.

### B. Define confidence-policy behavior

Avoid casually choosing an OCR confidence threshold after inspecting Real-vs-Generated separation.

Safest initial pilot policy is likely either:

- use **all detector-returned regions** already accepted by PP-OCRv6 postprocessing, or
- if confidence filtering is scientifically necessary, freeze the threshold using detector documentation / Train-only technical rationale before evaluating class effects.

Do not use Validation/Test class performance to pick the threshold.

### C. Normalize polygons/boxes

For each polygon, derive source-size-normalized coordinates such as:

```text
x_norm = x / image_width
y_norm = y / image_height
```

If B1 uses axis-aligned boxes, make conversion deterministic:

```text
xmin = min(x vertices)
ymin = min(y vertices)
xmax = max(x vertices)
ymax = max(y vertices)
```

Keep raw polygons available for area computations.

### D. Freeze text-density formula

Preferred scientific definition to consider:

> **text coverage density = union area of detected text polygons / total image area**

Why union area rather than naive sum:

- OCR regions can overlap;
- naive area summation can double-count pixels;
- union-area coverage has a clearer geometric meaning.

Need to freeze exact implementation, including polygon validity and boundary assumptions, before class analysis.

Also consider retaining simpler auxiliary measures such as:

- region count;
- total non-union polygon area / image area (diagnostic only);
- mean box area;

but do not redefine “density” opportunistically after results.

### E. Density bins

Do **not** compute tertile cut points from all 2,400 images.

Preferred approach:

1. compute density for Train + Validation using frozen OCR;
2. derive **Low / Medium / High** thresholds from the **training distribution only**, likely training tertiles;
3. apply those frozen thresholds to Validation;
4. only after final method freeze, OCR Test and apply the same thresholds unchanged.

Do not tune cut points for maximum A-vs-C separation.

### F. B1 — simple geometric layout statistics

Candidate features should remain small/interpretable, for example:

- number of regions;
- union text coverage density;
- mean/median normalized box width;
- mean/median normalized box height;
- width/height variability;
- mean aspect ratio;
- normalized center spread in x/y;
- horizontal/vertical gap or spacing summaries;
- alignment summaries if defined deterministically.

Avoid feature explosion. B1 exists to test whether explicit layout geometry carries signal, not to create a handcrafted mega-classifier.

### G. B2 — 64×64 layout map

Likely representation:

```text
OCR polygons/boxes
→ normalize to page coordinates
→ rasterize text regions into fixed 64×64 map
→ binary or grayscale spatial mask
```

The map must discard:

- words;
- OCR recognized text;
- original image texture;
- font/color;
- semantic content.

Need to freeze:

- polygon vs bounding-box rasterization;
- filled vs outline;
- binary vs confidence-weighted;
- coordinate rounding;
- overlap behavior;
- output dtype/range.

Default should favor **simple binary filled layout occupancy** unless evidence justifies something more complex.

### H. T006 scope

Use **Train + Validation only**. Do not OCR or derive layout features for Test yet.

T006 should create deterministic manifests/features/maps and technical sanity checks, but **should not yet train classification models unless explicitly included by the Research Lead**.

## T007 — Visual resize/preprocessing freeze + EXP-A001

Expected baseline remains:

- MobileNetV3-Small
- ImageNet pretrained
- frozen pilot split
- Train for learning
- Validation for method selection
- Test unopened

Need to freeze:

- input resolution;
- aspect-ratio handling (resize/crop/pad);
- interpolation;
- ImageNet normalization;
- backbone freeze/unfreeze strategy;
- augmentation policy;
- optimizer;
- learning rate;
- epochs / early stopping;
- seed policy.

Keep the first baseline intentionally simple.

## T008 — B1 / B2 layout-only controls

- B1: simple geometric features → Logistic Regression or small MLP.
- B2: 64×64 layout map → tiny CNN.
- Development on Train/Validation only.

## T009 — Model C fusion

- visual embedding from Model A branch;
- layout embedding from B2 (or frozen best simple layout representation if justified);
- concatenate embeddings;
- small MLP classifier;
- no attention/gating complexity initially.

## T010 — Freeze final A/B/C configurations and open Test once

Only after Train/Validation development is complete.

Then:

- OCR the 360 Test images with **exact D035 frozen OCR config**;
- derive layout/density using exact frozen T006 transformations;
- run final A/B/C evaluation once under the one-way-door policy.

## T011 — Final analysis + GO / MODIFY / DROP

Report:

- Accuracy
- Precision
- Recall
- F1
- Macro-F1 where relevant
- ROC-AUC
- confusion matrices
- per-category performance
- Low/Medium/High density performance
- A vs B1 vs B2 vs C
- repeated seeds/confidence intervals if warranted

Then decide whether the thesis direction survives.

# 30. CRITICAL THINGS A NEW AI MUST NOT DO

A new AI taking over should **not**:

1. Restart novelty search from zero without reading this handoff.
2. Claim OCR/layout is novel.
3. Claim “first ever.”
4. Replace TextRich casually.
5. Change the frozen split.
6. Touch the test set during development.
7. Switch OCR model or thresholds without approval.
8. Upgrade Paddle packages mid-extraction.
9. Add OCR recognition/semantic text features.
10. Introduce CLIP/ViT/Transformer just because they are stronger.
11. Turn the study into a model tournament.
12. Add augmentations or tuning because Model C loses.
13. Remove difficult samples.
14. Treat pHash candidates as confirmed duplicates.
15. Claim re-encoding erases JPEG/source bias.
16. Claim balanced sampling solves source bias.
17. Treat filename/file size as direct CNN inputs; they are mainly provenance indicators.
18. Draft strong thesis novelty claims before the pilot proves the cue.
19. Open the test set before Train/Val method freeze.
20. Let implementation convenience override the research protocol.

---

# 31. WHAT THE NEXT AI MUST DO BEFORE ISSUING T006

If this handoff is loaded into a new Research Lead instance, do not immediately improvise T006. First internalize the following accepted facts and open design choices.

## 31.1 Accepted facts

1. T005 is complete and accepted.
2. Train+Validation OCR artifacts = exactly **2,040**.
3. Valid OCR polygons = **145,771**.
4. Test OCR artifacts = **0**.
5. D035 is physically recorded.
6. OCR model artifact hashes are frozen.
7. High-count images are retained; do not remove them by observation.
8. No model has been trained.
9. No final density formula or density thresholds exist.
10. No layout features/maps exist.

## 31.2 Known implementation issue to carry forward

`run_frozen_ocr_extraction.py` resume validation should be hardened before it is trusted for a future resumed/test extraction. Current T005 results remain valid because the accepted run had `skipped_verified=0`.

## 31.3 Design decisions T006 still needs

The next AI/Research Lead must explicitly freeze:

- use-all OCR regions vs confidence filtering;
- polygon vs axis-aligned box behavior for each representation;
- exact text-density formula;
- overlap handling for density;
- training-only density-bin thresholds;
- B1 feature list and formulas;
- B2 map rasterization format;
- output file formats/checksums;
- sanity checks;
- whether layout representation is generated for Train+Val only (recommended) until final method freeze.

## 31.4 Strong default recommendation

For graduation-first simplicity, favor:

- all accepted OCR detector outputs, no extra confidence threshold initially;
- raw quadrilateral polygon union area for density;
- normalized axis-aligned boxes for simple B1 geometry where helpful;
- binary filled 64×64 map for B2;
- density tertiles based only on Train;
- Validation receives thresholds frozen from Train;
- no Test processing yet.

These are recommendations, not yet physical D036+ decisions.

## 31.5 Audit requirement

When DeepSeek returns T006, independently verify the generated feature files mathematically. Do not rely only on its prose summary. At minimum recalculate samples of:

- normalized coordinates;
- polygon/union areas;
- density values;
- training tertile thresholds;
- B1 feature formulas;
- layout-map occupancy/rasterization;
- Train/Validation sample coverage;
- absence of Test IDs.

# 32. CURRENT RESEARCH ASSESSMENT

Approximate qualitative scoring from prior review:

- Problem relevance: ~9/10
- Broad method novelty: ~4/10
- Exact-intersection novelty: moderate, roughly ~5.5–8/10 depending framing; no direct duplicate found, but uniqueness is not proven
- Dataset feasibility: ~8–9/10
- Compute feasibility: ~9/10
- Experimental clarity: ~9/10
- Risk of weak result: moderate
- Defense potential: ~7.5–8/10 if framed as evaluation/enhancement
- Graduation suitability: ~8/10

Current ranking:

1. **Text-rich AIGI + OCR-derived spatial-layout cue evaluation** — leading
2. **Resource-efficient/quantized cross-generator detection** — backup
3. Few-shot adaptation — not recommended
4. Localized edits — higher risk
5. Generator attribution — more complex

---

# 33. SIMPLE ONE-PARAGRAPH PROJECT SUMMARY FOR A NEW AI

This is a Bicol University BSCS Thesis 1 project investigating whether **explicit OCR-derived page-level text layout** can improve a **lightweight visual detector** for identifying **AI-generated text-rich images** such as receipts, tables, posters, infographics and UI screenshots. The contribution is **not OCR itself, not layout itself, and not generic visual-text fusion**; related literature already contains those ideas. The current defensible contribution is a controlled evaluation of **visual-only vs layout-only vs visual+layout** representations, especially across **text-density levels**. TextRich v2 was fully audited, exact and perceptual duplicates were conservatively controlled, and a frozen balanced 2,400-image pilot was created with **1,680 Train / 360 Validation / 360 Test**. The test set remains blind. `PP-OCRv6_small_det` was first validated on a 24-image Train-only smoke test, then frozen under D035 (`paddle_static`, CPU, `enable_mkldnn=False`, no recognition) and run on **all 2,040 Train+Validation images with 2,040/2,040 success and 145,771 valid detected text polygons**. No Test image has been OCR-processed and no classifier has been trained. The immediate next stage is to freeze **text-density, B1 geometric-layout features, and B2 64×64 layout-map construction** before beginning Model A/B/C experiments.

# 34. FINAL CONTINUITY DIRECTIVE

If this handoff is given to another AI, that AI should behave as though it has been following the project from the beginning.

Preserve all of the following:

- the graduation-first research philosophy;
- the exact novelty caution;
- the frozen 2,400-image pilot;
- the post-T003-CORR split checksums;
- the no-test-tuning rule;
- the opaque sample IDs;
- the exact duplicate/pHash group-control history;
- the T002 clean-loader policy;
- D035 frozen OCR model/environment/config/checksums;
- the fact that Train+Validation OCR is already complete and accepted;
- the fact that Test OCR has not happened;
- the rule that high OCR-count images are not removed merely because they look unusual;
- the known T005 resume-validator weakness, which needs hardening before future reuse;
- ChatGPT/Research Lead as methodology authority and DeepSeek/OpenCode as Implementation Engineer;
- the Project Owner as the human communication bridge and final authority;
- the requirement to audit DeepSeek outputs independently rather than rubber-stamp them;
- the rule that negative results must not trigger hidden result-chasing.

Do not restart completed tasks unless there is evidence of a real defect.

Do not draft inflated novelty claims.

Do not touch the Test image files during T006/T007/T008/T009 development.

Do not switch OCR model, OCR thresholds, package versions, or frozen split for convenience.

Do not introduce OCR-recognized words or semantic text features into the initial pilot.

Do not let a stronger but more complicated architecture replace the controlled A/B/C experiment before the simple hypothesis is tested.

**Immediate next Research Lead action:** design and issue **T006 — OCR-derived geometry / text-density / layout representation freeze**. T006 must remain Train+Validation-only, preserve D035, define density without class-result chasing, generate simple B1/B2 representations, and leave Test untouched.

After T006 is audited, proceed toward the visual baseline and controlled A/B/C proof-of-concept. Only after Train/Validation method freeze should the Test set be opened once for final pilot evaluation.
