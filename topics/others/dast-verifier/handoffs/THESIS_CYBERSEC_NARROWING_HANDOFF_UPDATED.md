# THESIS CYBERSEC NARROWING HANDOFF

## PURPOSE OF THIS FILE

This file is the canonical continuation context for the user's BS Computer Science thesis planning.

The user may move to another AI chat at any time. The next AI should read this file and continue from the **latest state** without making the user re-explain prior decisions.

The goal is continuity. Do not reopen settled steps unless the user explicitly asks.

---

# USER WORKING STYLE

- Main language: **Taglish**
- Prefer practical, direct, easy-to-understand explanations
- Avoid long academic explanations unless needed
- The user often has **very limited time to read**
- When Deep Research is used, do **not** ask the user to read the full report
- Summarize only:
  - strongest findings
  - genuine research gaps
  - feasibility
  - implementation implications
  - final verdict
  - next step
- Do not jump to a final title too early
- The user cares a lot about **actual feasibility**
- For groupmate-facing explanations, use simple Taglish
- Current stage is no longer topic dumping

---

# BROADER THESIS PROJECT CONTEXT

The group already completed a large topic-dumping phase across many CS domains.

Completed topic-bank batches include:

- Wide CS Topic Bank
- Cybersecurity General
- LAN/WLAN/Internal Network Security
- AI / ML / Predictive Analytics
- NLP / RAG / LLM / AI Agents
- Computer Vision / Image Processing / Video Analytics
- Disaster / Climate / Environment / Geospatial AI
- Agriculture / Food Security / Smart Farming
- Education / Learning Analytics / Campus Intelligence
- Healthcare / Public Health / Mental Health Computing
- IoT / Edge AI / Smart Devices / Digital Twins
- Software Engineering / AI-Assisted Development
- HCI / Accessibility / Assistive Technology
- Games / AR / VR / Serious Simulations
- Tourism / Culture / Local Navigation
- Business / MSME / Governance Analytics
- Blockchain / Emerging Computing / Digital Identity

The **domain topic-dumping phase is complete**.

The current phase is:

> **Narrowing → research-gap validation → feasibility validation → proposal construction**

---

# CURRENT CYBERSECURITY NARROWING

The user narrowed interest to three cybersecurity research families:

1. Malware Analysis
2. Vulnerability Detection
3. Intrusion Detection

The agreed strategy is:

- Research them **one at a time**
- Do not compare all three at once
- For each field, identify:
  - current approaches
  - recurring limitations
  - genuine research gaps
  - novelty opportunities
  - undergraduate feasibility
  - public datasets/test environments
  - prototype potential
  - evaluation metrics

Recommended order:

1. Vulnerability Detection
2. Malware Analysis
3. Intrusion Detection

Current active field:

> **Vulnerability Detection**

More specifically:

> **Deployed web application vulnerability analysis using DAST**

---

# CRITICAL CLARIFICATION: WHAT THE USER MEANS BY VULNERABILITY DETECTION

The user does **not** mean source-code vulnerability detection.

The first research run accidentally focused on:

- SAST
- source code scanning
- CodeQL
- Semgrep
- line-level vulnerability detection
- dependency analysis

That is not the user's intended idea.

The user's actual idea is:

> A website is already deployed. The system scans the deployed website using its URL and analyzes vulnerabilities.

Correct research family:

- Dynamic Application Security Testing (DAST)
- Black-box Web Vulnerability Scanning
- Deployed Web Application Vulnerability Analysis

Core flow:

```text
Authorized Deployed Website
        ↓
Enter URL
        ↓
OWASP ZAP Performs Initial Scan
        ↓
Raw Selected Findings
        ↓
Proposed Verification Layer
        ↓
Context / Behavior / Evidence Analysis
        ↓
Confirmed / Needs Review / Downgraded
        ↓
Confidence + Explanation
        ↓
Prioritized Report
```

Testing must stay within:

- local lab targets
- intentionally vulnerable applications
- university-controlled systems
- explicitly authorized websites

