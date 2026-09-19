# PISO-WIFI SECURITY THESIS HANDOFF — LATEST CANONICAL CONTEXT

## STATUS OF THIS FILE

This file is the **latest canonical continuation context** for the user's BS Computer Science thesis planning.

It supersedes all previous thesis handoff files and all older cybersecurity narrowing states, including:

- the older DAST/CORS handoffs;
- the broader WPA2 topic-exploration state;
- the first generic WPA2 Deep Research report;
- the initial unverified Gemini Piso-WiFi recommendations.

The next AI should treat this file as the current truth and continue from the exact state below without making the user re-explain prior conversations.

The user explicitly wants continuity such that the next AI behaves as if it had participated in the whole conversation.

Do not reopen settled decisions unless the user explicitly asks.

---

# USER WORKING STYLE

- Main language: **Taglish**
- Prefer practical, direct, technically honest explanations
- Avoid unnecessary jargon
- Avoid long academic prose unless needed
- The user values being corrected and explicitly does **not** want the AI to blindly accept technical assumptions
- The user is interested in cybersecurity, especially Wi-Fi/WPA/WPA2 topics
- The user has practical familiarity with WPA/WPA2 handshake capture and brute-force concepts from a past tutorial
- The user is not claiming expert-level mastery of wireless security
- The user wants the thesis to be in a field they genuinely understand and enjoy
- The user strongly prefers low-cost work
- Preferred additional budget ceiling: approximately **PHP 3,000**
- Strong preference for no extra hardware purchase if possible
- Do not force ML/AI
- Do not jump to a final title too early
- Do not confuse geographic focus with novelty
- When Deep Research is used, the user prefers uploading the report here for auditing rather than reading it alone

---

# BROADER THESIS REQUIREMENTS

The thesis is for BS Computer Science.

The project must contain a substantial computing contribution such as:

- cybersecurity mechanism;
- algorithm;
- detection method;
- verification framework;
- protocol;
- stateful analysis;
- formal model;
- data-driven method;
- intelligent or computational system.

A software interface, dashboard, scanner wrapper, or ordinary information system alone is not enough.

The final proposal must eventually identify:

- CS domain;
- computing contribution;
- research gap;
- beneficiary;
- expected innovation;
- evaluation method;
- feasible scope;
- BU research agenda alignment;
- SDG alignment.

The user’s university values:

- originality;
- applicability;
- social impact;
- technical feasibility;
- strong methodology;
- clear figures/tables;
- well-defined research problem.

---

# IMPORTANT HISTORICAL CONTEXT

## Previous rejected direction

The group previously explored CORS post-scan behavioral analysis for OWASP ZAP.

That idea was eventually rejected because:

- ZAP already performs active CORS behavioral checks;
- comparable tools already do similar testing;
- proposed labels risked duplicating scanner confidence/risk;
- the ML dataset design risked circular labeling;
- the supposed novelty was not defensible.

This history matters because the current process must continue to be adversarial:

> **Problem first, solution later.**

Do not repeat the CORS mistake of designing a system before proving the problem is genuinely unresolved.

## WPA2 broad exploration

The user later switched to WPA2-related wireless security because it is a field they understand.

A broad WPA2 Deep Research report was generated.

The report’s initial top candidates included:

- generalizable Wi-Fi IDS;
- explainable/lightweight Wi-Fi IDS;
- rogue AP detection;
- WPA2/WPA3 downgrade detection;
- Wi-Fi posture assessment.

After auditing, several problems were found:

- generic AWID cross-dataset generalization had already been substantially studied;
- lightweight IDS was not novel by itself;
- client-side evil twin detection had a long prior-art history;
- WPA3 downgrade detection already had recent dedicated work and a public dataset;
- Wi-Fi posture auditor was too close to existing tools and too weak as a CS contribution.

However, one **new and locally relevant research family** emerged:

> **Piso-WiFi / pay-for-use Wi-Fi security in the Philippines**

That became the current active direction.

---

# WHY PISO-WIFI BECAME THE ACTIVE DIRECTION

A recent 2026 paper:

> **“Open Challenges for Secure and Scalable Wi-Fi Connectivity in Rural Areas”**

studied pay-for-use Wi-Fi in the Philippines and India.

For the Philippines, it examined Piso-WiFi and experimentally demonstrated:

1. **Paid-session hijacking / user masquerading**
2. **Rogue or fake Piso-WiFi hotspot attacks**

The paper is important because it proves the problem is real and current.

But the paper mainly:

