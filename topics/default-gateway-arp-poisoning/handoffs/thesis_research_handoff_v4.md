# THESIS RESEARCH HANDOFF v4

## Canonical continuation document

Use this as the authoritative handoff for continuing the thesis discussion in a new chat. Do not restart generic ARP thesis brainstorming unless an exact prior work is found that invalidates the current direction.

---

## 1. User preferences and research style

The student wants a BS Computer Science thesis that is simple, narrow, inexpensive, virtualization-friendly, defensible as CS, and not dependent on managed hardware, SDN, ML/AI, or flashy complexity unless genuinely necessary.

The student has a strong trust concern about novelty and prefers that weak ideas be killed rather than defended. Future work should:

- aggressively verify prior art;
- distinguish “not identified in our search” from “does not exist”;
- avoid “first ever” claims;
- prefer narrow incremental novelty;
- explain simply first, then add technical detail;
- use Taglish when helpful.

---

## 2. Current thesis direction

The thesis is **not about creating a new ARP spoofing detector**.

The current direction is:

> **systematically testing existing host-based ARP spoofing detectors under controlled default-gateway poisoning using an application-specific behavioral test model and ground-truth oracle.**

### Current preferred title direction

Previous working title:

> **Model-Based Behavioral Testing of Host-Based ARP Spoofing Detectors Under Default-Gateway Poisoning**

After the latest deep novelty audit, a more precise title is now preferred:

> **A Behavioral Test Model for Host-Based ARP Spoofing Detectors Under Default-Gateway Poisoning**

Reason: model-based testing is already established. The actual candidate contribution is the **behavioral test model + oracle**, while established model-based testing techniques may be used to operationalize it.

Do not fully lock the final title yet, but the second wording is currently stronger.

---

## 3. Simplest explanation

If someone asks:

> “Ano ang thesis niyo?”

Use:

> **“Hindi kami gagawa ng bagong ARP detector. Gagawa kami ng behavioral test model na parang standardized test rulebook at answer key para systematically i-test ang existing host-based ARP spoofing detectors kapag ang victim’s default-gateway ARP mapping ay dumadaan sa controlled attack, recovery, legitimate gateway change, at detector/trust setup conditions.”**

If asked:

> “Ano ang CS contribution?”

Use:

> **“The application-specific behavioral test model, the ground-truth oracle, and detector profiles that map different detector setup/trust behaviors into reproducible black-box tests.”**

---

## 4. Exact network security scope

The experiment focuses only on the **victim host’s IPv4 ARP mapping for the default gateway**.

Normal:

```text
Gateway_IP → Legitimate_Gateway_MAC
```

Example:

```text
192.168.1.1 → AA:AA:AA:AA:AA:AA
```

Poisoned:

```text
192.168.1.1 → ATTACKER_MAC
```

The attacker makes the victim associate the legitimate default-gateway IP with the attacker’s MAC.

Scope exclusions:

- not the gateway/router’s own ARP table;
- not every LAN mapping;
- not IPv6 NDP;
- not DHCP spoofing;
- not generic MITM detection;
- not switch/router defenses.

Use the phrase **victim’s ARP table** in simple explanations.

---

## 5. Important SUT/title clarification

Not every detector under test must be specifically designed only for the default gateway.

A generic host-based ARP spoofing detector may be included if the experiment tests it specifically under **default-gateway poisoning**.

Therefore prefer:

> **host-based ARP spoofing detectors under default-gateway poisoning**

rather than:

> **host-based default-gateway ARP poisoning detectors**

because the latter implies every DUT is gateway-only.

---

## 6. Low-cost virtualized topology

Preferred setup:

```text
              Isolated Virtual LAN
                       |
            +----------+----------+
            |          |          |
         Victim     Attacker    Gateway
           VM          VM         VM
```

Use VirtualBox, VMware, or equivalent.

The Gateway VM may optionally have a second NAT adapter for Internet access, but Internet is not required.

