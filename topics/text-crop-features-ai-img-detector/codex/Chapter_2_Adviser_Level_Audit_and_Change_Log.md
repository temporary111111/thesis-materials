# Chapter 2 Adviser-Level Audit and Change Log

**Thesis:** *Machine Learning Classification of AI-Generated and Real Text-Containing Images Using Visual Text-Region Features*  
**Audit date:** September 19, 2026  
**Manuscript audited:** `CHAPTER 2 - Review of Related Literature and Studies - Draft.md`  
**Audit basis:** Chapter 1, the professor's Chapter 2 guide, the latest source-to-section matrix, the research handoff, and verified publication records

## Audit verdict

**Status: Pass after revisions applied.**

The chapter now provides a coherent thematic review, uses sufficient source coverage for each principal literature section, distinguishes established evidence from the proposed study's hypotheses, states a bounded and defensible research gap, and remains aligned with the scope defined in Chapter 1. It is ready for adviser review as a complete Chapter 2 draft. Decisions that properly belong to Chapter 3 remain open and are identified at the end of this report.

## Quantitative audit

| Check | Result | Status |
|---|---:|---|
| Major Chapter 2 sections | 12 | Pass |
| Feature subsections | 5 | Pass |
| References | 35 | Pass |
| Published sources | 33 | Pass |
| Explicitly labeled preprints | 2 | Pass |
| Sources published from 2021 onward | 25 | Pass |
| Older foundational or adjacent sources | 10 | Acceptable with stated roles |
| References cited in the manuscript | 35 of 35 | Pass |
| Cited works missing from the reference list | 0 | Pass |
| Conceptual framework | Input–Process–Output | Pass |

## Source coverage by section

| Section | Unique cited sources | Audit assessment |
|---|---:|---|
| 2.1 Introduction | 4 | Sufficient framing |
| 2.2 AI-Generated Image Detection | 11 | Strong coverage of methods, benchmarks, and generalization |
| 2.3 Text-Rich Images and Data | 5 | Sufficient; direct text-rich literature remains limited and is acknowledged |
| 2.4 Text-Region Detection | 4 | Sufficient foundational and recent method coverage |
| 2.5 Visual Text-Region Features | 12 | Strong interdisciplinary support |
| 2.6 Traditional ML Classifiers | 4 | Sufficient foundations plus applied precedent |
| 2.7 Evaluation and Reliability | 10 | Strong coverage of metrics, leakage, validation, and reproducibility |
| 2.8 Systems and Prototype Context | 3 | Sufficient for a bounded research prototype |
| 2.9 Synthesis | 26 | Integrates the major evidence streams |
| 2.10 Research Gap and Contribution | 10 | Directly supported and bounded |

Sections 2.11 and 2.12 do not require new sources because they present the study-derived conceptual framework and summarize the reviewed chapter.

## Guide-compliance audit

### Thematic organization — Pass

The manuscript is organized by concepts and research functions rather than by presenting one article per paragraph. Individual studies are compared within the themes of detector design, data, localization, visual features, classifiers, evaluation, and system implementation.

### Integration of literature and studies — Pass

The chapter links findings from AI-image detection, scene-text detection, document-image quality, image forensics, traditional machine learning, and evaluation methodology. Each major theme ends by explaining its implication or boundary for the present study.

### Recent and credible sources — Pass

Twenty-five of the 35 references are from 2021–2026. Older sources are retained for defined reasons: classifier foundations, the Stroke Width Transform, early localized-forensic evidence, and established evaluation methodology. The two non-peer-reviewed works, TextFake and PatchCraft, are explicitly described as arXiv preprints and are not used as the sole basis of the method.

### Synthesis and research gap — Pass after revision

The original draft contained wording that could be read as a universal claim that no integrated pipeline exists. That wording was replaced with an evidence-bounded formulation: the reviewed literature leaves an unresolved integration question. The revised gap is divided into representation, localization-to-classification integration, and comparative evaluation issues.

### Conceptual framework — Pass

The Input–Process–Output framework preserves the image as the unit of classification, treats detected text regions as intermediate measurement units, separates development feedback from final testing, and positions the prototype after model selection.

