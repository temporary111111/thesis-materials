# THESIS RESEARCH HANDOFF v2
## Host-Based Default-Gateway ARP Poisoning — Computer Science Thesis

### 0. CRITICAL INSTRUCTION TO THE NEXT AI

You are continuing an extensive thesis research and novelty-audit process with a Bachelor of Science in Computer Science student.

**Do not restart from generic ARP-spoofing thesis ideas.**

Many obvious directions have already been examined, researched, and intentionally discarded because they were:
- already done;
- too obvious;
- too implementation-oriented;
- insufficient as a Computer Science contribution;
- or vulnerable to the professor saying **“meron na niyan.”**

The student's priorities are:

- host-based only;
- focus only on the victim's **IPv4 default-gateway IP-to-MAC ARP binding**;
- simple;
- inexpensive;
- preferably fully virtualized;
- no expensive network equipment;
- no unnecessary AI/ML;
- no SDN unless absolutely necessary;
- small/incremental contribution is acceptable;
- novelty must be conservatively claimed;
- literature must be aggressively searched before committing;
- weak ideas should be killed early instead of defended emotionally.

The student has a trust concern about novelty and expects the AI to actively search for prior art rather than reassure them without evidence.

The current leading direction is **NOT a new ARP detector**.

The current leading thesis concept is:

> **Model-Based Test Generation for Black-Box Evaluation of Host-Based Default-Gateway ARP Poisoning Detectors**

or a closely related working title.

Current status:

> **Promising candidate, not yet final thesis title.**

The immediate next step after restoring context should be **adviser/panel attack simulation of the Topic Concept v1**, unless new evidence invalidates the concept.

---

# 1. EXACT SECURITY SCOPE — THIS IS FIXED

The research focuses only on the **victim host's local IPv4 ARP table entry for the default gateway**.

Normal victim state:

```text
Default Gateway IP → Legitimate Gateway MAC

192.168.1.1 → AA:AA:AA:AA:AA:AA
```

ARP poisoning of interest:

```text
192.168.1.1 → ATTACKER_MAC
```

The attacker causes the victim to associate the legitimate default-gateway IP address with the attacker's MAC address.

The protected object is therefore:

> **Integrity of the victim's IPv4 default-gateway IP-to-MAC binding.**

Do not widen the thesis to generic ARP security unless required.

---

# 2. WHAT IS NOT THE SCOPE

Do not accidentally change the thesis into any of the following:

- poisoning the gateway/router's own ARP table;
- protecting every ARP entry on the victim;
- protecting every device on the LAN;
- IPv6 Neighbor Discovery / NDP;
- DHCP spoofing;
- DNS spoofing;
- Wi-Fi deauthentication;
- generic MITM detection;
- full network IDS;
- SDN-wide ARP defense;
- Dynamic ARP Inspection implementation;
- router firmware security;
- Secure ARP deployment;
- whole-LAN PKI;
- machine-learning packet classification.

The threat is ARP poisoning, but **ARP poisoning itself is not automatically the thesis contribution**.

---

# 3. BASIC ARP TERMINOLOGY ALREADY CLARIFIED

The user previously became confused by the term **“neighbor table.”**

Use:

> **Victim's ARP table**

for simplicity.

On Linux, the broader OS structure may be called a neighbor table, but this does **not** mean computers share their ARP tables with each other.

Each host has its own local ARP/neighbor state.

Example:

```text
Victim:
192.168.1.1 → Gateway MAC

Gateway:
has its own separate ARP table

Attacker:
has its own separate ARP table
```

ARP messages cross the LAN.

The whole ARP table does not.

Avoid reintroducing this terminology confusion.

---

# 4. DEPLOYMENT AND COST CONSTRAINTS

The student wants the thesis to be **as cheap as possible**.

Preferred experiment:

```text
               Virtual LAN
                   |
        +----------+----------+
        |          |          |
     Victim     Attacker    Gateway
       VM          VM         VM
```

Possible platforms:

- VirtualBox;
- VMware;
- equivalent virtualization.

No additional physical equipment should be required.

Prefer an **Internal Network / isolated virtual LAN** rather than using the hypervisor's built-in NAT engine as the gateway under test.