Never frame the project as scanning arbitrary public websites.

---

# MAIN RESEARCH CONCLUSION SO FAR

Simply creating another scanner is weak.

Weak framing:

> “We created a web vulnerability scanner.”

Stronger framing:

> “We improve the reliability of selected DAST findings by applying context-aware verification and confidence ranking.”

The proposed system uses OWASP ZAP as the **baseline detector**.

The group's contribution is the layer **after** the scan.

---

# CURRENT PROPOSED THESIS CONCEPT

Simple Taglish:

> Gagamit ang system ng OWASP ZAP para sa initial vulnerability scanning ng authorized deployed website. Pagkatapos, may sariling verification layer ang system na kumukuha ng additional evidence para sa selected findings under Security Headers, Cookie Security, at CORS. Based sa context at behavior ng website, nire-rank ang findings as Confirmed, Needs Review, o Downgraded, kasama ang explanation kung bakit.

Short form:

> **ZAP detects. Our system verifies, contextualizes, and prioritizes.**

Current proposed contribution:

> **A context-aware rule-based verification and confidence-ranking framework for selected DAST findings.**

---

# FEASIBILITY CORRECTION

The broad version is infeasible.

Reject:

> Scan any website, verify every vulnerability type, remove all false positives.

The realistic version is:

> Use OWASP ZAP for initial scanning, then verify only selected categories on controlled or authorized targets.

Do not build:

- a browser engine
- a full crawler from scratch
- an exploit framework
- a universal scanner
- a Burp Suite replacement

Use ZAP as the initial detector.

---

# FINAL CATEGORY VALIDATION STATUS

Three categories were researched one at a time at implementation-feasibility level.

## 1. Security Headers

Final verdict:

> **KEEP, but NEEDS PARTNER CATEGORY**

Role:

> **Supporting deterministic module**

Why:

- very feasible
- easy to automate
- clear ground truth
- good for contextual filtering
- too simple to be the whole thesis alone

Selected alert families:

- CSP
- HSTS
- Anti-clickjacking
- optionally X-Content-Type-Options

Strong recommendation:

> Keep CSP, HSTS, and anti-clickjacking as the main header set.

Possible contextual checks:

- HTML vs JSON/API/static resource
- sensitive page vs public page
- final response vs redirect
- HTTP vs HTTPS
- alternate protection such as CSP `frame-ancestors`
- authenticated vs anonymous route

Possible output:

- Confirmed
- Needs Review
- Downgraded

---

## 2. Cookie Security

Final verdict:

> **KEEP**

Role:

> **Secondary contextual module**

Selected alerts:

- Missing `HttpOnly`
- Missing `Secure`
- Missing / invalid `SameSite`

Main research finding:

Raw cookie alerts often lack context.

The proposed verifier can check:

- Is it a session/authentication cookie?
- Did it appear only after login?
- Is the app using HTTPS?
- Is the cookie used across authenticated routes?
- What are the Path and Domain?
- Is it persistent?
- Is `SameSite=None` used without `Secure`?
- Is it a harmless analytics/tracking cookie?

Cookie Security alone is not enough for the whole thesis, but it is a strong partner category.

---

## 3. CORS

Final verdict:

> **KEEP**

Role:

> **Main technical module**

This is the strongest technical category of the three.

Main verification logic:

- send requests with different `Origin` values
- check arbitrary-origin reflection
- inspect `Access-Control-Allow-Origin`
- inspect `Access-Control-Allow-Credentials`
- compare trusted vs untrusted origins
- send safe preflight `OPTIONS`
- compare preflight vs actual response
- check route/resource sensitivity
- distinguish public/static resources from sensitive/authenticated endpoints

Strong case:

```text
Fake origin accepted
+
Credentials allowed
+
Sensitive/authenticated endpoint
=
CONFIRMED
```

Weak case:

```text
Wildcard CORS
+
No credentials
+
Public static resource
=
DOWNGRADED
```

