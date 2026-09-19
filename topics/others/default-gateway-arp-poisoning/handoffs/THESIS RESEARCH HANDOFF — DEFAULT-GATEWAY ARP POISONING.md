# THESIS RESEARCH HANDOFF — DEFAULT-GATEWAY ARP POISONING

## 0. Instruction to the next AI

You are continuing a long thesis brainstorming and literature-audit session with a Computer Science student.

Do **not** restart from generic ARP-spoofing thesis suggestions. A large number of candidate ideas have already been considered, researched, and deliberately discarded because of prior art or weak novelty.

The goal is:

> Find a **simple, inexpensive, narrow, defensible Computer Science thesis contribution** related specifically to ARP poisoning of the **victim host's IPv4 default-gateway IP-to-MAC mapping**.

The user strongly prefers:
- simple implementation;
- no expensive hardware;
- no managed switch requirement;
- no SDN requirement;
- no ML/AI unless absolutely necessary;
- virtualization is preferred;
- a small contribution is acceptable;
- novelty claims must be conservative and heavily researched;
- the user is specifically worried about an adviser/professor saying **“meron na niyan.”**

The user values intellectual honesty over flashy novelty.

The current leading direction is **not a new ARP detector**. It is a **model-based black-box testing framework for existing host-based default-gateway ARP-poisoning detectors**.

Do not claim this is “the first ever.” Current safe wording is only:

> “We did not identify prior work that exactly matches this combination.”

Further literature verification is still required.

---

# 1. EXACT NETWORK SECURITY SCOPE

This scope is FIXED unless the user explicitly changes it.

We are interested only in the ARP entry inside the **victim host** corresponding to its IPv4 default gateway.

Normal victim ARP table:

    Gateway IP       Gateway MAC
    192.168.1.1  →   AA:AA:AA:AA:AA:AA

During ARP poisoning:

    192.168.1.1  →   ATTACKER_MAC

The attacker is falsely associating the legitimate default-gateway IP address with the attacker's MAC address in the **victim's local ARP cache/table**.

We are NOT primarily studying:
- poisoning of the router's own ARP table;
- every IP-MAC mapping on the LAN;
- IPv6 Neighbor Discovery;
- DNS spoofing;
- DHCP spoofing;
- Wi-Fi deauthentication;
- general MITM attacks;
- SDN-wide protection;
- enterprise Dynamic ARP Inspection;
- router firmware modification;
- managed switch solutions.

The protected object is specifically:

> **Victim's IPv4 default-gateway IP → MAC binding**

---

# 2. IMPORTANT TERMINOLOGY ALREADY CLARIFIED

The user initially got confused by “neighbor table.”

For this discussion, prefer the simpler term:

> **Victim's ARP table**

Linux calls the broader structure a “neighbor table,” but that does NOT mean computers broadcast or share their whole ARP tables with other LAN hosts.

Each host maintains its own local ARP/neighbor state.

ARP messages travel across the LAN; the ARP table itself is local.

Do not unnecessarily use “neighbor table” unless discussing an OS API.

---

# 3. DEPLOYMENT / COST CONSTRAINTS

The entire thesis should ideally be performable through virtualization.

No physical networking hardware is required.

Preferred conceptual topology:

                 Virtual LAN
                     |
          +----------+----------+
          |          |          |
       Victim     Attacker    Gateway
         VM          VM         VM

VirtualBox, VMware, or comparable virtualization can be used.

A dedicated virtual LAN / Internal Network is preferable to making the hypervisor's built-in NAT engine the gateway-under-test.

Possible design:

- Victim VM → Internal Network
- Attacker VM → same Internal Network
- Gateway VM → same Internal Network
- Gateway VM may have a second NAT adapter if Internet access is desired, but Internet is not required for the experiment.

Important:
- Linux is NOT inherently required because this is an ARP thesis.
- Linux was previously discussed only because some implementation mechanisms are convenient there.
- The final testing-framework idea should ideally remain conceptually detector/OS agnostic where practical.
- No Raspberry Pi, Cisco switch, SDN controller, GPU, cloud VM, or special hardware should be necessary.

