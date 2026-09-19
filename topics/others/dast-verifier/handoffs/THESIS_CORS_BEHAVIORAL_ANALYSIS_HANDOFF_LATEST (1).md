# THESIS CORS BEHAVIORAL ANALYSIS HANDOFF

## STATUS OF THIS FILE

This file is the **latest canonical continuation context** for the user's BS Computer Science thesis planning.

It supersedes:

- `THESIS_CYBERSEC_NARROWING_HANDOFF_UPDATED.md`
- the earlier version of `THESIS_CORS_BEHAVIORAL_ANALYSIS_HANDOFF_LATEST.md`

The user previously had a long AI conversation that was deleted. The current conversation reconstructed the newer direction from the user's memory and then corrected an important architectural misunderstanding:

> **OWASP ZAP is not part of the training/data-generation pipeline.**

The controlled training pipeline belongs to the group's own Layer 2 system.

The next AI should read this file carefully and continue from the latest state without making the user re-explain prior decisions.

The goal is continuity.

Do not reopen settled steps unless the user explicitly asks.

---

# USER WORKING STYLE

- Main language: **Taglish**
- Prefer practical, direct, easy-to-understand explanations
- Avoid unnecessarily long academic explanations
- The user often has limited time to read
- The user values **actual technical feasibility** more than flashy ideas
- Do not force AI/ML just to make the thesis sound advanced
- Do not blindly accept the user's technical assumptions; the user explicitly appreciates being corrected when necessary
- The user is not yet knowledgeable about CORS or web security, so explain technical details carefully without being condescending
- Do not jump to a final title too early
- When explaining to the user or groupmates, use simple Taglish
- The user may not remember exact technical wording but can recognize whether a reconstructed idea matches the deleted conversation
- Never assume an older handoff is the latest truth

---

# BROADER THESIS PROJECT CONTEXT

The group already completed a large topic-dumping phase across many Computer Science domains.

The earlier broad cybersecurity narrowing considered:

1. Malware Analysis
2. Vulnerability Detection
3. Intrusion Detection

The group then focused on:

> **Vulnerability Detection**

More specifically:

> **Deployed web application vulnerability analysis using DAST**

An older concept considered three finding categories:

- CORS
- Cookie Security
- Security Headers

That version is no longer the active direction.

The project later narrowed to:

> **CORS only**

Do not return to broad topic hunting.

Do not re-add Cookie Security or Security Headers unless the user explicitly asks.

---

# LATEST RECONSTRUCTED THESIS DIRECTION

The current thesis concept is:

> OWASP ZAP acts as Layer 1 and detects a possible CORS issue on an authorized deployed website. The group's own system acts as Layer 2 and independently performs behavioral analysis of the affected endpoint. Based on the observed cross-origin behavior, the Layer 2 system classifies the finding as Confirmed Misconfiguration, Needs Further Review, or Not Confirmed / Downgraded.

Simple one-line explanation:

> **ZAP points to a possible CORS issue; our system independently investigates the application's actual cross-origin behavior.**

Another useful phrasing:

> **ZAP is the candidate finder. The group's system is the behavioral analysis and classification layer.**

---

# CRITICAL ARCHITECTURE CORRECTION

The earlier reconstructed flow incorrectly placed OWASP ZAP inside the training/data-generation pipeline.

That is **not** the current intended design.

## Correct separation

### Layer 1 — OWASP ZAP

Role:

- initial DAST scanner
- detects or flags a possible CORS issue
- identifies the affected URL or endpoint
- hands the candidate finding to Layer 2

### Layer 2 — The Group's System

Role:

- receives the candidate endpoint
- sends its own controlled cross-origin probes
- observes actual server behavior
- extracts behavioral features
- classifies the finding
- provides supporting evidence and explanation

The intended architecture is:

```text
OWASP ZAP
    ↓
Possible CORS finding
    ↓
Affected endpoint / candidate target
    ↓
GROUP'S LAYER 2 SYSTEM
    ↓
Behavioral probing
    ↓
Feature extraction
    ↓
Classification
    ↓
Confirmed / Needs Review / Downgraded
```

Important:

> **The model should not need ZAP's judgment in order to classify behavior.**

