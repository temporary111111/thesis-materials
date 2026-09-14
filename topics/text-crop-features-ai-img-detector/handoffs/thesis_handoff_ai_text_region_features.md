# HANDOFF FOR NEXT AI

## Purpose of this handoff

This file contains the working context for an undergraduate Computer Science thesis project. The user may paste this entire handoff into another AI if the current conversation is deleted. The next AI should continue from this context instead of restarting the topic from the beginning.

The current task is to refine and write a thesis topic proposal. The user has already uploaded the official thesis guides and has asked for a simple, focused, and feasible proposal.

## User profile and working preferences

- The user is an undergraduate Computer Science student.
- The user's main priority is to complete a clear, focused, manageable thesis that is sufficient for graduation.
- The user is not aiming for an overly impressive or highly advanced thesis.
- The user is worried that the dataset may be difficult to build or obtain.
- Explanations should usually be in simple Tagalog or Taglish.
- Thesis proposal wording should be in simple, natural English because the proposal will likely be submitted in English.
- The English should sound like a real undergraduate student who understands the topic. It should be formal enough for a proposal but easy to understand even for a nontechnical panel.
- Avoid high-level jargon, unnecessarily polished wording, long technical explanations, complicated formulas, and writing that obviously sounds AI-generated.
- Do not make the proposal unnecessarily ambitious.
- Do not bring back a methodology that the user has already excluded because it is too complicated.
- The user's goal is clarity, feasibility, and passing the thesis requirements.

## Core thesis idea

The thesis will study the classification of images into two classes:

1. Real image
2. AI-generated image

The study will focus only on images that contain visible text. The main idea is to locate or crop the text regions in an image and analyze the visual appearance of the text itself.

The study will not focus on the whole-image visual representation as its main signal. It will also not analyze the meaning of the words.

The intended process is:

1. Collect a dataset of real and AI-generated images that contain visible text.
2. Locate the text regions in each image.
3. Crop or isolate those text regions.
4. Extract visual features from the text regions.
5. Use the extracted features as input to a machine learning classifier.
6. Classify the image as real or AI-generated.
7. Evaluate the classifier and demonstrate it through a simple prototype.

The expected contribution is an evaluation of whether visual features from text regions can provide useful information for classifying real and AI-generated text-containing images.

## Latest binding decisions

These are the latest decisions and should be treated as more important than older ideas in the conversation.

### 1. Text meaning is excluded

The study does not care what the text says. It will not use word meaning, sentence meaning, topic, spelling correctness, word embeddings, language models, or semantic text features as the main input.

If OCR is used, it is only for locating text, estimating text-related measurements, or supporting annotation. OCR is not being used to understand the message of the text.

### 2. The text features should be visually meaningful and reasonably complete

The features should describe the appearance of text in several related areas, rather than using only one simple measurement such as text density.

Suggested feature families are:

- Text density and occupancy: amount of text area in the image, occupied area, number of detected text regions, and approximate text coverage.
- Stroke and thickness: stroke width, thickness consistency, foreground-to-background balance, and irregular stroke appearance.
- Character shape and geometry: contours, connected components, aspect ratios, compactness, shape irregularity, and consistency among characters.
- Spacing and layout: distance between characters or text boxes, line spacing, alignment, margins, and regularity of text placement.
- Edge and rendering quality: edge sharpness, edge smoothness, anti-aliasing-related appearance, blur, and boundary consistency.
- Local texture and contrast: texture inside and around the text, local contrast, sharpness, and intensity variation.

The proposal should name these feature groups in plain language. It does not need to list every formula or implementation detail at the proposal stage. Detailed formulas and exact preprocessing steps can be reserved for Chapter 3.

### 3. The task is binary classification only

The study will classify an image as real or AI-generated. It will not identify the exact generator. It will not determine whether the image is legally authentic or prove provenance.

### 4. No universal-detector claim

The study must not claim to detect all AI-generated images or work for every generator, language, image type, platform, or real-world condition.