---

# 4. SECURE ARP HAS ALREADY BEEN DISCUSSED

The user correctly asked:

> “If Secure ARP already exists, why do this research at all?”

Relevant conceptual answer:

Secure-ARP-type proposals such as S-ARP attempt to solve ARP authentication more fundamentally, e.g. using cryptographic authentication/public-key infrastructure.

However, such approaches generally require deployment/support beyond a single victim host:
- protocol modifications or extensions;
- certificates / PKI;
- participating hosts;
- network infrastructure support;
- trusted servers;
- specialized mechanisms.

Therefore our intended environment is explicitly:

> **legacy/ordinary IPv4 LAN using standard unauthenticated ARP, where the victim can control only itself and cannot modify the gateway, other hosts, or switching infrastructure.**

This is a crucial scope/motivation sentence.

Do NOT argue that Secure ARP is bad or ineffective.

The distinction is:

**Protocol/infrastructure solution:**
Fix/authenticate ARP ecosystem.

**Our niche:**
What can be tested/protected when only the endpoint is under our control and ordinary ARP remains deployed?

Secure ARP therefore does NOT automatically invalidate the scope.

---

# 5. IDEAS ALREADY CONSIDERED AND DISCARDED / DOWNRANKED

Do NOT casually suggest these again without substantially new evidence.

## 5.1 Simple gateway-MAC monitor
Example:

    save initial gateway MAC
    periodically compare
    if changed → alert

STATUS: RED / ALREADY DONE.

There are multiple host/client-side approaches already doing this.

This is NOT enough contribution.

---

## 5.2 Polling versus event-driven monitoring

Previous candidate:

> Instead of checking the ARP table every N seconds, listen for OS-generated table-change events.

STATUS: DROPPED.

Reason:
- OS event notification is largely an implementation mechanism.
- Could be seen as engineering rather than a meaningful research contribution.
- “Short poisoning might happen between polling intervals” felt too common-sense and weak as a thesis question.

Do not return to this unless a genuinely non-obvious research gap is found.

---

## 5.3 Short-duration / low-duration poisoning

Question previously considered:

> Can short-duration poisoning occur between detector polling observations?

STATUS: DROPPED as primary research question.

User explicitly disliked it because the answer feels predictable/common-sense.

---

## 5.4 Generic active verification

Ideas like:
- send ARP probes;
- send ICMP probes;
- actively verify conflicting mappings;
- detect multiple MACs claiming one IP.

STATUS: RED / substantial prior art.

Active host-based ARP verification has existed for many years.

Do not propose “active verification” by itself as novelty.

---

## 5.5 Voting / asking other hosts which MAC is genuine

STATUS: RED.

MR-ARP and later voting-based schemes already explored this.

Recent voting-based ARP proposals also exist.

Not safe novelty.

---

## 5.6 Poisoned-start problem by itself

Problem:

If detector starts after victim has already been poisoned:

    Gateway IP → ATTACKER_MAC

and detector simply saves the current mapping as trusted:

    trusted_mac = ATTACKER_MAC

STATUS: REAL PROBLEM, BUT NOT SUFFICIENT AS THESIS NOVELTY.

Recent papers explicitly assume a clean initial state or acknowledge trusted-baseline initialization issues.

Also older active schemes already avoid dependence on a static clean baseline.

So:
- useful threat condition;
- useful benchmark test case;
- NOT enough as standalone contribution.

---

## 5.7 “Baseline inversion”

Working concept previously explored:

If attacker MAC is learned as trusted at startup, after attacker disappears and real gateway returns, detector might treat the real gateway as anomalous.

STATUS: Interesting FAILURE SEQUENCE, but not sufficiently safe as standalone novelty.

Keep it as a possible **test sequence** inside the eventual framework.

Do NOT build the thesis title around the term “baseline inversion” unless experimentally established and literature-verified.

