# HANDOFF — BSCS Thesis Research on MAC Randomization / DHCPv4
**Prepared for continuation in a new ChatGPT conversation**
**Date of handoff:** 2026-08-07

---

## 0. HOW TO USE THIS HANDOFF

This document is intended to let a new AI continue the thesis work with as little loss of context as possible.

The user is a **Bachelor of Science in Computer Science (BSCS)** student working on **Thesis 1 / CS 124**. The user wants a thesis topic that is:

- **Low to zero cost**
- **Simple**
- **Feasible**
- **Manageable**
- **Defensible**
- Closely related to something the user already understands and is comfortable defending: **MAC address changing / MAC randomization / MAC spoofing concepts**
- The user explicitly prefers **deep research quality over speed** and is okay with very long research passes before committing to a title or research gap.

The prior conversation deliberately used a **“kill-test” approach**:
1. Generate candidate directions.
2. Deep-research them.
3. Actively try to disprove the assumptions and novelty.
4. Reject broad or already-saturated ideas.
5. Keep only directions that survive feasibility, novelty, cost, and defense checks.

The current strongest direction is **NOT a MAC changer application** and **NOT generic MAC spoofing detection**. It is a **computational modeling + emulation study of DHCPv4 resource utilization under randomized/changing MAC address behavior**.

The next AI should **continue cautiously**. Do not claim a universal research gap until the exact gap is independently revalidated.

---

# 1. USER CONTEXT AND WORKING PREFERENCES

### User's thesis priorities
The user wants a thesis that is:
- low/zero additional financial cost;
- implementable on an ordinary laptop if possible;
- not dependent on paid APIs, cloud GPUs, Raspberry Pi, specialized Wi-Fi NICs, or institutional data;
- not overly ambitious;
- technically understandable enough to defend confidently;
- a genuine **Computer Science research project**, not just a CRUD/software application;
- supported by real literature and standards;
- not based on fake novelty claims.

### User's knowledge comfort zone
The user said their initial field of interest is **anything about a MAC changer**, because that is something they understand and feel confident defending.

Interpret this as the family of topics around:
- MAC address changing
- MAC spoofing
- MAC randomization
- randomized/changing MAC (RCM)
- network identity
- DHCP behavior under changing L2 identities
- Wi-Fi privacy/device identity

Do not force the thesis into a completely unrelated area unless this direction is eventually disproven.

### Research style requested by user
The user explicitly said:
> deep research is okay even if it takes a very long time, as long as quality is high.

So future work should:
- prioritize standards and peer-reviewed sources;
- distinguish standards, peer-reviewed papers, patents, vendor docs, preprints, and inference;
- correct earlier assumptions when evidence contradicts them;
- avoid premature title finalization.

---

# 2. PRIMARY THESIS GUIDES PROVIDED BY THE USER

The user uploaded three official/course files. If they are not available in the new conversation, ask the user to re-upload them before drafting formal proposal sections.

## File 1
**Thesis_Domains_CS.pdf**

Core requirements extracted from the file:

### General principle
A BSCS thesis must primarily contribute to **computing knowledge** through development, evaluation, enhancement, or application of:
- computational methods,
- intelligent models,
- algorithms,
- architectures,
- emerging computing technologies.

A software application is only the **vehicle** for implementing/evaluating the computing contribution.

### Acceptable substantial CS components include
- Algorithm development/optimization
- AI / ML / Deep Learning
- NLP
- Computer Vision
- Data Analytics / Predictive Modeling
- Knowledge Representation / Reasoning
- Intelligent Decision Support
- Recommender Systems
- Cybersecurity Mechanisms
- Blockchain
- Distributed Computing
- Cloud / Edge Computing
- IoT Intelligence
- HCI
- Computational Modeling and Simulation
- Computational Science Applications
- Emerging Computing Technologies

### Non-qualifying by themselves
Generic:
- student information systems,
- enrollment,
- payroll,
- inventory,
- POS,
- library systems,
- reservation systems,
- e-commerce,
- general apps,
- general databases,
- portals,
- business information systems.

### Relevant approved domains for this thesis direction
- **Cybersecurity and Digital Forensics**
- **Computational Modeling and Simulation**
- potentially **Data Analytics**
- potentially **Intelligent/Computing Systems**

### Required proposal alignment fields
Every proposal title should explicitly indicate:
- **CS Domain**
- **Computing Contribution**
- **BU Agenda**
- **SDG**
- **Beneficiary**
- **Expected Innovation**

### BU Research Agenda categories potentially relevant
For the current candidate:
- **Institutional Development and Policy Innovation**
Possibly also:
- Global Competitiveness of Business and Industry
but Institutional Development is the cleaner fit for university/guest network administration.

### Likely SDG
- **SDG 9 — Industry, Innovation and Infrastructure**

---

## File 2
**Topic_Proposal_Template_CS.pdf**

Important format and expectations:

### Recommended title structure
**[Computing Technique/Approach] + [Problem Being Solved] + [Application Domain]**

### Proposal content flow
1. Proposed Title
2. Required alignment fields
3. Background
4. Introduction of the Proposed System/Solution
5. General Objective
6. Specific Objectives
7. Scope and Limitations

### Background must contain
- Context and relevance
- SDG / BU agenda / priorities
- Existing challenges and research gaps
- Opportunities and proposed computing approach
- Discussion of computing components
- Concluding synthesis

### Important warning from the guide
The background must **not merely describe a problem or propose an application**.
It must emphasize the **computing contribution**.

### Required logical structure for Specific Objectives
1. **Data acquisition / preparation / analysis**
2. **Algorithm/model/computational technique implementation**
3. **System/prototype development**
4. **Evaluation and assessment**

For the current candidate, “data acquisition” can be reframed as:
- standards-informed parameterization,
- generation of simulation/emulation experiment data,
- collection of DHCP server statistics and packet-level outputs.

### Evaluation expectations
Algorithm/computational evaluation may use:
- accuracy, precision, recall, F1, etc. where appropriate;
- but for this topic, more appropriate metrics are network/system resource metrics.

System evaluation may include:
- ISO/IEC 25010
- SUS
- user/expert evaluation

However, do not over-focus on UI/system usability if the primary contribution is a simulation/model.

---

## File 3
**Thesis_1_Course_Introduction_Sy.pptx**

Important course context:
- Thesis is independent research/development.
- Must solve a specific complex problem in CS.
- Research should include **original aspects** or meaningful validation/extension of existing work.
- Thesis 1 includes:
  - topic selection,
  - topic presentation,
  - problem identification,
  - objectives,
  - proposal,
  - manuscript,
  - proposal defense,
  - revision,
  - Chapters 1–3.
- Grading:
  - **System Development / initial technical work: 40%**
  - **Manuscript/Documentation Chapters 1–3: 60%**
- Research originality, RRL, methodology, and designs/figures/tables matter heavily.
- Timeline in the original slide deck:
  - Topic proposal submission was July 11, 2026
  - Proposal defense dates in Sept/Oct 2026
  - Chapters 1–3 deadlines in Aug 2026
  - The current date at this handoff is Aug 7, 2026, so exact course deadlines should be rechecked if relevant.

---

# 3. INITIAL THESIS DIRECTIONS THAT WERE CONSIDERED

The conversation began by considering several thesis families related to the user's MAC changer interest.

## Initial candidate families
1. Generic MAC spoofing detection using ML
2. Legitimate MAC randomization vs suspicious MAC changes
3. Rule-based vs ML MAC anomaly detection
4. Privacy analysis of MAC randomization
5. Device re-identification despite MAC randomization
6. Network identity continuity
7. DHCP/network-state effects of changing MAC identities

The deep research progressively rejected or downgraded most of these.

---

# 4. IMPORTANT DISTINCTIONS ESTABLISHED

## 4.1 MAC spoofing is not the same as MAC randomization

### MAC spoofing / changing
Deliberately changes the address presented by a network interface.
Can be:
- legitimate,
- testing/admin,
- privacy-related,
- malicious.

### MAC randomization / RCM
A built-in privacy mechanism in modern operating systems.

This distinction matters because:
- **changed MAC ≠ attacker**
- **locally administered address (LAA) ≠ malicious**
- **randomized MAC ≠ classical MAC cloning attack**

Do NOT use:
> “MAC changed, therefore suspicious.”

Do NOT use:
> “LAA means spoofed attacker.”

---

# 5. MODERN OPERATING SYSTEM BEHAVIOR THAT MUST NOT BE MISREPRESENTED

## Android
Current Android documentation indicates:
- MAC randomization is mainstream.
- Android 10+ has randomized Wi-Fi MAC behavior.
- Persistent randomization is the common/default behavior.
- Android 12+ can support non-persistent randomization in appropriate contexts.
- Non-persistent re-randomization is not simply “new MAC every reconnect”; it can depend on conditions such as:
  - lease expiry,
  - sufficiently long disconnection,
  - age of randomized address.