Possible architecture:

```text
Victim VM
   |
Internal Virtual LAN
   |
Attacker VM
   |
Gateway VM
```

The Gateway VM may optionally have another NAT interface for Internet connectivity, but the security experiment itself does not require Internet access.

Do not imply that Linux must be installed on the physical laptop.

Linux was previously discussed because some networking APIs are convenient there, not because ARP poisoning requires Linux.

---

# 5. SECURE ARP QUESTION HAS ALREADY BEEN ADDRESSED

The user correctly challenged:

> “Secure ARP already exists. Why would this thesis still matter?”

Important distinction:

### Secure-ARP family

Examples such as S-ARP attempt to solve ARP authentication more fundamentally through mechanisms such as:

- cryptographic signing;
- PKI/certificates;
- trusted authorities;
- changed or extended ARP behavior;
- supporting infrastructure.

These are stronger approaches when deployed.

### Our intended environment

The thesis deliberately assumes:

> **ordinary legacy IPv4 LAN using standard unauthenticated ARP, where the victim controls only itself and cannot require changes to the default gateway, switch, other hosts, or network infrastructure.**

Therefore the thesis is not competing with Secure ARP by claiming to solve ARP authentication universally.

The deployment question is different:

```text
Secure ARP:
"Can we change/authenticate the ARP ecosystem?"

Our niche:
"What can we test/evaluate when only the endpoint can be controlled?"
```

Do not disparage Secure ARP.

Use it to clearly define the deployment boundary.

---

# 6. SCHOOL DOCUMENTS NOW AVAILABLE

Three official/academic course-related files were uploaded and reviewed:

1. **Thesis_Domains_CS.pdf**
2. **Topic_Proposal_Template_CS.pdf**
3. **Thesis_1_Course_Introduction_Sy.pptx**

These materially changed the confidence in the current direction.

---

# 7. WHAT THE SCHOOL DOCUMENTS SAY ABOUT ACCEPTABLE CS CONTRIBUTION

The approved CS domains document states that a CS thesis may contribute through the **development, evaluation, enhancement, or application of computational methods, models, algorithms, architectures, or innovative computing technologies**.

It explicitly recognizes substantial computing components including:

- **Cybersecurity Mechanisms**
- **Computational Modeling and Simulation**

It also states that a software application should serve only as the vehicle for implementing and evaluating the actual computing contribution.

This is crucial.

The thesis does **not** have to invent a brand-new machine-learning algorithm to qualify as Computer Science.

---

# 8. AUTOMATED TESTING IS EXPLICITLY AN APPROVED AREA

Under **Intelligent Software Engineering and Computing Systems**, the school document explicitly lists:

> **Automated Testing**

as an approved research area.

The Cybersecurity and Digital Forensics area separately includes:

- Intrusion Detection;
- Vulnerability Assessment;
- other cybersecurity topics.

Therefore the current concept can legitimately sit at the intersection of:

```text
Cybersecurity
+
Automated Testing
+
Computational Modeling
```

This greatly reduces the previous concern:

> “Baka sabihin na framework lang at hindi Computer Science.”

But this does **not** mean any framework automatically qualifies.

The computational contribution must remain explicit.

---

# 9. SOFTWARE MUST NOT BE THE MAIN CONTRIBUTION

The school Topic Proposal Template repeatedly emphasizes that the proposed work must explain:

- computing problem;
- computational approach;
- algorithms/models/frameworks;
- computing contribution;
- research gap.

It explicitly warns that the study must not merely describe a software application; the system is supposed to implement/evaluate the underlying computational contribution.

Therefore the thesis should NOT be presented as:

> “We will develop an ARP testing application.”

Instead:

> **We will develop a finite-state behavioral model, a model-based test-generation method, and a ground-truth behavioral oracle; the testing framework is the implementation vehicle.**

This distinction is extremely important in proposal defense.

---

# 10. OFFICIAL TITLE STYLE FROM THE SCHOOL

The Topic Proposal Template recommends a title structure resembling:

> **[Computing Technique/Approach] + [Problem Being Solved] + [Application Domain]**

and asks the student to identify:

- CS Domain;
- Computing Contribution;
- BU Agenda;
- SDG;
- Beneficiary;
- Expected Innovation.