- demonstrated the attacks;
- framed threat models;
- proposed possible defensive directions;
- did not implement and validate a production-ready low-cost defense.

This created a plausible thesis search space.

Important:

> The thesis must not merely repeat the 2026 attack demonstrations.

Do not propose:

- another MAC/IP spoofing demo;
- another rogue AP demo;
- another barangay vulnerability survey;
- a dashboard of Piso-WiFi weaknesses;
- a generic scanner;
- “Piso-WiFi security assessment in Barangay X” as novelty.

---

# CURRENT EVIDENCE BASE

Two dedicated Deep Research reports were compared:

## Gemini report

Main recommendations:

1. TCP/RSSI/IPID-based gateway-side spoof detection
2. Pause-resume state machine verification
3. Browser-native WebAuthn/RFC 8910 rogue AP validation
4. Client-isolation verification

Useful contributions from the Gemini report:

- detailed ecosystem reconstruction;
- highlighted paid-session hijacking;
- surfaced pause/resume and continuity issues;
- correctly rejected unnecessary ML;
- proposed small lab tests.

But several claims were overconfident or weak:

- RSSI/sequence-based spoof detection is not automatically novel;
- TCP anomalies are not inevitable;
- RSSI may not be visible at the actual Piso gateway;
- pause/resume race-condition evidence was weak and unverified;
- WebAuthn does not automatically authenticate the wireless AP;
- weighted rankings gave false precision.

The Gemini report must therefore be treated as a source of technical suspects, not final truth.

## ChatGPT Deep Research report

This report was stronger and more cautious.

It reframed the problem as:

> **Gateway-side, stateful paid-session ownership verification using gateway-observable events**

rather than immediately locking into TCP/RSSI/IPID features.

It also recognized important prior art:

- MikroTik duplicate-MAC protections;
- Cisco NAC anomaly detection;
- enterprise endpoint profiling;
- CAPPORT/session APIs;
- hotspot product resume/continuity features;
- existing AP isolation controls;
- existing Enterprise/Passpoint/TOFU/SAE-PK mechanisms.

The ChatGPT report concluded that the strongest surviving research space is:

1. **Gateway-side session ownership anomaly detection**
2. **Secure continuity and anti-replay for pause/resume or device migration**
3. **Cross-family session-binding assessment with an attached verifier**

This is the current corrected shortlist.

---

# CURRENT ACTIVE THESIS FAMILY

The current active field is:

> **Defensive security of paid sessions in Piso-WiFi / pay-for-use captive portal systems**

The most promising central problem is:

> **How can a low-cost hotspot detect or constrain suspicious paid-session ownership changes using only gateway-visible events, without requiring client applications, expensive enterprise infrastructure, or specialized wireless hardware?**

This is not yet a finalized thesis topic.

It is still a candidate problem family that must survive a small empirical sanity test.

---

# CURRENT STRONGEST CANDIDATE

## Candidate 1 — Gateway-Side Paid-Session Ownership Verification

### Core problem

Piso-WiFi hotspots often authorize paid access using weak or transferable identifiers such as:

- MAC address;
- IP address;
- captive portal session state;
- cookies;
- session tokens;
- resume codes.

The 2026 paper demonstrated that a paid session can be hijacked through MAC/IP impersonation.

The remaining problem is not proving that hijacking exists.

The remaining problem is:

> **Can the gateway distinguish legitimate reconnect or continuity from malicious paid-session takeover?**

### Correct technical framing

Do not frame the contribution as:

> “MAC spoofing detection”

That is too broad and has prior art.

Do not frame it as:

> “RSSI-based spoof detector”

That is too early, hardware-dependent, and not necessarily novel.

Do not frame it as:

> “TCP sequence anomaly detector”

That is not guaranteed to work if the legitimate client is already gone.

The better current framing is:

> **A stateful hotspot-side detector that models the lifecycle of a prepaid session and flags suspicious ownership changes using gateway-observable events.**

### Possible gateway-visible events

Candidate observables include:

- login event;
- logout event;
- payment/activation event;
- session start;
- session stop;
- idle timeout;
- pause event;
- resume event;
- reconnect time;
- MAC change;
- IP change;
- DHCP lease change;
- cookie or token reuse;
- continuity/resume token use;
- session bytes;
- session duration;
- old/new device identity;
- concurrent use;
- session migration;
- interface or hotspot-node change;
- repeated failed reattachment;
- sudden continuity state change.

The exact feature set is not final.

### Possible analysis style