Important:
Do **not** write:
> “Android generates a new MAC every time it reconnects.”

That is too broad and likely false.

## Apple
Current Apple documentation indicates Private Wi-Fi Address modes including:
- Off
- Fixed
- Rotating

Current behavior differs depending on network security and context.
Stronger networks often use a fixed private address; weaker/open networks may use rotating behavior.
Rotating behavior is not “new MAC every minute” and can be relatively infrequent.

Do **not** write:
> “iPhones constantly change MACs.”

---

# 6. STANDARDS / OFFICIAL REFERENCES THAT SHAPED THE RESEARCH

These should be revalidated in a new conversation before formal citation.

## RFC 9724 (2025)
Topic: randomized/changing MAC addresses.
Important implications:
- RCM is a real standards-level issue.
- Defines/treats different generated MAC patterns/policies.
- Useful as the basis for standards-informed RCM scenarios instead of arbitrary simulation behavior.

Use it to justify categories like:
- stable/per-network style,
- periodic behavior,
- per-session behavior.

## RFC 9797 (2025)
Discusses:
- network impacts of randomized/changing MACs,
- loss of persistent network state,
- DHCP consequences,
- AAA/NAC/session continuity issues,
- potential address-pool pressure,
- operational tradeoffs.

Very important nuance:
It supports the claim that RCM **can** affect DHCP/network state.
It does **not** mean every modern device will exhaust DHCP pools.

## RFC 7844
Important for DHCP privacy behavior.
Key idea:
- DHCP Client Identifier (Option 61) can identify a client independently of its MAC.
- A stable identifier may preserve continuity.
- But a stable identifier can also undermine privacy because it can correlate the client across randomized MACs.
- Privacy-oriented behavior may evolve/change the identifier along with the randomized link-layer address.

This creates a major thesis variable:
**persistent Client-ID vs changing/synchronized Client-ID**

## RFC 2131
Base DHCPv4 behavior.
Important correction:
- a valid DHCPRELEASE frees the allocation under the base specification.
Do not model:
> DHCPRELEASE always leaves the IP occupied.

Instead separate:
- client disconnects without RELEASE → lease can remain until expiration
- client sends RELEASE → allocation is freed

## IEEE 802.11bh-2024
Modern standard relevant to randomized/changing MAC addresses and maintaining network services/session continuity.
Useful for context.

---

# 7. RESEARCH LITERATURE THAT KILLED THE GENERIC MAC SPOOFING TOPIC

The broad title:
> “Machine Learning-Based MAC Spoofing Detection System”

was rejected because the space is mature.

Examples identified in earlier research:

## Sheng et al., IEEE INFOCOM 2008
- RSS-based MAC spoof detection
- multiple monitors
- foundational work

## Alotaibi & Elleithy, Sensors 2016
- Random Forest + RSS
- two air monitors
- reported high detection accuracy depending on attacker/victim separation

Important implication:
“Random Forest MAC spoof detection” is not novel.

## Later work
Research has already used:
- RSSI
- deep/adaptive learning
- sequence number/ACK behavior
- CSI amplitude/phase
- CNNs
- multiple monitoring stations

Therefore generic:
- ML spoof detector
- RF/RSSI spoof detector
- deep learning spoof detector
is a poor fit for a low-risk undergraduate thesis unless a very narrow new problem is identified.

### Why rejected
- literature saturation;
- possible specialized hardware requirements;
- panel can easily ask “what is new?”;
- not aligned with simplicity/zero-cost priority.

---

# 8. RESEARCH THAT KILLED THE GENERIC DEVICE FINGERPRINTING / DE-RANDOMIZATION TOPIC

Another broad direction considered:
> “Identify devices despite MAC randomization.”

This was also found to be crowded.

Prior/recent research families included:
- probe request content fingerprints,
- Information Elements,
- sequence behavior,
- timing,
- RSS/RSSI,
- self-supervised association,
- clustering,
- same-device-model/OS differentiation,
- finite-state management-frame behavior,
- lightweight fingerprints.

Examples discussed:
- Martin et al. 2017
- Fenske et al. 2021
- Pintor & Atzori datasets / work
- Uras et al. 2022
- Cappuccino / He, Tan & Chan (IEEE TMC)
- Bleach (2024)
- Baccichet et al. 2024/2025
- recent 2025/2026 probe-template / state-based fingerprinting work
- 2026 preprints on ML against Wi-Fi privacy

### Conclusion
Do NOT propose broad:
> “Machine Learning-Based Device Identification Despite MAC Randomization.”

It is too saturated.

---

# 9. PUBLIC DATASET FINDING

One initially attractive advantage of the fingerprinting direction was that there are public datasets of Wi-Fi Probe Requests under MAC randomization.

Examples found:
- Pintor/Atzori-related labeled datasets
- updated datasets
- UJI Probes / large probe-request datasets

This made zero-cost experimentation possible.

However, due to literature saturation, this is now considered a **backup direction**, not the leading thesis.

---

# 10. EARLIER IDEA THAT WAS WITHDRAWN

At one point, the conversation considered:
> “Classify legitimate MAC randomization versus suspicious MAC changes using ML.”

This was explicitly downgraded/withdrawn.

Reason:
The label “malicious” cannot be reliably inferred from MAC metadata alone.
A manually changed MAC may be legitimate.
A randomized MAC may be OS-generated.
A network admin may assign an LAA.
A privacy tool may do so.

Without stronger ground truth or attack context, the classification premise is scientifically weak.

Do not revive this without a very different threat model.

---

# 11. THE CURRENT STRONGEST DIRECTION: DHCPv4 + RANDOMIZED/CHANGING MACS

After rejecting the saturated paths, the research moved toward operational/network-state consequences of RCM.

The current thesis family is:

> **Computational modeling and emulation of DHCPv4 resource utilization under randomized and changing MAC address behaviors/policies.**

This is now the strongest fit to the user's priorities.

---

# 12. WHY DHCPv4 / RCM IS A REAL PROBLEM

Evidence gathered from:
- RFCs
- vendor operational documentation
- academic experiments
- surveys/tutorials

General validated problem:
Networks historically use MAC addresses as a convenient/persistent identity anchor.
RCM changes that assumption.

Potential impacts include:
- DHCP lease/state duplication or churn
- address pool pressure
- stale/inactive-but-valid leases
- session re-establishment
- NAC/AAA complications
- loss of continuity
- increased transaction overhead

Important:
Do NOT claim:
> “MAC randomization always causes DHCP exhaustion.”

The correct research posture is:
> determine **when**, **how much**, and **under what conditions** RCM materially increases DHCP resource utilization/failure risk.

---

# 13. IMPORTANT PRIOR ART: 2015 REAL-WORLD MAC-RANDOMIZATION TRIALS

A 2015 peer-reviewed IEEE CSCN paper by Bernardos, Zúñiga, and O’Hanlon was identified as important prior art.

It involved real MAC-randomization trials at IETF/IEEE meetings.

Key historical observations discussed:
- many randomized/local MAC identities were observed;
- IP allocations and DHCP client identifier behavior interacted;
- some IP addresses were associated across multiple randomized MACs when a common DHCP client identifier was used;
- later trials used shorter DHCP lease durations;
- some server behavior around existing client identifiers had operational implications.

### Why this matters
It disproves any claim like:
> “No one has studied DHCP under MAC randomization.”

Do NOT use such a claim.

A safer framing:
> Early experimental work established that DHCP identity and lease configuration interact with changing Layer-2 identities, but modern OS RCM behavior and current network policies have evolved substantially.

---

# 14. IMPORTANT PRIOR ART: DHCP LEASE OPTIMIZATION IS NOT NEW

The thesis must NOT claim invention of general lease optimization.

Prior work already exists on:
- usage-based DHCP lease optimization;
- dynamic lease duration;
- adaptive address pool allocation;
- behavior-aware DHCP configuration.

Examples mentioned:
- early work around 2007 on usage-based lease-time optimization;
- Li et al. on modeling DHCP leases / smart terminals;
- BDAC (IEEE ICNP 2019), behavior-aware dynamic adaptive DHCP configuration;
- large-campus DHCP empirical studies.

### Consequence
Do NOT propose:
> “Optimize DHCP lease time to prevent exhaustion.”

Too broad and not novel.

---

# 15. IMPORTANT INDUSTRY PRIOR ART: RCM-AWARE DHCP MECHANISMS

Two important patent families were identified.

## Cisco patent
Title family:
**Address rotation aware dynamic host control protocol**

Concepts discussed include:
- detecting MAC rotation using a stable identifier;
- reusing/reassigning previous IP;
- comparing active leased addresses vs actual active clients;
- shortening lease time near exhaustion.

