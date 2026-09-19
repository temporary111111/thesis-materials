# HANDOFF FILE: Text-Density-Aware AI-Generated Image Detection Thesis

**Prepared for:** continuation with another AI assistant if this conversation becomes unavailable  
**Date prepared:** 08 September 2026  
**Working language:** Filipino/Taglish, with English technical terms when useful  
**User role:** Computer Science student working with a thesis group  

---

## 0. How to use this handoff

Upload this file to the next AI or paste the section titled **“Bootstrap prompt for the next AI”** into a new conversation. The next AI should treat this file as the working project memory and should not restart the discussion from zero.

The project is still in the **concept and feasibility stage**. No experimental results, accuracy values, trained model, or final methodology have been produced yet. Any numerical result mentioned below is only an example or target, not an actual finding.

The user wants direct, honest, practical guidance. Avoid making the project sound easier than it is. Clearly distinguish:

- established information from the literature;
- proposed design choices;
- assumptions;
- examples or target values;
- actual experimental findings.

---

## 1. Bootstrap prompt for the next AI

You are continuing a thesis-planning conversation with a Computer Science student from the Philippines. The project concerns the difficulty of AI-generated image detectors on text-rich images, informally called the **“Text Density Curse.”**

The student wants to investigate a feasible solution that can be implemented as an undergraduate Computer Science thesis. The proposed direction is an **OCR-guided, text-region-aware, density-aware multi-branch detector** that processes:

1. text-region features;
2. non-text-region features; and
3. global-image features;

then combines them through feature fusion to classify an image as real or AI-generated.

Important clarification: the proposed design does **not** stop using visual pixels. All three feature groups are still extracted from image data. The improvement is that the image is processed in separate regions and representations instead of being treated only as one undifferentiated whole-image input.

The practical thesis goal is to **reduce false negatives** in text-rich AI-generated images, not to claim perfect or universal detection. OCR should primarily locate text regions and estimate text density; it should not be treated as a perfect semantic checker of spelling or correctness.

The user needs help with feasibility, scope control, dataset construction, model design, experimental protocol, coding steps, thesis title/objectives, diagrams, and documentation. Recommend a minimum viable version first, then an expanded version only if resources permit. Do not recommend training a large image generator or a detector from scratch unless there is a strong reason.

Use Filipino/Taglish explanations unless the user asks for formal English. Be direct and identify risks, data leakage, overfitting, and unsupported assumptions.

---

## 2. The project in one paragraph

AI-generated image detectors often rely on visual, spatial, texture, noise, or frequency patterns. In text-rich images such as screenshots, posters, documents, receipts, interfaces, and news pages, dense glyphs create many legitimate edges and high-frequency patterns. These may mask or overwhelm the subtle artifacts produced by image generators. The thesis will test whether a detector that explicitly identifies text regions, separates text and non-text information, preserves global image context, and fuses these features can improve detection—especially AI recall and false-negative rate—at different text-density levels.

---

## 3. What “Text Density Curse” means in this project

### Working definition

> The Text Density Curse refers to the degradation of AI-generated image detection performance as the amount, spatial density, and structural complexity of text in an image increase, because legitimate glyph patterns can obscure or overwhelm forensic clues used by the detector.

### Correct interpretation

The student’s original understanding was broadly correct: detectors may struggle more when an image contains dense text. The more precise interpretation is:

- it is a performance degradation, not a total failure in every case;
- the effect may be stronger for detectors that rely on low-level spatial or frequency artifacts;
- the common observed direction is a reduction in AI-image recall, producing false negatives;
- text-rich real images can still be classified correctly, so overall accuracy alone can hide the problem;
- not every detector or architecture will show the same degree of degradation;
- the term is a recent research label and should not be presented as a universally standardized term without qualification.

### Important literature context

The 2026 *TextFake: Benchmarking AI-Generated Image Detection on Text-Rich Images* preprint names “Text Density Curse” as one of several failure modes. It reports that performance declines as text density increases and that dense glyph structures can overwhelm low-level detectors. The work evaluates text-rich images across languages, scene types, and topics.

Primary source:

<https://arxiv.org/abs/2606.01050>

Use this as an important starting source, but verify its publication and peer-review status before treating it as the only foundation of the final thesis.

---

## 4. Central thesis idea

