# THESIS RESEARCH HANDOFF v3
## Model-Based Behavioral Testing of Host-Based ARP Spoofing Detectors Under Default-Gateway Poisoning

> **Canonical recovery document for continuing the thesis discussion in a new AI conversation.**
>
> If this handoff is pasted into a new chat, the next AI must **continue from the current research state** and must **not restart generic ARP topic brainstorming**.

---

# 0. CRITICAL INSTRUCTIONS TO THE NEXT AI

You are continuing a long, adversarial thesis-topic development and literature-audit process with a Bachelor of Science in Computer Science student.

The student has repeatedly emphasized that they have a **trust issue regarding novelty** and does not want superficial reassurance. The AI should actively try to **invalidate weak ideas**, search for prior art, correct previous mistakes, and use conservative novelty language.

## User priorities

The thesis should ideally be:

- technically legitimate as a Computer Science thesis;
- simple enough for an undergraduate group;
- inexpensive;
- implementable mostly or completely through virtualization;
- narrow and easy to explain;
- not dependent on expensive switches, routers, or special hardware;
- not dependent on SDN;
- not dependent on ML/AI unless genuinely necessary;
- based on a specific, defensible computing contribution;
- supported by aggressive related-work checking;
- honest about incremental rather than revolutionary novelty.

The student strongly dislikes ideas that a professor can dismiss with:

> **“Meron na niyan.”**

Therefore:

- never overstate novelty;
- prefer “we did not identify…” over “no prior work exists”;
- distinguish established methodology from the application-specific contribution;
- kill the topic if exact prior work is found;
- do not add flashy complexity simply to make the thesis look advanced.

---

# 1. CURRENT THESIS STATUS

The thesis is **NOT** about creating another ARP spoofing detector.

The current leading concept is:

> **Model-Based Behavioral Testing of Host-Based ARP Spoofing Detectors Under Default-Gateway Poisoning**

This is still a **working title**, not yet final.

The current proposed contribution is:

> **an application-specific behavioral testing model and ground-truth oracle for systematically evaluating host-based ARP spoofing detectors when the victim's IPv4 default-gateway binding undergoes controlled network and detector-lifecycle transitions.**

Established model-based testing methods and coverage criteria may be used to operationalize the model, but they are **not claimed as novel**.

---

# 2. EXACT SECURITY SCOPE

The controlled attack target is only the victim host's local IPv4 ARP entry for the default gateway.

Normal:

```text
Default Gateway IP → Legitimate Gateway MAC

192.168.1.1 → AA:AA:AA:AA:AA:AA
```

Poisoned:

```text
192.168.1.1 → ATTACKER_MAC
```

The attacker makes the victim associate the legitimate default-gateway IP address with the attacker's MAC address.

The experiment is therefore specifically about:

> **default-gateway poisoning on the victim host.**

Important title correction:

The detectors under test do **not all need to be gateway-only detectors**.

A generic host-based ARP spoofing detector may be eligible if it can detect poisoning involving the victim's default-gateway mapping.

Therefore the currently preferred wording is:

> **host-based ARP spoofing detectors under default-gateway poisoning**

rather than:

> **host-based default-gateway ARP poisoning detectors**

because the latter falsely implies every detector was specifically designed only for the gateway.

---

# 3. WHAT IS OUTSIDE THE SCOPE

Do not accidentally expand the thesis into:

- poisoning the gateway/router's own ARP table;
- every ARP mapping on the LAN;
- IPv6 Neighbor Discovery/NDP;
- DHCP spoofing;
- DNS spoofing;
- Wi-Fi deauthentication;
- generic MITM detection;
- whole-network IDS design;
- SDN protection;
- Dynamic ARP Inspection;
- Secure ARP deployment;
- router firmware modifications;
- enterprise switching defenses;
- ML packet classification;
- malware detection;
- every possible ARP attack variant.

Primary experiment:

> **host-based detection behavior under controlled poisoning of the victim's IPv4 default-gateway mapping.**

---

# 4. TERMINOLOGY ALREADY CLARIFIED

Use:

> **Victim's ARP table**

when explaining the concept to the student.

Linux may use the broader term “neighbor table,” but this does not mean hosts share their ARP tables.

Each host has a separate local mapping table.

ARP packets/messages move across the LAN.

The whole ARP table does not.

Avoid unnecessarily reintroducing “neighbor table” terminology unless discussing a specific OS API.

---

# 5. LOW-COST / VIRTUALIZED DEPLOYMENT

Preferred experimental topology:

```text
               Isolated Virtual LAN
                       |
            +----------+----------+
            |          |          |
         Victim     Attacker    Gateway
           VM          VM         VM
```

Recommended platform:

- VirtualBox;
- VMware;
- equivalent hypervisor.

Prefer an **Internal Network / isolated virtual Layer-2 LAN**.

Do not make the hypervisor's built-in NAT service itself the gateway under test if a dedicated Gateway VM can be used.

The Gateway VM may optionally have a second NAT adapter for Internet access, but Internet is not required for the ARP experiment.

Virtualization is not merely a cost-saving choice. It improves:

- reset reproducibility;
- controlled MAC identities;
- isolation;
- repeatability;
- snapshotting;
- automated setup;
- controlled gateway replacement;
- controlled attack initiation and recovery.

No physical Linux computer is required.

Linux may be used in VMs because many relevant detectors/tools run conveniently there.

---

# 6. SECURE ARP QUESTION ALREADY RESOLVED

The student asked:

> “May Secure ARP na. Bakit kailangan pa itong thesis?”

Relevant distinction:

Secure ARP/S-ARP-like approaches attempt stronger protocol authentication using mechanisms such as:

- digital signatures;
- PKI;
- trusted authorities;
- protocol extensions;
- host/network support.

Our thesis does not claim to replace those mechanisms.

The intended environment is:

> **ordinary legacy IPv4 LAN using standard unauthenticated ARP, where the researcher/victim controls only the endpoint and cannot require modifications to the gateway, switch, or all participating hosts.**

Therefore:

```text
Secure ARP question:
Can the ARP ecosystem itself be authenticated or modified?

Current thesis question:
How can existing host-based ARP spoofing detectors be systematically evaluated under controlled default-gateway poisoning behavior?
```

Do not criticize Secure ARP as ineffective. It solves a different deployment problem.

---

# 7. SCHOOL DOCUMENTS REVIEWED

Three school/course documents were uploaded and reviewed:

1. `Thesis_Domains_CS.pdf`
2. `Topic_Proposal_Template_CS.pdf`
3. `Thesis_1_Course_Introduction_Sy.pptx`

The school materials materially support the current direction.

## Important findings from the school documents

The approved CS thesis areas explicitly include or support:

- Cybersecurity Mechanisms;
- Intrusion Detection;
- Vulnerability Assessment;
- Computational Modeling and Simulation;
- Automated Testing;
- Intelligent Software Engineering and Computing Systems.

The documents also state that a CS thesis may contribute through:

- development;
- evaluation;
- enhancement;
- application

of computational methods/models/algorithms/technologies.

The software application/framework should be the **vehicle** for implementing and evaluating the actual computing contribution, not the contribution by itself.

This is important because the thesis does **not** need to invent a new ML model or cybersecurity detection algorithm merely to qualify as CS.

The remaining risk is mainly **novelty specificity**, not basic CS-domain eligibility.

---

# 8. COURSE / PROPOSAL STRUCTURE IMPLICATION

The official Topic Proposal Template emphasizes:

- computing problem;
- computational approach;
- core model/algorithm/technique;
- research gap;
- proposed system/framework;
- objectives;
- evaluation.

Therefore avoid saying:

> “We will build an ARP testing application.”

Prefer:

> **“We will define a behavioral testing model and oracle, then implement them in an automated virtual testing framework.”**

Current approximate classification:

### Primary CS Domain
**Cybersecurity and Digital Forensics**

### Secondary area
**Intelligent Software Engineering and Computing Systems**

### Relevant computing components
- Automated Testing
- Computational Modeling
- Intrusion Detection Evaluation
- Vulnerability/Security Assessment

---

# 9. SCHOOL ORIGINALITY REQUIREMENT

The Thesis 1 slides state that merely repeating prior work is generally insufficient unless the purpose is to confirm or reject previous findings.

Therefore the thesis must clearly contribute something beyond:

> “We replicated an ARP spoofing experiment.”

The current attempt to provide that contribution is:

> **a reusable application-specific behavioral test model and oracle for controlled state-sequence evaluation.**

---

# 10. IDEAS ALREADY REJECTED OR DOWNRANKED

Do not casually propose these again.

## 10.1 Simple default-gateway MAC monitor

```text
save gateway MAC
compare later
alert if different
```

**Status: RED**

Already widely done.

---

## 10.2 Polling vs event-driven monitoring

**Status: DROPPED**

Reason:
- implementation-level distinction;
- weak research question;
- “short attacks can occur between polls” felt obvious.

---

## 10.3 Short-duration poisoning as the thesis

**Status: DROPPED**

Too obvious/common-sense as the central question.

---

## 10.4 Generic active verification

ARP probes / ICMP / verification of conflicting mappings.

**Status: RED**

Substantial old prior art.

---

## 10.5 Voting / peer consensus

**Status: RED**

MR-ARP and later voting approaches exist.