This was one reason the current title evolved toward:

> **Model-Based Test Generation for Black-Box Evaluation of Host-Based Default-Gateway ARP Poisoning Detectors**

rather than simply:

> “An ARP Testing Framework.”

---

# 11. COURSE REQUIREMENT ON ORIGINALITY

The Thesis 1 course slides state that research should contribute to common knowledge and must generally have original aspects.

They also explicitly state that simply repeating prior work is generally insufficient **unless the purpose is to confirm or reject previous findings**.

This validates the student's initial concern about:

> “Hindi dapat ulitin lang yung study.”

But it also means an experimental extension/replication can still be academically legitimate when it tests a limitation or finding.

---

# 12. COURSE FLOW

The course slides describe the progression roughly as:

- Topic Selection;
- Topic Presentation for initial feedback;
- Problem Identification;
- Objective Setting;
- Proposal Development;
- manuscript/proposal defense.

Therefore the **Topic Concept v1** being developed in this chat is an informal intermediate reasoning artifact, not an official school-required one-page document.

Its purpose is to ensure the research concept is solid before filling the full proposal.

---

# 13. COURSE GRADING ALSO SUPPORTS THE CURRENT STRATEGY

The course grading gives meaningful weight to:

- contribution to new knowledge;
- creativity/originality;
- RRL depth;
- methodology;
- technical feasibility.

This supports the current philosophy:

> **small contribution + rigorous gap + rigorous methodology**

rather than a flashy but weak “new cybersecurity app.”

---

# 14. SAMPLE SCHOOL TOPICS ALSO MATTER

The course slides include a recent sample topic involving:

> **Automated Functional Test Case Creation**

as a Computer Science thesis example.

This does not prove that our specific thesis will automatically be approved, but it is evidence that automated-testing-oriented research is compatible with the program's idea of CS thesis work.

---

# 15. IDEAS ALREADY CONSIDERED AND REJECTED / DOWNRANKED

The next AI should NOT casually suggest these again.

## A. Simple gateway MAC monitor

Example:

```text
save gateway MAC
if gateway MAC changes:
    alert
```

**Status: RED**

Already well explored.

Not enough novelty.

---

## B. Polling versus event-driven ARP monitoring

Previous idea:

```text
poll ARP every 3 seconds
```

versus OS event notifications.

**Status: DROPPED**

Reason:
- mostly implementation detail;
- likely weak as main CS contribution;
- user explicitly did not like the direction;
- “short attack may happen between polling intervals” felt too predictable.

---

## C. Short-duration ARP poisoning

Question considered:

> “Can a short attack occur between polling observations?”

**Status: DROPPED**

User correctly felt that it risked being common sense.

Do not revive as main thesis question.

---

## D. Generic active verification

Ideas like:

- ARP probing;
- ICMP probing;
- conflicting-response verification.

**Status: RED**

Substantial old prior art exists.

---

## E. Voting among hosts

Question:

> “Ask other hosts which gateway MAC is real.”

**Status: RED**

MR-ARP and later voting methods already exist.

---

## F. Poisoned startup alone

Scenario:

```text
Victim already poisoned
↓
Detector starts
↓
Detector saves attacker MAC as trusted
```

**Status: REAL ISSUE, BUT NOT STANDALONE NOVELTY**

Useful as a future test case.

Not enough as thesis itself.

---

## G. “Baseline inversion”

Working phenomenon:

```text
attacker learned as baseline
↓
attack disappears
↓
real gateway returns
↓
real gateway appears anomalous
```

**Status: keep as possible test sequence, not thesis novelty.**

The term “baseline inversion” was working terminology only and should not be claimed as established literature terminology.

---

## H. Context-aware re-baselining

Question:

> “Can local network context decide whether a changed gateway MAC is legitimate?”

**Status: DOWNRANKED**

Prior work, gateway history, WiSC-like context, commercial/patent ideas, etc. come too close.

---

## I. Generic trust-establishment comparison

Strategies:

- manually configured MAC;
- learn at startup;
- active verification.

**Status: DOWNRANKED**

General comparative ARP-security studies already exist.

---

## J. Legitimate gateway MAC changes / false positives