### One-sentence explanation for group members

> Instead of treating a text-heavy image as one undivided visual signal, the proposed detector separately analyzes the text regions, non-text regions, and whole-image context, then combines these features to reduce false negatives in AI-generated text-rich images.

### Short explanation

An ordinary detector may process the entire image at once. When the image contains dense text, legitimate letter edges and texture patterns can dominate the representation. The proposed system uses OCR or a text detector to identify the text regions, extracts features from separate regions, and uses a fusion layer to make the final prediction.

### What the system is NOT doing

It is not simply:

```text
Ignore text regions.
Use non-text regions only.
```

It is instead:

```text
Text region       -> separate feature analysis
Non-text region   -> separate feature analysis
Whole image       -> global feature analysis
All features      -> feature fusion
Final output      -> real / AI-generated probability
```

Text may contain useful AI artifacts, so it should not automatically be deleted or ignored.

---

## 5. Proposed system architecture

```text
INPUT IMAGE
    |
    v
TEXT DETECTOR / OCR
    |-- identifies text bounding boxes
    |-- estimates text-density score
    |
    +--------------------+----------------------+-------------------+
    |                    |                      |
    v                    v                      v
TEXT-REGION         NON-TEXT-REGION       GLOBAL-IMAGE
BRANCH              BRANCH                BRANCH
    |                    |                      |
    |                    |                      |
    +--------------------+----------------------+
                         |
                         v
                   FEATURE FUSION
              (may use density-aware weighting)
                         |
                         v
                 AI-IMAGE CLASSIFIER
                         |
             Real / AI-generated + confidence
```

### Branch 1: Text-region branch

Possible information:

- glyph shapes and texture;
- letter edges and local gradients;
- spacing and alignment;
- rendering artifacts;
- local noise and compression patterns;
- optional OCR confidence and layout descriptors.

This branch must not depend only on whether the text is grammatically correct. Modern generators may render readable text, and real images can contain spelling errors.

### Branch 2: Non-text-region branch

Possible information:

- background texture;
- sensor-like noise;
- gradients and shadows;
- reflections;
- objects and surrounding visual context;
- frequency or compression artifacts outside dense glyph regions.

This branch may help when text overwhelms the detector’s low-level representation.

### Branch 3: Global-image branch

Possible information:

- overall layout;
- relationship among text, objects, and background;
- screenshot, poster, or document structure;
- global visual consistency;
- image-level semantic representation.

This branch prevents the model from losing the larger context when the image is divided into regions.

### Feature fusion

The features from the three branches and the text-density score are combined. The implementation can begin simply:

```text
global feature + text-region feature + non-text feature + density score
                         |
                         v
                 fully connected classifier
```

An attention or learned gating mechanism may be added later, but it is not necessary for the first feasible prototype.

---

## 6. Recommended thesis scope

To keep the project feasible, initially limit it to:

- screenshots, posters, documents, receipts, or infographics;
- English and Filipino text, or English only if OCR is a major limitation;
- two or three AI image generators;
- low, medium, and high text-density groups;
- binary classification: real versus AI-generated;
- JPEG compression and resizing as basic robustness tests;
- a pretrained vision model instead of a model trained completely from scratch.

Do not initially promise:

- detection of every AI generator;
- every language and writing system;
- perfect accuracy;
- reliable attribution of the exact generator;
- detection after every possible editing operation;
- legal or forensic certainty from the model score alone.

---

## 7. Minimum viable thesis version

If the group has limited time, computing power, or machine-learning experience, use this version first:

### MVP title direction

> Evaluating Density-Aware Calibration for AI-Generated Image Detection on Text-Rich Images

### MVP design

1. Use a pretrained global-image detector.
2. Use OCR/text detection to estimate text density.
3. Create low-, medium-, and high-density test groups.
4. Evaluate the baseline detector separately by density group.
5. Add density-aware calibration, balanced training data, or non-text crop features.
6. Compare AI recall and false-negative rates against the baseline.

This is more manageable than immediately building a complex multi-branch neural network. If the MVP works, add a separate text-region branch as an extension.

---

## 8. Full proposed thesis version

### Candidate title 1: recommended

> Reducing False Negatives in AI-Generated Image Detection through OCR-Guided Feature Fusion for Text-Rich Images

### Candidate title 2