---

## 10.6 Poisoned startup alone

Scenario:

```text
victim already poisoned
→ detector initializes
```

**Status: useful test condition, not enough standalone novelty.**

---

## 10.7 “Baseline inversion”

Working observation:

```text
attacker trusted as baseline
→ attack stops
→ legitimate gateway returns
→ legitimate gateway may appear anomalous
```

**Status: keep only as a possible behavioral trace.**

“Baseline inversion” was an internal working term, not an established literature term.

---

## 10.8 Context-aware re-baselining

**Status: DOWNRANKED**

Prior art such as WiSC and historical/contextual trust approaches are too close.

---

## 10.9 Generic trust-strategy comparison

Manual MAC vs learned baseline vs active verification.

**Status: DOWNRANKED**

Comparative ARP-security studies already exist.

---

## 10.10 Legitimate gateway change as standalone novelty

**Status: NOT NOVEL BY ITSELF**

Existing literature already recognizes legitimate mapping changes / false positives.

Still useful as a test event.

Technical correction:

Do not use standard VRRP/HSRP failover as the primary example of a gateway MAC changing. Redundancy protocols often preserve a virtual MAC.

Use instead:

- actual gateway VM replacement;
- gateway NIC replacement;
- explicit administrative reconfiguration.

---

## 10.11 New state-machine ARP detector

**Status: RED**

Stateful/DES ARP defenses already exist.

---

## 10.12 Generic “ARP testing framework”

**Status: TOO BROAD**

ARP protocol test suites, IDS test frameworks, automated security testing, and comparative evaluations already exist.

---

# 11. IMPORTANT PRIOR ART / DANGER LIST

Future AI must preserve these categories.

## Secure ARP / S-ARP
Cryptographic/authenticated ARP approaches are old.

## Stateful / fuzzy ARP defenses
State models inside ARP defenses are old.

## Active host-based ARP IDS
Active probing and multi-scenario testing are old.

## DES/state-model ARP detection
Formal state machines inside detectors are old.

## Comparative ARP security studies
“Compare detectors” is not enough novelty.

## 2019 client-side gateway baseline approach
Default-gateway baseline monitoring is already done.

## WiSC (MobiCom 2021)
Very important prior art:
- client-side;
- default gateway `(IP, MAC)` checking;
- initial compromise awareness;
- historical/cross-connection context.

Kills generic gateway-history/startup-trust novelty.

## ASD / benign false-positive-aware work
False-positive evaluation is not novel.

## Modern voting-based ARP schemes
Voting-based genuine-mapping resolution is not novel.

## 2025 IEEE Access host/router ARP method
Relevant clean-snapshot/trusted-baseline assumptions.

## 2026 client-side default-gateway detector
Extremely close to the original simple detector topic.

## IWL ARP Test Suite
Automated ARP protocol conformance/robustness testing exists.

## SCADA IDS Test Framework
Virtualized / IDS-agnostic testing frameworks exist.

## DELTA / similar security assessment systems
Automated security evaluation exists.

## raw-packet / network security tools
Automated ARP-security checking exists.

## Model-Based Security Testing literature
Model-based automatic security-test generation is established.

## Mutation-based security testing
Mutation/fault-seeded security-test assessment is established.

## Stateful network-software sequence testing
Recent work such as stateful SDN controller testing shows sequence-sensitive network-software testing is established.

Therefore none of these generic techniques should be presented as inventions.

---

# 12. NOVELTY CLAIMS THAT MUST NOT BE MADE

Never claim:

- first ARP detector;
- first host-based ARP detector;
- first gateway detector;
- first state-machine ARP system;
- first model-based security tester;
- first automated security test generator;
- first black-box network tester;
- first mutation-based security testing;
- first transition-coverage testing;
- first ARP test suite;
- first IDS testing framework;
- first evaluation of startup poisoning;
- first recovery testing;
- first false-positive testing;
- first stateful network sequence testing;
- “no prior work exists.”

Safe language:

> **“Our literature search has not identified a reusable behavioral test model and corresponding oracle specifically for this class of host-based ARP spoofing detectors under controlled default-gateway poisoning and detector-lifecycle transitions.”**

---

# 13. CURRENT NOVELTY BOUNDARY

Established:

```text
ARP attacks                    existing
ARP detectors                  existing
default-gateway monitoring     existing
active verification            existing
state machines                 existing
model-based testing            existing
model-based security testing   existing
automatic test generation      existing
transition/state coverage      existing
mutation testing               existing
black-box testing              existing
network software testing       existing
IDS/security frameworks        existing
```

Potentially original / not yet found as an exact prior system:

> **the ARP-detector-specific behavioral abstraction and oracle that separate network-binding transitions, monitor lifecycle, and trust-establishment actions, then use those semantics to systematically evaluate host-based ARP spoofing detectors under default-gateway poisoning.**

This is **incremental novelty**.

Do not overstate it.

---

# 14. IMPORTANT METHODOLOGICAL REFINEMENT — PRIMARY SCOPE IS DETECTION ONLY

The current recommendation is:

> **Evaluate detection behavior only as the standardized primary outcome.**

Do not make mitigation correctness a universal comparison requirement.

Reason:

Different tools may:

- only alert;
- rewrite ARP entries;
- block MACs;
- modify firewall state;
- enforce static mappings.

Including mitigation would make the black-box model substantially more complicated.

For the primary experiment normalize detector output to:

```text
ALERT
NO_ALERT
```

Mitigation may be:

- disabled in reproductions when feasible;
- allowed only if it does not invalidate the modeled experiment;
- explicitly excluded from comparative evaluation.

This is especially important for the 2026 detector, which includes mitigation. A reproduction may implement/evaluate the **detection logic only**, with this limitation disclosed.

---

# 15. CURRENT DETECTOR-UNDER-TEST STRATEGY

Three strong DUT roles have emerged.

## D1 — 2019 client-side Bash detector reproduction

Published architecture:

1. first script saves trusted default-gateway IP/MAC to a file;
2. second script later loads the stored value and monitors for mismatch;
3. polling interval around five seconds.

Key property:

> **trust/reference establishment is separate from monitoring-process startup.**

This directly caused a major correction to Model v1.

Original maintained source repository was not located.

Therefore D1 should be described as:

> **a reproduction of the published algorithm**, not the authors' original artifact.

Role:

> persistent saved-baseline comparison.

---

## D2 — 2026 default-gateway detector reproduction

Published logic includes:

- trusted gateway MAC;
- current gateway MAC;
- polling around 3 seconds;
- multiple/consecutive mismatch confirmation;
- a step for checking legitimate gateway changes;
- optional re-baselining;
- alert/mitigation.

The publication describes initialization of the trusted gateway reference but does not make every restart/persistence semantic perfectly explicit.

Therefore:

> startup/restart behavior should be treated as an experimental property of the faithful reproduction, not assumed.

Original public source repository was not located.

Role:

> recent gateway-specific baseline + temporal confirmation / claimed legitimate-change handling.

---

## D3 — open-source active detector

Open-source Scapy implementation of active ARP spoofing detection.

Important implementation characteristics:

- runtime learned mapping dictionary starts empty;
- unknown mappings undergo active verification;
- verified pairs are learned dynamically;
- changed known mapping can trigger an alert;
- source produces a machine-observable attack message;
- process restart clears in-memory learned state.

Role:

> independent original artifact + dynamic active verification.

Unlike D1/D2, D3 is not gateway-only, but it can be evaluated specifically under default-gateway poisoning.

This motivated the revised title wording.

---

# 16. WHY THE THREE DUTS ARE USEFUL TOGETHER

They represent meaningfully different detection/trust strategies.

```text
D1:
persistent trusted baseline comparison

D2:
trusted baseline + temporal confirmation / re-baselining

D3:
dynamic learning + active verification
```

This is better than comparing three near-identical scripts.

Potential experimental roles:

```text
D1 = published-algorithm reproduction
D2 = recent published-algorithm reproduction
D3 = independent open-source artifact
```

---

# 17. MAJOR MODEL v1 CORRECTION — START ≠ TRUST ESTABLISHMENT

This is one of the most important insights found so far.

Previous Model v1 used:

```text
POISON → START
```

to represent “detector starts while poisoned.”

That is **underspecified**.

For D1:

### Case A

```text
ESTABLISH_REFERENCE while clean
→ POISON
→ START_MONITOR
```

Reference remains legitimate.

### Case B

```text
POISON
→ ESTABLISH_REFERENCE
→ START_MONITOR
```

Reference may be attacker-controlled.

Both previously looked like “poison before startup,” but they are behaviorally different.

Therefore:

> **monitor lifecycle and trust/reference-establishment lifecycle must be modeled separately.**

This is now a core part of Model v2.

Do not collapse them again.

---

# 18. CURRENT MODEL v2 — CORE NETWORK VARIABLES

Define:

```text
G = current legitimate gateway MAC
A = attacker MAC
O = MAC currently associated by victim with the default-gateway IP
```

Invariant:

```text
A ≠ G
```

Derived binding conditions:

### CLEAN

```text
O = G
```

### POISONED

```text
O = A
and
A ≠ G
```

Detector process state:

```text
L ∈ {OFF, ON}
```

Avoid universal internal trusted-MAC variable `T`, because black-box detectors may not expose it.

