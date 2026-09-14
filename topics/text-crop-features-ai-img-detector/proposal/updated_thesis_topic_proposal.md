# THESIS TOPIC PROPOSAL

## I. Proposed Title

**Machine Learning Classification of AI-Generated and Real Text-Containing Images Using Visual Text-Region Features**

**CS Domain:** Machine Learning and Artificial Intelligence, with Computer Vision and Pattern Recognition  
**Application Area:** Digital media authenticity and image analysis  
**Computing Contribution:** A simple machine-learning classification approach that uses visual features extracted from text regions in images.  
**Bicol University Research and Development Agenda:** Social Development Promotion  
**Sustainable Development Goal:** SDG 16 – Peace, Justice and Strong Institutions  
**Expected Innovation:** A focused analysis of the visual appearance of embedded text, without using the meaning of the words as a classification basis.

## II. Background of the Study

Generative artificial intelligence has made it easier to create realistic digital images. These images can be useful for design, education, and entertainment, but they can also be used for misleading posts, fake announcements, fabricated documents, and other false digital content. For this reason, identifying whether an image is real or AI-generated has become an important problem in Computer Science.

AI-generated image detection remains difficult because an image may look realistic or may come from a source that was not represented in the training data. Existing benchmarks and studies have shown that detector performance can change across different image sources and conditions (Zhu et al., 2023; Ojha et al., 2023; Yan et al., 2025). These findings show that results from one dataset should not automatically be treated as effective for all images.

Text-containing images present a more specific challenge. Posters, announcements, and promotional graphics may contain many strokes, edges, repeated shapes, and closely arranged characters. These visual patterns can interfere with the general image clues commonly used by detectors. The TextFake benchmark reported that detection performance may decline on text-rich images and described this problem as the “Text Density Curse” (Zhang et al., 2026).

This study will examine whether visual features taken from text regions can provide useful information for classifying real and AI-generated images. The study will focus on the visible appearance of the text, such as stroke appearance, character shape, spacing, alignment, edge quality, texture, contrast, and text density. It will not analyze the meaning, topic, spelling, or semantic content of the words.

The study supports SDG 16 by contributing to the responsible checking of digital information. It also supports the Bicol University research agenda on Social Development Promotion by addressing a current concern in digital communication. The expected output is a small, research-based classification prototype. It will not be presented as a universal detector or as final proof of image authenticity.

## III. Existing Challenges, Limitations, and Research Gap

Many existing approaches use whole-image texture, frequency patterns, noise, or high-level visual features. Large-scale benchmarks are valuable, but they do not always explain how the embedded text itself affects classification. Recent evidence identifies text-rich images as a difficult setting, yet the usefulness of visual features extracted specifically from text regions remains limited or underexplored in a small controlled study.

This research addresses that gap by preparing a dataset of labeled real and AI-generated text-containing images, extracting visual features from their text regions, and comparing selected machine-learning classifiers. The study will determine whether these features provide useful classification information under the chosen dataset and conditions. It will not claim that the approach works for every generator, image type, script, or real-world situation.

## IV. Opportunities and Proposed Computing Approach

The proposed approach will use existing image-processing and machine-learning tools. First, visible text regions will be located and cropped. Next, selected visual properties will be measured from the crops. The resulting feature values will be used by selected classifiers, such as Logistic Regression, Support Vector Machine, or Random Forest, to predict whether an image is real or AI-generated.

The study will primarily use publicly available datasets containing labeled real and AI-generated text-containing images. Candidate sources may include TextRich, TextFake, or other suitable public datasets. The final dataset will be selected during the methodology phase based on accessibility, image quality, labels, usage permissions, and relevance to the study. No paid subscription to an AI image generator is required by this proposal. Creating additional images may be considered only if it becomes necessary and feasible.

## V. Introduction of the Proposed System

The proposed system will accept a text-containing image, locate its text regions, extract selected visual text-region features, and classify the image as real or AI-generated. It may display the predicted class and selected feature values. The prototype is intended for research demonstration and preliminary screening only; it will not replace human verification or professional fact-checking.