## ARRIS patent
Title:
**DHCP server IP address allocation improvement to nullify the impact of MAC randomization**

Concepts include:
- detecting randomized MACs;
- correlating clients using hostname/other context;
- potentially reusing prior IP;
- assigning shorter leases to randomized-MAC clients.

### Consequence
Do NOT claim novelty for:
- “shorter lease for randomized MAC clients”;
- “adaptive RCM-aware DHCP”;
- “reuse previous IP after MAC rotation”;
- “detect RCM and dynamically adjust lease.”

Patents are not peer-reviewed empirical studies, but they are strong prior art against “we invented this mechanism.”

This is why the current thesis shifted from **new algorithm** to **evaluation/modeling**.

---

# 16. THE CURRENT CANDIDATE RESEARCH GAP

The prior conversation repeatedly searched around:
- RCM policy
- DHCP Client-ID
- lease duration
- address pool capacity
- pool exhaustion
- simulation/emulation
- network utilization

No contemporary peer-reviewed study was found **in that search** whose central controlled experiment jointly quantifies all four:

1. **RCM / MAC identity policy**
2. **DHCP Client-Identifier strategy**
3. **DHCP lease duration**
4. **Constrained address-pool / network load**

This is a **candidate gap**, not a proven universal absence.

Use cautious wording such as:

> “The literature located thus far has not identified a contemporary peer-reviewed empirical study that jointly quantifies the interaction of randomized/changing MAC behavior, DHCP client-identifier persistence, lease duration, and constrained address-pool capacity.”

Do NOT write:
> “No prior study has ever…”

The next AI should continue trying to kill this exact gap before formalizing it.

---

# 17. WHY DHCP CLIENT IDENTIFIER IS CENTRAL

This became one of the strongest aspects of the candidate thesis.

Conceptual strategies:

## Continuity-oriented strategy
MAC changes:
- MAC1
- MAC2
- MAC3

But Client-ID remains:
- Client123

Potential effect:
- DHCP can potentially recognize a continuing logical client.
- lower duplicate lease pressure.

Potential privacy cost:
- stable identifier can correlate the device across changing MACs.

## Privacy-oriented strategy
MAC changes:
- MAC1 → MAC2 → MAC3

Client-ID changes together:
- ID1 → ID2 → ID3

Potential effect:
- stronger unlinkability;
- DHCP may perceive multiple logical identities over time;
- potentially greater lease/resource pressure.

These are **hypotheses**.
Do not present as already proven universal outcomes.

---

# 18. CURRENT PROPOSED RESEARCH QUESTION FAMILY

The thesis should NOT ask:
> “Does MAC randomization cause DHCP exhaustion?”

That is too simple and already partly established.

Better core question:

> **Under what combinations of randomized/changing MAC behavior, DHCP client-identifier strategy, lease duration, and address-pool pressure does changing Layer-2 identity materially increase DHCPv4 resource utilization and allocation failures compared with stable identity?**

Current provisional RQs:

### RQ1
How does RCM policy affect DHCPv4 lease utilization under different network-load conditions?

### RQ2
How does DHCP Client-Identifier persistence interact with changing MAC identities in terms of address allocation and resource utilization?

### RQ3
How does DHCP lease duration affect the trade-off between address-pool availability and DHCP transaction overhead under different RCM conditions?

### RQ4
Under what combinations of RCM behavior, Client-ID strategy, lease duration, and pool pressure do address-allocation failures become significant?

These are stronger because they focus on:
- interaction effects,
- magnitude,
- thresholds,
- tradeoffs,
not just an obvious binary effect.

---

# 19. CURRENT PROPOSED INDEPENDENT VARIABLES

Keep the thesis manageable.

## Core four factors

### 1. MAC / RCM identity behavior
Provisional levels:
- Stable / per-network
- Periodic
- Per-session / frequent session-based identity change

These should be anchored to RFC-defined / standards-informed categories rather than invented arbitrarily.

### 2. DHCP Client-ID strategy
- Persistent Client-ID
- Changing/synchronized Client-ID

Potentially also:
- Client-ID aware server vs MAC/chaddr-only matching
as a validation/sensitivity condition rather than a main factor.

### 3. DHCP lease duration
Provisional:
- 1 hour
- 4 hours
- 8 hours
- 24 hours

These are not final.
Need literature/operational justification.

### 4. Pool pressure / network load
- Low
- Medium
- High

Better to define quantitatively as:
- ratio of physical clients/concurrent demand to available address pool
rather than vague labels in the final methodology.

---

# 20. CURRENT PROPOSED EXPERIMENT SIZE

Example factorial design:
- 3 RCM policies
- 2 Client-ID strategies
- 4 lease durations
- 3 pool-pressure levels

Total:
**3 × 2 × 4 × 3 = 72 configurations**

With 30 random repetitions:
**2,160 simulation runs**

This is computationally trivial for an ordinary laptop.

Do not overexpand to 10+ variables.

---

# 21. CURRENT PROPOSED DEPENDENT METRICS

Recommended primary metrics:

1. **Peak lease-pool utilization (%)**
2. **Allocation failure rate (%)**
3. **Probability/frequency of pool exhaustion**
4. **Time to exhaustion**
5. **DHCP messages per simulated hour**
6. **Inactive-but-valid lease count**
7. **Address reclamation time** (optional)
8. **Cumulative allocations** (optional)

For validation:
- compare simulator output against emulated DHCP implementation
- MAE/RMSE or percentage deviation may be used for selected metrics.

---

# 22. PROPOSED METHODOLOGY ARCHITECTURE

The current preferred design is a **two-stage study**.

## Stage 1 — Main computational experiment
**Python discrete-event simulation**

Purpose:
- run thousands of controlled scenarios;
- isolate variables;
- produce threshold maps / response surfaces;
- evaluate resource utilization and transaction overhead;
- avoid hardware dependence.

Potential software:
- Python
- SimPy or custom event simulator
- pandas
- NumPy
- matplotlib / seaborn
- scipy/statsmodels if needed

No ML is necessary.

## Stage 2 — Emulation validation
Use:
- Linux VM or native Linux
- network namespaces / virtual Ethernet
- Kea DHCPv4 server
- possibly dnsmasq for secondary comparison
- packet capture
- Kea statistics
- perfdhcp for selected load cases

Purpose:
- verify simulator behavior against a real DHCP server implementation;
- answer panel criticism that the simulator is purely theoretical.

### Important scope statement
This does **not** emulate the full IEEE 802.11 radio layer.

It models:
> the DHCPv4 consequences of changing Layer-2 client identities.

Explicitly outside scope:
- RF propagation
- 802.11 scanning
- association/reassociation details
- Wi-Fi roaming
- interference
- actual mobile OS Wi-Fi stacks
unless separately tested.

---

# 23. WHY KEA DHCPv4 WAS IDENTIFIED AS A GOOD VALIDATION PLATFORM

Kea DHCPv4 was investigated as a realistic zero-cost testbed.

Important capabilities found:
- Client-ID matching behavior can be configured.
- `match-client-id=true` can use Client Identifier and fallback behavior.
- server can expose lease/statistics counters.
- statistics can include address assignments, reclaimed leases, packet counts.
- `perfdhcp` can generate DHCP load and randomize identifiers/hardware addresses.

This makes Kea useful for:
- testing identity continuity vs MAC-only identity;
- measuring actual lease pool occupancy;
- validating simulation.

Need re-check current Kea documentation/version before final methodology.

---

# 24. DHCP RELEASE BEHAVIOR — MUST MODEL CORRECTLY

Important correction from RFC 2131:
- Valid DHCPRELEASE should free the address allocation.
- If a client disappears without RELEASE, the lease may remain valid until expiry.

Therefore:
Main model should distinguish:
- **graceful release**
- **silent disappearance / no release**

But do not necessarily make this a main factorial variable.
It can be a sensitivity experiment.

Avoid artificially forcing exhaustion by assuming every released address remains occupied.

---

# 25. CLIENT ARRIVAL / SESSION BEHAVIOR SHOULD NOT BE ARBITRARY

A potential panel question:
> “Where did your simulated client arrival/session distributions come from?”

The prior research found campus Wi-Fi/DHCP trace studies that model:
- smartphone session lengths,
- concurrent address usage,
- connection behavior.

Next AI should find and verify high-quality peer-reviewed traces/models and use them to justify:
- session duration distribution,
- arrival process,
- reconnect intervals,
- concurrency.

Fallback:
Use multiple distributions in a sensitivity analysis:
- short-stay guest,
- medium-stay,
- long-stay
with parameters anchored to literature.

Avoid saying:
> “We assumed users stay 2 hours”
without justification.

---

# 26. THE BIGGEST REALISM RISK

Current devices often use relatively stable private/randomized MACs.

This means a thesis premised on ultra-aggressive MAC rotation may exaggerate real-world risk.

