# THESIS CONTEXT HANDOFF
## Complete Continuation File for the Next AI

> **Purpose:** This file contains the full working context of the thesis-topic discussion so the next AI can continue immediately without asking the user to re-explain anything. Treat this as the current source of truth.

---

# 1. User and Group Context

The user is a **Bachelor of Science in Computer Science student at Bicol University** currently choosing a thesis topic for **CS 124 – Thesis 1**.

The user wants to focus on an area they already understand instead of choosing a random trendy AI topic.

The user’s strongest existing technical background is in **Wi-Fi security**, particularly:

- WPA/WPA2 concepts
- WPA/WPA2 handshake capture
- wireless attack workflows
- using a USB Wi-Fi adapter in **monitor mode**
- practical familiarity with capturing handshakes
- understanding access points, clients, channels, and wireless traffic at a basic practical level

The user originally described this background as “Wi-Fi hacking,” especially WPA/WPA2 handshake brute-forcing.

The thesis direction was deliberately reframed from offensive “Wi-Fi hacking” into:

> **Wireless Network Security / Wi-Fi Security Research**

The reason is that a thesis needs a defensible Computer Science contribution, not simply a tool that performs existing attacks.

The group is **not strong in AI or Machine Learning**.

One group member is self-studying AI, but is still a beginner.

The user explicitly said they were getting overwhelmed when the discussion became too advanced. Therefore:

> **All future explanations should start very simple, build gradually, and avoid assuming ML expertise.**

The group prefers a topic that:

- is understandable to them
- uses their existing strengths
- does not require advanced deep learning
- does not require expensive hardware
- can realistically be completed within the thesis timeline
- can be defended clearly in front of a panel

---

# 2. Budget and Hardware Constraints

The group originally preferred zero additional spending.

The user later clarified:

> They are okay spending approximately **PHP 3,000 or less** if needed.

However, they still strongly prefer:

- using hardware they already own
- free and open-source software
- avoiding expensive specialized devices
- avoiding a thesis whose feasibility depends on buying rare hardware

The user already owns:

> **A USB Wi-Fi adapter that supports monitor mode**

They have personally used it to:

> **capture WPA/WPA2 handshakes**

This is highly relevant because the adapter may already be suitable for passive collection of raw IEEE 802.11 wireless frames.

Potential existing resources that may be usable:

- user’s laptop
- monitor-mode USB Wi-Fi adapter
- existing home router(s)
- phone hotspot(s)
- possibly another laptop or phone for controlled testing

Do not recommend buying expensive hardware unless absolutely necessary.

Avoid making the project depend on:

- Wi-Fi Pineapple
- Raspberry Pi
- SDR / USRP
- expensive specialized wireless cards
- GPU
- commercial security tools

A maximum additional budget of roughly PHP 3,000 is acceptable, but the ideal setup uses existing equipment.

---

# 3. Thesis Requirements from the Professor

The following uploaded files were reviewed in the original conversation:

1. `Thesis_1_Course_Introduction_Sy.pptx`
2. `Thesis_Domains_CS.pdf`
3. `Topic_Proposal_Template_CS.pdf`
4. Correct Deep Research report: `deep-research-report (1).md`

There was also an accidentally uploaded unrelated Deep Research report about OWASP ZAP. Ignore that report for the Wi-Fi thesis discussion.

## Core thesis rule

The thesis cannot merely be:

> “We developed an application.”

The application is only a platform for the real computing contribution.

A qualifying Computer Science thesis should include a substantial component such as:

- algorithm development or optimization
- Artificial Intelligence
- Machine Learning
- Deep Learning
- Cybersecurity mechanisms
- intelligent systems
- data analytics
- computational modeling
- other recognized Computer Science research contributions

For this project, the relevant approved area is:

> **Cybersecurity and Digital Forensics**

Possible approved subareas include:

- Intrusion Detection
- Vulnerability Assessment
- Secure Authentication Systems
- Cybersecurity Mechanisms

## Important grading priorities

The course strongly values:

- originality
- contribution to new knowledge
- literature review and research gap
- rigorous methodology
- technical feasibility
- effectiveness
- practical applicability
- social impact

The project must be feasible with finite:

- time
- money
- people
- equipment