Benefits:

- controlled MAC addresses;
- repeatable reset;
- snapshots;
- automation;
- isolation;
- controlled gateway replacement;
- inexpensive implementation.

No special hardware is required.

---

## 7. Secure ARP question already resolved

Secure ARP / S-ARP and similar authenticated ARP approaches already exist and may require PKI, signatures, protocol changes, trusted infrastructure, or coordinated deployment.

The current thesis assumes:

> **legacy IPv4 ARP where only the victim endpoint is under research control.**

This thesis does not replace Secure ARP. It asks how existing host-based ARP spoofing detectors can be systematically evaluated in ordinary unauthenticated ARP environments.

---

## 8. School / CS-domain fit

The uploaded school materials previously reviewed explicitly support areas such as:

- Cybersecurity Mechanisms;
- Intrusion Detection;
- Vulnerability Assessment;
- Computational Modeling and Simulation;
- Automated Testing;
- Intelligent Software Engineering and Computing Systems.

The school materials also allow contribution through development, evaluation, enhancement, or application of computational methods/models/algorithms/technologies.

The implementation/system should be the **vehicle**, not the sole contribution.

Therefore the current direction is strongly defensible as BSCS if framed around the behavioral model, oracle, test derivation, and systematic evaluation.

---

## 9. Ideas already rejected or downranked

Do not casually revive these:

- simple default-gateway MAC monitor;
- polling vs event-driven detector as novelty;
- short-duration poisoning as thesis centerpiece;
- generic active verification;
- voting/consensus;
- poisoned startup alone;
- “baseline inversion” as standalone novelty;
- context-aware re-baselining/history;
- generic false-positive reduction;
- generic recovery testing;
- new ARP state-machine detector;
- generic ARP testing framework;
- “novel coverage-guided MBT algorithm”;
- mutation testing as contribution.

---

## 10. Latest deep novelty audit — bottom line

A new aggressive research pass was done specifically to try to **kill the current topic**.

Searches covered combinations such as:

- ARP spoofing detector behavioral test model;
- ARP detector test oracle;
- default gateway detector testing framework;
- ARP spoofing lifecycle testing;
- state-transition testing ARP detector;
- model-based ARP security testing;
- host-based ARP detector evaluation;
- relevant theses, patents, commercial test suites, IDS testing frameworks, and recent 2025–2026 work.

### Result

> **No exact duplicate of the current thesis concept was identified.**

This does **not** prove no obscure work exists.

Safe wording remains:

> **“We have not identified…”**

not:

> **“No prior work exists.”**

Current rough qualitative confidence that the exact current gap is not obviously occupied:

> **about 8/10**

This is not a statistical probability.

---

## 11. Closest and most dangerous prior art

### Stateful / DES ARP detector work
Formal/state models inside ARP detectors already exist.

Consequence: state models for ARP are not novel.

### Active host-based ARP IDS
Active probing and multi-scenario evaluation already exist.

Consequence: “we test several scenarios” is not novel.

### 2019 client-side Bash gateway detector
Important because it separates:

1. saving trusted default-gateway IP/MAC;
2. later running the monitoring script.

Consequence: trust/reference establishment and monitor startup were already distinct in an existing detector architecture.

Do not claim we invented that distinction.

### WiSC, MobiCom 2021
Very dangerous prior art.

WiSC:

- monitors default gateway `(IP, MAC)`;
- considers initial compromise;
- recognizes that saved information may already contain the attacker MAC;
- uses historical/cross-connection context.

Consequence: do not claim novelty for poisoned-start awareness, client-side gateway history, or default-gateway consistency checking.

But WiSC is itself a detection/security system, not a reusable behavioral tester for heterogeneous ARP detectors.

### 2025 IEEE Access host/router ARP defense
Relevant trusted-baseline/snapshot and active-verification ideas.