CORS gives the project most of its technical personality.

---

# FINAL CATEGORY HIERARCHY

## Main technical contribution

### CORS Verification

Focus on:

- arbitrary-origin reflection
- wildcard-origin behavior
- credential-enabled CORS
- optional `null` origin handling

## Secondary technical contribution

### Cookie Security Verification

Focus on:

- missing `HttpOnly`
- missing `Secure`
- missing or invalid `SameSite`

## Supporting module

### Security Headers Verification

Focus on:

- CSP
- HSTS
- anti-clickjacking

Optional:

- X-Content-Type-Options

Current recommendation:

> **Keep all 3 categories.**

Do not treat them as equal.

Hierarchy:

```text
CORS = main technical module
Cookie Security = secondary contextual module
Security Headers = supporting deterministic module
```

---

# CURRENT SYSTEM ARCHITECTURE

```text
User enters authorized URL
        ↓
OWASP ZAP scans website
        ↓
System retrieves selected alerts
        ↓
┌─────────────────────────────┐
│ Security Headers Verifier   │
│ Cookie Security Verifier    │
│ CORS Verifier               │
└─────────────────────────────┘
        ↓
Evidence + Context Analysis
        ↓
Verification Rules
        ↓
Confirmed / Needs Review / Downgraded
        ↓
Confidence + Explanation
        ↓
Final Prioritized Report
```

Possible modules:

1. ZAP integration
2. Alert parser and normalizer
3. Evidence collector
4. Category-specific verifier
5. Confidence-ranking engine
6. Explanation generator
7. Results dashboard

Important:

> Do not force Machine Learning.

Start with a **rule-based framework**.

Only use ML if later evidence clearly shows:

- enough labeled data exists
- it improves the contribution
- the group can handle the added complexity

---

# CURRENT MINIMUM VIABLE SCOPE

Security Headers:

- CSP
- HSTS
- anti-clickjacking

Cookie Security:

- missing `HttpOnly`
- missing `Secure`
- missing/invalid `SameSite`

CORS:

- wildcard origin
- arbitrary-origin reflection
- credential-enabled CORS
- optional `null` origin handling

Do not add yet:

- XSS
- SQL injection
- CSRF
- BOLA
- full API security
- custom crawler
- broad OWASP Top 10 coverage

The project should stay focused.

---

# CURRENT TEST ENVIRONMENT PLAN

Primary:

## Custom controlled mini lab

Reason:

- deterministic ground truth
- easy to create secure/insecure variants
- easy to reproduce
- ideal for true-positive / false-positive evaluation

Possible routes:

```text
/login-no-csp
/login-with-csp
/https-no-hsts
/page-with-frame-ancestors

/login-no-httponly
/login-no-secure
/login-no-samesite
/tracking-cookie

/no-cors
/wildcard-public
/reflect-any-origin
/credentials-enabled
/null-origin
/trusted-origin-only
/sensitive-api
/static-resource
```

Secondary realism checks:

- OWASP Juice Shop
- OWASP crAPI
- optionally WebGoat or DVWA

Do not use all of them unless necessary.

---

# CURRENT EVALUATION DESIGN

Baseline:

> **Raw OWASP ZAP findings**

Proposed:

> **OWASP ZAP + context-aware verification layer**

Metrics:

- Precision
- Recall
- F1-score
- False Positive Rate
- False-positive reduction
- Verification time
- Coverage
- optional ranking accuracy

Main research-question pattern:

> Does the proposed verification layer improve the precision and prioritization of selected DAST findings without causing an unacceptable loss in recall?

---

# CURRENT READINESS FOR JULY 11 PROPOSAL

Deadline:

> **July 11, 2026**

Current concept readiness:

> **Approximately 75–80%**

Already clear:

- General field
- DAST focus
- Baseline scanner
- Candidate categories
- Main module
- Supporting modules
- Basic architecture
- Feasibility
- Testing approach
- Evaluation metrics

Still missing before final title/proposal:

1. **Exact research-gap wording**
2. **Exact computing-contribution wording**
3. **Final scope boundaries**
4. **Final novelty / similar-work check**
5. **3–5 title variants**
6. **Final provisional title**
7. **Full proposal draft**

The project does **not** need major narrowing from 3 categories to 1 at this point.

What needs narrowing is:

> exactly what verification logic each category includes

---

# CURRENT RECOMMENDED RESEARCH GAP DIRECTION

Approximate problem framing:

> Existing DAST scanners such as OWASP ZAP can detect potential web security issues, but raw findings may lack sufficient application context and behavioral verification, limiting their reliability and prioritization.

Proposed gap direction:

> The study will investigate whether additional contextual and behavioral evidence can improve the verification and prioritization of selected DAST findings.

This wording is still provisional.

Do not lock it until the final novelty check is done.

---

# CURRENT COMPUTING CONTRIBUTION DIRECTION

Do not say:

> “We integrated OWASP ZAP.”

That is not enough.

Use something like:

> **A context-aware rule-based verification and confidence-ranking framework that combines scanner alerts with additional HTTP, route, session, and behavioral evidence.**

Conceptual core:

```text
ZAP Alert
   +
Response Context
   +
Repeated Observation
   +
Category-Specific Evidence
   ↓
Verification Rules
   ↓
Confirmed / Needs Review / Downgraded
   +
Explanation
```

This is the likely computing heart of the thesis.

---

# PROPOSAL MAPPING CURRENTLY RECOMMENDED

## CS Domain

Cybersecurity / Web Application Security

## Computing Contribution

Context-Aware Rule-Based Verification and Confidence-Ranking Framework for DAST Findings

## BU Agenda

Global Competitiveness of Business and Industry

## SDG

SDG 9: Industry, Innovation and Infrastructure

## Primary Beneficiaries

- web developers
- organizations maintaining deployed web applications
- security testers working in controlled or authorized environments

## Expected Innovation

Post-scan verification of selected DAST findings using category-specific contextual and behavioral evidence.

---

# CURRENT MOST IMPORTANT NEXT STEP

The next exact step is:

## Final novelty and similar-work validation

This should use Deep Research.

Exact research question:

> **Has a context-aware post-scan verification framework already been developed that combines OWASP ZAP findings across CORS, cookie security, and security headers using additional behavioral and contextual evidence? What are the closest existing studies or systems, and what defensible gap remains for an undergraduate thesis?**

The goal is to determine:

1. What is the closest existing work?
2. Does something already do the same combined architecture?
3. What part is genuinely different?
4. What exact gap can be defended?
5. What wording is safest for the proposal?
6. Is the scope still novel enough?
7. Should all 3 categories remain?

This is the **last major Deep Research step before title finalization**.

---

# AFTER THE FINAL NOVELTY CHECK

Do this sequence:

## Step 1

Lock the exact research gap.

## Step 2

Lock the exact computing contribution.

## Step 3

Generate 3–5 title variants.

## Step 4

Choose one provisional title.

## Step 5

Draft the July 11 topic proposal.

## Step 6

If time permits, make a tiny CORS proof-of-concept.

Do not return to broad topic hunting.

---

# FIRST PROTOTYPE RECOMMENDATION

Before full implementation, prove only this:

> Can the group take one ZAP CORS finding and independently verify it using its own logic?

Suggested proof-of-concept:

```text
1. Run local vulnerable test endpoint
2. Scan using ZAP
3. Retrieve one CORS alert
4. Send custom Origin requests
5. Parse response headers
6. Apply one simple verification rule
7. Output final verdict
```

Example:

```text
ZAP Alert:
Possible CORS Misconfiguration

Our Tests:
Fake origin accepted: Yes
Credentials allowed: Yes
Sensitive endpoint: Yes

Final Verdict:
CONFIRMED

Reason:
Arbitrary origin accepted with credentialed access.
```

This is the best first technical sanity check.

---

# WHAT IS NOT FINAL YET