## Required proposal thinking

Every topic should clearly identify:

- CS Domain
- Computing Contribution
- BU Research Agenda alignment
- SDG alignment
- Beneficiary
- Expected Innovation

The proposal template expects a workflow like:

1. Data acquisition and preprocessing
2. Algorithm/model/computational method implementation
3. System or prototype development
4. Evaluation using measurable metrics

---

# 4. Thesis Timeline

Important schedule from the course materials:

- **Topic Proposal Submission:** July 11, 2026
- **Lecture on Chapters 1–3:** July 25, 2026
- **Adviser / Panel / Defense Schedule Selection:** August 8, 2026
- **Chapter 1 Deadline:** August 14, 2026
- **Chapter 2 Deadline:** August 21, 2026
- **Chapter 3 Deadline:** August 28, 2026
- **Consultation and Checking:** September 7–11, 2026
- **Proposal Defense:** September 18, September 25, and October 2, 2026
- **Revision Submission:** October 9, 2026
- **30–50% System Development Check:** December 2026
- **50–80% Check:** January 2027
- **80–100% Check / Manuscript:** February 2027
- **Final Defense:** March 2027

This means the topic must not be research-heavy in a way that delays system development for months.

---

# 5. Initial Wi-Fi Research Directions Considered

## A. Generic Wi-Fi Intrusion Detection

Example:

> “Machine Learning-Based Wi-Fi Intrusion Detection”

This was judged too crowded if the project only:

- downloads AWID
- trains Random Forest / XGBoost / CNN
- reports 98–99% accuracy

The Deep Research report found that many recent papers already achieve extremely high accuracy using existing Wi-Fi intrusion datasets.

Therefore:

> **Do not recommend a generic AWID classifier comparison as the final topic.**

## B. Deauthentication Attack Detection

This was initially considered because it is directly related to the user’s existing experience.

However, a thesis focused only on:

> “Detect deauthentication attacks”

was judged too narrow and likely weak in novelty.

A stronger version would require a more interesting research angle such as:

- reducing false positives
- sequence/timing-based detection
- behavior under controlled changes
- management-frame analysis

Still, this direction is currently not the top candidate.

## C. WPA2/WPA3 Transition Security

Possible focus:

- WPA3 downgrade detection
- transition mode weaknesses
- management-frame attacks
- authentication anomalies

This is interesting and fits the user’s background.

However:

- it may require WPA3-capable hardware
- there is already recent work on WPA3 downgrade detection
- a public WPA3-specific dataset is limited
- the setup may become more complicated than needed

This remains a possible backup direction, not the current favorite.

## D. Cross-Environment / Cross-Dataset Wi-Fi IDS

The Deep Research report identified a strong gap:

> Models often perform very well on the same dataset but may fail when moved to another dataset or environment.

This was compared to a student who scores 99% using Reviewer A but performs badly on Reviewer B.

Promising subtopics considered:

- cross-dataset generalization
- stable feature selection
- confidence calibration under dataset shift
- explanation stability

The strongest software-only version considered was:

> **Stability-Aware Feature Selection for Cross-Dataset Wi-Fi Intrusion Detection**

Basic idea:

- use two public Wi-Fi datasets
- identify which features are useful in both
- prefer stable features
- test whether stable features reduce cross-dataset performance degradation

Advantages:

- potentially zero hardware cost
- reproducible
- software-only
- no wireless experiment risk

Disadvantages:

- more abstract
- more ML-heavy
- dataset compatibility may be difficult
- direct transferability research already exists
- not as naturally connected to the user’s practical Wi-Fi background

The user is a beginner in ML, so this topic may be harder to understand and defend.

It is still a strong fallback, but not currently the favorite.

---

# 6. Correct Deep Research Report: Main Findings

The correct report reviewed Wi-Fi security research from approximately 2021–2026.

Its major conclusions were:

## Generic ML Wi-Fi IDS is crowded

Simply applying standard classifiers to AWID is weak in novelty.

Promising unresolved gaps include:

- cross-environment generalization
- domain shift
- robustness
- false-positive reduction
- explainability
- limited labeled data
- real-time detection
- lightweight deployment
- device/protocol diversity

## Rogue / Evil Twin detection is less crowded