Therefore, the methodology should separate:

## A. Vendor-realistic baseline scenarios
Approximate documented current Android/Apple patterns.

## B. Standards-informed RCM scenarios
Use broader RFC-defined categories such as:
- per-network
- periodic
- per-session

This lets the study ask:
- whether current realistic behavior produces negligible impact;
- when more aggressive RCM policies create measurable pressure.

A finding of “little impact under realistic defaults” is valid and should not be treated as thesis failure.

---

# 27. WHAT MAKES THE CURRENT DIRECTION NONTRIVIAL

A weak conclusion would be:
> “More MAC changes + longer leases = more IPs consumed.”

That is obvious.

The thesis must instead quantify:
- interaction effects;
- thresholds;
- critical operating regions;
- tradeoff between pool availability and DHCP overhead;
- how Client-ID persistence changes the result;
- when effects become operationally significant.

Example conceptual output:
- heatmaps;
- threshold curves;
- probability of allocation failure;
- recommended safe configuration regions;
- not a single “best lease time.”

---

# 28. POSSIBLE COMPUTATIONAL CONTRIBUTION

The contribution is **not** a novel MAC changer or a novel DHCP server.

The current contribution is:

> **A standards-informed, validated computational model and experimental framework for quantifying DHCPv4 resource behavior under randomized/changing Layer-2 identity policies.**

Potential contribution components:
1. Formalized RCM/DHCP identity scenarios based on standards.
2. Discrete-event model of lease allocation and identity churn.
3. Controlled factorial evaluation.
4. Threshold/interaction analysis.
5. Validation against Kea DHCPv4 emulation.
6. Reproducible configuration recommendations for constrained guest networks.

This aligns with the official thesis domain:
**Computational Modeling and Simulation** and potentially **Cybersecurity / Network Computing**.

---

# 29. WHY MACHINE LEARNING SHOULD NOT BE ADDED

The prior conversation explicitly decided **not** to force ML into the topic.

Reasons:
- no need;
- makes defense harder;
- introduces unnecessary complexity;
- ML does not solve the core research question better;
- general adaptive DHCP optimization already has prior art;
- the official guide allows computational modeling/simulation.

Do not add AI/ML merely to make the title “sound more CS.”

---

# 30. CURRENT PROVISIONAL TITLE OPTIONS

These are working formulations, NOT final titles.

### Preferred current formulation
**Computational Modeling and Emulation of DHCPv4 Lease Utilization under Randomized and Changing MAC Address Policies in University Guest Networks**

Potential issue:
“University Guest Networks” should only be retained if the application domain is truly appropriate and the study does not falsely imply access to BU’s production network.

Safer alternative:
**Computational Modeling and Emulation of DHCPv4 Lease Utilization under Randomized and Changing MAC Address Policies in Constrained Guest Networks**

### Slightly shorter
**Computational Modeling of DHCPv4 Resource Utilization under Randomized and Changing MAC Address Policies in Guest Networks**

### More evaluation-oriented
**A Computational Evaluation of DHCPv4 Lease Policies under Randomized and Changing MAC Address Behaviors in Constrained Guest Networks**

Do not finalize until:
- exact gap is revalidated;
- methodology variables are fixed;
- “guest network” context is justified.

---

# 31. CURRENT REQUIRED PROPOSAL ALIGNMENT MAPPING

Provisional only.

| Criterion | Current candidate |
|---|---|
| **CS Domain** | Computational Modeling and Simulation / Cybersecurity & Network Computing |
| **Computing Contribution** | Standards-informed DHCPv4 resource-utilization model with emulation-based validation |
| **BU Agenda** | Institutional Development and Policy Innovation |
| **SDG** | SDG 9 – Industry, Innovation and Infrastructure |
| **Beneficiary** | University / guest-network administrators |
| **Expected Innovation** | Reproducible threshold and configuration analysis showing when different RCM and DHCP identity policies materially affect constrained address pools |

This mapping should be refined to the exact terminology in the user's official thesis guide.

---

# 32. CURRENT “KILL LIST” — DO NOT REVIVE WITHOUT STRONG NEW EVIDENCE

Reject these formulations unless new evidence changes the situation:

## 32.1 MAC changer application
Example:
> Development of a MAC Address Changer App
Reason:
- software tool only;
- weak research contribution;
- likely IT/project rather than CS thesis.

## 32.2 Generic ML MAC spoof detector
Reason:
- heavily studied;
- hardware/feature complexity;
- weak novelty.

## 32.3 Generic de-randomization / fingerprinting ML
Reason:
- crowded, including recent 2024–2026 work.

## 32.4 Legitimate vs malicious MAC classifier
Reason:
- ground truth cannot be inferred from MAC metadata alone.

## 32.5 “Optimize DHCP lease time”
Reason:
- old and mature research area.

## 32.6 “Adaptive DHCP for randomized MACs”
Reason:
- prior academic optimization + Cisco/ARRIS prior art.

## 32.7 “Shorter leases for randomized clients”
Reason:
- known operational mitigation / prior art.

## 32.8 “Modern phones change MAC every reconnect”
Reason:
- false overgeneralization.

## 32.9 “New MAC automatically means new IP”
Reason:
- DHCP Client Identifier and server matching complicate this.

## 32.10 “RCM always causes DHCP exhaustion”
Reason:
- unsupported universal claim.

---

# 33. CAUTIOUS NOVELTY WORDING

Use language like:
- “The literature located thus far…”
- “Few studies appear to jointly evaluate…”
- “The interaction among X, Y, Z remains insufficiently quantified in the literature reviewed…”
- “This study does not claim to introduce RCM-aware DHCP as a new concept; rather, it provides a controlled computational evaluation…”

Avoid:
- “First ever”
- “No existing study”
- “No one has investigated”
unless systematic review evidence is genuinely sufficient.

---

# 34. POSSIBLE GENERAL OBJECTIVE — PROVISIONAL

Do not use this verbatim yet; it needs final methodological wording.

> To develop and validate a standards-informed computational model for evaluating DHCPv4 lease utilization and address-allocation behavior under randomized and changing MAC address policies, DHCP client-identifier strategies, lease durations, and constrained network-load conditions.

This is aligned with the official guide because it centers the computational contribution.

---

# 35. POSSIBLE SPECIFIC OBJECTIVES — PROVISIONAL STRUCTURE

Must follow the official 4-step objective logic.

### Objective 1 — Parameterization / experiment data
Identify and define standards- and literature-informed RCM policies, DHCP client-identifier strategies, lease durations, pool sizes, and client session/load parameters for simulation and emulation.

### Objective 2 — Computational model
Design and implement a discrete-event model that simulates DHCPv4 lease allocation, identity changes, lease expiration/release, and address-pool utilization under controlled RCM/DHCP scenarios.

### Objective 3 — Prototype / experimental framework
Develop an experimental framework that integrates the simulator with a Linux/Kea DHCPv4 emulation environment for selected validation scenarios and records DHCP resource/transaction metrics.

### Objective 4 — Evaluation
Evaluate the effects and interactions of RCM policy, Client-ID strategy, lease duration, and pool pressure using lease utilization, allocation failure, exhaustion probability/time, message overhead, inactive-valid leases, and simulation-vs-emulation validation metrics.

These objectives still need refinement.

---

# 36. PROVISIONAL SCOPE

Likely scope:
- IPv4 DHCP only
- DHCPv4 server resource behavior
- simulated/emulated changing L2 identities
- guest/constrained network scenarios
- standards-informed RCM identity policies
- selected DHCP Client-ID strategies
- selected lease durations
- constrained pool sizes/load levels
- simulation + emulation validation

Likely exclusions:
- DHCPv6
- full Wi-Fi RF/802.11 stack
- actual user tracking
- active attacks against third-party networks
- enterprise 802.1X/NAC/RADIUS
- real BU production network deployment
- actual Android/iOS source-code implementation
- specialized Wi-Fi hardware
- MAC spoofing attack detection
- device fingerprinting/de-randomization
- invention of new DHCP protocol standards

---

# 37. PROVISIONAL LIMITATIONS

Possible limitations to state honestly:
- simulation abstracts physical Wi-Fi behavior;
- vendor-specific OS behavior may evolve;
- standards-informed scenarios do not imply all devices behave identically;
- emulation represents selected DHCP implementation behavior, not every DHCP server;
- guest-network workload distributions rely on published traces/sensitivity ranges rather than BU production logs;
- IPv6/SLAAC not included;
- results may not generalize directly to enterprise NAC-heavy networks.

---

# 38. ETHICS / SAFETY PROFILE

This direction is preferable because it avoids:
- attacking real networks;
- bypassing access controls;
- tracking real users;
- collecting personal data;
- needing production Wi-Fi credentials;
- adversarial device fingerprinting.

The experiment can be fully isolated and virtualized.