Do not assume the following are locked:

- final thesis title
- exact research-gap wording
- exact scoring weights
- exact confidence formula
- exact rule thresholds
- final software stack
- final set of secondary test applications
- whether `null` origin stays in scope
- whether X-Content-Type-Options stays in scope
- exact proposal wording

---

# WHAT IS ALREADY SETTLED

Do not reopen these unless the user asks:

- This is deployed-web DAST, not SAST
- OWASP ZAP is the baseline scanner
- The group will not build a scanner from scratch
- Broad all-vulnerability verification is rejected
- Security Headers is a supporting category
- Cookie Security is a secondary contextual category
- CORS is the main technical category
- Current recommendation is to keep all 3
- Rule-based verification comes before ML
- Controlled/authorized testing only
- Next major step is final novelty/similar-work validation

---

# DEEP RESEARCH WORKFLOW

When the user says:

`@Deep research go`

At the current state, the next Deep Research should be the **final novelty and similar-work validation** described above.

Do not start another category research.

After Deep Research:

Do not ask the user to read the long report.

Summarize only:

- closest existing work
- whether the exact concept already exists
- defensible remaining gap
- novelty risk
- recommended final scope
- proposal-ready research-gap wording
- proposal-ready computing-contribution wording
- next action

---

# LATER TRACKS, NOT NOW

After this vulnerability-detection concept is proposal-ready, the user may later continue with:

## Malware Analysis

Possible themes:

- static vs dynamic analysis
- malware family classification
- behavior-based analysis
- API call sequence analysis
- obfuscation/packing
- unseen-family generalization
- graph representations
- explainability

## Intrusion Detection

Possible themes:

- false-positive reduction
- concept drift
- unseen attack detection
- cross-dataset generalization
- explainability
- LAN/internal threat detection
- lightweight/edge IDS
- encrypted traffic

Do not research these yet unless the user explicitly switches tracks.

---

# DEFENSIVE CYBERSECURITY FRAME

Always keep the project framed as:

- defensive cybersecurity
- authorized testing
- controlled lab evaluation
- detection and validation
- risk assessment
- secure configuration analysis
- intentionally vulnerable training applications

Avoid operational instructions for attacking unauthorized systems.

---

# SIMPLE TAGLISH EXPLANATION FOR GROUPMATES

Use this version:

> May possible thesis direction tayo sa vulnerability analysis. Instead na source code ang i-scan habang development, deployed website na mismo ang isi-scan gamit ang URL.
>
> Gagamit tayo ng existing scanner like OWASP ZAP para sa initial detection. Tapos yung system natin ang mag-a-analyze ulit ng selected findings para malaman kung alin ang mas likely na valid at relevant based sa additional evidence.
>
> Hindi tayo gagawa ng vulnerability scanner from scratch at hindi rin lahat ng vulnerability types ang iko-cover.
>
> Current categories natin are Security Headers, Cookie Security, and CORS. CORS ang main technical module, Cookie Security ang secondary contextual module, at Security Headers ang supporting module.
>
> So basically: existing scanner detects possible vulnerabilities, tapos system natin ang nagva-validate, nagra-rank, at nag-e-explain ng selected findings.

Short version:

> Deployed website vulnerability scanning siya. Mag-iinput ng authorized website URL, then gagamit ng OWASP ZAP for initial findings. Yung contribution natin is a context-aware verification and confidence-ranking layer for selected findings under CORS, Cookie Security, and Security Headers.

---

# ONE-LINE CURRENT STATUS

> The group is now in proposal-construction mode for a deployed-web DAST thesis. OWASP ZAP provides the initial findings, while the proposed system adds context-aware verification and confidence ranking for selected CORS, Cookie Security, and Security Header findings. Security Headers, Cookies, and CORS have all passed feasibility validation. CORS is the main technical module. The next exact step is one final Deep Research run to validate novelty and identify the closest existing work before locking the research gap, computing contribution, title, and July 11 proposal.