---

## 5.8 Context-aware re-baselining

Question:

> When gateway MAC changes, can local context decide whether new MAC is legitimate?

STATUS: DOWNRANKED / prior art too close.

Historical gateway bindings, network context, trust histories, re-learning, etc. have already appeared in prior work/tools/patents.

Not safe as primary contribution.

---

## 5.9 Generic trust-strategy comparison

Possible comparison:
- manually configured known-good MAC;
- learn-at-startup;
- active verification.

STATUS: DOWNRANKED.

Comparative ARP-security studies already exist broadly.

Could become “just another comparison study.”

---

## 5.10 Legitimate gateway-MAC transitions / false positives

Previously considered:

> Evaluate detectors when the legitimate gateway MAC changes.

STATUS: Important test condition, but NOT novel by itself.

Older host-based ARP literature already documented problems with genuine IP-MAC changes and false positives.

Also be technically careful:

Do NOT casually use VRRP/HSRP failover as proof that a gateway's host-facing MAC necessarily changes.

Standard VRRP/HSRP commonly uses a virtual MAC specifically so failover remains transparent to hosts.

Better legitimate MAC-change examples:
- actual router replacement;
- virtual NIC replacement;
- administrative gateway reconfiguration;
- real gateway device/NIC replacement.

Legitimate transition handling may still be included in tests, but cannot itself be claimed as the novel discovery.

---

## 5.11 “New state-machine ARP detector”

STATUS: RED.

Stateful / DES / formal ARP detectors have existed for years.

State machine by itself is NOT novel.

---

## 5.12 Generic “ARP benchmark”

STATUS: TOO BROAD.

ARP datasets, testbeds, comparative studies, protocol test suites, security-assessment tools, and IDS frameworks already exist.

If pursuing evaluation, it must be far more narrowly defined.

---

# 6. IMPORTANT PRIOR ART / DANGER LIST

The next AI should treat these as mandatory related-work categories.

Bibliographic details must be re-verified before formal citation.

## A. S-ARP / Secure ARP
Classic cryptographically authenticated ARP proposal around 2003.

Relevance:
Shows ARP authentication itself is an old research area.

Does NOT kill our legacy-host-only scope because deployment assumptions differ.

---

## B. Stateful ARP / fuzzy stateful ARP work (~2007)
Relevant because it already treats ARP behavior as stateful and addresses network-change handling.

Implication:
Do not claim novelty from using state machines/states.

---

## C. Comparative ARP security studies (~2009/2010)
Studies have already compared existing ARP-security mechanisms.

Implication:
“Comparing detectors” alone is insufficient.

---

## D. Active host-based ARP IDS (~2011)
Relevant characteristics:
- host-based;
- active verification;
- multiple attack scenarios;
- may avoid static IP-MAC mappings;
- recognizes difficulty distinguishing conflicting claims;
- discusses genuine mapping-change behavior.

Implication:
Do not claim active verification, multiple-scenario testing, or lack of static baseline as new.

---

## E. Discrete Event System / state-model ARP IDS (~2011)
Uses formal/state models inside the IDS.

Implication:
State-machine ARP detection is not new.

Critical distinction for our current proposal:
Their model is part of the DETECTOR.

Our candidate model would be outside the detector as a TESTER.

---

## F. 2019 client-side Bash gateway protection
Relevant characteristics:
- client-side;
- saves default-gateway IP/MAC;
- later monitors it.

Implication:
Simple gateway-MAC baseline monitoring is definitely not new.

---

## G. WiSC — MobiCom 2021
VERY IMPORTANT.

WiSC already:
- operates client-side;
- records/checks default gateway `(IP, MAC)`;
- considers connection establishment;
- considers possibility of existing compromise;
- uses historical/cross-connection context to improve security/precision.

Implication:
Do NOT claim novelty from:
- default-gateway-only client-side consistency;
- startup-compromise awareness;
- remembered history/context.