Prefer:

- finite-state machine;
- stateful rule engine;
- event-sequence validation;
- soft enforcement;
- optional simple statistics.

Do not use ML by default.

### Why this candidate is promising

- real problem already experimentally proven;
- low-cost;
- locally relevant;
- directly tied to pay-for-use logic;
- possible substantial CS contribution;
- does not require building a whole wireless IDS;
- can be tested in a controlled lab;
- may generalize across hotspot implementation families.

### Main technical risk

The biggest risk is:

> Legitimate reconnects, device changes, pause/resume, or continuity actions may look too similar to malicious takeover using only gateway telemetry.

If benign and malicious traces are not separable, this idea should be killed or reframed.

---

# SECOND STRONGEST CANDIDATE

## Candidate 2 — Secure Pause/Resume or Device-Migration Protocol

### Core problem

Some Piso-WiFi products support:

- pause;
- resume;
- resume codes;
- continuity across devices or hotspot nodes;
- session migration.

These features are useful, but may create replay or sharing risks.

The research question is:

> **Can a prepaid session be paused, resumed, or migrated securely without becoming a replayable or shareable bearer token?**

### Possible computing contribution

- one-time continuity token;
- expiry rules;
- replay protection;
- challenge-response;
- prior-identity invalidation;
- secure state transition;
- browser-mediated migration;
- device-change confirmation;
- continuity protocol without custom app.

### Main technical risk

Existing products already provide resume and continuity features.

The contribution must therefore be more than “add a resume code.”

The novelty must be in:

- anti-replay semantics;
- secure state transitions;
- identity binding;
- migration verification;
- usability-security trade-off.

### Current status

> **GO, BUT REFRAME**

Promising, but must be differentiated carefully from commercial continuity features.

---

# THIRD CANDIDATE

## Candidate 3 — Cross-Family Session-Binding Assessment with Verifier

### Core problem

Piso-WiFi is not one single architecture.

Important implementation families include:

- MikroTik/RouterOS-based systems;
- Linux SBC-based systems;
- OpenWrt/openNDS-like systems;
- cloud-managed systems;
- vendor-specific commercial stacks.

These may bind payment to session ownership differently.

Possible research question:

> **Can a standardized and reproducible verifier reveal meaningful differences in session-binding strength across common Piso-WiFi implementation families?**

### Required contribution

This cannot be a simple comparative survey.

It needs:

- formalized session-binding invariants;
- standardized scenario corpus;
- automated verifier;
- repeatable metrics;
- defensive interpretation.

### Main risk

It can collapse into:

> “We tested several vendors and listed differences.”

That would be weak.

### Current status

> **GO, BUT REFRAME**

Useful as a backup or combined validation framework, but weaker than Candidate 1.

---

# OTHER DIRECTIONS AND CURRENT STATUS

## Rogue Piso-WiFi authentication

General hotspot authenticity is not an open problem because strong mechanisms already exist:

- WPA2/WPA3-Enterprise;
- certificate validation;
- Passpoint;
- TOFU;
- SAE-PK;
- CAPPORT-related standards;
- profile provisioning.

The potentially open design corner is:

> low cost + old-phone compatibility + low operator complexity + preferably no app

However, this is high-risk because:

- the 2026 paper already proposed QR, TOFU, SAE-PK, Enterprise, Passpoint, LED OOB;
- WebAuthn does not automatically bind the user to the physical AP;
- captive portal mini-browser restrictions may break browser-native cryptography;
- the work can drift into protocol design too complex for the schedule.

Current status:

> **High-risk, not the first choice**

## Client isolation

Basic AP isolation exists already.

Recent research shows deeper bypasses, but a simple checker would be too weak.

Current status:

> **Not recommended as the primary thesis**

It may be used as an evaluation dimension, not the main contribution.

## Pause/resume race condition

Gemini suggested a race-condition vulnerability.

But the evidence was weak and not reliably reproduced.

Current status:

> **Unverified lead only**

Do not treat it as a known confirmed vulnerability.

## RSSI/TCP/IPID detector

This was Gemini’s top concrete mechanism.

Current status:

> **Do not lock this in**

Reasons:

- prior art exists;
- RSSI may not be available at the gateway;
- TCP anomalies are not inevitable;
- IPID behavior varies;
- false positives may be high;
- it may only work during simultaneous legitimate/attacker activity.

These may later become optional features only if empirical evidence supports them.

---

# WHAT IS SETTLED

Do not reopen these unless the user asks:

- The current active field is Piso-WiFi security
- The thesis should remain defensive and authorized
- The 2026 paper already proved paid-session hijacking
- The 2026 paper already proved rogue hotspot attacks
- Repeating those demonstrations is not thesis novelty
- A barangay is not novelty by itself
- A local deployment can only serve as a validation site
- Generic WPA2 brute forcing is rejected
- Generic Wi-Fi IDS is not the current focus
- Wi-Fi posture auditor is rejected
- Basic client-isolation checker is weak
- ML is not currently justified
- Stateful algorithms and rules are preferred
- Gateway-visible data should be preferred over monitor-mode/RF features
- The strongest current candidate is session ownership verification
- The next step is a small empirical sanity check, not a final title

---

# WHAT IS NOT FINAL

Do not assume the following are locked:

- final thesis title;
- final research-gap wording;
- exact hotspot platform;
- exact implementation stack;
- exact features;
- exact state machine;
- exact enforcement action;
- exact number of platforms;
- exact barangay or municipality;
- exact vendor;
- exact hardware;
- exact evaluation metrics;
- exact proposal wording;
- whether Candidate 1 or Candidate 2 ultimately wins;
- whether session continuity becomes part of Candidate 1;
- whether two hotspot families can be tested;
- whether a real Piso machine is needed.

---

# MOST IMPORTANT NEXT STEP

The immediate next step is:

## **Design and run a small controlled session-ownership sanity experiment**

The purpose is to answer:

> **Are legitimate reconnect/continuity events and malicious takeover events distinguishable using only low-cost gateway-visible telemetry?**

Do not proceed to final proposal writing until this is answered.

---

# RECOMMENDED MINIMAL EXPERIMENT

## Minimum equipment

Prefer:

- one owned or authorized hotspot stack;
- one router/AP or laptop-based hotspot;
- one admin laptop;
- two client devices;
- no extra hardware purchase if possible.

Possible stacks:

- MikroTik HotSpot;
- OpenWrt + openNDS;
- Linux captive portal;
- AdoPiSoft only if legally and technically accessible;
- another controlled open-source hotspot stack.

Do not use live public Piso-WiFi without explicit operator consent.

## Three mandatory scenarios

### Scenario A — Normal reconnect

1. User pays/activates session
2. User disconnects
3. User reconnects normally
4. Log all gateway events

### Scenario B — Legitimate continuity action

Depending on platform support:

- pause/resume;
- resume code;
- reconnect after idle;
- legitimate device migration;
- session restoration.

If platform does not support this, choose the closest legitimate continuity flow.

### Scenario C — Authorized session takeover simulation

On owned devices only:

1. Create paid session on Device A
2. Simulate identity takeover on Device B
3. Observe gateway logs and state transitions
4. Do not test on public or unauthorized systems

The goal is not to publish the attack.

The goal is to collect defensive traces.

---

# DATA TO COLLECT

Collect only what is realistically available at the gateway.

Candidate logs:

- timestamp;
- client MAC;
- client IP;
- DHCP lease;
- login/logout;
- portal authentication event;
- session identifier;
- payment activation;
- pause/resume;
- token or cookie reuse;
- bytes transferred;
- session duration;
- connection start/stop;
- old identity;
- new identity;
- hotspot node/interface;
- duplicate identity event;
- forced reauthentication;
- continuity code use;
- session expiration;
- unexpected state transition.

Do not assume RSSI unless the selected platform exposes it reliably.

Do not assume raw 802.11 monitor-mode captures are necessary.

---

# SANITY-CHECK SUCCESS CRITERIA

Continue Candidate 1 if:

- takeover produces a meaningfully different event sequence;
- at least one feature is available at the gateway;
- a simple stateful baseline can separate attack vs legitimate behavior;
- false-positive risk appears manageable;
- the approach adds value beyond duplicate-MAC blocking;
- the same logic may generalize to another hotspot stack.

Kill or reframe Candidate 1 if:

- malicious and legitimate traces are indistinguishable;
- the only useful signal is simultaneous duplicate MAC;
- existing platform defenses already fully handle the tested scenarios;
- specialized wireless monitoring is required;
- false positives are too high;
- the mechanism would frequently block legitimate users.

---

# EXPECTED ANALYSIS STYLE

After collecting traces:

1. Draw the session lifecycle
2. Mark valid state transitions
3. Mark suspicious state transitions
4. Compare three scenarios
5. Identify candidate invariants
6. Build a minimal rule/state baseline
7. Test repeatability
8. Decide whether the problem survives