The intended model learns from the group's own observable behavioral evidence.

---

# IMPORTANT DISTINCTION: OPERATIONAL VS MODEL DEPENDENCY

The system may be operationally connected to OWASP ZAP in the final workflow.

Meaning:

```text
ZAP finding
    ↓
Layer 2 analyzes the endpoint
```

However, the classification model should ideally not depend on:

- ZAP risk level
- ZAP confidence level
- ZAP severity
- ZAP's final interpretation

The current default design is:

> **ZAP provides the candidate endpoint, but the Layer 2 classifier uses independent behavioral evidence.**

This creates a cleaner research architecture because the Layer 2 system does not simply learn to copy ZAP.

The Layer 2 system could theoretically analyze an endpoint supplied by another authorized source, although the intended thesis workflow currently uses ZAP as Layer 1.

---

# IMPORTANT DISTINCTION: THIS IS NOT SAST

The user does **not** mean source-code vulnerability detection.

This project is about:

- DAST
- black-box testing
- deployed web applications
- CORS behavior
- authorized or controlled targets

The system analyzes a deployed website using requests and responses.

Testing must stay within:

- local lab targets
- intentionally vulnerable applications
- university-controlled systems
- explicitly authorized websites

Never frame the project as scanning arbitrary public websites.

---

# CORRECT TRAINING / DATA-GENERATION PIPELINE

The training pipeline is independent of OWASP ZAP.

The current intended flow is:

```text
Custom Controlled Web Application
        ↓
Automatically modify CORS configuration
        ↓
Generate many controlled CORS scenarios
        ↓
The group's Behavioral Analyzer tests each scenario
        ↓
Observe request-response behavior
        ↓
Extract behavioral features
        ↓
Use the known controlled scenario as ground-truth reference
        ↓
Assign label:
- Confirmed Misconfiguration
- Needs Further Review
- Not Confirmed / Downgraded
        ↓
Build labeled dataset
        ↓
Determine whether Rule-Based, ML-Based, or Hybrid analysis is justified
```

The key corrected relationship is:

> **Configuration → Observed Behavior → Label**

Not:

> Configuration → Label only

And not:

> Configuration → ZAP → Label

---

# WHY "CONFIGURATION → OBSERVED BEHAVIOR → LABEL" MATTERS

The controlled environment knows the internal server-side CORS configuration.

For example:

```text
Internal controlled configuration:
- reflect arbitrary origins
- allow credentials
- allow selected methods
```

However, on a future external authorized website, the Layer 2 system normally cannot see the server's internal configuration file or source code.

It can only observe behavior.

For example:

```text
Trusted origin probe       → accepted
Random origin A probe      → accepted
Random origin B probe      → accepted
Origin value               → reflected
Credentials                → allowed
Preflight                  → accepted
Actual request             → data returned
```

Therefore:

> **The known CORS configuration is used to generate controlled scenarios and help establish ground truth, but the model should learn from externally observable behavior.**

This sentence is central to the thesis design.

---

# CONTROLLED SCENARIO GENERATOR

The group plans to build a controlled web application where CORS configurations can be changed automatically.

The goal is not to manually build hundreds of separate websites.

The controlled environment should be able to:

1. select or generate a CORS configuration;
2. apply the configuration to the test web application;
3. expose one or more controlled routes/endpoints;
4. let the group's behavioral analyzer test the scenario;
5. record the observable results;
6. assign a ground-truth label;
7. save the scenario as a row or set of rows in a CSV/spreadsheet;
8. move to the next scenario automatically.

Conceptual loop:

```text
for each CORS scenario:
    apply configuration
    run behavioral tests
    extract observable features
    determine ground-truth label
    save to dataset
```

OWASP ZAP is intentionally absent from this training loop.

---

# CURRENT DATASET CONCEPT

The user currently visualizes the output as a CSV or spreadsheet containing many generated CORS scenarios and three labels.

That is broadly correct.

However, the dataset should distinguish between:

## A. Internal Experimental Metadata

This is known because the researchers control the test environment.

Examples:

- scenario ID
- internal CORS configuration
- allowed-origin mode
- credentials setting
- allowed methods
- allowed headers
- route type
- endpoint sensitivity
- server framework
- known scenario family