### 2026 client-side gateway detector
Recent default-gateway detector using trusted/current MAC comparison, repeated mismatch confirmation, legitimate-change handling, and mitigation.

Consequence: simple gateway-detector space is saturated.

### User-side ARP spoofing patent
User-side gateway ARP detection and containment/alerting is already patented.

Consequence: endpoint-only gateway security is old.

### IWL ARP Test Suite
Automated ARP protocol/conformance/robustness testing already exists.

IWL asks roughly:

> “Does this ARP implementation behave correctly?”

The current thesis asks:

> “Given this controlled network/trust/lifecycle history, how does this ARP security detector behave?”

Different object under test.

### Generic IDS virtual testing frameworks
IDS-agnostic VM-based frameworks already exist.

Consequence: multi-detector virtual testing itself is not novel.

### Model-Based Security Testing literature
MBST is mature. Automatic security-test generation, formal models, and coverage/test-selection criteria are established.

### Mutation-based security testing
Mutation/fault-seeded assessment already exists.

Consequence: can only be an evaluation method.

### Stateful network-software sequence testing
Recent systems such as SeqFuzzSDN show that sequence-sensitive testing of stateful network software is established.

### Philippine undergraduate ARP thesis
A DLSU undergraduate ARP poisoning detector thesis (ARPoiDS) exists.

Consequence: never claim no Philippine BSCS thesis has addressed ARP spoofing.

---

## 12. What is definitely NOT novel

Do not claim novelty for:

```text
ARP spoofing
ARP detectors
host-based ARP detection
default-gateway monitoring
clean-start assumptions
poisoned initialization awareness
history/context
state machines
model-based testing
model-based security testing
automatic test generation
state coverage
transition coverage
transition-pair coverage
black-box testing
virtualized IDS testing
mutation/fault seeding
stateful network sequence testing
```

---

## 13. Current possible novelty — very narrow

After stripping away all established pieces, the surviving candidate contribution is:

> **a reusable, application-specific behavioral test specification and oracle for host-based ARP spoofing detectors under controlled victim default-gateway poisoning, with detector profiles that explicitly map different setup/reference and lifecycle semantics into one reproducible black-box evaluation process.**

Simpler:

> **the specific standardized test rulebook + answer key for this detector class.**

This is incremental novelty.

---

## 14. Safe research-gap wording

Use something close to:

> **Model-based security testing, automated test generation, state-transition coverage, virtual IDS testing, and host-based ARP spoofing detection are all established. However, in the literature reviewed so far, we have not identified a reusable behavioral test model and corresponding ground-truth oracle specifically for systematically evaluating heterogeneous host-based ARP spoofing detectors under controlled default-gateway poisoning while distinguishing network-binding transitions, detector-process lifecycle, and detector-specific trust/reference-establishment behavior.**

Never replace “have not identified” with “does not exist.”

---

## 15. Important modeling distinction

The current model explicitly separates:

1. **network/gateway state**;
2. **detector process lifecycle**;
3. **trust/reference establishment**.

This is useful and necessary for heterogeneous detectors.

Do **not** claim this separation itself was never used before.

Safe wording:

> **The proposed behavioral model makes these distinctions explicit for testing across heterogeneous detectors.**

---

## 16. Current Model v2

Core variables:

```text
G = legitimate gateway MAC
A = attacker MAC
O = MAC currently associated by victim with Gateway_IP
```

Invariant:

```text
A ≠ G
```

Derived conditions:

### BENIGN / CLEAN

```text
O = G
```

### ATTACK / POISONED

```text
O = A
```

Detector process:

```text
L ∈ {OFF, ON}
```

Avoid a universal hidden trusted-MAC variable because black-box DUTs may not expose internal state.

---

## 17. Model v2 event categories

### Network/environment events

```text
POISON
RESTORE
REPLACE
```

### Detector process events

```text
START
STOP
RESTART
```

### Optional setup/trust event

```text
ESTABLISH_REFERENCE
```