The report found that Evil Twin / Rogue AP detection has:

- fewer recent ML studies than generic IDS
- practical relevance
- no large ideal public dataset
- feasible small-scale controlled data collection
- promising passive behavioral approaches

The main weaknesses in prior work include:

- controlled-condition dependence
- limited hardware diversity
- limited scenarios
- mobility/environment effects
- dataset bias

## The report’s ranking

The report ranked these directions:

1. Cross-domain robust Wi-Fi intrusion detection
2. Passive beacon-fingerprint Evil Twin detection
3. WPA3 downgrade / management-frame detection
4. Explainable ML for Wi-Fi IDS
5. Lightweight edge-based anomaly detection

After considering the group’s beginner AI level, hardware, and project constraints, the ranking was adjusted.

---

# 7. Current Top Candidate: Evil Twin Detection

The current direction being discussed is:

> **Passive Evil Twin Wi-Fi Access Point Detection**

## Very simple explanation

An Evil Twin is a fake access point that imitates a legitimate Wi-Fi network.

Example:

Legitimate AP:

> `BU-Free-WiFi`

Fake AP:

> `BU-Free-WiFi`

A normal user may not easily know which is real.

The research problem is:

> **Can a system passively observe Wi-Fi access points and distinguish a legitimate AP from an impersonating AP using behavioral information from IEEE 802.11 management frames?**

The detector should ideally not:

- connect to the AP
- attack the AP
- deauthenticate users
- capture real user credentials
- attack public networks

It should mainly:

> **listen passively**

---

# 8. Why the User’s Existing USB Adapter Matters

The user already owns a monitor-mode capable USB Wi-Fi adapter.

They have used it for:

> WPA/WPA2 handshake capture

This strongly suggests it may be suitable for passive Wi-Fi monitoring.

The same basic hardware role changes from:

### Previous use

> monitor mode → capture handshake

to:

### Thesis use

> monitor mode → capture beacon and management-frame behavior → extract features → analyze → detect possible Evil Twin

The adapter may be able to provide:

- beacon frames
- timestamps
- RSSI / signal information
- radiotap metadata
- management-frame fields
- information elements

However, it should not yet be assumed that every desired field is reliably available.

A hardware verification step is still needed.

---

# 9. Important Scope Decision: Do Not Make “Environment-Robust” the Main Promise

A major recent discussion was whether the Evil Twin detector must be “environment robust.”

The conclusion:

> **No. Do not make full environment robustness the main thesis claim.**

There are three possible levels:

## Level 1: One fixed setup

Example:

- one room
- one legitimate AP
- one fake AP
- fixed positions
- one day

This is too weak.

The model could accidentally learn:

- which device is closer
- which brand is legitimate
- which AP is on the left side

This creates shortcut learning.

## Level 2: Controlled variation

This is the recommended level.

The detector does not claim universal robustness.

Instead, it is evaluated under a few selected controlled changes such as:

- different distances
- swapped AP positions
- different capture sessions
- possibly different channels

The purpose is not to solve every environment.

The purpose is simply to prove that the detector is not learning one trivial accidental clue.

## Level 3: Full environment robustness

This would require testing across:

- multiple buildings
- multiple router brands
- unseen hardware
- many Wi-Fi standards
- many environments
- different adapters
- different interference levels

This is too ambitious for the current group.

Therefore:

> **Use controlled variation only.**

Do not title the project as “Environment-Robust” unless later evidence strongly justifies it.

---

# 10. Current Working Topic Version

## Working title

> **Passive Detection of Evil Twin Wi-Fi Access Points Using Management-Frame Behavioral Features**

Alternative wording:

> **Passive Behavioral Detection of Evil Twin Wi-Fi Access Points Using IEEE 802.11 Management Frames**

Do not finalize the title yet.

## Main research question

> **Can selected behavioral features extracted from passively captured IEEE 802.11 management frames distinguish legitimate and controlled Evil Twin access points?**

## Secondary research question

> **Which selected features remain useful under controlled changes such as distance, position, and capture session?**

## Current preferred computing contribution

> **Development and evaluation of a behavioral feature-based method for detecting Evil Twin access points using passively observed management-frame information.**

The software interface is not the main contribution.