> An OCR-Guided Density-Aware Multi-Branch Detector for AI-Generated Text-Rich Images

### Candidate title 3

> Improving AI-Generated Image Detection on Text-Rich Images through Text-Region-Aware Feature Analysis

### Candidate title 4: evaluation-focused

> An Empirical Evaluation of Density-Aware AI-Generated Image Detection on Text-Rich Images

The title should be narrowed after the group confirms the actual implementation. Do not claim “universal,” “perfect,” or “real-time” unless the experiments justify those terms.

---

## 9. Proposed research questions

1. Does AI-generated image detection performance decline as text density increases?
2. What is the effect of text density on AI-image recall and false-negative rate?
3. Does OCR-guided region separation improve detection on text-rich images compared with a whole-image baseline?
4. Does combining text-region, non-text-region, and global-image features improve F1-score or AI recall?
5. How robust is the proposed detector to JPEG compression, resizing, and screenshot-like distortions?
6. Does the proposed method generalize to an AI generator or template not used during training?

---

## 10. Suggested objectives

### General objective

To develop and evaluate a text-density-aware AI-generated image detector that reduces false negatives in text-rich images.

### Specific objectives

1. To construct a balanced dataset of real and AI-generated text-rich images categorized by text density.
2. To implement an OCR- or text-detector-based procedure for locating text regions and calculating text density.
3. To establish a whole-image pretrained detector as a baseline.
4. To develop a region-aware detector using text-region, non-text-region, and global-image features.
5. To compare the baseline and proposed detector using precision, recall, F1-score, AUROC, and false-negative rate.
6. To evaluate robustness under selected image perturbations such as compression and resizing.

---

## 11. Step-by-step implementation plan

### Step 1: Lock the research question and scope

Decide the image types, languages, generators, density definition, and metrics before collecting data.

Recommended first scope:

- image types: screenshots, posters, and documents;
- language: English, with Filipino added only if OCR works reliably;
- generators: at least two for training data and, if possible, one unseen generator for testing;
- output: real versus AI-generated.

### Step 2: Set up the development environment

Suggested tools:

- Python;
- PyTorch and torchvision;
- OpenCV and Pillow;
- EasyOCR, PaddleOCR, Tesseract, or another text detector;
- scikit-learn;
- pandas;
- matplotlib or seaborn;
- Google Colab or another GPU environment;
- Git/GitHub for version control;
- Streamlit only if an interface is required.

Do not spend time training a text-recognition model from scratch.

### Step 3: Build a 200-image pilot dataset

Start with approximately:

- 100 real images;
- 100 AI-generated images;
- examples at different text densities;
- more than one image type.

Check whether:

- OCR finds text boxes reasonably well;
- density can be measured consistently;
- the baseline can train or run;
- the performance difference is observable;
- the team understands the data labeling process.

If the pipeline fails on the pilot, revise the scope before creating the final dataset.

### Step 4: Define and compute text density

A possible operational definition is:

```text
Text density = area covered by detected text regions / total image area
```

Additional possible features:

- number of text boxes;
- estimated character count;
- character count per image area;
- average text-box size;
- total text-region perimeter or connected-component density.

Use low, medium, and high categories based on the distribution of the collected data or clearly justified thresholds.

### Step 5: Build the final dataset

A reasonable undergraduate target is approximately 1,200–2,400 total images, balanced between real and AI-generated samples. A smaller dataset may work with transfer learning, but the group must report the limitation.

Recommended metadata columns:

```text
filename
label
density_level
density_score
scene_type
language
generator
source_or_template
resolution
compression_setting
split
```

Use source-level or template-level splitting, not only random image-level splitting. Near-duplicate real/fake pairs, repeated templates, and identical generator prompts can cause leakage.

### Step 6: Standardize the data

Apply the same general preprocessing to all samples:

- common resolution or controlled resizing;
- same color format;
- metadata removal;
- consistent file format;
- controlled JPEG encoding;
- documented preprocessing settings.

Do not let the model use trivial shortcuts such as file extension, metadata, or generator-specific compression.

### Step 7: Train the baseline

Start with a pretrained global-image classifier such as ResNet, EfficientNet, ViT, or a CLIP-based model. Fine-tune it for binary classification.

The baseline sees the whole image and outputs a probability for real versus AI-generated.