This applies only to detectors with explicit trusted-reference setup.

---

## 18. Critical event semantics

### POISON

Do not define POISON as merely editing the victim ARP cache.

Correct semantics:

**Action:** attacker sends forged ARP traffic claiming:

```text
Gateway_IP → Attacker_MAC
```

**Required postcondition:**

```text
O = A
```

before the event is considered successfully established.

Reason:

- packet-oriented detectors see forged ARP traffic;
- cache-oriented detectors see the poisoned mapping.

### RESTORE

Stop poisoning and re-establish legitimate ARP resolution.

Required postcondition:

```text
O = G
```

### REPLACE

Legitimately replace/change the gateway identity.

Recommended implementation:

```text
Gateway VM G1 / MAC1
→ administratively replace with
Gateway VM G2 / MAC2
```

Then verify the victim resolves the new legitimate MAC.

Do not rely on VRRP/HSRP as the primary example.

---

## 19. Why event order matters

Example:

```text
ESTABLISH_REFERENCE
→ POISON
→ START
```

versus:

```text
POISON
→ ESTABLISH_REFERENCE
→ START
```

Both may end with the detector running while the victim is poisoned, but the detector may have learned different trust information.

The thesis does not claim this phenomenon is newly discovered.

The behavioral model uses it as a sequence-sensitive testing dimension.

---

## 20. Primary evaluation scope — detection only

To keep the thesis manageable, the standardized primary output is:

```text
ALERT
NO_ALERT
```

Do not make mitigation correctness the universal evaluation target.

Different tools may alert, rewrite the ARP table, block MACs, or enforce static mappings.

Mitigation complicates the model and is outside the primary comparative scope.

---

## 21. Ground-truth oracle

The controlled environment knows:

```text
G = legitimate gateway
A = attacker
O = victim-observed gateway MAC
```

Objective ground truth:

```text
O = G
→ BENIGN

O = A
→ ATTACK
```

Detector output is normalized to:

```text
ALERT
NO_ALERT
```

---

## 22. Dual-layer oracle

Do not automatically call every benign alert a software bug.

### Layer 1 — Objective security-state behavior

| Ground truth | Detector output | Observation |
|---|---|---|
| ATTACK | ALERT | attack detected |
| ATTACK | NO_ALERT | attack missed |
| BENIGN | ALERT | benign-condition alert |
| BENIGN | NO_ALERT | quiet benign behavior |

### Layer 2 — Detector policy conformance

Ask whether observed behavior matches the detector’s documented intended policy.

A detector may intentionally warn on every gateway-MAC change. In that case `BENIGN + ALERT` may still conform to its design.

---

## 23. Detector profiles and adapters

Do not promise a zero-configuration “fully detector-agnostic” system.

Better wording:

> **detector-independent behavioral specification with detector-specific profiles/adapters.**

A profile specifies:

- startup/setup;
- applicable reference actions;
- restart semantics;
- observation window;
- alert recognition;
- documented expected policy.

Adapter output:

```text
ALERT
NO_ALERT
```

---

## 24. Current three DUT roles

### D1 — 2019 gateway-baseline reproduction
Persistent trusted default-gateway baseline.

Important property:

> reference establishment is separate from monitor startup.

Original maintained source was not located.

Must be described as:

> **reproduction of the published algorithm**

not the original program.

### D2 — 2026 gateway detector reproduction
Trusted gateway baseline + repeated mismatch confirmation + claimed legitimate-change handling/re-baselining.

Original public source was not located.

Mitigation should ideally be disabled or excluded because the thesis evaluates detection behavior.

### D3 — independent open-source active detector
Dynamic active verification and learning.

Important:

- independent open-source artifact;
- not gateway-only;
- can be tested specifically under default-gateway poisoning;
- process restart clears in-memory learned state, making restart relevant.

---

## 25. Why these DUTs are useful together

They represent different philosophies:

```text
D1 = persistent stored reference

D2 = stored reference + temporal confirmation / re-baselining

D3 = active verification + dynamic learning
```

The goal is not to benchmark every ARP detector.

The goal is to show the model can accommodate meaningfully heterogeneous designs.

---

## 26. DUT eligibility

A detector should:

1. run on/from the victim endpoint;
2. detect poisoning involving the default gateway;
3. expose machine-observable alert output;
4. work in the virtual environment;
5. have enough documentation/source behavior to define a profile;
6. not fundamentally prevent the modeled poisoned state from being established before observation.

Prevention-only systems are poor primary DUTs.

---

## 27. Observation windows

Different detectors have different timing behavior.

Define:

```text
W(D)
```

as the valid observation window for detector `D`.

Determine from:

- published configuration;
- documented polling interval;
- confirmation behavior;
- predefined calibration if necessary.

Procedure:

```text
apply event
↓
verify network postcondition
↓
start observation window
↓
collect detector output
↓
apply oracle
```

Detection latency may be recorded separately.

---

## 28. Model-based test generation

Established MBT techniques may be used to derive valid sequences.

Candidate adequacy criteria:

- transition coverage;
- transition-pair coverage;
- bounded path/sequence coverage.

Coverage method is **not the novelty**.

Reason for model-derived testing:

- systematic rather than ad hoc;
- reproducible;
- explicit event preconditions;
- history-sensitive traces;
- exact failing sequences.

---

## 29. Old “38 transition pairs” number is obsolete

Do not use the Model v1 claim of four states / six events / twelve transitions / 38 pairs as final methodology.

Model v2 includes detector profiles and explicit reference establishment.

Coverage counts must be recomputed after the model is frozen.

---

## 30. Optional fault-seeded validation

May be used secondarily.

Possible fault classes:

- missed attack;
- poisoned reference establishment;
- restart-related loss of detection;
- continued alert after recovery;
- incorrect benign-change behavior.

Mutation/fault seeding is existing methodology, not the contribution.

---

## 31. Expected research output

Do not report only aggregate accuracy.

Useful output looks like:

```text
Detector A:
passes START → POISON

misses:
POISON
→ ESTABLISH_REFERENCE
→ START
```

or:

```text
Detector B:
BENIGN ground truth
after REPLACE

Observed:
ALERT
```

The important knowledge product is:

> **which behavioral sequence produced which externally observable detector behavior.**

---

## 32. Why this differs from dataset benchmarking

A dataset benchmark may say:

> detector classified 98% of attack samples correctly.

The proposed behavioral model can say:

> detector works after clean initialization but behaves differently when trust was established while the victim was already poisoned.

Focus:

> **state/history-sensitive live behavior**, not just static packet/flow classification.

---

## 33. Current contribution statement

Preferred wording:

> **The primary proposed contribution is an application-specific behavioral test model and ground-truth oracle for evaluating host-based ARP spoofing detectors under controlled default-gateway poisoning. The model explicitly represents network-binding transitions, detector-process lifecycle, and detector-specific trust/reference-establishment actions where applicable. Established model-based test-generation and coverage techniques are then used to derive systematic reproducible tests through detector-specific profiles and output adapters.**

---

## 34. Current novelty assessment

- Generic methodology novelty: **none claimed**
- Application-specific novelty: **moderate, incremental, currently defensible**
- Exact duplicate found: **no exact duplicate identified**
- Risk of obscure/unindexed prior work: **still exists**
- Safe to claim “first ever”: **absolutely not**
- Worth continuing: **yes**

The latest deep audit produced enough confidence to stop searching for a completely different topic direction.

Future searching should be targeted citation-chaining / exact-close-work verification, not generic ARP brainstorming.

---

## 35. Current “do not claim” list

Never say:

- first ARP detector tester;
- first automated ARP testing;
- first model-based ARP security system;
- first state-machine ARP study;
- first poisoned-start evaluation;
- first black-box network security framework;
- first transition-coverage testing;
- no prior work exists;
- trust-establishment vs startup is our new discovery;
- stateful sequence testing is new.

---

## 36. Safe one-sentence gap

> **Existing work provides ARP detectors, ARP protocol test suites, general IDS testing frameworks, and established model-based security-testing techniques; our literature search has not yet identified a reusable behavioral test model and ground-truth oracle specifically for heterogeneous host-based ARP spoofing detectors under controlled default-gateway poisoning with explicit network, detector-lifecycle, and trust/reference-establishment semantics.**

---

## 37. Simple defense against “pinagsama lang existing”

If challenged:

> “Pinagsama niyo lang state machine, ARP, black-box testing, at MBT.”

Use:

> **“Yes, those individual techniques are established and we are not claiming otherwise. The contribution we are investigating is the application-specific behavioral specification and oracle for a narrowly defined detector class. Existing work we identified either builds ARP defenses, tests ARP protocol implementations, or provides general IDS/security testing; we have not yet identified the exact reusable detector-behavior abstraction we propose.”**

---

## 38. Current next step

The latest deep novelty audit supports **freezing the research direction**.

Next work should be refinement:

1. finalize exact title;
2. finalize research gap;
3. finalize contribution statement;
4. finalize research questions;
5. finalize general and specific objectives;
6. finalize scope and limitations;
7. finalize CS Domain / Computing Contribution / Expected Innovation;
8. finalize SDG / BU Agenda / beneficiary;
9. map everything into the official Topic Proposal Template.

Before locking final wording, do one last **citation-chain audit** on the closest works, especially:

- 2019 Bash gateway detector;
- WiSC 2021;
- IWL ARP Test Suite;
- general IDS virtual testing framework;
- MBST taxonomy;
- recent stateful network sequence testing;
- 2025–2026 ARP/default-gateway detector papers.

The goal of that audit is not to find a new topic, but to ensure the final wording does not overclaim novelty.

---

## 39. Current status in one paragraph

The thesis began as a search for a simple host-based ARP poisoning detector focused on the victim’s default-gateway mapping, but repeated literature audits showed that gateway-MAC monitoring, active verification, stateful detection, poisoned initialization awareness, history/context, legitimate-change handling, false-positive reduction, and related detector ideas already exist. The direction therefore shifted from building another detector to systematically testing existing host-based ARP spoofing detectors. Further research established that model-based security testing, automatic test generation, coverage criteria, mutation testing, black-box IDS testing, and stateful network sequence testing are also established, so none are claimed as novel. The surviving candidate contribution is much narrower: an application-specific behavioral test model and ground-truth oracle for host-based ARP spoofing detectors under controlled default-gateway poisoning, with explicit network-binding events, detector-process lifecycle, and detector-specific trust/reference-establishment semantics implemented through profiles/adapters. The experiment is detection-focused, fully virtualized, low-cost, and can use three contrasting detector strategies: a 2019 persistent-baseline reproduction, a 2026 temporal-confirmation/re-baselining reproduction, and an independent open-source active-verification detector. The latest deep prior-art audit found many close neighbors—including WiSC, IWL’s ARP test suite, generic IDS test frameworks, MBST literature, stateful network-software testing, patents, and a Philippine ARP thesis—but still did not identify an exact duplicate of the proposed behavioral model + oracle combination. The research direction is therefore currently worth freezing and refining, with incremental rather than revolutionary novelty.

---

## 40. Recommended continuation prompt

If this handoff is pasted into a new conversation:

> **“Continue from Handoff v4. Freeze the research direction and help me finalize the exact title, research gap, contribution, research questions, objectives, scope and limitations, expected innovation, CS domain, SDG/BU alignment, and beneficiary. Before locking the wording, do one last citation-chain check against the closest works. Do not restart generic ARP topic brainstorming unless an exact duplicate is found.”**