This is a major positive for feasibility and defense.

---

# 39. CURRENT COST ASSESSMENT

Potential additional cost:
**₱0**

Assuming user already has:
- ordinary laptop/PC;
- enough RAM for a Linux VM or native Linux.

Free/open-source stack:
- Python
- Linux
- Kea DHCPv4
- Wireshark/tshark
- network namespaces
- perfdhcp
- pandas
- matplotlib

No required:
- cloud GPU
- paid API
- specialized Wi-Fi NIC
- Raspberry Pi
- university network access
- proprietary dataset

---

# 40. CURRENT THESIS-READINESS ASSESSMENT

| Criterion | Current assessment |
|---|---|
| Real/current problem | Strong |
| Literature basis | Strong |
| Standards basis | Strong |
| Feasibility | Strong |
| Zero-cost potential | Strong |
| Hardware dependence | Very low |
| Ethical risk | Low |
| Research measurability | Strong |
| CS contribution | Strong |
| Exact novelty certainty | Moderate, requires continued verification |
| Risk of obvious result | Reduced if threshold/interaction framing is used |
| Defensibility | High if methodology is rigorous |
| Need for ML | None |

The topic was upgraded from:
**promising direction**
to:
**serious thesis candidate**

but not yet “final approved title.”

---

# 41. NEXT STEP THAT WAS AGREED BEFORE THIS HANDOFF

The next phase should move from broad topic survival into a **proposal dossier / methodology hardening phase**.

Before writing a polished Background, the next AI should build:

1. **Exact research-gap argument**
2. **Literature backbone**
   - what each prior study solved;
   - what it did not solve;
   - direct relation to the current candidate.
3. **Final RQs**
4. **Hypotheses / expected directional relationships** (if the thesis format needs them)
5. **Conceptual/computational model**
6. **Exact independent/dependent variables**
7. **Simulation event/state model**
8. **Validation architecture**
9. **Experimental scenarios**
10. **Statistical analysis plan**
11. **Final General Objective**
12. **Four Specific Objectives**
13. **Strict Scope and Limitations**
14. **Only after that: polished Background / Introduction**

The previous AI specifically advised:
**Do not write a polished Background yet.**

---

# 42. HIGH-PRIORITY RESEARCH TASKS FOR THE NEXT AI

## Task A — Re-validate the exact gap
Search specifically:
- randomized changing MAC DHCP empirical study
- RCM DHCP Client Identifier lease duration pool exhaustion
- MAC randomization DHCP simulation
- MAC randomization DHCP lease utilization
- RCM DHCP pool capacity
- MAC randomization DHCP client identifier empirical
- randomized MAC guest network DHCP
- DHCP identity churn simulation
- randomized MAC address allocation performance

Search:
- IEEE Xplore
- ACM Digital Library
- Springer
- Elsevier / ScienceDirect
- Wiley
- USENIX
- arXiv only as supplementary evidence
- theses/dissertations as secondary
- standards RFCs/IETF/IEEE
- vendor docs only for operational confirmation
- patents only as prior art, not experimental evidence

Goal:
Try to find a paper that already jointly studies:
**RCM × Client-ID × lease duration × pool pressure**
If found, compare methodology and decide whether to:
- narrow further;
- replicate with newer behavior;
- change variable;
- abandon.

## Task B — Verify the 2024 IEEE survey/tutorial
A prior research pass cited a 2024 IEEE Communications Surveys & Tutorials article on privacy/RCM and WLAN implications.
Re-open the actual peer-reviewed source and verify:
- its research-challenge table;
- exact wording on RCM-aware DHCP;
- optimal lease duration;
- pool exhaustion;
- Client Identifier tradeoff.

This source may become central to the gap argument.

## Task C — Verify RFC details
Re-read:
- RFC 9724
- RFC 9797
- RFC 7844
- RFC 2131

Extract exact sections relevant to:
- RCM taxonomy;
- DHCP allocation consequences;
- Client Identifier privacy;
- DHCPRELEASE semantics.

## Task D — Verify current Android/Apple behavior
Use official vendor docs only for formal claims.
Do not rely on blogs.

## Task E — Verify Kea behavior on current version
Check:
- `match-client-id`
- lease storage logic
- statistics API
- expiration/reclamation
- perfdhcp capabilities
- client ID and chaddr matching
- release handling

## Task F — Choose workload model
Find peer-reviewed client/session/arrival distributions for:
- guest Wi-Fi,
- campus Wi-Fi,
- smartphone DHCP usage.

If no strong guest-specific trace exists:
use multiple sensitivity distributions and say so.

---

# 43. RECOMMENDED SEARCH/SOURCE QUALITY HIERARCHY

For formal thesis:
1. RFC / IEEE standard
2. Peer-reviewed journal/conference
3. Official OS/vendor documentation
4. University repository / dissertation
5. Patent as prior art
6. Preprint only if clearly labeled
7. Avoid relying on ResearchGate pages when publisher/DOI version is available

The prior conversation sometimes used ResearchGate or Justia as discovery links.
The next AI should replace those with original sources/DOIs where possible.

---

# 44. CLAIMS THAT REQUIRE RE-VERIFICATION BEFORE FORMAL MANUSCRIPT USE

The following were found/discussed but should be independently rechecked before citation:

- exact Android non-persistent re-randomization conditions;
- exact Apple fixed/rotating defaults and rotation interval;
- exact details/results of Bernardos et al. 2015 trial;
- exact performance/result details of old spoofing studies;
- exact content of Cisco/ARRIS patents;
- exact research challenges in the 2024 IEEE tutorial;
- exact Kea version behavior;
- exact Apple router lease recommendations;
- exact campus DHCP trace distributions.

The handoff preserves the research direction, not a guarantee that every number from earlier conversation is citation-perfect.

---

# 45. POSSIBLE STATISTICAL ANALYSIS DIRECTION

Not fully finalized, but a rigorous plan could include:

## Descriptive
- mean/median peak utilization
- failure rate
- exhaustion probability
- message overhead
- inactive-valid leases

## Factorial effects
Because the design is factorial:
- ANOVA / generalized linear model if assumptions allow;
- otherwise nonparametric / bootstrap / robust regression.

Potential model:
Outcome = RCM policy + Client-ID + lease duration + load + interactions.

Important interactions:
- RCM × Client-ID
- RCM × lease duration
- Client-ID × lease duration
- RCM × Client-ID × load

## Threshold analysis
Determine operating regions where:
- allocation failure probability exceeds X%;
- pool utilization exceeds Y%;
- overhead rises significantly.

Do not choose arbitrary X/Y without justification.
Can report continuous surfaces instead.

## Simulation validity
- compare selected simulation metrics against Kea emulation
- report MAE/RMSE/relative error
- inspect qualitative lease-state behavior

---

# 46. POSSIBLE CONCEPTUAL MODEL

A clean conceptual flow:

Physical/Logical Client Population
→ Session/Arrival Behavior
→ RCM Policy
→ MAC Identity Churn
→ DHCP Client-ID Strategy
→ DHCP Server Identity Matching
→ Lease Allocation / Renewal / Release / Expiration
→ Address Pool State
→ Resource Utilization / Failure / Overhead

Moderating/configuration variables:
- lease duration
- pool size
- load/concurrency

Outputs:
- utilization
- failures
- exhaustion
- message overhead
- stale/inactive-valid leases

This can be turned into a formal conceptual framework diagram later.

---

# 47. POSSIBLE SIMULATION STATE MODEL

Entities:
- Client
- Logical identity
- MAC identity
- DHCP client ID
- Lease
- Address pool
- DHCP server

Events:
- client arrival
- request/lease acquisition
- reconnect
- MAC rotation
- Client-ID rotation/persistence
- renewal
- release
- silent departure
- lease expiration
- address reclamation

State:
- active physical clients
- active logical identities
- valid leases
- available addresses
- inactive-but-valid leases
- message counters

Need validate exact DHCP event sequence against RFC 2131.

---

# 48. POTENTIAL DEFENSE QUESTIONS AND PREPARED ANSWERS

## “Why is this Computer Science and not IT/network admin?”
Answer direction:
The contribution is a **validated computational model and controlled experimental evaluation** of identity-churn effects on DHCPv4 resource behavior. The thesis investigates interactions, thresholds, and system behavior using computational simulation/emulation, not merely configuring a router.

## “Why not just use shorter lease times?”
Because shorter leases increase reclamation speed but can also increase DHCP transaction/renewal overhead. Existing work shows a tradeoff. This study quantifies the tradeoff specifically under changing identity strategies.

## “Is MAC randomization even a problem today?”
Standards and vendor docs acknowledge operational impacts, but current devices often use relatively persistent private addresses. That uncertainty is exactly why the study does not assume failure—it quantifies when the effect becomes significant.