## VI. Statement of the Problem

This study aims to examine whether visual features extracted from text regions can be used to classify real and AI-generated text-containing images.

Specifically, it seeks to answer the following questions:

1. What visual features can be extracted from the text regions of selected text-containing images?
2. How accurately can selected machine-learning classifiers distinguish real images from AI-generated images using these features?
3. Which groups of visual text-region features provide useful information for the classification task?
4. What limitations can be observed when the approach is tested on the selected dataset?

## VII. Objectives of the Study

### General Objective

To develop and evaluate a machine-learning classification approach that uses visual text-region features to distinguish real and AI-generated text-containing images.

### Specific Objectives

1. To identify and prepare a suitable public dataset of labeled real and AI-generated text-containing images;
2. To identify and extract selected visual text-region features and implement selected machine-learning classifiers;
3. To develop a simple prototype that accepts an image and provides a real or AI-generated prediction; and
4. To evaluate the classifiers using accuracy, precision, recall, F1-score, and confusion matrix, and to check the basic functionality of the prototype.

## VIII. Significance of the Research

The study may help content reviewers and digital-media researchers understand the difficulty of checking text-containing images. It may serve as a practical example for Computer Science students learning image processing, feature extraction, and machine learning. Organizations that handle online posts or digital announcements may also gain a clearer understanding of the limits of automated image classification. Future researchers may use the documented feature groups, dataset preparation process, and limitations as a starting point for related studies.

## IX. Scope and Limitations

The study will focus on selected digital images with visible text, such as posters, announcements, or similar text-rich visual materials, depending on data availability. It will use publicly available datasets containing labeled real and AI-generated images. The exact dataset sources, number of images, and final composition will be determined in Chapter 3.

The task is limited to binary classification: real or AI-generated. The system will not identify the exact image generator, determine legal authenticity, or prove image provenance. The main inputs will be visual text-region features, including text density, stroke appearance, character shape, spacing, alignment, edge quality, texture, contrast, and sharpness. Text meaning, spelling, topic, and other semantic information will not be analyzed.

The study will compare selected traditional machine-learning classifiers and develop a simple demonstration prototype. It will not create a new deep-learning architecture or a production-level public service. Unseen-generator testing, broad cross-generator generalization, multilingual comparison, and common image-degradation experiments such as blur, resizing, and JPEG compression are outside the initial scope. The findings will apply only to the selected dataset and controlled testing conditions.

## X. Definition of Terms

**AI-Generated Image** – An image labeled as produced by an artificial-intelligence image-generation process in the selected dataset.

**Real Image** – An image labeled as non-AI-generated in the selected dataset.

**Text-Containing Image** – A digital image with visible printed, rendered, or embedded text.

**Text Region** – The part of an image where visible text is located and cropped for analysis.

**Visual Text-Region Features** – Measurable properties of a text region, including stroke appearance, character shape, spacing, alignment, edges, texture, contrast, and density.

**Machine-Learning Classifier** – A computational model that predicts whether an image is real or AI-generated based on extracted features.

**Classification Prototype** – The simple application developed to demonstrate image input, feature extraction, and classification.

## Initial References

Ojha, U., Li, Y., & Lee, Y. J. (2023). *Towards universal fake image detectors that generalize across generative models.* https://arxiv.org/abs/2302.10174

Yan, S., et al. (2025). *A sanity check for AI-generated image detection.* https://proceedings.iclr.cc/paper_files/paper/2025/file/b0303773962ea1b5394c3a83cc7dd066-Paper-Conference.pdf

Zhang, Y., et al. (2026). *TextFake: Benchmarking AI-generated image detection on text-rich images.* https://arxiv.org/abs/2606.01050

Zhu, M., et al. (2023). *GenImage: A million-scale benchmark for detecting AI-generated image.* https://proceedings.neurips.cc/paper_files/paper/2023/hash/f4d4a021f9051a6c18183b059117e8b5-Abstract-Datasets_and_Benchmarks.html