This paper is dangerous prior art and should be thoroughly read.

---

## H. ASD / false-positive-aware ARP detection (~2022)
Relevant because prior work explicitly studies false-positive issues and benign VM/network behavior.

Implication:
Do not claim “nobody evaluates false positives.”

---

## I. Recent voting-based ARP work (~2024)
There are modern voting/consensus schemes for resolving suspect mappings.

Implication:
“Determine genuine MAC through voting” is not new.

---

## J. 2024 SDN ARP detection/mitigation work
Some work measures network behavior before/during/after attack.

Implication:
Do not claim “nobody studies post-attack recovery.”

However, network-performance recovery is different from testing the correctness of a host detector's gateway decision state.

---

## K. 2025 IEEE Access host/router ARP-spoofing detector
Relevant characteristics reportedly include:
- host-side router/default-gateway focus;
- initial router MAC snapshot or manual entry;
- assumption that initial state should not already be poisoned;
- multiple host-side mechanisms.

Implication:
Trusted-initial-gateway assumption and poisoned-start issue are known.

---

## L. 2026 IJERT client-side default-gateway detector
VERY IMPORTANT because it is extremely close to the user's original simple idea.

Reported characteristics:
- Linux/client side;
- monitors trusted default gateway MAC;
- trusted MAC saved during initialization;
- polling around every 3 seconds;
- requires consecutive mismatches;
- automatic mitigation;
- VirtualBox-based evaluation;
- reports very low/zero false positives in a small number of trials;
- includes an abstract step resembling “check for legitimate gateway change.”

Implication:
A simple lightweight client-side default-gateway detector is not novel.

This paper is useful as an example of why standardized behavioral testing may matter.

---

## M. IWL ARP protocol test suite
Commercial ARP test suite reportedly with dozens of RFC-oriented tests.

Tests:
- ARP protocol implementation;
- conformance;
- robustness.

Implication:
Cannot claim “first automated ARP test suite.”

Key distinction:
It tests ARP protocol implementations, NOT necessarily ARP-security detectors as black boxes.

---

## N. SCADA IDS test frameworks
Some IDS evaluation frameworks include ARP spoofing as one attack among many.

Implication:
Cannot claim “first security testing framework to include ARP spoofing.”

---

## O. DELTA / SDN security assessment frameworks
Automated security assessment frameworks exist and may include ARP spoofing.

Implication:
“Automated security evaluation” itself is not novel.

---

## P. raw-packet / Network Security Check tooling
Open-source network-security checking utilities can automate ARP-spoofing-related vulnerability tests.

Implication:
Cannot claim “first automated ARP-security tester.”

---

# 7. IMPORTANT RESEARCH CORRECTIONS ALREADY MADE

The next AI must preserve these corrections.

## Correction 1
A previously mentioned 2021 review phrase about “no universally accepted benchmark scheme” may have referred to lack of a universally accepted DEFENSE scheme, not lack of a testing benchmark.

DO NOT use this source as proof that no ARP testing benchmark exists without re-reading and verifying the exact wording.

---

## Correction 2
Do not claim:
> “VRRP/HSRP failover normally changes the gateway MAC seen by hosts.”

That is technically unsafe.

Virtual router redundancy protocols commonly maintain a virtual MAC specifically to preserve the default gateway identity across failover.

---

## Correction 3
Do not claim:
> “No prior research evaluates recovery.”

There is prior work measuring post-attack recovery/network state.

Our potential distinction is specifically:
**behavioral/trust decision correctness of a host-based gateway detector across controlled transitions.**

---

## Correction 4
Do not claim:
> “Nobody evaluates false positives.”

False-positive-aware ARP work exists.

---

## Correction 5
Do not claim:
> “Nobody studies poisoned startup.”

Clean-start assumptions and initial-compromise problems are already visible in prior work.

---

# 8. CURRENT LEADING THESIS DIRECTION

Current candidate title:

> **A Model-Based Black-Box Testing Framework for Host-Based Default-Gateway ARP Poisoning Detectors**