The safest framing is that the study evaluates the usefulness of visual text-region features under a selected and controlled dataset.

### 5. Unseen generators and common image degradations are outside the initial scope

Do not include unseen-generator testing, cross-generator generalization, JPEG robustness, blur testing, resizing experiments, screenshot perturbations, or other degradation experiments in the initial proposal unless the user explicitly changes the scope later.

These may be mentioned as limitations or possible future work, but they should not be presented as required parts of the undergraduate thesis.

### 6. No complicated model design

The proposal should use selected existing machine learning classifiers, such as Logistic Regression, Support Vector Machine, or Random Forest. The final list can be reduced to two or three models depending on feasibility.

The study should not propose a new deep learning architecture, a multi-branch detector, a large vision-language model, or an advanced robustness framework.

An earlier idea involved OCR-based density groups and comparing training strategies such as standard ERM, density-balanced sampling, and GroupDRO. This was considered too complicated for the user's goal. Do not reintroduce these methods unless the user specifically asks for them.

### 7. The rushed pilot testing must not be used as evidence

The user previously performed a rushed pilot, but the user clearly stated that the data preparation and methodology were not reliable enough. The pilot results must not be cited, summarized, or used to justify the proposal.

### 8. Language restriction is not conceptually required

The user questioned why the scope was previously described as English-only. The study is based on visual text features, so the meaning or language of the text is not conceptually important.

The proposal should therefore use the broader term “text-containing images.” If a language or script restriction becomes necessary because of dataset availability or the chosen text-region detection tool, it should be described as a practical dataset limitation, not as a theoretical requirement of the method.

## Working image scope

To keep the dataset manageable, the current working scope is text-rich digital images such as:

- posters;
- announcements; and
- social-media promotional graphics.

This is a working choice and still needs to be finalized based on the availability of real and AI-generated examples. The scope can be narrowed to one image type if the dataset becomes difficult to prepare.

The images should have visible, rendered, or printed text. The study is not intended for ordinary natural images that contain no text.

## Main motivation

The general motivation is that AI-generated image detection remains difficult, especially when images are realistic or differ from the data used during training.

GenImage, a large benchmark introduced by Zhu et al. (2023), contains more than one million pairs of real and AI-generated images. It also includes cross-generator evaluation and degraded-image evaluation. This shows that image detection must be tested under different conditions and that results from one setting may not transfer automatically to another.

Ojha et al. (2023) also showed that a detector trained using images from some generative models may have difficulty detecting images from newer or different generators. This supports the broader point that generalization is a continuing problem.

Yan et al. (2025) evaluated several existing detectors using the Chameleon dataset, which contains AI-generated images that can appear realistic to human viewers. Their findings showed that existing detection is still far from solved.

The most direct motivation is TextFake by Zhang et al. (2026). TextFake is a recent benchmark for text-rich AI-generated image detection. It contains 20,000 images across multiple languages, topics, and scene types. The study reported a large performance gap between natural-image benchmarks and text-rich images. It identified the “Text Density Curse,” where dense glyphs and text structures can overwhelm the low-level visual cues used by detectors.

The proposal should use careful wording. It should say that recent evidence suggests that detector performance can decline on text-rich images. It should not say that all existing detectors fail whenever an image contains text.

The proposed thesis responds to this problem by isolating the text regions and evaluating visual properties such as stroke, character shape, spacing, edges, texture, contrast, and density. The study does not claim that these features will definitely improve detection. It asks whether they are useful and how well selected classifiers can use them under the chosen conditions.

TextFake should not be the only source used in the final Chapter 2 because it is a recent preprint. It should be supported with peer-reviewed work on AI-generated image detection, generalization, image forensics, text rendering, scene text analysis, and machine learning classification.

## Working research gap

Do not state that “no study has ever done this.” The guide specifically requires an evidence-based gap.

The safer research gap is:

> Existing AI-generated image detectors and benchmarks commonly focus on whole-image information, general image artifacts, frequency patterns, noise, or high-level visual features. Recent evidence shows that text-rich images create a difficult detection setting. However, the usefulness of visual features extracted specifically from text regions, while excluding text meaning and semantic analysis, remains limited or underexplored in a small controlled classification study.

The thesis will address this gap by:

- preparing a dataset of text-containing real and AI-generated images;
- extracting several groups of visual text-region features;
- implementing selected traditional machine learning classifiers;
- evaluating their binary classification performance; and
- presenting the method through a simple prototype.

The contribution is empirical and focused. It is not a universal detector and it is not a new generative model or advanced deep learning architecture.

## Uploaded official guides and their requirements

The user uploaded the following files:

1. `2_CHAPTER 1-Thesis-2026.docx.pdf`
2. `3_CHAPTER 2-Review of RL&S-Thesis-2026.docx.pdf`
3. `Topic_Proposal_Template_CS.pdf`
4. `Thesis_Domains_CS.pdf`
5. `Thesis_1_Course_Introduction_Sy.pptx`

### Requirements from the proposal template

The proposed title should show the computing problem, the computational approach, and the application area.

The proposal background should cover:

1. Context and relevance
2. Connection to SDGs, the Bicol University Research and Development Agenda, and other priorities when applicable
3. Existing challenges, limitations, and research gaps
4. Opportunities and proposed computing approach
5. Discussion of computing components and research areas
6. Concluding synthesis

The Introduction of the Proposed System should cover:

1. Core idea and computing innovation
2. Intended functionality and system components
3. Problem addressed and expected benefits
4. Relationship to existing studies
5. Concluding overview

The proposal should also include:

- General Objective
- Specific Objectives
- Statement of the Problem
- Significance of the Research
- Scope and Limitations
- Definition of Terms

### Required objective sequence

The guide recommends the following sequence:

Data → Algorithms/Models → System/Application → Evaluation

A suitable objective structure for this thesis is:

1. Collect, label, and prepare text-containing real and AI-generated images.
2. Identify and extract visual text-region features and implement selected machine learning classifiers.
3. Develop a simple prototype that accepts an image and provides a real or AI-generated prediction.
4. Evaluate the classifiers using accuracy, precision, recall, F1-score, and confusion matrix, and check the basic functionality of the prototype.

Do not put detailed train-test splits, formulas, advanced preprocessing, or complex feature engineering in the proposal. Those details belong in Chapter 3.

### Scope and limitations guidance

The guide says that scope should be directly aligned with the objectives and should define:

- data used;
- algorithms or models;
- system or prototype;
- evaluation procedures; and
- intended users or use setting.

Limitations should identify important constraints, such as data availability, selected algorithms, controlled conditions, and limited deployment. They should not become a random list of every possible feature that was excluded.

For this thesis, the scope should explicitly state that the study does not include unseen generators, common degradation testing, semantic text analysis, exact generator attribution, or universal real-world claims.

### Chapter 2 guidance

The Chapter 2 guide recommends:

- primarily recent sources from 2021 to 2026;
- older sources only when they are foundational or necessary;
- integrated related literature and related studies within themes;
- approximately 3 to 5 relevant sources for each major theme;
- at least 30 RRL sources for the complete review, based on the guide;
- full-text reading of sources, not abstract-only citation;
- complete and verified author and bibliographic information;
- consistent APA formatting;
- every in-text citation appearing in the reference list;
- synthesis across studies rather than one paragraph per author;
- an evidence-based research gap and study contribution;
- an IPO conceptual framework aligned with the objectives; and
- a closing paragraph that transitions to the next chapter.

Possible Chapter 2 themes for this thesis are:

1. AI-generated image detection and digital image authenticity
2. Generalization and limitations of existing detectors
3. Text-rich images and the Text Density Curse
4. Text-region detection and visual text analysis
5. Visual and typographic features of rendered text
6. Machine learning classification using handcrafted or structured features
7. Existing systems and applications for digital image forensics
8. Evaluation of binary image classifiers