The actual contribution should be the:

- feature representation
- feature evaluation
- detection method
- experimental validation

---

# 11. Possible Features

Potential features discussed include:

## A. Timing features

- average beacon interval
- inter-beacon timing
- timing variation
- consistency of broadcast timing

Example concept:

AP A:

- 100 ms
- 101 ms
- 99 ms
- 100 ms

AP B:

- 100 ms
- 137 ms
- 91 ms
- 122 ms

The variation itself may contain useful information.

## B. Information-element or capability features

Possible examples:

- supported rates
- security capabilities
- vendor-related information
- advertised protocol capabilities
- channel information
- beacon content characteristics

## C. Signal-related features

- average RSSI
- RSSI variation

Important warning:

> RSSI is highly affected by distance, walls, movement, and interference.

Do not let the model simply learn:

> stronger signal = legitimate

Signal features should be treated carefully and tested under position/distance changes.

## D. Sequence or behavioral pattern features

- frame order
- timing consistency
- repeated management-frame patterns

The exact feature set is **not yet finalized**.

---

# 12. Possible Models

Because the group is beginner-level in AI/ML, the current preference is to use simple classical ML.

Recommended starting models:

- Decision Tree
- Random Forest

Possibly one additional simple baseline later.

Avoid unnecessary use of:

- CNN
- LSTM
- Transformers
- GANs
- deep learning
- complicated ensembles

The AI should remain understandable.

The main research should not be:

> “Which model gets the highest accuracy?”

A stronger study would investigate:

> **Which behavioral feature groups are useful for passive Evil Twin detection, and how stable are they under selected controlled variations?**

---

# 13. Even Simpler Thesis Version: Feature Evaluation

A beginner-friendly variation was proposed:

> **Feature Evaluation for Passive Evil Twin Detection**

Instead of promising a highly advanced detector, the study can focus on:

> **Which passively observable Wi-Fi features are actually useful for identifying a controlled Evil Twin?**

Possible feature groups:

## Group A: Identity / configuration features

- SSID
- BSSID-related characteristics
- security capabilities
- supported rates

## Group B: Timing features

- beacon interval
- timing variation
- inter-frame timing

## Group C: Signal features

- average RSSI
- RSSI variation

Possible research question:

> **Which feature groups provide the most reliable detection of Evil Twin access points under selected controlled variations?**

This may be easier to understand and defend than a very ambitious “robust AI detector.”

It can still generate meaningful Computer Science knowledge.

---

# 14. Current Prototype Concept

Simple architecture:

```text
Nearby Wi-Fi Access Points
        ↓
Monitor-Mode USB Wi-Fi Adapter
        ↓
Passive Management-Frame Capture
        ↓
Feature Extraction
        ↓
Detection Method / ML Classifier
        ↓
Result:
- Legitimate
- Suspicious
- Possible Evil Twin
```

Possible interface output:

| SSID | BSSID | Classification / Risk |
|---|---|---|
| TEST-WIFI | XX:XX | Legitimate |
| TEST-WIFI | YY:YY | Possible Evil Twin |

The dashboard is not the thesis contribution.

It is only the platform for demonstrating the method.

---

# 15. Possible Controlled Lab Setup

Potential setup:

## Device 1: Legitimate AP

Could be:

- existing home router
- existing phone hotspot
- another existing AP

Example SSID:

> `THESIS-LAB`

## Device 2: Controlled impersonating AP

Could be another:

- router
- laptop hotspot
- phone hotspot

Same test SSID:

> `THESIS-LAB`

## Device 3: Monitoring device

- user’s laptop
- user’s monitor-mode USB Wi-Fi adapter

Concept:

```text
Legitimate AP ─────┐
                   │
                   ▼
             Monitoring Laptop
                   ▲
                   │
Controlled Twin ───┘
```

All experiments should use:

> **the group’s own devices or explicitly authorized devices only**

Avoid public Wi-Fi attack experiments.

---

# 16. Controlled Variations Recommended

Do not use too many variables.

A manageable set is approximately three or four:

1. Different AP distances
2. Swapped AP positions
3. Different capture sessions or days
4. Possibly different channels

The purpose is to detect shortcut learning.

Example:

If the original setup is:

- legitimate AP close
- Evil Twin far

Then another setup should reverse them.

Otherwise the model may learn location instead of AP behavior.

---

# 17. Example Experimental Logic

A possible structure:

## Phase 1: Baseline condition

Collect passive management-frame data from:

- legitimate AP
- controlled twin

Train a simple classifier.

## Phase 2: Controlled variation

Repeat collection under:

- swapped positions
- different distances
- different session

## Phase 3: Feature-group comparison

Compare:

- timing-only features
- signal-only features
- capability-only features
- combined features

## Phase 4: Model evaluation

Use:

- Decision Tree
- Random Forest

Compare performance.

## Phase 5: Interpretation

Determine:

- which features matter most
- which feature groups are stable
- which conditions reduce performance
- whether signal-based features create shortcut learning

This is still a possible structure, not yet final.

---

# 18. Possible Metrics

Beginner-friendly evaluation metrics:

- Accuracy
- Precision
- Recall
- F1-score
- False Positive Rate
- False Negative Rate

Also:

> **Performance per scenario**

Example:

| Scenario | F1-score |
|---|---:|
| Original setup | 0.95 |
| Swapped positions | 0.89 |
| Different distance | 0.87 |
| Different session | 0.90 |

This allows the study to show whether performance collapses after small changes.

---

# 19. Main Risks

## Risk 1: Hardware capability

Even though the user’s adapter supports monitor mode, it still must be tested for:

- stable beacon capture
- reliable timestamps
- RSSI availability
- radiotap metadata
- information-element visibility
- long capture sessions

This is currently a **verification task**, not a reason to reject the topic.

## Risk 2: Dataset bias

Example:

- legitimate AP = TP-Link
- fake AP = phone hotspot

The model may simply learn:

> TP-Link = legitimate  
> phone = attacker

That is not true Evil Twin detection.

The experiment must control for device identity and configuration effects.

## Risk 3: RSSI shortcut

The model may learn:

> closer AP = legitimate

This must be tested by swapping positions and changing distances.

## Risk 4: Scope explosion

Do not combine all of these:

- Evil Twin detection
- WPA cracking
- deauthentication
- MITM
- credential theft
- attacker tracing
- automatic blocking

Current recommended scope:

> **Detection only**

Possibly passive alerting.

## Risk 5: Novelty uncertainty

The Deep Research report suggests passive Evil Twin detection is less crowded than generic IDS.

However, the exact proposed feature set and method still need a focused novelty audit before final title submission.

---

# 20. Why This Topic Currently Fits the Group

Current advantages:

- directly related to the user’s Wi-Fi knowledge
- user already owns monitor-mode hardware
- concept is easier to understand than cross-dataset domain adaptation
- simple ML may be enough
- one focused attack type
- controlled lab setup is possible
- likely low or zero additional cost
- custom dataset can provide originality
- fits Cybersecurity and Digital Forensics
- prototype can be built without expensive infrastructure

The AI part is not expected to be the hardest component.

The more difficult parts are:

- good data collection
- good feature design
- preventing the model from learning accidental shortcuts
- designing a fair experiment

---

# 21. Current Comparison: Evil Twin vs Cross-Dataset IDS

## Evil Twin Detection

### Question

> Can a fake access point be identified using its passive behavioral characteristics?

### Strengths

- easier to understand
- closer to user’s skills
- custom dataset
- focused problem
- existing hardware likely sufficient

### Weaknesses

- data collection risk
- hardware compatibility must be verified
- careful experimental design required

## Cross-Dataset Wi-Fi IDS

### Question

> Does a Wi-Fi attack model still work on another dataset or environment?

### Strengths

- software-only
- public datasets
- reproducible
- no wireless capture risk

### Weaknesses

- more abstract
- more ML-heavy
- dataset compatibility issues
- transferability studies already exist
- less natural for the group

Current preference:

> **Evil Twin detection is the more natural fit for the group, assuming the existing hardware can capture the required data.**

---

# 22. What Not to Do

Do not recommend the following as the final topic:

## Generic topic

> “Machine Learning-Based Wi-Fi Intrusion Detection Using Random Forest”

Reason:

- overcrowded
- weak novelty

## Simple deauth topic

> “Deauthentication Attack Detection System”