## “Are you attacking/spoofing real users?”
No. All changing L2 identities are simulated/emulated in an isolated environment.

## “Why not use AI?”
The research question is about system behavior and configuration interactions; simulation/modeling is a more direct and interpretable computational method.

## “What is novel?”
Do NOT claim RCM-aware DHCP itself is new.
Claim the specific contribution is a **controlled, standards-informed joint evaluation** of RCM policy, Client-ID persistence, lease duration, and constrained pool pressure, plus validation against an actual DHCP implementation—if continued literature review confirms this combination remains insufficiently studied.

## “Why guest networks?”
Guest/constrained networks naturally have dynamic clients and limited address pools without the extra complexity of enterprise NAC/RADIUS. But the final domain wording must be justified.

---

# 49. BACKUP THESIS DIRECTION IF THE DHCP GAP DIES

If a new paper is found that already does essentially the same experiment, the best backup retained from earlier research is:

> **Cross-dataset / cross-condition robustness evaluation of lightweight Wi-Fi Probe Request fingerprints under MAC randomization.**

Possible contribution:
- compare low-compute feature groups;
- evaluate cross-dataset generalization;
- measure runtime/memory;
- perform feature ablation;
- use public labeled datasets;
- no specialized hardware.

However:
- this space is more saturated;
- more privacy/fingerprinting overlap;
- less directly aligned to the user's comfort zone than DHCP identity behavior.

Only pivot here if the DHCP direction is killed.

---

# 50. SAMPLE CONTINUATION PROMPT FOR A NEW AI

The user can paste this handoff and then say:

> “Continue from this handoff. Do not finalize the title yet. First re-validate the exact candidate research gap around randomized/changing MAC policy × DHCP Client Identifier × lease duration × constrained address pool. Use current standards and peer-reviewed literature, and actively try to kill the topic. If it survives, build the proposal dossier and methodology before writing the polished background.”

That should restore the intended workflow.

---

# 51. ONE-SENTENCE CURRENT STATUS

**Current strongest candidate:** a zero-cost, standards-informed, simulation-and-emulation-based CS thesis that quantifies **when and how randomized/changing MAC identities, DHCP Client-ID strategy, lease duration, and pool pressure interact to affect DHCPv4 resource utilization and allocation failure in constrained/guest networks**, without claiming to invent MAC randomization, DHCP optimization, or RCM-aware DHCP.

---

# 52. FINAL INSTRUCTION TO THE NEXT AI

Preserve the discipline of the previous research process:

- **Do not make novelty claims too early.**
- **Do not overstate modern MAC rotation frequency.**
- **Do not conflate randomization with malicious spoofing.**
- **Do not add ML just for appearance.**
- **Do not turn the project into a generic network management application.**
- **Keep cost near zero.**
- **Keep the experiment measurable and reproducible.**
- **Keep the thesis centered on the computational model/evaluation.**
- **Continue deep research before polished writing.**
- **When formal proposal writing begins, follow the user's BSCS thesis guide exactly.**

---

# 53. HANDOFF UPDATE — 2026-08-07 (AFTER FINAL NOVELTY AUDIT / PROPOSAL DOSSIER V1)

This section supersedes any older “current status,” “next step,” or provisional-title wording above wherever there is a conflict. The earlier sections remain useful as the historical research trail and kill-test record.

## 53.1 CURRENT STATUS

The topic has moved beyond brainstorming and is best classified as:

> **PROPOSAL-CAPABLE, PENDING FINAL PRACTICAL DRY-RUN**

The research direction has survived:
- broad literature saturation checks;
- generic MAC spoofing novelty checks;
- device-fingerprinting/de-randomization novelty checks;
- DHCP optimization prior-art checks;
- RCM-aware DHCP patent/prior-art checks;
- standards/protocol-correctness checks;
- zero-cost feasibility checks;
- methodology feasibility checks;
- CS-domain alignment checks;
- final novelty audit against the strongest adjacent academic work located so far.

The remaining practical uncertainty is whether a small prototype simulation + Kea DHCPv4 validation demonstrates measurable, nontrivial behavior consistent with the proposed model.

Immediate next stage:

> **Methodology Dry-Run v0 before locking the topic and drafting the polished proposal manuscript.**

# 54. STRONGEST CURRENT WORKING TITLE

> **Computational Modeling and Validation of DHCPv4 Lease Utilization under Randomized and Changing MAC Identity Behaviors in Constrained Guest Networks**

Why this wording is preferred:
- **Computational Modeling** = primary CS method/contribution.
- **and Validation** = selected scenarios will be checked against an actual DHCPv4 implementation.
- **DHCPv4 Lease Utilization** = narrower than “resource utilization.”
- **Randomized and Changing MAC Identity Behaviors** = avoids claiming to reproduce every IEEE 802.11 or vendor-specific RCM detail.
- **Constrained Guest Networks** = realistic domain with transient clients and finite pools, without enterprise NAC/RADIUS complexity.

Still a **working title**, not final.

# 55. CURRENT NOVELTY POSITION

The search process has not identified a contemporary peer-reviewed study whose central controlled experiment jointly varies and quantifies:

1. **DHCP-visible MAC identity behavior / identity turnover**
2. **DHCP Client-Identifier continuity**
3. **DHCP lease duration**
4. **Constrained address-pool pressure / physical client demand**

This remains a **candidate novel combination**, not proof of absolute firstness.

Preferred novelty framing:

> **Although prior work has established the operational effects of Randomized and Changing MAC addresses on DHCP and separately investigated DHCP lease and address-pool optimization, the literature reviewed thus far does not provide a controlled quantitative characterization of how DHCP-visible MAC identity turnover interacts with DHCP Client-Identifier continuity, lease duration, and address-pool pressure. Consequently, the operating conditions under which identity turnover produces negligible, moderate, or service-impacting DHCPv4 lease amplification remain insufficiently characterized.**

Use cautious wording:
- “insufficiently characterized”
- “the literature reviewed thus far”
- “controlled quantitative characterization”

Avoid:
- “first ever”
- “no existing study”
- “nobody has investigated”
- “RCM-aware DHCP is new”

# 56. UPDATED RRL BACKBONE

## RFC 2131 — DHCPv4
Use for:
- DHCP lease lifecycle;
- client identification;
- Client Identifier precedence when present;
- fallback to `chaddr` when absent;
- renewal/rebinding;
- DHCPRELEASE semantics.

Important:
> A valid DHCPRELEASE frees the allocation under the base protocol model.

## RFC 4361
Use for:
- DHCPv4 Client Identifier based on DUID/IAID;
- evidence that DHCP logical identity can be independent of the MAC address.

## RFC 7844
Use for:
- privacy implications of DHCP identifiers;
- persistent Client Identifier can correlate a client across randomized MACs;
- privacy-oriented behavior may change Client-ID together with MAC.

Core experiment contrast:

**Continuity-oriented**
- changing MAC;
- persistent Client-ID.

**Privacy-oriented**
- changing MAC;
- changing Client-ID.

These are experiment conditions, not claims about all devices.

## RFC 9724
Use for:
- standards-informed RCM taxonomy;
- per-network / per-period / per-session generated MAC behavior.

Important terminology:
Use **DHCP-visible MAC identity behavior / turnover** rather than saying “every MAC change causes DHCP.”

## RFC 9797
Use for:
- network-state impact of randomized/changing MACs;
- DHCP continuity issues;
- possible pool/scope pressure;
- broader NAC/AAA context.

Do not read it as proving every modern device causes pool exhaustion.

## 2024 IEEE Communications Surveys & Tutorials RCM tutorial
This is one of the strongest Chapter 1/2 gap anchors.

It reportedly identifies research challenges around:
- RCM-aware DHCP handling;
- lease management;
- optimal lease duration under RCM;
- preventing DHCP pool exhaustion;
- efficient IP allocation;
- balancing Client Identifier continuity with privacy.

Before formal citation, verify the publisher/DOI version and exact table wording.

## Bernardos et al., IEEE CSCN 2015
Use to show:
- DHCP/identity interaction under randomized MAC is not new;
- real experimental trials already existed;
- basic phenomenon cannot be claimed as novel.

## General DHCP optimization literature
Includes:
- usage-based lease optimization;
- smartphone-era DHCP configuration;
- Li et al. DHCP modeling/emulation;
- BDAC;
- large-scale DHCP empirical work;
- PredHCP (2025).

Implication:
> Generic DHCP optimization is mature. Our thesis is not an optimizer.

## Industrial prior art
Cisco and ARRIS patent families already include:
- detecting MAC rotation;
- address reuse;
- active-client vs lease divergence;
- shorter/adaptive leases under RCM.

Therefore, do not claim novelty for a new RCM-aware DHCP algorithm.

# 57. FINAL RESEARCH PROBLEM — CURRENT FORM