The final Chapter 2 should not merely repeat the proposal background. It should compare sources, identify patterns and differences, and connect the review directly to the selected features and models.

### CS domain and alignment

The best primary CS domain is:

- Machine Learning and Artificial Intelligence

Relevant computing areas are:

- Computer Vision
- Image Processing
- Pattern Recognition
- Digital Image Forensics

Digital forensics or cybersecurity can be treated as the application area, but the main contribution must remain the computing method and its evaluation.

A reasonable proposed alignment is:

- Bicol University Research and Development Agenda: Social Development Promotion
- Primary SDG: SDG 16, Peace, Justice and Strong Institutions
- Possible secondary SDG: SDG 9, Industry, Innovation and Infrastructure

This alignment should be worded cautiously. The thesis may support the checking of digital information, but it will not claim to solve misinformation or guarantee image authenticity.

## Current working title

The current working title is:

> Machine Learning Classification of AI-Generated and Real Text-Containing Images Using Visual Text-Region Features

This title is intentionally framed as classification and evaluation. It avoids words such as universal, robust, generalizable, or authentication, which could create claims beyond the actual scope.

## Current proposal draft direction

### General Objective

The main objective is to develop and evaluate a machine learning classification approach that uses visual text-region features to distinguish real and AI-generated text-containing images.

### Specific Objectives

1. To collect, label, and prepare a dataset of selected real and AI-generated text-containing images, particularly text-rich digital images such as posters and social-media graphics;

2. To identify and extract visual features from the detected text regions, including stroke appearance, character shape, spacing, alignment, edge quality, texture, contrast, and text density;

3. To implement selected machine learning classifiers and develop a simple prototype that uses the extracted visual text-region features to classify images as real or AI-generated; and

4. To evaluate the classification performance of the selected models using accuracy, precision, recall, F1-score, and confusion matrix, and to check the basic functionality of the developed prototype.

### Current proposed system

The prototype is only a simple demonstration platform. A user may upload an image. The prototype will locate the visible text regions, extract the selected visual features, pass them to the trained classifier, and display a predicted class.

The prototype may also show selected feature values so that the process is easier to understand. It should not be described as a public or production-level service.

### Current statement of the problem

The study aims to examine whether visual features extracted from text regions can be used to classify real and AI-generated text-containing images.

Possible research questions are:

1. What visual features can be extracted from the text regions of selected text-containing images?
2. How accurately can selected machine learning classifiers distinguish real images from AI-generated images using these features?
3. Which groups of visual text-region features provide useful information for the classification task?
4. What limitations can be observed when the approach is tested on the selected dataset?

### Current significance direction

Potential beneficiaries should be described realistically:

- Content reviewers and fact-checking practitioners may use the prototype as a preliminary screening aid, but not as final proof.
- Digital media researchers may use the findings as a reference for studying text-rich images.
- Computer Science students may use the study as an example of Computer Vision, feature extraction, and Machine Learning.
- Organizations that handle digital posts, announcements, or visual documents may gain a better understanding of the problem.
- Researchers and future researchers may use the feature grouping, dataset preparation process, results, and limitations as a starting point for later work.

### Current scope direction

The study will focus on selected digital images with visible text, initially posters, announcements, and social-media promotional graphics. The dataset will contain real and AI-generated examples from selected sources or selected image generators.

The study will use visual text-region features only. It will not analyze text meaning, spelling, language content, or semantic embeddings. It will use selected traditional machine learning classifiers and a simple prototype.

The study will not include:

- unseen-generator testing;
- common image degradation experiments;
- universal detector claims;
- exact generator identification;
- provenance verification;
- whole-image semantic embeddings as the main feature source;
- a new deep learning architecture; or
- the rushed pilot results.

## Important wording rules for the next AI

Use phrases such as:

- “under the selected dataset and controlled conditions”;
- “may provide useful information”;
- “the study evaluates the usefulness of…”;
- “recent evidence suggests…”;
- “limited evaluation of…”;
- “the prototype is intended for research and demonstration.”

Avoid phrases such as:

- “solves misinformation”;
- “detects all AI-generated images”;
- “works for every generator”;
- “guarantees authenticity”;
- “no previous study has done this”;
- “state-of-the-art”;
- “universal detector”; and
- “fully robust in real-world conditions.”

## Open decisions that still need to be finalized

These are the remaining practical decisions. The next AI should help the user decide them one at a time without making the proposal unnecessarily complex.

1. Exact image category: posters only, posters and announcements, or posters and social-media graphics.
2. Exact data source and approximate dataset size.
3. Which real-image sources are accessible and legally usable.
4. Which AI image generator or generators are available for creating or collecting the AI-generated examples.
5. Final list of two or three machine learning classifiers.
6. Basic text-region detection or OCR tool that is feasible for the group.
7. Whether text density will be used only as one feature or also reported as a simple supporting variable.
8. Whether the prototype will include only prediction or also display selected feature values.
9. Final confirmation of the Bicol University agenda and SDG alignment.

The next AI should not ask the user to reconfirm decisions that are already settled, such as excluding semantics, excluding unseen generators, excluding degradation testing, and not using the rushed pilot.

## Verified initial literature

These sources were checked during the earlier research stage and can serve as starting points. The final Chapter 2 must expand the list and verify complete APA details from the full papers.

1. Zhang, Y., Miao, C., Liao, M., Liu, T., Wang, X., Gong, T., Chu, Q., & Yu, N. (2026). *TextFake: Benchmarking AI-Generated Image Detection on Text-Rich Images*. arXiv preprint. https://arxiv.org/abs/2606.01050

   Main use: text-rich image detection, Text Density Curse, performance gap on text-containing images. Treat as recent supporting evidence and supplement it with peer-reviewed sources.

2. Zhu, M., Chen, H., Yan, Q., Huang, X., Lin, G., Li, W., Tu, Z., Hu, H., Hu, J., & Wang, Y. (2023). *GenImage: A Million-Scale Benchmark for Detecting AI-Generated Image*. Advances in Neural Information Processing Systems, 36. https://proceedings.neurips.cc/paper_files/paper/2023/hash/f4d4a021f9051a6c18183b059117e8b5-Abstract-Datasets_and_Benchmarks.html

   Main use: large-scale real-versus-AI benchmark, cross-generator task, and degraded-image task.

3. Ojha, U., Li, Y., & Lee, Y. J. (2023). *Towards Universal Fake Image Detectors that Generalize Across Generative Models*. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. https://arxiv.org/abs/2302.10174

   Main use: limits of generalization across generative models.

4. Yan, S., Li, O., Cai, J., Hao, Y., Jiang, X., Hu, Y., & Xie, W. (2025). *A Sanity Check for AI-generated Image Detection*. International Conference on Learning Representations. https://proceedings.iclr.cc/paper_files/paper/2025/file/b0303773962ea1b5394c3a83cc7dd066-Paper-Conference.pdf

   Main use: challenging AI-generated images, detector limitations, and the fact that the task is not solved.

## Recommended next step

The next AI should first review this handoff, then help the user lock the smallest practical dataset scope. After that, revise the proposal draft in the official template order. The proposal should remain simple and should not yet contain advanced methodology.

The most practical immediate task is to compare two or three possible image categories and select the one with the easiest access to both real and AI-generated examples. Once that is decided, the title, objectives, scope, background, and Chapter 2 themes should be updated so that all parts remain consistent.

## One-sentence summary

This is a focused undergraduate Computer Science thesis that evaluates whether visual features extracted from text regions can classify real and AI-generated text-containing images, using selected traditional machine learning models and a simple prototype, under controlled conditions and without analyzing text meaning or claiming universal detection.