Evaluate it separately on low-, medium-, and high-density subsets. This establishes whether the problem exists in the group’s own dataset.

### Step 8: Implement the region-aware method

Initial practical implementation:

1. Run OCR or text detection.
2. Generate text bounding boxes and a density score.
3. Extract global features from the whole image.
4. Extract features from text-region crops.
5. Extract features from non-text regions or low-overlap patches.
6. Concatenate these features with the density score.
7. Train a small fusion classifier.

A simple concatenation plus multilayer perceptron is acceptable for the first version. A sophisticated attention module is optional.

### Step 9: Perform ablation studies

Compare:

1. global-image baseline;
2. baseline plus density score;
3. baseline plus non-text-region features;
4. baseline plus text-region features;
5. full three-branch model.

This shows which component actually contributes to improvement.

### Step 10: Evaluate robustly

Report:

- accuracy;
- precision;
- recall;
- F1-score;
- AUROC;
- AI-class recall;
- false-negative rate;
- confusion matrices;
- results per density level.

Test selected perturbations:

- JPEG quality changes;
- resizing;
- screenshots;
- mild blur;
- brightness changes;
- moderate noise;
- moire-like screen capture artifacts, if feasible.

### Step 11: Test generalization

If possible, train using two generators and test on a third unseen generator. Alternatively, hold out a template family or source type. This is stronger than a random split that contains visually similar samples in both training and testing.

### Step 12: Optional prototype

Create a simple Streamlit application that displays:

- uploaded image;
- detected text regions;
- estimated text-density level;
- real/AI-generated prediction;
- confidence score;
- a warning that the output is probabilistic and should not be treated as conclusive proof.

The application is optional. The scientific comparison is the primary thesis contribution.

---

## 12. Dataset design warnings

This is likely the hardest and most important part of the project.

Avoid this invalid setup:

```text
All real images = Canva exports
All fake images = one AI generator
Different image formats = different classes
```

The model could learn software, compression, or source identity rather than AI-generation artifacts.

Better practice:

- match scene types and topics between real and synthetic samples;
- standardize file format and resolution;
- remove metadata;
- use multiple sources and generators;
- keep templates or sources separated during testing;
- manually inspect a subset of labels;
- record every generation and preprocessing step.

### Privacy and copyright

- Avoid private documents and personal information.
- Blur or remove names, addresses, account numbers, and faces when not needed.
- Prefer self-created, openly licensed, or properly documented examples.
- Keep the dataset and metadata organized so the thesis can explain where samples came from.

---

## 13. Feasibility and approximate timeline

Assumption: three to four students, basic Python knowledge, 10–15 hours per week per student, and access to Google Colab or another GPU.

| Work package | Approximate time | Difficulty |
|---|---:|---|
| Literature review and scope | 1–2 weeks | Moderate |
| Tool setup and pilot | 1 week | Low to moderate |
| Dataset collection/generation | 3–5 weeks | High |
| OCR and density labeling | 1–2 weeks | Moderate |
| Baseline model | 1–2 weeks | Moderate |
| Proposed model | 2–3 weeks | High |
| Robustness and ablation tests | 2 weeks | Moderate to high |
| Optional interface | 1 week | Low to moderate |
| Analysis and writing | 2–3 weeks | Moderate |
| **Total** | **14–20 weeks** | — |

For a two-person team, weak hardware, or limited data-generation access, plan for approximately 16–24 weeks or use the MVP scope.

### Feasibility checkpoints

**Checkpoint A: after pilot setup**  
Can the group run OCR, measure text density, and process a sample image?

**Checkpoint B: after baseline**  
Does performance actually change across density groups?

**Checkpoint C: after proposed model**  
Does the proposed method improve AI recall or reduce false negatives on high-density images?

If the proposed model does not improve, the study can still become a valid evaluation or ablation study, provided the experiment is rigorous and the conclusion is honest.

---

## 14. Suggested success criteria

These are proposed targets, not guaranteed outcomes:

- the baseline shows measurable performance differences across density levels;
- the proposed method is compared against a clearly defined baseline;
- high-density AI recall and false-negative rate are reported separately;
- the model does not rely on obvious metadata or source shortcuts;
- the proposed approach shows a meaningful improvement, such as a pre-specified percentage-point gain in high-density AI recall, or provides a well-supported analysis explaining why it did not;
- robustness and limitations are clearly reported.