Alternative:

> **Model-Based Black-Box Evaluation of Host-Based Default-Gateway ARP Poisoning Detectors**

Avoid “robustness” unless precisely defined.

The contribution is NOT a new detector.

The object under test is an existing or representative host-based ARP-poisoning detector.

The proposed framework would:

1. model legitimate and malicious states of the victim's default-gateway ARP binding;
2. generate valid event/test sequences from that model;
3. execute them in a reproducible virtual LAN;
4. observe the detector's externally visible behavior;
5. compare that behavior with a ground-truth oracle;
6. produce PASS/FAIL and metrics.

---

# 9. EXACT NOVELTY BOUNDARY CURRENTLY CONSIDERED DEFENSIBLE

Unsafe claim:

> “No ARP testing framework exists.”

FALSE / unsupported.

Unsafe claim:

> “No state-based ARP research exists.”

FALSE.

Unsafe claim:

> “No host-based gateway ARP detector exists.”

FALSE.

Unsafe claim:

> “No automated ARP security testing exists.”

FALSE.

Unsafe claim:

> “No one compares ARP detectors.”

FALSE.

Current conservative gap statement:

> **Although host-based ARP-spoofing detectors, state-based ARP defenses, protocol test suites, and broader IDS/security evaluation frameworks already exist, we did not identify a detector-agnostic model-based testing framework that systematically generates and evaluates behavioral state-transition scenarios specifically for the victim host's IPv4 default-gateway IP-to-MAC binding.**

This is the best current formulation.

DO NOT upgrade “we did not identify” to “none exists” without stronger evidence.

---

# 10. WHY “BLACK-BOX” MATTERS

Different detectors have different implementations.

Some:
- only raise an alert;
- print an attacker MAC;
- restore an ARP entry;
- block a MAC address;
- modify firewall state;
- expose an internal trusted MAC;
- do not expose an internal trust state at all.

Therefore the universal framework should NOT require access to detector internals.

Earlier variables:

    G = actual legitimate gateway MAC
    O = victim-observed gateway MAC
    T = detector's internally trusted MAC
    D = detector decision

were refined.

Better universal model:

    G = actual legitimate gateway ground truth
    O = victim's observed/default-gateway ARP mapping
    V = externally observable detector verdict/action

Optional only when exposed:

    T = detector's internal trusted gateway MAC

The universal oracle should primarily evaluate external behavior.

Possible observations:
- Did it alarm?
- Did it incorrectly alarm?
- Did mitigation restore victim's mapping to G?
- Did it block G?
- Did victim remain mapped to attacker?
- Did detector become silent after recovery?
- Did detector behave correctly after restart?

This makes the framework genuinely closer to black-box testing.

---

# 11. PROPOSED MODEL-BASED TESTING CONCEPT

Model-based testing itself is NOT novel.

The application-specific behavioral model + test oracle + detector adapter are the candidate contribution.

Possible environment states:

### NORMAL
Actual gateway and victim-observed mapping agree.

    G = A
    O = A

### POISONED
Actual gateway remains A, but victim maps gateway IP to attacker X.

    G = A
    O = X

### LEGITIMATE_REPLACEMENT
Legitimate gateway identity changes.

    G: A → B
    O eventually → B

### RECOVERED
Attack disappears and legitimate mapping is restored.

    G = A
    O = A

Potentially also distinguish:
- detector running;
- detector stopped/restarted.

Do not overcomplicate the state space initially.

---

# 12. PROPOSED EVENTS

Small event alphabet could include:

    START        = start detector
    STOP         = stop detector
    RESTART      = restart detector

    POISON       = make victim map gateway IP to attacker MAC

    RESTORE      = restore legitimate gateway mapping

    REPLACE      = legitimate gateway replacement / MAC change

Potentially:
    RESET        = return experiment to known clean baseline

Not every sequence is legal.

The framework should maintain a transition relation so it only generates meaningful paths.

---