---

# 19. MODEL v2 EVENT CATEGORIES

## A. Environment/network events

```text
POISON
RESTORE
REPLACE
```

## B. Detector process events

```text
START
STOP
RESTART
```

## C. Optional detector setup/trust event

```text
ESTABLISH_REFERENCE
```

This event is applicable only to detectors whose public configuration/design includes an explicit reference-establishment process.

Examples:

- D1: clearly applicable;
- D2 reproduction: likely tied to initialization, profile must define exact semantics;
- D3: not applicable because it dynamically verifies/learns mappings.

---

# 20. REVISED POISON SEMANTICS — VERY IMPORTANT

`POISON` must **not** simply mean:

```text
edit victim ARP cache so O = A
```

That would unfairly favor cache-monitoring detectors and may not stimulate packet-based detectors.

Instead define `POISON` as:

### Action

Attacker emits forged ARP traffic asserting:

```text
Gateway_IP → Attacker_MAC
```

### Required postcondition

The experiment controller verifies:

```text
O = A
```

before declaring the event successful.

Therefore both kinds of detectors receive appropriate stimulus:

```text
packet-oriented detector
→ sees forged ARP traffic

cache-oriented detector
→ sees resulting gateway mapping
```

This is a major methodological improvement.

---

# 21. REVISED RESTORE SEMANTICS

`RESTORE` must also be an action + verified postcondition.

Conceptually:

### Action

- stop active poisoning;
- cause legitimate ARP resolution / corrective gateway mapping.

### Required postcondition

```text
O = G
```

Possible implementation later:

- corrective ARP;
- cache flush followed by legitimate resolution;
- another controlled mechanism.

Exact mechanism should be standardized before methodology is finalized.

---

# 22. REPLACE EVENT — NOW KEEP IT

Earlier `REPLACE` was uncertain.

After mapping to actual detector designs, it is now justified.

Definition:

> **legitimate replacement/change of the default gateway's MAC identity while remaining a benign network condition.**

Implementation should be unambiguous:

```text
Gateway G1 (MAC1)
→ administratively replace/configure Gateway G2 (MAC2)
→ victim correctly resolves Gateway_IP → MAC2
```

Do not depend on VRRP/HSRP for this test.

Why keep `REPLACE`?

The three DUT types can react differently:

```text
D1:
changed MAC vs stored baseline
→ likely alert

D2:
claims to check for legitimate gateway change
→ potentially re-baseline

D3:
known IP + changed MAC
→ alert according to learned mapping logic
```

This makes `REPLACE` a useful benign-transition event.

---

# 23. RESTART EVENT — KEEP, BUT PROFILE-SPECIFIC

`RESTART` is not equally meaningful for all detectors.

## D1
Restarting the monitor likely does **not** erase the trusted baseline because it lives in a persistent file.

## D2
Restart behavior may matter, but publication details about persistence/reinitialization are not fully explicit.

## D3
Restart definitely clears process-memory learned state, so it is highly relevant.

Therefore:

> `RESTART` remains available in the model but should not be a universally mandatory test transition for every DUT.

Use detector profiles.

---

# 24. DETECTOR PROFILES / ADAPTERS

Do not promise a zero-configuration “fully detector-agnostic” system.

Better terminology:

> **detector-independent behavioral specification with detector-specific profiles/adapters.**

Architecture:

```text
                Core Behavioral Model
                        |
             +----------+----------+
             |          |          |
          Profile D1 Profile D2 Profile D3
             |          |          |
             v          v          v
        Detector D1 Detector D2 Detector D3
             |
          Adapter
             |
             v
        ALERT / NO_ALERT
```

Each profile specifies:

- applicable events;
- configuration/setup requirements;
- whether `ESTABLISH_REFERENCE` applies;
- observation window;
- how to map detector output to ALERT/NO_ALERT;
- documented intended policy;
- restart semantics if known.

---

# 25. DUT ELIGIBILITY CONTRACT

A detector is eligible if it:

1. runs on/from the victim endpoint;
2. can meaningfully detect poisoning involving the default gateway;
3. produces machine-observable detection output;
4. can run in the isolated virtual environment;
5. has enough documentation/source behavior to define an adapter/profile;
6. does not fundamentally prevent the modeled poisoned state from being established before the detection observation.

This excludes primary use of prevention-only mechanisms such as systems that make `O = A` impossible.

ArpON is therefore not preferred as a primary detection-only DUT.

XArp is also not preferred because of artifact age/distribution issues.

---

# 26. BLACK-BOX OUTPUT NORMALIZATION

Primary normalized verdict:

```text
V ∈ {ALERT, NO_ALERT}
```

Examples:

```text
"Under Attack"
→ ALERT

"Gateway MAC mismatch"
→ ALERT

no relevant alert during observation window
→ NO_ALERT
```

Detector-specific adapters implement the normalization.

The framework should not require source-code access for real DUT evaluation, even though source may be available for some tools.

---

# 27. GROUND-TRUTH SECURITY ORACLE

The controlled VM environment knows:

```text
G = legitimate gateway MAC
A = attacker MAC
O = victim-observed gateway mapping
```

Therefore objective security state:

```text
GT = BENIGN  if O = G

GT = ATTACK  if O = A and A ≠ G
```

The detector does **not** define ground truth.

This avoids circular validation.

---

# 28. DUAL-LAYER ORACLE — KEEP THIS

Do not automatically call every benign-condition alert a software bug.

Use two evaluation layers.

## Layer 1 — Objective security-state behavior

| Ground Truth | Detector Output | Observation |
|---|---|---|
| ATTACK | ALERT | attack detected |
| ATTACK | NO_ALERT | attack missed |
| BENIGN | ALERT | benign-condition alert |
| BENIGN | NO_ALERT | quiet benign behavior |

## Layer 2 — Detector policy conformance

Check whether the observed behavior matches the detector's **documented intended policy**.

Example:

A detector may intentionally warn on any gateway MAC change, even a legitimate one.

Then:

```text
Ground truth = BENIGN
Detector = ALERT
```

is still objectively a benign-condition alert, but may:

```text
CONFORM to the detector's documented policy
```

This protects the study from unfairly imposing one security philosophy on all DUTs.

---

# 29. OBSERVATION WINDOW

Different detectors have different timing assumptions.

Define:

```text
W(D)
```

= valid observation window for detector `D`.

Determine from:

1. published/documented polling/confirmation behavior;
2. configuration;
3. otherwise a predefined calibration procedure.

Important event procedure:

```text
apply event
↓
verify required network postcondition
↓
start detector observation window
↓
collect ALERT/NO_ALERT
↓
apply objective oracle
↓
apply documented-policy conformance check
```

Do not start timing before the network state has actually been established.

Detection latency may be recorded separately.

---

# 30. TEST-CASE REPRESENTATION

A test should be reproducible from the model specification.

Example:

```text
Test ID: TC-XX

Detector profile:
D1

Initial environment:
G = MAC_G
A = MAC_A
O = G
Monitor = OFF

Setup:
ESTABLISH_REFERENCE

Sequence:
START → POISON → RESTORE

Expected ground-truth states:
BENIGN → ATTACK → BENIGN

Observation checkpoints:
after each relevant event

Detector outputs:
NO_ALERT / ALERT / NO_ALERT

Objective interpretation:
quiet benign / attack detected / quiet benign

Policy conformance:
PASS / PASS / PASS
```

Important output:

> exact failing trace, not only aggregate accuracy.

---

# 31. COVERAGE CRITERIA

Model-based coverage is established methodology, not novelty.

Candidate methodology:

- transition coverage;
- transition-pair coverage;
- possibly a bounded sequence criterion.

The old Model v1 raw count:

> **38 transition pairs**

is now **obsolete**.

Why?

Because Model v2 separates `ESTABLISH_REFERENCE`, uses detector profiles, and changes applicable transition semantics.

Do not use “38” in the proposal or future defense.

Coverage counts must be recomputed only after Model v2 is formally frozen.

---

# 32. COMMON CORE VS PROFILE-SPECIFIC TESTS

Not every DUT should be forced through exactly the same lifecycle sequence.

Potential common-core events/tests:

```text
START → POISON
START → POISON → RESTORE
START → REPLACE
START → REPLACE → POISON
```

Profile-specific examples:

### D1
```text
POISON
→ ESTABLISH_REFERENCE
→ START
```

### D3
```text
START
→ learn/verify legitimate gateway
→ POISON
→ RESTART
```

The model should distinguish:

> **common cross-detector behavior**

from:

> **detector-specific trust/lifecycle behavior.**

---

# 33. ONE OF THE MOST IMPORTANT CONCEPTUAL INSIGHTS SO FAR

The research process discovered that:

> **trust/reference establishment and monitoring-process lifecycle must not be collapsed into a single startup event when behaviorally testing heterogeneous ARP spoofing detectors.**

This is now central to the application-specific model.

Do **not** automatically claim this insight is globally novel.

Generic security testing/modeling may already distinguish setup/configuration from execution.

Its value is currently:

> **a required modeling distinction for this ARP-detector evaluation domain.**

---

# 34. WHY AUTOMATIC / MODEL-DERIVED TESTING IS STILL JUSTIFIED

Do not claim automatic generation is novel.