Question:

> “Will detector falsely flag legitimate gateway replacement?”

**Status: useful test case, but not novelty by itself.**

Older ARP literature already recognizes legitimate IP-MAC changes and false positives.

Also:

Do NOT casually say:

> “VRRP/HSRP failover causes gateway MAC changes.”

That is technically unsafe because redundancy protocols often intentionally maintain a virtual MAC.

Better benign-change examples:

- actual gateway replacement;
- gateway NIC replacement;
- administrative reconfiguration;
- VM gateway replacement.

---

## K. New state-machine ARP detector

**Status: RED**

Stateful/DES ARP defenses already exist.

---

## L. Generic “ARP benchmark”

**Status: TOO BROAD**

ARP test suites, datasets, comparative studies, IDS testbeds, and automated security tools exist.

The current candidate must remain much narrower.

---

# 16. DANGEROUS / MANDATORY PRIOR ART CATEGORIES

Future literature review must include at least the following families.

### Secure ARP / S-ARP
Important because cryptographic ARP protection is old.

### Stateful ARP / fuzzy-state ARP
Important because state-based ARP defenses exist.

### Active host-based ARP IDS
Important because active verification and multiple-scenario testing are old.

### DES/state-model ARP detection
Important because formal state models inside detectors exist.

### Comparative ARP-security studies
Important because comparison alone is not novel.

### 2019 client-side gateway-MAC protection
Important because simple endpoint gateway monitoring is already done.

### WiSC — MobiCom 2021
Extremely important.

WiSC already:
- operates client-side;
- checks gateway `(IP, MAC)` consistency;
- considers initial compromise;
- uses historical/cross-connection context.

This kills any claim that:
- gateway-only monitoring is new;
- historical gateway trust is new;
- initial-compromise awareness is new.

### ASD / false-positive-aware ARP work
Shows false-positive analysis is not new.

### Voting-based ARP methods
Shows genuine-MAC selection using voting is old/ongoing.

### 2025 IEEE Access host/router ARP defense
Important because it uses initial trusted/snapshot router state and explicitly depends on clean initialization.

### 2026 client-side default-gateway detector
Extremely close to the user's original simple topic.

Reported characteristics include:
- host/client-side;
- trusted gateway MAC;
- VirtualBox evaluation;
- automatic mitigation;
- polling;
- multiple mismatch checks.

Therefore the original “lightweight host gateway detector” topic is definitely not novel.

### IWL ARP Test Suite
Important because automated ARP protocol testing already exists.

But it primarily tests:
> correctness/conformance/robustness of ARP implementations,

not necessarily security-detector behavior.

### SCADA IDS Test Framework
Important because detector-agnostic/virtualized IDS testing frameworks already exist.

### DELTA / automated security assessment
Important because automated security evaluation frameworks are not new.

### raw-packet / network security test tooling
Important because automated ARP-security checks are not new.

---

# 17. IMPORTANT LITERATURE CLAIMS THAT MUST NOT BE MADE

Never claim:

> “No ARP detector exists for default gateways.”

False.

Never claim:

> “No host-based ARP detector exists.”

False.

Never claim:

> “No state-based ARP defense exists.”

False.

Never claim:

> “No model-based testing exists.”

False.

Never claim:

> “No ARP test suite exists.”

False.

Never claim:

> “No automated ARP-security testing exists.”

False.

Never claim:

> “No one tests false positives.”

False.

Never claim:

> “No one studies recovery.”

False.

Never claim:

> “No one studies startup compromise.”

Unsafe/false.

Never claim:

> “This is the first ever.”

Current evidence does not justify this.

Safe wording remains:

> **“We did not identify prior work that exactly combines…”**

---

# 18. CURRENT LEADING RESEARCH DIRECTION

Current candidate:

## **Model-Based Test Generation for Black-Box Evaluation of Host-Based Default-Gateway ARP Poisoning Detectors**

Alternative wording still possible:

> **A Model-Based Black-Box Testing Framework for Host-Based Default-Gateway ARP Poisoning Detectors**

The first wording is currently preferred because it exposes the **computational technique** rather than making “framework” sound like the main contribution.

---