# 13. AUTOMATIC TEST-SEQUENCE GENERATION

This is a possible small algorithmic CS component.

Represent valid states/transitions as a directed graph / finite-state machine.

Then use simple BFS or DFS to generate all valid paths up to depth `k`.

Example valid sequences:

    START → POISON → RESTORE

Normal startup, attack, recovery.

    POISON → START → RESTORE

Detector starts while victim is already poisoned.

    START → REPLACE

Legitimate gateway replacement.

    START → REPLACE → POISON → RESTORE

Legitimate replacement, then poisoning, then recovery.

    POISON → START → RESTORE → POISON

Compromised initialization, recovery, second attack.

Important:
The novelty is NOT BFS/DFS.

The possible contribution is the specific test model and systematic model-derived coverage of detector behavior.

---

# 14. GROUND-TRUTH ORACLE

This is one of the stronger proposed components.

Because the framework controls the Gateway VM and Attacker VM, it knows:

> Which MAC is actually the legitimate gateway at each step?

Therefore it can compare detector behavior with the known truth.

Example:

Ground truth:
    G = AA

Victim observed:
    O = XX

Detector:
    NO ALERT

Oracle:
    FAIL

After recovery:

    G = AA
    O = AA

Detector still blocks AA.

Oracle:
    FAIL

This is more informative than a simple packet-classification accuracy score.

---

# 15. POSSIBLE METRICS

Keep metrics narrow and meaningful.

Potential universal metrics:

## Attack Detection Rate
Did detector correctly respond while O represented attacker rather than G?

## False Alarm Rate
Did detector signal an attack during modeled benign states?

## Recovery Correctness
After attack termination, did the externally observable system/detector behavior return to a correct benign state?

## Incorrect Mitigation Rate
Did the detector block or reject the legitimate gateway?

## State-Sequence Pass Rate
How many generated valid sequences were completed without violating expected behavioral properties?

## Detection latency
Optional.

## Resource overhead
Optional, secondary only.

Avoid inventing meaningless scores simply to make the thesis look mathematical.

---

# 16. POSSIBLE TEST ORACLE PROPERTIES

Examples only; should be formally refined.

### Security property
When victim's gateway mapping is attacker-controlled, the detector should not silently accept the condition indefinitely.

### Benign property
During a purely legitimate sequence, the detector should not permanently classify the legitimate gateway as malicious.

### Recovery property
After the attack ends and legitimate gateway mapping is restored, mitigation should not leave the victim unable to communicate with the legitimate gateway.

### Initialization property
Detector startup under an already-poisoned state should have a defined observable outcome rather than being silently assumed clean.

These properties must be adjusted based on the advertised behavior of each detector.

Do NOT force every detector to implement the same internal trust mechanism.

---

# 17. IMPORTANT ARCHITECTURAL ISSUE: DETECTOR ADAPTER

Because each detector outputs different things, the framework likely needs an adapter/interface.

Concept:

    Test model
        ↓
    Experiment controller
        ↓
    Virtual network
        ↓
    Detector under test
        ↓
    Detector adapter
        ↓
    normalized observable verdict/action
        ↓
    Oracle
        ↓
    PASS / FAIL

Possible normalized output categories:

    ALERT
    NO_ALERT
    MITIGATION_ACTIVE
    MITIGATION_INACTIVE
    LEGITIMATE_GATEWAY_REACHABLE
    LEGITIMATE_GATEWAY_BLOCKED

Do not overdesign this before selecting concrete detectors to evaluate.

---

# 18. MINIMUM PROTOTYPE ENVIRONMENT

Virtualized environment should remain cheap and reproducible.

Possible:

Host computer
    |
    VirtualBox / VMware
    |
    +-- Victim VM
    +-- Attacker VM
    +-- Gateway VM

All connected to isolated virtual LAN.

Optional automation scripts can:
- configure/reset MAC addresses;
- start/stop detector;
- induce controlled poisoning;
- restore correct gateway state;
- restart VMs/processes;
- capture ARP state;
- collect detector output;
- timestamp transitions;
- score tests.