> DHCP can associate a client through a DHCP Client Identifier when supplied, or through the link-layer `chaddr` field when it is not. Randomized and changing MAC identities alter the identity visible to the network, while privacy-oriented DHCP behavior may also rotate the Client Identifier. Depending on how MAC identity turnover, Client-Identifier continuity, lease duration, and address-pool pressure interact, the DHCP server may retain more valid leases than the number of currently active physical clients, potentially increasing address-pool pressure and allocation failures. The magnitude and threshold conditions of this interaction remain insufficiently characterized in the literature reviewed so far.

Do not reduce this to:
> “MAC randomization causes IP exhaustion.”

# 58. FINAL RESEARCH QUESTIONS — CURRENT VERSION

## RQ1
**How do different DHCP-visible randomized and changing MAC identity behaviors affect DHCPv4 lease utilization under varying address-pool pressure?**

## RQ2
**How does DHCP Client-Identifier continuity influence lease utilization when a physical client presents changing MAC identities?**

## RQ3
**How does lease duration affect the trade-off between address availability and DHCP transaction overhead under different MAC identity and Client-Identifier conditions?**

## RQ4
**Under what combinations of MAC identity behavior, Client-Identifier continuity, lease duration, and pool pressure do DHCPv4 allocation failures or address-pool exhaustion become operationally significant?**

# 59. CURRENT HYPOTHESES — PROVISIONAL

## H1
Increasing DHCP-visible identity turnover will increase valid lease occupancy when logical DHCP identity changes with the MAC address.

## H2
A persistent DHCP Client Identifier will reduce lease amplification caused by changing MAC addresses when the DHCP server uses Client-ID-based lease matching.

## H3
Shorter DHCP lease durations will reduce inactive-but-valid lease accumulation and allocation failures but increase DHCP renewal/message overhead.

## H4
Identity-turnover effects will become substantially larger as physical client demand approaches DHCP address-pool capacity.

These are hypotheses, not predetermined results.

# 60. CONCEPTUAL FRAMEWORK

```text
Physical Client Population
          │
          ▼
Session / Arrival Behavior
          │
          ▼
DHCP-visible MAC Identity Behavior
 Stable / Periodic / Session-based
          │
          ▼
DHCP Client-ID Strategy
 Persistent / Changing
          │
          ▼
DHCP Identity Matching
          │
          ▼
Lease Acquisition / Renewal / Release / Expiration
          │
          ▼
Address Pool State
          │
          ├──────────────┬───────────────┐
          ▼              ▼               ▼
 Lease Utilization   DHCP Overhead   Allocation Failures
          │
          ▼
Threshold / Interaction Analysis
```

Moderators:
- lease duration;
- address-pool pressure.

# 61. INDEPENDENT VARIABLES — CURRENT PROVISIONAL FREEZE

## Factor 1 — DHCP-visible MAC identity behavior
Levels:
1. Stable / per-network identity
2. Periodic identity turnover
3. Session-based identity turnover

These are standards-informed experimental conditions, not claims about all mobile OSes.

## Factor 2 — DHCP logical identity continuity
Levels:
1. Persistent Client Identifier
2. Rotating / MAC-synchronized Client Identifier

## Factor 3 — Lease duration
Preferred levels:
- 1 hour
- 2 hours
- 8 hours
- 24 hours

Exact rationale/source details must be verified before final Chapter 3.

## Factor 4 — Pool pressure
Provisional levels:
- 50%
- 75%
- 90%

Final methodology must define exactly how physical demand is operationalized.

# 62. CORE FACTORIAL DESIGN

3 MAC identity conditions
× 2 Client-ID conditions
× 4 lease durations
× 3 pressure conditions
= **72 main configurations**

Replication:
- minimum 30 independent random seeds per configuration;
- add repetitions until 95% CI on the primary outcome reaches acceptable precision;
- practical maximum may be around 100 runs per configuration.

# 63. WORKLOAD MODEL

Do not invent user behavior arbitrarily.

## Main profile
Use a published bursty public/guest WLAN workload as a reproducible literature-informed profile.

Prior research discussed:
- two-state MMPP arrivals;
- short sessions;
- heavy-tailed session durations.

## Sensitivity profile
Use more recent large-scale campus DHCP observations to inform:
- session duration;
- explicit DHCPRELEASE frequency;
- difference between active time and lease occupancy.

Do not claim an old public WLAN trace directly represents current smartphones.

# 64. DHCP RELEASE BEHAVIOR

Do not make release probability a main factor initially.

Normative base:
- valid DHCPRELEASE → address becomes reusable;
- silent departure → lease persists until expiry.

Suggested:
- main condition = low literature-informed release probability;
- sensitivity = 0% vs 100% release boundary conditions.

# 65. DHCP RENEWAL / REBINDING — MANDATORY

Do not simulate:
> allocation → wait until expiry → drop.

Model RFC 2131 lifecycle.

Conceptual timers:
- T1 ≈ 0.5 × lease duration
- T2 ≈ 0.875 × lease duration

While active:
- renew at T1;
- rebind at T2 if necessary;
- lose lease only if expiration is reached without renewal.

# 66. SIMULATION HORIZON / WARM-UP

Provisional start:
- approximately 48-hour warm-up;
- 7-day measured period.

But final warm-up should be based on pilot convergence/stability analysis, not arbitrary choice.

# 67. MAIN OUTCOME METRICS

## Peak pool utilization
`U_peak = max(valid leases / pool capacity)`

## Allocation failure rate
`failed allocation attempts / total allocation attempts`

## Pool-exhaustion probability
`runs with exhaustion / total runs`

## Time to first exhaustion

## Valid-lease-to-active-client ratio
`valid DHCP leases / currently active physical clients`

Use descriptively, not as a claimed revolutionary metric.

## DHCP message overhead
Prefer messages per client-hour or simulated hour.

## Inactive-but-valid lease count

# 68. STATISTICAL ANALYSIS

Primary goal:
**interaction effects**, not just main effects.

Potential terms:
- MAC identity behavior
- Client-ID behavior
- lease duration
- pool pressure

Important interactions:
- MAC × Client-ID
- MAC × lease
- MAC × pressure
- Client-ID × lease
- MAC × Client-ID × pressure

Report:
- means/medians;
- 95% confidence intervals;
- effect sizes;
- interaction plots/heatmaps;
- not only p-values.

Use factorial regression/ANOVA-style methods when assumptions hold; robust/nonparametric/bootstrap alternatives if not.

Use binomial/logistic modeling for binary/probability outcomes.

# 69. SIMULATION ARCHITECTURE

## Client
```text
physical_client_id
current_mac
current_client_id
mac_identity_behavior
client_id_behavior
connection_state
session_start
session_end
current_lease
```

## Lease
```text
ip_address
identity_key
client_id
chaddr
lease_start
T1
T2
lease_expiration
lease_state
```

## DHCP server
```text
address_pool
active_bindings
expired_bindings
assigned_address_count
allocation_failure_count
message_counters
```

## Core events
```text
client_arrival
session_start
MAC identity selection
Client-ID selection
DHCP acquisition
lease allocation
renewal
rebinding
departure
DHCPRELEASE
silent departure
lease expiration
next session
```

Identity matching:
- Client Identifier if present;
- otherwise `chaddr`.

# 70. VALIDATION ARCHITECTURE

Main:
> Python discrete-event simulation.

Validation:
> selected representative scenarios using Kea DHCPv4 in an isolated Linux virtual network.

Potential tools:
- Linux VM/native Linux
- network namespaces
- veth/bridge
- Kea DHCPv4
- perfdhcp
- Wireshark/tshark
- Kea statistics

Validate about 8–12 representative/extreme cases, not the full factorial set.

Compare:
- active lease count over time;
- peak pool occupancy;
- assignment/failure counts;
- renewal/message counts.

Possible validation metrics:
- MAE
- RMSE
- relative error

# 71. KEA ROLE

Kea remains the preferred validation server because its documentation supports:
- Client Identifier lease matching;
- `match-client-id`;
- lease statistics;
- assigned-addresses;
- cumulative assignments;
- reclaimed leases;
- per-subnet/pool statistics;
- perfdhcp client/load generation.

Before implementation, re-check the current Kea version and exact configuration semantics.

# 72. REALISM CAUTION — MODERN OS BEHAVIOR

Do not overstate current phone rotation frequency.

Android and Apple behavior is nuanced and often relatively stable.

The simulation intentionally manipulates standards-informed DHCP-visible identity behavior, not vendor-specific OS internals.

A useful limitation:
> In some actual OSes, RCM timing and DHCP lease timing may be coupled. The controlled simulation isolates them to estimate individual and interaction effects.

# 73. GENERAL OBJECTIVE — DRAFT V1