# 19. CORE THESIS IDEA IN SIMPLE LANGUAGE

Do not create another ARP detector.

Instead create an:

> **automated examiner for existing ARP detectors.**

Concept:

```text
Behavioral model
      ↓
Generate valid tests
      ↓
Virtual network
      ↓
Detector under test
      ↓
Observe behavior
      ↓
Ground-truth oracle
      ↓
PASS / FAIL
```

The testing method focuses only on detectors whose protected object is:

```text
Victim:
Default Gateway IP → MAC
```

---

# 20. CURRENT COMPUTING CONTRIBUTIONS

The proposed contribution is currently composed of three core computational elements.

## Contribution 1 — Behavioral State Model

Create a finite-state representation of relevant network states.

Possible minimal states:

```text
NORMAL
POISONED
RECOVERED
LEGITIMATE_GATEWAY_REPLACEMENT
```

Potential detector lifecycle state:

```text
DETECTOR_RUNNING
DETECTOR_STOPPED
```

Do not overcomplicate the state model.

---

## Contribution 2 — Model-Based Test Generation

Instead of manually writing test cases, derive valid event sequences from the state model.

Possible events:

```text
START
STOP
RESTART
POISON
RESTORE
REPLACE
```

Possible generated sequences:

```text
START → POISON → RESTORE
```

```text
POISON → START → RESTORE
```

```text
START → REPLACE → POISON → RESTORE
```

Possible implementation:

- BFS;
- DFS;
- graph traversal up to bounded depth `k`.

Important:

> BFS/DFS itself is NOT the novelty.

The possible contribution is:

> **the domain-specific model and systematic derivation of valid gateway-binding detector tests.**

---

## Contribution 3 — Ground-Truth Behavioral Oracle

Because the framework controls the Gateway and Attacker VMs, it knows the true legitimate gateway state.

Possible variables:

```text
G = actual legitimate gateway MAC
O = victim's currently observed gateway mapping
V = externally observable detector verdict/action
```

Optional only if exposed:

```text
T = detector's internal trusted MAC
```

The framework should remain **black-box** wherever possible.

Example:

```text
Ground truth:
G = AA

Victim sees:
O = attacker XX

Detector:
NO ALERT
```

Oracle:

```text
FAIL
```

Or:

```text
Ground truth normal
Detector blocks legitimate gateway
```

Oracle:

```text
FAIL
```

---

# 21. WHY BLACK-BOX MATTERS

Different detectors expose different outputs.

Detector A:

```text
ALERT / NO ALERT
```

Detector B:

```text
ATTACKER_MAC
```

Detector C:

```text
restores ARP entry
```

Detector D:

```text
blocks MAC
```

Therefore the framework should not require source-code or internal trusted-state access.

Potential observable properties:

- alarm raised;
- no alarm;
- legitimate gateway reachable;
- legitimate gateway blocked;
- attacker mapping persists;
- mitigation active;
- mitigation recovered.

A detector adapter may normalize outputs.

---

# 22. POSSIBLE DETECTOR ADAPTER ARCHITECTURE

Concept:

```text
Model
   ↓
Test sequence
   ↓
Experiment Controller
   ↓
Virtual Network
   ↓
Detector Under Test
   ↓
Detector Adapter
   ↓
Normalized behavior
   ↓
Oracle
   ↓
PASS / FAIL
```

Possible normalized capabilities:

```text
DETECTION_CAPABLE
MITIGATION_CAPABLE
BLOCKING_CAPABLE
```

Do not force all detectors to expose the same internal state.

The behavioral expectations may depend on the advertised capability.

---

# 23. CURRENT EXACT NOVELTY BOUNDARY

Most individual ingredients already exist:

```text
ARP attacks              → existing
host-based detection     → existing
default-gateway monitor  → existing
state machines           → existing
model-based testing      → existing
black-box IDS testing    → existing
automated testing        → existing
ARP protocol test suites → existing
```

The candidate gap is the **specific combination**:

> **an external, detector-agnostic behavioral model + automatically generated valid gateway-binding state-transition tests + ground-truth behavioral oracle for black-box evaluation of host-based detectors protecting only the victim's IPv4 default-gateway ARP binding.**

Current safe gap wording:

> **Although host-based ARP-spoofing detectors, state-based ARP defenses, protocol test suites, comparative security evaluations, and broader IDS testing frameworks already exist, our current literature audit has not identified a detector-agnostic model-based approach that systematically generates valid behavioral state-transition tests and evaluates host-based default-gateway ARP poisoning detectors against known gateway ground truth.**

Do not change:

> “has not identified”

into:

> “does not exist.”

---

# 24. CURRENT TOPIC CONCEPT v1

## Candidate title

> **Model-Based Test Generation for Black-Box Evaluation of Host-Based Default-Gateway ARP Poisoning Detectors**

---

## Problem

Existing host-based ARP poisoning detectors already exist.

However, different detectors are commonly evaluated under different scenarios, assumptions, and experimental conditions.

A detector may be shown to work under:

```text
clean
↓
start detector
↓
attack
↓
detected?
```

but this does not systematically characterize its behavior across other valid gateway/detector-state sequences.

The proposed research does not claim that these individual scenarios are new.

It proposes a **systematic model-derived method for generating and evaluating them**.

---

# 25. THESIS IN ONE SIMPLE SENTENCE

If asked:

> **“Ano ang thesis ninyo?”**

The user should eventually be able to answer:

> **“Gagawa kami ng model-based automated method para systematically i-test ang host-based detectors na nagpoprotekta sa victim's default-gateway ARP mapping.”**

If asked:

> **“Ano ang CS contribution?”**

Answer:

> **“A finite-state behavioral model, model-derived test generation, and a ground-truth behavioral oracle.”**

This should remain the conceptual anchor.

---

# 26. CURRENT PROPOSED RESEARCH QUESTIONS

Tentative only.

### RQ1
How can the behavior of a host-based default-gateway ARP poisoning detector be represented as a finite-state black-box testing model?

### RQ2
How can valid test sequences be automatically generated from the model to exercise different default-gateway ARP states and detector lifecycle conditions?

### RQ3
Can the proposed model-based testing method expose behavioral differences or failures in selected host-based ARP poisoning detectors beyond those observed in a conventional clean-start attack test?

RQ3 still needs refinement.

Do not presuppose that hidden failures will definitely be discovered.

---

# 27. CURRENT TENTATIVE OBJECTIVES

The school's Topic Proposal Template expects objectives to progress logically through:

- computational technique/model;
- prototype/framework;
- evaluation.

Tentative objectives:

1. **Analyze** representative host-based default-gateway ARP poisoning detection approaches and identify externally observable behavioral requirements suitable for black-box testing.

2. **Design** a finite-state behavioral model and model-based technique for generating valid default-gateway ARP test sequences.

3. **Develop** an automated virtualized black-box testing prototype that executes the generated sequences and evaluates detector behavior through a ground-truth oracle.

4. **Evaluate** the proposed testing method using selected host-based ARP poisoning detectors in terms of test coverage, behavioral violations identified, repeatability, and execution outcomes.

These are not yet official objectives.

---

# 28. CURRENT SCHOOL CLASSIFICATION

Tentative:

### CS Domain
**Cybersecurity and Digital Forensics**

Secondary:
**Intelligent Software Engineering and Computing Systems**

### Computing Contribution
**Model-Based Test Generation + Behavioral Modeling + Automated Test Oracle**

### Relevant Research Areas
- Automated Testing
- Intrusion Detection
- Vulnerability Assessment
- Computational Modeling

These categories have explicit support in the school documents.

---

# 29. SDG / BU AGENDA STATUS

Do not force this prematurely.

Tentative SDG:

> **SDG 9 — Industry, Innovation and Infrastructure**

because the study concerns security and reliability of computing/network infrastructure.

Possibly SDG 16 could be argued through digital security, but SDG 9 currently feels cleaner.

The school document says SDG alignment is encouraged but the main requirement remains a substantial CS contribution.

BU Agenda alignment is not yet firmly decided.

Possible area:

> Global Competitiveness of Business and Industry / technological infrastructure

but this needs careful wording and should not be fabricated.

---

# 30. POSSIBLE METRICS

Keep them meaningful.

Possible metrics:

### Test Sequence Coverage
How much of the modeled transition graph was exercised?