Important:
Attack activity must remain inside isolated lab environment.

---

# 19. WHY THIS IS COMPUTER SCIENCE RATHER THAN JUST A CYBERSEC DEMO

Potential CS contributions:

### A. Behavioral model
Formal finite-state representation of relevant gateway-binding and detector-lifecycle states.

### B. Test-generation procedure
Automatically derive valid test sequences from the model.

### C. Black-box adapter/oracle architecture
Normalize observable detector behavior and automatically determine PASS/FAIL against ground truth.

### D. Reproducible evaluation artifact
Same tests can be applied to multiple detector implementations.

This makes the thesis closer to:

> software testing + network security

rather than:

> “we ran an ARP spoofing tool and watched Wireshark.”

---

# 20. WHAT MUST NEVER BE CLAIMED AS THE CONTRIBUTION

Do NOT say:

> “We invented ARP spoofing detection.”

Do NOT say:

> “We invented host-based protection.”

Do NOT say:

> “We invented gateway-MAC monitoring.”

Do NOT say:

> “We invented state machines for ARP.”

Do NOT say:

> “We invented model-based testing.”

Do NOT say:

> “We invented ARP security testing.”

Do NOT say:

> “We invented automated ARP attacks.”

Do NOT say:

> “We are the first to test multiple attack scenarios.”

Do NOT say:

> “No one studies recovery.”

Do NOT say:

> “No one studies false positives.”

Do NOT say:

> “No ARP benchmark exists.”

The possible contribution is the narrow combination:

> **an application-specific black-box model, generated state-transition tests, and ground-truth oracle for host-based detectors protecting the victim's IPv4 default-gateway ARP mapping.**

---

# 21. CURRENT CONFIDENCE ASSESSMENT

After several research passes:

Generic ARP detection is already mature:
    Confidence: 10/10

Host-based default-gateway detection already exists:
    Confidence: 10/10

State-based ARP defenses exist:
    Confidence: 10/10

Active ARP verification exists:
    Confidence: 10/10

Comparative ARP evaluations exist:
    Confidence: 10/10

Generic security/IDS test frameworks exist:
    Confidence: 10/10

Automated ARP/security testing tools exist:
    Confidence: 10/10

Exact candidate:
“detector-agnostic model-based black-box tester specifically for victim default-gateway ARP binding”
not found so far:
    Confidence that no exact match was identified: roughly 7.5/10

Safe enough to show an adviser as a CANDIDATE research gap:
    roughly 8–8.5/10

Safe enough to claim “first ever”:
    very low confidence.
    DO NOT CLAIM IT.

---

# 22. WHY THE USER ASKED FOR ANOTHER DEEP RESEARCH PASS

The user explicitly has a trust concern and wants to be reassured that the thesis direction will not collapse when a professor says:

> “Meron na niyan.”

The correct response style going forward is:

- aggressively search for prior art;
- try to kill the idea rather than defend it emotionally;
- explicitly correct previous mistakes;
- distinguish “not found” from “does not exist”;
- avoid hype;
- explain why near prior art does or does not invalidate the exact contribution.

The user appreciates when weak ideas are discarded early.

---

# 23. NEXT REQUIRED STEP

Do NOT immediately write Chapter 1.

Do NOT finalize the title yet.

The next step should be a **formal related-work / novelty audit** centered on the current candidate.

Build a matrix including approximately 15–30 highly relevant works.

Suggested columns:

| Work | Year | Host-based? | Default-gateway-specific? | Detection or testing? | State model? | Model inside detector or external tester? | Automated test generation? | Ground-truth oracle? | Black-box? | Startup-compromise case? | Recovery tests? | Benign transitions? | Extra infrastructure? | Key limitation relative to our idea |