## Findings addressed during revision

### 1. Meaning of “real image”

**Risk:** The term could imply that every non-AI-generated sample is camera-native, unedited, or forensically authentic in a broader sense.  
**Revision:** Section 2.1 now defines *real* operationally as non-AI-generated according to the dataset criteria and states that the term does not automatically mean unedited or camera-native.

### 2. Research-gap overclaim

**Risk:** Phrases such as “absence of an integrated pipeline” could be interpreted as a universal no-prior-work claim.  
**Revision:** Sections 2.9, 2.10, and 2.12 now describe an unresolved integration question established by the reviewed evidence. The chapter acknowledges TextFake as direct prior work on text-rich images while distinguishing the proposed representation and traditional-classifier pipeline.

### 3. Scope drift from robustness literature

**Risk:** Discussion of unseen generators, cross-dataset evaluation, degradation, transmission, and re-digitization could be mistaken for promised experiments.  
**Revision:** Section 2.2 states that these studies identify threats to external validity and future work. Section 2.7 explicitly limits the study's conclusions to its defined data and split design.

### 4. OCR and semantic-feature boundary

**Risk:** “Text detection” could be confused with OCR transcription or language analysis.  
**Revision:** Sections 2.1 and 2.4 distinguish localization from recognition. Recognized words, spelling, language, and semantic meaning are excluded from the feature space.

### 5. Feature-evidence boundary

**Risk:** Related work on faces, general scenes, documents, or manipulation forgeries could be presented as proof that the proposed text features will work.  
**Revision:** Section 2.5 now states consistently that these studies establish plausibility and measurement precedent, while usefulness for the target task remains an empirical question.

### 6. Prototype overreach

**Risk:** General MLOps literature could make the project appear to promise a production platform.  
**Revision:** Section 2.8 restricts the prototype to a thin, traceable implementation of the evaluated pipeline and excludes claims of scalability, security, usability certification, forensic admissibility, and production-grade MLOps.

### 7. Bibliographic defects in the source matrix

The manuscript uses the corrected records for DBNet++, CG-DIQA, NPR, PatchCraft, Fu et al., AIDE, and Gösgens et al. The detailed corrections appear in `Chapter_2_Source_Verification_Notes.md`.

## Scope alignment with Chapter 1

The revised Chapter 2 preserves the following Chapter 1 commitments:

- Binary image classification: AI-generated versus real/non-AI-generated text-containing images.
- The complete image remains the classification unit.
- Text detection is used only to localize visual evidence.
- OCR transcription, spelling, language, and semantic interpretation are excluded.
- Candidate features cover density, stroke appearance, character shape, spacing, alignment, edges, gradients, texture, contrast, and sharpness or blur.
- The compared classifiers are logistic regression, support vector machine, and random forest.
- Evaluation uses accuracy, precision, recall, F1-score, and a confusion matrix.
- Cross-generator, cross-dataset, degradation, re-digitization, and adversarial tests remain outside the initial scope.
- The reproducible experimental pipeline is the principal contribution; the prototype is secondary.

## Matters intentionally deferred to Chapter 3

The following are not unresolved defects in Chapter 2. They are methodological decisions that must be specified and justified in Chapter 3:

1. Final image sources, sample counts, class balance, and inclusion criteria.
2. Operational provenance rule for labeling real and AI-generated images.
3. Selected text detector, model version, threshold, and region representation.
4. Exact mathematical definitions for each visual feature.
5. Region-to-image aggregation statistics and missing-region handling.
6. Duplicate and near-duplicate detection procedure.
7. Train, validation, and test proportions or nested-validation design.
8. Hyperparameter search spaces, scaling, feature selection, and random seeds.
9. Statistical or uncertainty reporting beyond the required classification metrics.
10. Prototype technology, saved-artifact format, input restrictions, and functional-test cases.

## Submission-readiness note

The content is ready for adviser review. When the department's complete manuscript template is available, the clean Word file should be merged into it so page numbering, front matter, heading styles, table or figure numbering, margins, and the institution's exact APA conventions remain consistent across all chapters.