These fields are useful for:

- scenario generation
- experimental control
- auditing
- reproducibility
- ground-truth construction

But:

> **Internal-only metadata should not automatically become model input features.**

If a field would not be available when analyzing a future website, the model should not depend on it.

## B. Observable Behavioral Features

These are the primary candidate inputs for the classifier.

Examples:

- trusted origin accepted or rejected
- first random untrusted origin accepted or rejected
- second random untrusted origin accepted or rejected
- arbitrary origin reflection observed or not
- wildcard behavior observed or not
- `null` origin accepted or rejected
- `Access-Control-Allow-Credentials` observed or not
- preflight `OPTIONS` accepted or rejected
- requested method allowed or rejected
- requested headers allowed or rejected
- actual request accepted or rejected
- response status code
- response body similarity or difference
- behavior consistency across repeated probes
- response difference across origins
- credentialed response behavior
- whether protected or sensitive content appears exposed
- endpoint context, when inferable

The exact features are not yet final.

---

# CANDIDATE DATASET STRUCTURE

The exact schema is not final.

A candidate training table may contain:

```text
scenario_id
trusted_origin_accepted
random_origin_1_accepted
random_origin_2_accepted
arbitrary_origin_reflected
wildcard_observed
null_origin_accepted
credentials_allowed
preflight_accepted
requested_method_allowed
requested_headers_allowed
actual_request_accepted
response_status_code
response_similarity
protected_content_observed
behavior_consistency
endpoint_context
final_label
```

Optional internal-only columns may include:

```text
internal_cors_configuration
scenario_family
server_framework
route_type
known_ground_truth_notes
```

Important:

> Internal-only fields must not accidentally leak into the model feature set if they would be unavailable during real use.

---

# CURRENT THREE LABELS

The current intended labels are:

## 1. Confirmed Misconfiguration

Meaning:

> The behavioral evidence strongly supports the possible CORS issue.

Possible example:

```text
Untrusted arbitrary origins accepted
+
Origin dynamically reflected
+
Credentials allowed
+
Sensitive or authenticated response exposed
=
Confirmed Misconfiguration
```

## 2. Needs Further Review

Meaning:

> Suspicious behavior exists, but the evidence is incomplete, context-dependent, inconsistent, or ambiguous.

Possible example:

```text
Untrusted origin accepted
+
Credentials unclear or not observed
+
Endpoint sensitivity uncertain
+
Response behavior inconsistent
=
Needs Further Review
```

## 3. Not Confirmed / Downgraded

Meaning:

> The behavioral analysis does not support the original concern strongly enough to keep it at the same level.

Possible example:

```text
Wildcard CORS
+
Public resource
+
No credentials
+
No sensitive information exposed
=
Not Confirmed / Downgraded
```

The exact wording of the third class is not yet final.

Possible alternatives:

- Not Confirmed
- Downgraded
- Low-Concern Behavior
- Contextually Downgraded

Do not finalize the wording yet.

---

# CURRENT BEHAVIORAL ANALYSIS CONCEPT

Behavioral analysis means the system does more than read one response header.

It actively changes request conditions and observes how the server responds.

Example probes:

```text
Request A:
Origin: trusted-origin.example

Request B:
Origin: random-untrusted-a.example

Request C:
Origin: random-untrusted-b.example

Request D:
Origin: null
```

The analyzer may then ask:

- Did the server accept the trusted origin?
- Did it also accept arbitrary untrusted origins?
- Did it reflect the supplied origin?
- Did it return `Access-Control-Allow-Credentials: true`?
- Did preflight behavior match actual request behavior?
- Did response content differ across origins?
- Did authenticated or sensitive content remain accessible?
- Did repeated probes produce consistent behavior?

This is the technical heart of the current project.

---

# POSSIBLE CONTROLLED CORS SCENARIOS

The exact scenario matrix is not final.

Current likely candidates include:

- no CORS
- trusted origin only
- wildcard origin
- arbitrary origin reflection
- arbitrary origin reflection with credentials
- trusted vs untrusted origin comparison
- `null` origin acceptance
- preflight accepted but actual request rejected
- preflight rejected but simple request accepted
- method-specific CORS behavior
- header-specific CORS behavior
- public endpoint with permissive CORS
- authenticated endpoint with permissive CORS
- sensitive endpoint with credentialed cross-origin access
- inconsistent behavior across routes
- inconsistent behavior across repeated probes

Do not automatically include every possible combination.

The scenario space must remain:

- technically meaningful
- reproducible
- large enough for evaluation
- feasible for an undergraduate thesis

---

# ACTUAL USE / PREDICTION PIPELINE

The intended real-use flow is:

```text
Authorized deployed website
        ↓
OWASP ZAP scans it
        ↓
ZAP reports a possible CORS issue
        ↓
ZAP provides the affected endpoint / raw candidate information
        ↓
The group's Layer 2 system starts independent behavioral analysis
        ↓
Send controlled cross-origin probes
        ↓
Extract the same behavioral features used during training
        ↓
Analysis engine or trained model predicts:
- Confirmed Misconfiguration
- Needs Further Review
- Not Confirmed / Downgraded
        ↓
Provide supporting evidence and explanation
```

The training and actual-use pipelines must match at the feature level.

Meaning:

> **The same type of behavioral evidence used to train the model must be collectable from future authorized websites.**

---

# ROLE OF OWASP ZAP

OWASP ZAP is not the training data generator.

OWASP ZAP is:

- Layer 1
- initial scanner
- candidate finder
- trigger for Layer 2 analysis
- source of the affected endpoint or finding context

Do not say:

> “Our contribution is integrating OWASP ZAP.”

That is too weak.

The computing contribution is after the scan:

```text
Candidate CORS endpoint
        +
Custom behavioral probes
        +
Observable response evidence
        ↓
Feature extraction
        ↓
Classification / verification
        ↓
Confirmed
Needs Further Review
Downgraded
```

---

# CURRENT ML / AI STATUS

The group discussed possibly using AI or Machine Learning.

This is **not final**.

The current honest position is:

> **The use of ML must first be justified by the structure and complexity of the behavioral dataset.**

Do not force ML.

The key question is:

> **Are the final classifications complex enough that a learned model provides real value over deterministic rules?**

---

# WHY ML MAY NOT BE NEEDED

If the entire classification can be expressed using a few obvious rules such as:

```text
IF arbitrary origin reflection = yes
AND credentials allowed = yes
THEN Confirmed

ELSE IF wildcard = yes
AND public resource = yes
AND credentials = no
THEN Downgraded
```

then a rule-based system may be more appropriate, more explainable, and easier to defend.

Potential panel criticism:

> “Why use machine learning when the CORS logic is deterministic?”

That is a valid criticism.

---

# WHY ML MAY STILL MAKE SENSE

ML becomes more defensible if the classification depends on many interacting behavioral observations, for example:

- multiple origin probes
- repeated requests
- response consistency
- preflight vs actual request differences
- credential behavior
- route-specific behavior
- endpoint context
- ambiguous combinations
- partial evidence
- conflicting signals

The most likely class where ML could add value is:

> **Needs Further Review**

because it represents ambiguity rather than a simple deterministic condition.

Possible research direction:

> Can a machine learning model classify possible CORS findings based on dynamically observed cross-origin behavior more effectively than a deterministic rule-based baseline?

This is promising but not yet final.

---

# CRITICAL ML DESIGN RISK

Avoid this weak setup:

```text
Researchers create obvious CORS rules
        ↓
Researchers assign labels directly from those same rules
        ↓
Model is trained on those rule-derived labels
        ↓
Model learns to copy the rules
        ↓
High accuracy is reported
```

This may produce a working classifier but a weak research contribution.

Possible panel criticism:

> “What did the model learn that could not simply be written as rules?”

The study must avoid becoming artificial label recreation.

---

# CURRENT STRONGER RESEARCH DESIGN DIRECTION

The current strongest tentative design is:

```text
PHASE 1
Controlled CORS Scenario Generation

        ↓

PHASE 2
Independent Behavioral Analysis

        ↓

PHASE 3
Behavioral Feature Dataset Construction

        ↓

PHASE 4
Ground-Truth Label Assignment

- Confirmed Misconfiguration
- Needs Further Review
- Not Confirmed / Downgraded

        ↓

PHASE 5
Compare Analysis Approaches

Rule-Based Baseline
vs
Machine Learning Classifier

        ↓

PHASE 6
Evaluate

Which approach better classifies unseen
CORS behavioral scenarios?
```

This is not locked yet, but it is currently the most defensible direction.

The important framing is:

> **The thesis does not assume ML is automatically better. It empirically tests whether ML provides a real advantage.**

---

# GENERALIZATION REQUIREMENT

Do not train and test on effectively identical scenarios.

Weak evaluation:

```text
Train on Scenario A
Test on another copy of Scenario A
```

Stronger evaluation:

```text
Train on one set of CORS behavior combinations
Test on unseen combinations
```

Even stronger:

```text
Train on one controlled application structure
Test on a different application structure or framework
```

The goal should be to test whether the analysis method generalizes beyond memorizing the scenario generator.

---

# POSSIBLE MODELING OPTIONS

Do not select a final algorithm yet.

If ML is justified, prefer interpretable models for tabular behavioral data first.

Possible candidates:

- Decision Tree
- Random Forest
- XGBoost

Do not force:

- deep learning
- LLMs
- neural networks

unless the data structure later clearly justifies them.

---

# CURRENT POSSIBLE RESEARCH QUESTIONS

Provisional only:

> **Can machine learning improve the classification of possible CORS findings based on dynamically observed cross-origin behavior compared with a deterministic rule-based baseline?**

Alternative:

> **How effectively can behavioral analysis classify possible CORS findings across controlled and unseen CORS configurations?**

Alternative:

> **Does a machine-learning classifier provide a measurable advantage over rule-based analysis for classifying CORS findings as Confirmed Misconfiguration, Needs Further Review, or Not Confirmed / Downgraded?**

Do not lock the final research question yet.

---

# CURRENT POSSIBLE COMPUTING CONTRIBUTION

Provisional direction:

> **A behavioral analysis framework for classifying possible CORS findings using dynamically observed cross-origin request-response behavior.**

If ML proves justified:

> **A machine-learning-assisted behavioral classification framework for CORS findings.**

If ML does not prove justified:

> **A rule-based behavioral verification and classification framework for CORS findings.**

If the comparison itself becomes the thesis:

> **A comparative behavioral analysis framework evaluating rule-based and machine-learning approaches for classifying CORS findings.**

Do not finalize the wording until the data design and novelty check are complete.

---

# WHAT IS SETTLED

Do not reopen these unless the user asks:

- The project is about deployed web applications, not source code
- The project is DAST-oriented
- The current focus is CORS only
- OWASP ZAP is Layer 1
- The group's system is Layer 2
- OWASP ZAP is not part of the training/data-generation pipeline
- The Layer 2 system performs independent behavioral analysis
- A controlled web application will automatically vary CORS configurations
- The controlled environment will be used to generate labeled experimental data
- The correct training relationship is:
  - Configuration → Observed Behavior → Label
- The known configuration helps establish ground truth
- The model should learn from observable behavior available during future use
- The current target labels are:
  - Confirmed Misconfiguration
  - Needs Further Review
  - Not Confirmed / Downgraded
- ML/AI is not yet final
- The correct next step is to determine whether ML is justified
- The project must remain defensive and authorized

---

# WHAT IS NOT FINAL YET

Do not assume the following are locked:

- exact final thesis title
- exact research-gap wording
- exact novelty claim
- whether the final system is rule-based, ML-based, or hybrid
- exact ML algorithm
- exact labels and their final names
- exact scenario matrix
- exact dataset columns
- exact number of scenarios
- exact controlled web framework
- exact behavioral probes
- exact ground-truth labeling process
- exact evaluation protocol
- exact train/validation/test strategy
- exact secondary test applications
- whether `null` origin remains in scope
- whether public vs authenticated endpoint context is always available
- exact proposal wording

---

# MOST IMPORTANT NEXT STEP

The immediate next step is:

## **Finalize the experimental data-generation and behavioral-analysis design before deciding on ML.**

The next AI should help the user define:

1. the controlled CORS scenario generator;
2. the scenario dimensions;
3. the exact behavioral probes;
4. the observable features;
5. the labeling logic;
6. the ground-truth construction method;
7. the train/test split strategy;
8. the rule-based baseline;
9. the criteria for deciding whether ML is justified.

The output of that step should answer:

> **Does the problem genuinely require ML, or is a rule-based or hybrid method stronger?**

Do not jump to model selection before this step.

---

# RECOMMENDED NEXT ANALYSIS SEQUENCE

## Step 1 — Build the scenario space

Identify which CORS dimensions can vary.

Possible dimensions:

- allowed-origin behavior
- credential behavior
- `null` origin behavior
- preflight handling
- method handling
- header handling
- route sensitivity
- public vs authenticated context

## Step 2 — Define behavioral probes

Specify exactly what requests the analyzer sends.

## Step 3 — Define feature schema

Decide which observations become dataset columns.

## Step 4 — Define labels

Create defensible criteria for:

- Confirmed
- Needs Further Review
- Downgraded

## Step 5 — Define ground truth

Avoid circular labeling.

## Step 6 — Build rule-based baseline

Create a transparent baseline for comparison.

## Step 7 — Decide whether ML is justified

Only after inspecting the data complexity.

## Step 8 — If justified, select candidate models

Prefer interpretable tabular models first.

---

# DEFENSIVE CYBERSECURITY FRAME

Always frame the work as:

- defensive cybersecurity
- authorized testing
- controlled lab evaluation
- vulnerability validation
- behavior-based verification
- secure configuration analysis
- intentionally vulnerable test applications

Avoid operational instructions for attacking unauthorized systems.

---

# SIMPLE TAGLISH EXPLANATION FOR GROUPMATES

Use this:

> Focus na tayo sa CORS findings.
>
> Sa training phase, hindi kasama si OWASP ZAP. Gagawa tayo ng controlled web application na kayang magpalit-palit ng CORS configuration automatically. Sa bawat scenario, ite-test ng sarili nating behavioral analyzer kung paano talaga nagre-respond ang website sa iba't ibang cross-origin requests.
>
> Ang flow ay:
>
> known CORS configuration → observed behavior → label
>
> Ire-record natin ang behavioral results at gagawa ng labeled dataset.
>
> Ang labels natin ngayon ay:
> - Confirmed Misconfiguration
> - Needs Further Review
> - Not Confirmed / Downgraded
>
> Sa actual use naman, si OWASP ZAP ang Layer 1. Siya ang makakakita ng possible CORS issue at magbibigay ng affected endpoint. Pagkatapos, ang system natin bilang Layer 2 ang gagawa ng independent behavioral analysis, ie-extract ang same features na ginamit sa training, at iko-classify ang finding.
>
> Hindi pa final kung rule-based lang o gagamit ng ML. Kailangan muna nating tingnan kung enough ang complexity ng behavioral data para justified ang ML.

Short version:

> **ZAP is only Layer 1 and is not part of model training. The controlled website generates CORS scenarios, our analyzer observes their behavior, and those observations are labeled to create the dataset. During actual use, ZAP points to a possible CORS issue, then our Layer 2 system behaviorally analyzes and classifies it.**

---

# ONE-LINE CURRENT STATUS

> The thesis has narrowed to a CORS-only Layer 2 behavioral analysis system. A controlled web application will automatically vary CORS configurations, the group's own analyzer will convert those configurations into observable behavioral data, and the resulting dataset will be labeled as Confirmed, Needs Review, or Downgraded. OWASP ZAP is separate from training and acts only as Layer 1 during actual use by identifying candidate CORS findings for the independent Layer 2 system to analyze.

---

# CONTINUITY RULE FOR THE NEXT AI

Treat this file as the latest canonical context.

Do not ask the user to re-explain the deleted conversation.

Do not return to:

- broad cybersecurity topic hunting
- malware analysis
- intrusion detection
- SAST
- source-code scanning
- Cookie Security
- Security Headers
- full OWASP Top 10 coverage

unless the user explicitly changes direction.

Continue from:

> **Finalize the CORS scenario-generation, behavioral-probe, feature, labeling, and evaluation design, then determine whether ML is genuinely justified.**