### State-Sequence Pass Rate
How many generated valid sequences completed without violating the behavioral oracle?

### Attack Detection Outcome
Did the detector correctly identify attack state?

### False Alarm Outcome
Did it raise an alert during benign modeled state?

### Recovery Correctness
After a poisoning condition ends, did the externally observable system return to correct benign operation?

### Incorrect Mitigation
Did the detector block/reject the legitimate gateway?

### Repeatability
Does executing the same sequence from the same reset state produce consistent results?

Detection latency can be secondary.

CPU/RAM overhead is optional, not core.

Do not invent a meaningless composite “robustness score” merely to make it look mathematical.

---

# 31. POSSIBLE BEHAVIORAL PROPERTIES / ORACLE RULES

Examples only.

### Security property
When the victim is mapped to an attacker rather than the known legitimate gateway, a detection-capable detector should not remain indefinitely silent.

### Benign property
During a fully legitimate state sequence, the detector should not permanently classify the legitimate gateway as malicious.

### Recovery property
After an attack ends and legitimate mapping is restored, mitigation should not leave the victim unable to communicate with the legitimate gateway.

### Initialization property
Detector startup while the victim is already poisoned should produce a defined observable behavior and should be included as an explicit test rather than silently assuming clean initialization.

These must be tailored to the detector's advertised behavior.

---

# 32. IMPORTANT RESEARCH DESIGN ISSUE — TEST ORACLE VALIDITY

A professor may ask:

> “How can you know the true gateway MAC?”

Answer:

Because this is a **controlled virtual experiment**.

The framework itself creates/configures:

- Gateway VM;
- Attacker VM;
- network topology.

Therefore it knows which MAC belongs to the legitimate gateway at every modeled step.

This is not inferred from ARP.

It is ground truth supplied by the controlled test environment.

Very important distinction.

---

# 33. WHY VIRTUALIZATION IS ACTUALLY AN ADVANTAGE HERE

Virtualization is not just chosen because it is cheap.

It enables:

- reproducible reset states;
- controlled MAC identities;
- controlled attacks;
- repeatable experiment sequences;
- snapshot/reset;
- isolation;
- automation.

This makes the testing methodology easier to reproduce than relying on physical routers/switches.

---

# 34. CURRENT NOVELTY CONFIDENCE

After multiple research passes:

### Strongly established as existing

Generic ARP spoofing detector:
**10/10 existing**

Host-based ARP detector:
**10/10 existing**

Default-gateway-only client-side monitoring:
**10/10 existing**

Active verification:
**10/10 existing**

State-based ARP defense:
**10/10 existing**

Model-based testing generally:
**10/10 existing**

General automated IDS/security testing:
**10/10 existing**

ARP protocol test suites:
**10/10 existing**

Comparative ARP-security evaluation:
**10/10 existing**

### Current candidate

Exact combination:

> detector-agnostic + external behavioral model + model-derived valid gateway-state sequences + ground-truth oracle + host-based default-gateway ARP detectors

**No exact match identified so far.**

Working confidence:

> roughly **7.5–8/10 as an incremental novelty candidate**

Safe to show an adviser as a candidate:

> roughly **8–8.5/10**

Safe to call “first ever”:

> **No. Do not claim that.**

---

# 35. MAJOR NON-NOVELTY RISK NOW

Before the school files were uploaded, a major concern was:

> “Baka framework lang at hindi CS.”

After reading the actual school guidelines, this concern became substantially smaller because:

- Automated Testing is explicitly approved;
- Cybersecurity is explicitly approved;
- Computational Modeling is explicitly acceptable;
- frameworks/models/methodologies may be part of the proposed computing solution;
- evaluation/application of computational methods can constitute CS research.

The remaining risk is no longer:

> “CS ba ito?”

The main remaining risk is:

> **“Is the exact test model/test-generation/oracle contribution sufficiently distinct from existing IDS-testing and ARP-testing work?”**

That is the correct question.

---

# 36. THE HARDEST EXPECTED PROFESSOR QUESTION

Likely:

> **“Pinagsama niyo lang existing state machine, model-based testing, ARP, at IDS framework. Ano ang bago?”**

Best current answer:

> “Yes, the individual techniques are established. We are not claiming otherwise. The contribution is the domain-specific behavioral specification and automated oracle-driven test-generation method for a narrowly defined detector class: host-based detectors protecting the victim's IPv4 default-gateway ARP binding. Existing work we identified either designs ARP defenses, tests ARP protocol implementations, evaluates general IDSs, or performs detector-specific experiments; we have not yet identified one that provides this exact model-driven black-box test abstraction for that detector class.”

This is incremental research.

That is acceptable only if defended honestly.

---

# 37. CURRENT NEXT STEP

The Topic Concept v1 now exists.

Do **not** write Chapter 1 yet.

Do **not** finalize the title yet.

Do **not** begin coding yet.

The next planned activity is:

# **ADVISER / PANEL ATTACK SIMULATION**

Attack the concept with questions such as:

1. “Model-based testing already exists. What is new?”
2. “ARP test suites already exist. Why do we need this?”
3. “IDS testing frameworks already exist.”
4. “Why default gateway only?”
5. “Why host-based only?”
6. “Why not Secure ARP?”
7. “Framework lang ba ito?”
8. “What exact algorithm/model is your contribution?”
9. “How is your oracle guaranteed correct?”
10. “What detectors will you test?”
11. “What if detectors have different outputs?”
12. “How will test-generation coverage be measured?”
13. “Why automatically generate tests instead of writing five scenarios manually?”
14. “What knowledge does this add if no detector fails?”
15. “What is the beneficiary?”
16. “Is this substantial enough for BSCS?”
17. “What exact prior work is closest?”
18. “What happens if an existing paper already has a similar state-transition tester?”

The goal is to determine whether the concept survives an adversarial defense before preparing the official Topic Proposal Template.

---

# 38. AFTER PANEL ATTACK SIMULATION

If the concept survives:

### Step 1
Finalize exact research gap.

### Step 2
Finalize working title.

### Step 3
Finalize:
- CS Domain;
- Computing Contribution;
- Expected Innovation;
- SDG;
- BU Agenda;
- Beneficiary.

### Step 4
Finalize research questions/objectives.

### Step 5
Fill the official Topic Proposal Template.

### Step 6
Continue into Chapters 1–3 only after adviser feedback.

---

# 39. PRINCIPLE TO PRESERVE

The core principle throughout this entire discussion has been:

> **ARP poisoning is the experimental threat, not automatically the thesis contribution.**

The contribution must be a clearly isolated Computer Science component.

Current candidate:

```text
Finite-state behavioral specification
+
Model-derived test generation
+
Ground-truth behavioral oracle
+
Automated black-box evaluation
```

ARP poisoning supplies the cybersecurity context.

---

# 40. CURRENT STATUS IN ONE PARAGRAPH

The student initially wanted a simple, inexpensive host-based thesis focused only on poisoning of the victim's IPv4 default-gateway ARP entry. After repeatedly rejecting crowded ideas such as generic ARP detection, polling, event-driven detection, active verification, voting, startup poisoning, historical trust, false-positive handling, and stateful ARP defense, the current candidate shifted from building another detector to **testing detectors systematically**. Multiple literature passes have found host-based gateway detectors, stateful ARP defenses, protocol ARP test suites, comparative ARP evaluations, general IDS testing frameworks, and automated security-testing systems. However, no exact prior work has yet been identified that combines an **external behavioral model, automatic valid state-transition generation, black-box detector evaluation, and a controlled ground-truth oracle specifically for host-based detectors protecting the victim's IPv4 default-gateway IP-to-MAC binding**. The school's official materials explicitly recognize Cybersecurity, Automated Testing, and Computational Modeling as valid CS areas, so the principal remaining issue is novelty specificity rather than basic CS-domain eligibility.

---

# 41. CONTINUATION COMMAND FOR THE NEXT AI

When this handoff is pasted into a new conversation, continue with:

> **“Run the adviser/panel attack simulation on Topic Concept v1. Be adversarial. Do not protect the topic. Try to invalidate it using the strongest technical and novelty objections. For every objection, classify it as fatal, fixable, or weak, and update the thesis concept only when justified.”**

That is the exact point where this conversation currently stands.