Priority works/categories:
- S-ARP
- Stateful ARP
- active host-based HIDS
- DES/state-model ARP detection
- comparative ARP-security studies
- 2019 client-side gateway Bash approach
- WiSC 2021
- false-positive-aware ARP detectors
- 2024 voting approaches
- 2025 IEEE Access host/router method
- 2026 IJERT client-side gateway detector
- IWL ARP protocol test suite
- SCADA IDS test frameworks
- DELTA or similar automated security assessment
- raw-packet/network security testing utilities
- ARP-specific datasets/benchmarks
- any dissertations/theses specifically mentioning:
  - model-based ARP testing
  - ARP test oracle
  - state-transition ARP detector testing
  - gateway-binding detector benchmark
  - black-box ARP IDS testing

Search not only journals:
- IEEE
- ACM
- Springer
- Elsevier
- arXiv
- university repositories
- theses/dissertations
- patents
- GitHub/open-source
- commercial security-testing tools
- non-English literature if discoverable.

The critical search question is:

> **Has someone already built a detector-agnostic behavioral/model-based test harness that generates valid gateway-binding state sequences and uses known gateway ground truth to evaluate host-based default-gateway ARP-poisoning detectors?**

If YES:
Kill or narrow current idea.

If NO after citation chaining:
Proceed to adviser-ready formulation.

---

# 24. POSSIBLE ADVISER PITCH — CURRENT DRAFT

Do not present as final novelty claim.

Potential concise pitch:

> “Our thesis does not propose another ARP-spoofing detector. We focus only on host-based detectors that protect the victim's IPv4 default-gateway ARP mapping in ordinary legacy LANs. Existing detectors use different assumptions and evaluation scenarios, so we want to develop a model-based black-box test framework that generates valid gateway-state transitions, runs them reproducibly in a virtual LAN, and uses known gateway ground truth to determine whether a detector's externally observable behavior is correct. Our current literature search found protocol test suites, ARP detectors, state-based defenses, comparative studies, and general IDS test frameworks, but we have not yet identified one that combines these elements for this exact detector class.”

That is the current best adviser-facing explanation.

---

# 25. IF THE ADVISER REQUIRES A “NEW ALGORITHM”

Do NOT immediately invent another ARP detector.

Instead, the algorithmic component can remain on the SOFTWARE TESTING side:

- finite-state behavioral model;
- valid transition generation;
- coverage-based sequence selection;
- oracle evaluation;
- possibly test minimization.

Example:

Given state graph M and depth k:

1. traverse reachable valid transitions using BFS/DFS;
2. generate unique test traces;
3. execute trace;
4. compare observed verdict/action against oracle;
5. record violations;
6. optionally minimize failing trace.

This provides an algorithmic CS component without pretending to solve ARP authentication itself.

A potentially interesting extension, only if needed:

> **minimal failing sequence generation**

Example:

Instead of saying detector failed in a 12-step test, framework reduces failure to:

    POISON → START → RESTORE

This resembles debugging/model-based testing and could strengthen the CS contribution while staying simple.

But this is NOT yet researched enough to claim as novel.

---

# 26. PRINCIPLE THAT HAS GUIDED THE ENTIRE DISCUSSION

The most important insight:

> **ARP poisoning is the experimental threat, not automatically the thesis contribution.**

The contribution must be something more specific:
- testing model;
- evaluation methodology;
- oracle;
- test generation;
- experimentally demonstrated limitation;
- or another narrowly defined CS artifact.

The user does NOT want a flashy cybersecurity title with weak novelty.

Simple + rigorous + clearly delimited is preferred.

---

# 27. CURRENT STATUS IN ONE SENTENCE

We have moved from “build an ARP detector” to:

> **Investigate whether a model-based black-box testing framework for host-based detectors protecting only the victim's IPv4 default-gateway ARP binding can provide a small but defensible CS contribution through an external behavioral model, automated valid test-sequence generation, and a ground-truth oracle—while explicitly distinguishing this from existing ARP detectors, state-based defenses, protocol test suites, comparative studies, and general IDS-testing frameworks.**

This is the point from which the next AI should continue.