The justification is:

> tests are systematically derived from the behavioral model according to a defined coverage criterion rather than manually selected as an ad hoc list of scenarios.

Potential benefits:

- reproducibility;
- reduced scenario-selection bias;
- systematic state-order coverage;
- extensibility;
- exact failing traces;
- common experimental specification.

Avoid saying:

> “We automate because automation itself is innovative.”

---

# 35. FAULT-SEEDED / MUTANT VALIDATION — OPTIONAL SECONDARY METHOD

Previous proposal:

Create a small reference detector and deliberately introduce known behavioral faults, e.g.:

- missed attack;
- poisoned reference establishment;
- failure after restart;
- persistent alert after recovery;
- incorrect benign-change handling.

Use generated tests to see whether faults are exposed.

Important:

- mutation/fault-seeding is established;
- not a contribution;
- do not put it in the title;
- use only if needed to validate test-suite fault-revealing ability.

Avoid tailoring faults to generated tests after the fact.

Fault classes should be justified independently from literature or plausible detector design assumptions.

---

# 36. CURRENT WORKING CONTRIBUTION STATEMENT

Preferred current wording:

> **The primary proposed contribution is an application-specific behavioral test model and ground-truth oracle for evaluating host-based ARP spoofing detectors under controlled default-gateway poisoning. The model separates gateway-binding events, detector-process lifecycle, and explicit trust/reference-establishment actions where applicable. Established model-based test-generation and coverage techniques are then used to produce systematic, reproducible tests through detector-specific profiles and output adapters.**

This is more accurate than claiming a novel test-generation algorithm.

---

# 37. CURRENT WORKING RESEARCH GAP

Safe formulation:

> **Model-based security testing, automated test generation, state/transition coverage, mutation-based test assessment, and stateful network-software testing are well established. Host-based ARP spoofing detectors and default-gateway monitoring mechanisms also already exist. However, in the literature reviewed so far, we have not identified a reusable behavioral test model and corresponding ground-truth oracle specifically designed to evaluate heterogeneous host-based ARP spoofing detectors under controlled default-gateway poisoning while distinguishing network-binding transitions, detector-process lifecycle, and detector-specific trust-establishment behavior.**

Do not replace “we have not identified” with “none exists.”

---

# 38. CURRENT WORKING TITLE

Current preferred title:

> **Model-Based Behavioral Testing of Host-Based ARP Spoofing Detectors Under Default-Gateway Poisoning**

Possible alternative if later needed:

> **A Behavioral Testing Model for Host-Based ARP Spoofing Detectors Under Default-Gateway Poisoning**

Avoid final title lock until adviser-facing Topic Concept v2 is ready.

---

# 39. CURRENT SIMPLE EXPLANATION FOR THE STUDENT

If someone asks:

> “Ano thesis niyo?”

Good answer:

> **“Hindi kami gagawa ng bagong ARP detector. Gagawa kami ng systematic behavioral testing model para i-test ang existing host-based ARP spoofing detectors kapag ang victim's default-gateway ARP mapping ay dumadaan sa controlled attack, recovery, legitimate gateway change, at detector setup/lifecycle conditions.”**

If asked:

> “Ano ang CS contribution?”

Good answer:

> **“The application-specific behavioral model, the ground-truth oracle, and the detector profiles that map different trust and lifecycle behaviors into reproducible model-based tests.”**

Do not answer only:

> “ARP poisoning.”

---

# 40. CURRENT FEASIBILITY STATUS

## Novel algorithm required?
**No.**

## CS-domain fit?
**Strong**, based on school documents.

## Low-cost?
**Strong.**

## Fully virtualizable?
**Yes.**

## Actual runnable DUT available?
**Yes.**

## At least one independent open-source artifact?
**Yes.**

## Published gateway-specific algorithms available for reproduction?
**Yes.**

## Common normalized detection output possible?
**Yes: ALERT / NO_ALERT.**

## Model still trivial?
**No; meaningful lifecycle/trust distinctions emerged.**

## Mitigation modeling needed?
**No, primary scope should remain detection-only.**

---

# 41. CURRENT RISKS

## Risk 1 — novelty is incremental
The testing methodology itself is old.

The thesis survives only if the application-specific model/oracle is rigorous and not already implemented in close prior art.

## Risk 2 — reproduced detectors
D1 and D2 may be reproductions rather than original source artifacts.

Threat to validity must be acknowledged.

## Risk 3 — detector policy differences
Solved partly through dual-layer oracle and profiles.

## Risk 4 — restart semantics
Not universal. Keep profile-specific.

## Risk 5 — `ESTABLISH_REFERENCE` semantics for D2
Still needs careful faithful-reproduction definition.