Possible outputs:

- event-sequence diagram;
- state-transition table;
- session lifecycle model;
- suspicious transition rules;
- baseline confusion matrix;
- detection latency;
- user interruption cost.

---

# POSSIBLE EVALUATION METRICS LATER

If Candidate 1 survives:

- True Positive Rate
- False Positive Rate
- Precision
- Recall
- F1-score
- Detection latency
- CPU usage
- Memory usage
- User interruption rate
- Successful legitimate reconnect rate
- Successful continuity rate
- Cross-platform consistency
- Repeatability

Do not use ML metrics unless ML is later justified.

---

# CURRENT CAUTIOUS RESEARCH-GAP DIRECTION

Use only as provisional wording:

> Existing research has experimentally demonstrated paid-session hijacking in Piso-WiFi, while current hotspot platforms provide authentication, accounting, duplicate-MAC controls, and continuity features. However, a remaining gap may exist in low-cost, gateway-side verification of prepaid session ownership during reconnect, pause/resume, device migration, and identity changes without requiring client applications or enterprise onboarding.

Do not claim:

- no existing system;
- first of its kind;
- completely novel;
- no current defenses.

---

# CURRENT PROVISIONAL COMPUTING-CONTRIBUTION DIRECTION

Use only as provisional wording:

> A stateful hotspot-side session ownership verification mechanism that models prepaid session lifecycles and detects suspicious identity transitions using gateway-observable events.

Alternative if continuity becomes central:

> A secure state-transition and anti-replay protocol for prepaid hotspot session pause, resume, and migration.

Alternative if cross-platform comparison becomes central:

> A standardized session-binding assessment methodology and automated verifier for heterogeneous Piso-WiFi hotspot implementations.

---

# SIMPLE TAGLISH EXPLANATION FOR GROUPMATES

> Nakafocus na tayo ngayon sa Piso-WiFi paid-session security.
>
> Yung 2026 paper naprove na na puwedeng ma-hijack ang paid session gamit ang MAC/IP impersonation at puwedeng gumawa ng rogue Piso-WiFi.
>
> Hindi na natin uulitin yung attack.
>
> Ang gusto nating malaman ngayon ay kung kaya bang gumawa ng low-cost gateway-side mechanism na makakadetect kung legitimate reconnect/pause/resume/device change ba ang nangyayari o may nang-aagaw ng paid session.
>
> Hindi muna tayo gagamit ng ML.
>
> Ang initial plan ay gumawa ng controlled hotspot at ikumpara ang logs ng:
> 1. normal reconnect,
> 2. legitimate continuity action,
> 3. authorized session takeover simulation.
>
> Kapag distinguishable ang traces gamit lang ang gateway logs, viable ang thesis.
>
> Kapag hindi distinguishable o duplicate-MAC check lang ang result, papatayin o ire-reframe natin agad ang idea.

Short version:

> **The 2026 paper proved the attack. Our possible contribution is a low-cost stateful gateway mechanism that verifies prepaid session ownership during reconnect, pause/resume, and device changes. The next step is a small lab sanity test to see whether legitimate and malicious traces are actually distinguishable.**

---

# DO NOT DO THESE NEXT

Do not:

- generate final thesis titles yet;
- write the full proposal yet;
- add ML;
- buy hardware immediately;
- design a full dashboard;
- scan public Piso-WiFi;
- contact operators before the lab concept is clear;
- assume the attack trace is separable;
- assume RSSI is needed;
- assume AdoPiSoft or MikroTik is representative of all Piso-WiFi;
- claim novelty from barangay focus;
- claim no existing defenses.

---

# RECOMMENDED NEXT CONVERSATION ACTION

The next AI should help the user answer:

1. What hotspot stack is easiest and legal to set up?
2. What equipment does the group already have?
3. Which legitimate continuity scenario is available?
4. Which gateway logs can be collected?
5. What exact state transitions should be modeled?
6. What would count as a successful sanity test?
7. What would kill the idea?

Then produce a minimal experiment plan.

---

# ONE-LINE CURRENT STATUS

> The thesis search has narrowed from broad WPA2 security to Piso-WiFi paid-session ownership defense. The 2026 paper already proved session hijacking, so the current strongest candidate is not another attack demonstration but a low-cost, stateful gateway-side mechanism that distinguishes legitimate reconnect or continuity from suspicious session takeover using gateway-visible events. The idea is not yet final and must first survive a small controlled sanity experiment.