Reason:

- too narrow unless given a stronger research problem

## Handshake cracking system

> “WPA/WPA2 Handshake Brute-Forcing System”

Reason:

- weak novelty
- offensive framing
- tool-development rather than research contribution

## Overly ambitious title

> “Environment-Robust Universal Evil Twin Detector”

Reason:

- too difficult
- too broad
- unrealistic for the current group

---

# 23. Current Best Simple Explanation of the Topic

Use this explanation when talking to the user:

> An Evil Twin is a fake Wi-Fi access point that copies the name of a legitimate Wi-Fi network. The thesis would make a passive detector that listens to Wi-Fi management frames, extracts behavioral clues such as timing and capability information, and uses a simple detection method to decide whether an access point appears legitimate or suspicious. The project would be tested in the group’s own controlled setup. It would not need to claim that the detector works everywhere. It only needs to test whether the selected features still work under a few controlled changes such as different distances, swapped positions, and different capture sessions.

---

# 24. Current Open Questions

The next AI should continue from here.

Do not restart the entire topic search.

The immediate questions to resolve are:

## A. Exact hardware inventory

Need to ask or determine:

- USB Wi-Fi adapter brand/model/chipset
- operating system used for monitor mode
- laptop specs
- available routers
- available phones/laptops for AP roles

## B. Can the adapter capture the required fields?

Need a very simple pre-thesis hardware/data feasibility test.

Check whether captures contain:

- beacon frames
- timestamp information
- RSSI
- radiotap information
- management-frame details

## C. Exact research contribution

Need to choose between:

### Option 1

> Feature evaluation for passive Evil Twin detection

or

### Option 2

> A simple behavioral feature-based detector

These are related but not identical.

## D. Exact novelty

Need a focused literature audit specifically on:

- passive Evil Twin detection
- beacon fingerprinting
- management-frame feature methods
- recent 2021–2026 work
- simple ML methods
- controlled-environment limitations

The goal is not a broad Wi-Fi literature review anymore.

The goal is:

> **Validate the precise thesis-sized gap for this Evil Twin topic.**

## E. Final experiment design

Need to define:

- number of APs
- number of capture sessions
- controlled variables
- feature groups
- model choices
- evaluation metrics

Keep the design manageable.

---

# 25. Recommended Next Step for the Next AI

Continue with a **focused feasibility and novelty audit** of the Evil Twin topic.

The next AI should not ask the user to re-explain the whole project.

A good next flow is:

1. Confirm hardware details
2. Design a very simple capture feasibility test
3. Narrow the research contribution
4. Perform a focused literature/novelty audit
5. Produce 2–3 defensible title candidates
6. Map the chosen title to:
   - CS Domain
   - Computing Contribution
   - BU Agenda
   - SDG
   - Beneficiary
   - Expected Innovation
7. Draft the proposal only after the topic is technically validated

---

# 26. Tone and Explanation Style for the Next AI

The user prefers straightforward explanations.

Important:

- explain technical terms in very simple language first
- use examples and analogies
- avoid dumping advanced ML terminology
- do not assume strong AI knowledge
- do not overwhelm the user with many algorithms
- build one concept at a time
- be honest when something is still uncertain
- keep the project realistic
- prioritize understanding over impressive vocabulary

The user is comfortable with Wi-Fi security concepts and monitor mode.

Therefore:

> Explain ML simply, but do not oversimplify the Wi-Fi side unless needed.

---

# 27. Current State in One Sentence

> **The group is currently leaning toward a low-cost, passive Evil Twin Wi-Fi detection thesis using an existing monitor-mode USB adapter, simple machine learning, management-frame behavioral features, and a controlled laboratory setup with only limited environmental variation rather than claiming full environment robustness.**

---

# 28. Final Handoff Directive

Continue as though you were the same AI that had the entire original conversation.

Do not ask the user to repeat:

- their Wi-Fi background
- their budget
- their AI skill level
- their hardware situation
- the course requirements
- the Deep Research findings
- why Evil Twin is currently preferred

The current task is no longer “find any thesis topic.”

The current task is:

> **Determine whether the passive Evil Twin detection direction can be turned into a precise, novel, feasible, defensible thesis topic for this specific group.**