## Risk 6 — exact coverage criterion
Not yet frozen.

## Risk 7 — scope creep
Do not add mitigation, ML, SDN, packet taxonomy, multiple victims, etc. unless absolutely required.

---

# 42. CURRENT STATUS OF KEY MODEL EVENTS

| Event | Status |
|---|---|
| `POISON` | KEEP; action + verified `O=A` postcondition |
| `RESTORE` | KEEP; action + verified `O=G` postcondition |
| `REPLACE` | KEEP; now well justified |
| `START` | KEEP; means monitor/process activation only |
| `STOP` | KEEP as lifecycle operation |
| `RESTART` | KEEP but profile-specific |
| `ESTABLISH_REFERENCE` | ADD; critical for baseline-based detectors |

---

# 43. OBSOLETE CLAIMS / NUMBERS TO FORGET

Do not reuse:

> “The model has exactly four states, six events, twelve transitions, and 38 transition pairs.”

That was Model v1.

Model v2 changed the semantics and adds profile-specific trust establishment.

The old 38-pair count is obsolete.

Do not use it in the adviser pitch or proposal.

---

# 44. WHAT SHOULD NOT BE ADDED NOW

Do not add:

- machine learning;
- deep learning;
- eBPF;
- blockchain;
- SDN;
- fuzzy logic;
- genetic algorithms;
- optimization merely for appearance;
- huge state spaces;
- mitigation state machines;
- dozens of attack variants.

The project is intentionally narrow.

Its strength should come from:

> **rigor + reproducibility + explicit behavioral semantics**

not technological complexity.

---

# 45. CURRENT NEXT STEP — IMPORTANT

The technical stress tests have now progressed through:

1. broad novelty research;
2. school CS eligibility;
3. model-based testing prior-art research;
4. mutation/coverage prior-art research;
5. Formal Model v1;
6. runnable DUT feasibility;
7. Detector-to-Model Compatibility Matrix;
8. Model v2 correction.

The next step should **NOT** be another broad brainstorming round.

The next step is:

# **CREATE ADVISER-FACING TOPIC CONCEPT v2**

It should compress the research into something understandable in about 1–2 minutes.

It should contain:

1. current working title;
2. exact problem;
3. what existing work already does;
4. exact research gap;
5. proposed CS contribution;
6. simple Model v2 explanation;
7. exact default-gateway-only experimental scope;
8. three detector categories/DUT roles;
9. why it is not “another ARP detector”;
10. feasibility and low-cost setup;
11. expected output/knowledge contribution;
12. conservative novelty statement.

Then perform **one final adviser/panel attack** against Topic Concept v2.

Only if it survives should the project move to:

- finalizing title;
- finalizing objectives/RQs;
- BU Agenda/SDG/beneficiary classification;
- filling the official Topic Proposal Template;
- eventually Chapters 1–3.

---

# 46. RECOMMENDED NEXT-AI COMMAND

If this handoff is pasted into a new conversation, the user can say:

> **“Continue from the handoff. Create the adviser-facing Topic Concept v2 based strictly on Model v2 and the current novelty boundary. Keep it simple enough to explain in 1–2 minutes, then attack it as a professor. Do not add new technical features unless the current concept fails.”**

That is the exact continuation point.

---

# 47. CURRENT STATUS IN ONE PARAGRAPH

The thesis began as a search for a simple host-based ARP poisoning detector focused on the victim's default-gateway mapping, but repeated literature audits showed that simple gateway-MAC monitoring, polling/event-driven variations, active verification, voting, startup trust issues, legitimate-change handling, stateful defenses, and many other detector ideas already exist. The research direction therefore shifted from building another detector to **systematically testing existing host-based ARP spoofing detectors under controlled default-gateway poisoning**. Further research established that model-based security testing, coverage-guided generation, mutation testing, black-box network testing, and stateful network-software testing are themselves existing methodologies, so they are not claimed as novel. The remaining proposed contribution is an **application-specific behavioral model and oracle**. Formal modeling and mapping against three representative detector strategies revealed a critical distinction between **network-binding events, detector process lifecycle, and trust/reference establishment**, leading to Model v2. The primary comparison has been narrowed to detection behavior (`ALERT/NO_ALERT`), with objective ground truth supplied by a controlled virtual network and detector-policy conformance evaluated separately. Three DUT roles are feasible: a 2019 persistent-baseline reproduction, a 2026 temporal-confirmation/re-baselining reproduction, and an independent open-source active-verification detector. The topic currently remains viable, low-cost, and aligned with the school's approved CS areas, but novelty should continue to be described as incremental and application-specific. The next step is to create and adversarially test **Adviser-Facing Topic Concept v2** before filling the official topic proposal.