Do not choose a success threshold after seeing the results without explaining the reason. Ideally, predefine the primary metric and target in the proposal.

---

## 15. Common mistakes to avoid

### Mistake 1: Treating the detector score as proof

A detector produces a probabilistic output. It should not be described as certain proof of AI generation.

### Mistake 2: Using accuracy only

High real-image accuracy plus very low fake-image recall can produce a misleading overall accuracy. Report per-class metrics.

### Mistake 3: Training and testing on the same generator style

This can make results look strong but fail on unseen generators.

### Mistake 4: Using OCR as a spelling checker

Text correctness is not a reliable universal indicator of AI generation.

### Mistake 5: Deleting all text regions

Text can contain useful artifacts. Separate it and model it; do not automatically discard it.

### Mistake 6: Making the architecture too ambitious

Begin with transfer learning, simple feature fusion, and a controlled dataset. Add complexity only when the baseline and data pipeline work.

### Mistake 7: Claiming to solve the entire problem

Use “reduce,” “improve,” “mitigate,” or “evaluate.” Avoid “eliminate,” “perfect,” and “universal” unless the evidence supports those claims.

---

## 16. Current deliverable already created

An editable Word visual guide was created for the group:

```text
text_density_detector_group_guide.docx
```

It contains:

- a one-sentence explanation;
- a diagram of the ordinary detector problem;
- the proposed three-branch architecture;
- explanations of text-region, non-text-region, and global-image branches;
- the correction that text should not simply be ignored;
- a five-step thesis project workflow;
- an MVP recommendation;
- a short pitch for group discussion;
- a reference to the TextFake preprint.

If this file is not available in the new conversation, upload the DOCX again or recreate it from the architecture above.

---

## 17. Recommended division of group work

### Member A: dataset and documentation

- source and organize real images;
- record labels and metadata;
- check privacy and copyright issues;
- maintain the dataset documentation.

### Member B: OCR and preprocessing

- implement text detection;
- calculate density score;
- create text masks and region crops;
- check OCR quality.

### Member C: machine-learning pipeline

- train baseline;
- implement feature extraction and fusion;
- track experiments;
- save checkpoints and configurations.

### Member D: evaluation and interface

- compute metrics;
- generate confusion matrices and density-level comparisons;
- perform robustness tests;
- create optional Streamlit interface and presentation figures.

Every member should understand the complete pipeline before the defense. Division of labor should not create a situation where only one student can explain the model.

---

## 18. Immediate next actions

The next AI should help the user complete these actions in order:

1. Choose the exact thesis scope: MVP or full three-branch version.
2. Decide whether the first dataset will use English only or English plus Filipino.
3. Decide the allowed image categories.
4. Create a data schema and a 200-image pilot collection plan.
5. Define the text-density measurement and category thresholds.
6. Set up the baseline experiment before designing the full model.
7. Write the final title, statement of the problem, objectives, conceptual framework, and methodology only after the pilot confirms feasibility.

### Best immediate question for the group

> Do we have enough time, Python/deep-learning skill, and GPU access to build and test a baseline plus OCR-guided region-aware model, or should we begin with density-aware calibration as the minimum viable thesis?

---

## 19. Suggested first message in the next conversation

```text
We are continuing a Computer Science thesis project. Please read the attached handoff file completely before responding. Our topic is AI-generated image detection on text-rich images, particularly the problem called the Text Density Curse. We want a realistic undergraduate thesis, not an overambitious research project.

Our proposed direction is an OCR-guided, text-region-aware detector that separately processes text-region, non-text-region, and global-image features, then fuses them to reduce false negatives. We need you to help us decide between the minimum viable version and the full three-branch version, based on our actual team size, skills, timeline, and available GPU.

First, summarize the project in five points, identify any risky assumptions, and ask only the most important feasibility questions. Do not invent experimental results.
```

---

## 20. Final continuity note

The project should continue from **feasibility validation**, not from a generic explanation of how AI-image detectors work. The next AI must preserve the following core logic:

```text
Text density can overwhelm or mask detector signals.
OCR identifies where the text is and helps measure density.
Text, non-text, and global features are analyzed separately.
The branches are fused for a final prediction.
The research goal is to reduce false negatives, not claim perfect detection.
```