> **The primary goal of this study is to develop and validate a standards-informed computational model for evaluating DHCPv4 lease utilization under randomized and changing MAC identity behaviors by examining the interactions among MAC identity turnover, DHCP Client-Identifier continuity, lease duration, and constrained address-pool pressure in guest-network environments.**

# 74. SPECIFIC OBJECTIVES — DRAFT V1

## Objective 1
> To identify and parameterize standards- and literature-informed MAC identity behaviors, DHCP Client-Identifier strategies, lease durations, address-pool conditions, and client session workloads for use in controlled DHCPv4 simulation and emulation experiments.

## Objective 2
> To design and implement a discrete-event computational model that simulates DHCPv4 client identification, lease acquisition, renewal, rebinding, release, expiration, MAC identity turnover, and address-pool utilization under controlled experimental conditions.

## Objective 3
> To develop an experimental validation environment using an open-source DHCPv4 implementation that reproduces selected simulated identity, lease, and pool-pressure scenarios and records corresponding DHCP lease and protocol statistics.

## Objective 4
> To evaluate the individual and interaction effects of MAC identity behavior, DHCP Client-Identifier continuity, lease duration, and address-pool pressure using lease utilization, allocation-failure rate, exhaustion probability and time, DHCP message overhead, inactive-but-valid leases, and simulation-to-emulation agreement.

# 75. SCOPE — DRAFT V1

Includes:
- DHCPv4;
- constrained guest/public network scenarios;
- standards-informed stable, periodic, and session-based DHCP-visible MAC identity behaviors;
- persistent vs rotating Client Identifier;
- selected lease durations;
- selected normalized pool-pressure levels;
- literature-informed client/session workload profiles;
- discrete-event simulation;
- selected Kea emulation validation;
- lease utilization, failures, exhaustion, lease amplification, DHCP overhead.

Does not claim full Wi-Fi-stack emulation.

# 76. LIMITATIONS — DRAFT V1

Outside scope:
- full IEEE 802.11 PHY/MAC behavior;
- RF propagation;
- scanning;
- roaming;
- interference;
- AP-controller behavior;
- device fingerprinting;
- MAC spoofing attack detection;
- tracking real users;
- BU production Wi-Fi;
- enterprise 802.1X/RADIUS/NAC;
- DHCPv6/SLAAC;
- IPv6 privacy;
- vendor OS internals beyond contextual discussion;
- new DHCP protocol;
- new RCM standard;
- ML/AI optimization.

Other limitations:
- workload is literature-informed rather than from BU logs;
- validation uses selected DHCP implementation/scenarios;
- vendor behavior can evolve;
- factors isolated in simulation may be coupled in real OSes.

# 77. OFFICIAL THESIS ALIGNMENT

## CS Domain
Primary:
**Computational Modeling and Simulation**

Secondary:
Cybersecurity / privacy-aware network computing

## Computing Contribution
Standards-informed discrete-event DHCPv4 lease-utilization model with emulation validation and interaction/threshold analysis.

## BU Agenda
Current best fit:
**Institutional Development and Policy Innovation**

Do not overclaim direct BU deployment.

## SDG
**SDG 9 — Industry, Innovation and Infrastructure**

## Beneficiary
Network administrators managing constrained guest/public networks.

## Expected Innovation
Reproducible quantitative characterization of how DHCP-visible MAC identity turnover, DHCP logical-identity continuity, lease duration, and pool pressure interact, including threshold conditions where lease amplification becomes operationally significant.

# 78. PANEL DEFENSE STRESS TEST — UPDATED

### “Obvious naman na maraming identity = maraming lease.”
Answer:
The thesis quantifies interaction effects and thresholds, especially how Client-ID continuity and lease duration alter the relationship between physical clients and valid leases.

### “DHCP optimization has already been done.”
Answer:
Correct. This thesis does not propose another optimizer. RCM-induced identity semantics are the experimental phenomenon.

### “MAC randomization affecting DHCP is already known.”
Answer:
Correct. The candidate contribution is the joint quantitative characterization of identity turnover, Client-ID continuity, lease duration, and pool pressure.

### “Simulation lang?”
Answer:
Selected scenarios are validated against Kea DHCPv4.

### “Bakit CS?”
Answer:
The output is a validated computational model, discrete-event simulation, factorial interaction analysis, and quantitative characterization.

### “Bakit hindi ML?”
Answer:
The problem is about system-state dynamics and controlled factor interactions. ML is unnecessary.

### “Realistic ba ang session-based rotation?”
Answer:
It is a standards-informed sensitivity condition, not claimed as a universal phone default.

### “Wi-Fi ba talaga ito?”
Answer:
The study models DHCP-visible consequences of changing Layer-2 identities in guest-network settings, not the entire RF stack.

### “Saan galing user behavior?”
Answer:
Published public-WLAN and campus DHCP literature plus sensitivity analysis.

### “Paano kung walang exhaustion?”
Answer:
That is a valid result. The thesis identifies regimes where effects are negligible, moderate, or service-impacting.

### “Ano ang innovation?”
Answer:
Joint, validated characterization of identity turnover × logical DHCP identity × lease duration × pool pressure, subject to continued novelty surveillance.

# 79. CURRENT KILL LIST — STILL ACTIVE

Do not revive:
- MAC changer application;
- generic MAC spoof detector;
- generic ML MAC anomaly detector;
- malicious-vs-legitimate MAC classifier;
- generic device re-identification/de-randomization;
- generic DHCP lease optimization;
- adaptive DHCP for randomized MACs;
- shorter leases for randomized clients as “innovation”;
- RCM-aware DHCP as a “new concept”;
- modern phones always change MAC every reconnect;
- new MAC always means new IP;
- DHCP relies solely on MAC;
- DHCPRELEASE always leaves IP occupied;
- RCM always causes exhaustion;
- “first ever” claims.

# 80. IMMEDIATE NEXT STEP — METHODOLOGY DRY-RUN v0

Before polished proposal writing, implement the smallest useful proof.

## Dry-run objectives
1. Verify simplified DHCP state machine.
2. Verify persistent vs rotating Client-ID semantics.
3. Verify renewal/release/expiration logic.
4. Confirm identity turnover can produce measurable differences in valid lease count.
5. Validate selected scenario(s) against Kea DHCPv4.
6. Determine whether the result is nontrivial enough for the full factorial study.
7. Catch implementation errors before topic lock.

## Suggested minimal dry-run
Use only:
- 1 pool size;
- 1 workload profile;
- 2 pressure levels;
- 2 lease durations;
- 3 MAC identity conditions;
- 2 Client-ID conditions.

Do not immediately build all 72 configurations.

## Dry-run success criteria
- correct DHCP lifecycle;
- correct identity matching;
- interpretable lease-utilization differences;
- meaningful interaction rather than only trivial monotonic behavior;
- reasonable simulation-vs-Kea agreement.

If dry-run fails or differences vanish:
diagnose honestly; do not force the thesis.

# 81. TOPIC LOCK CONDITION

Lock the topic only when:
1. no fatal directly overlapping peer-reviewed paper is found;
2. simulator behaves correctly;
3. persistent vs rotating Client-ID is reproduced correctly;
4. Kea validation is feasible;
5. outcomes are measurable and interpretable;
6. cost remains near zero;
7. computational modeling remains the primary contribution;
8. the user is comfortable explaining the DHCP identity/lease model.

# 82. AFTER TOPIC LOCK

Draft the actual Topic Proposal in this order:

1. Final Title
2. CS Domain / Computing Contribution / BU Agenda / SDG / Beneficiary / Expected Innovation
3. Final Problem Statement
4. Final Research Gap
5. Background
6. Introduction of the Proposed Solution
7. General Objective
8. Four Specific Objectives
9. Scope and Limitations
10. Preliminary Methodology summary
11. RRL source map
12. Conceptual framework figure

Follow the official CS 124 template exactly.

# 83. CURRENT ONE-SENTENCE STATUS

> **The strongest surviving thesis direction is a near-zero-cost, standards-informed, discrete-event simulation and Kea-validated study that quantifies when DHCP-visible randomized/changing MAC identity turnover, DHCP Client-Identifier continuity, lease duration, and constrained address-pool pressure produce negligible, moderate, or service-impacting DHCPv4 lease amplification; the topic is proposal-capable but should not be formally locked until a small Methodology Dry-Run v0 succeeds.**

# 84. UPDATED CONTINUATION PROMPT FOR A NEW AI

> **Continue from this handoff. The topic is not yet formally locked. Do not write the polished proposal first. Perform the Methodology Dry-Run v0 plan: verify the DHCP state model, persistent-vs-rotating Client-ID behavior, lease renewal/release/expiration, and selected Kea DHCPv4 validation. Continue to search for any directly overlapping peer-reviewed study. If the dry-run works and no fatal overlap appears, lock the topic and then draft the Topic Proposal according to my official CS 124 template.**
