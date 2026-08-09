# THESIS CYBERSEC NARROWING HANDOFF

## START HERE

You are continuing a BS Computer Science thesis-planning conversation for a student at Bicol University.

The user does **not** want to re-explain the context. Treat this file as the current canonical handoff.

The user is intentionally moving between AI chats. Continue from the latest state in this file without making them restate prior decisions. The goal is continuity, not re-opening settled steps.

Preferred interaction style:

- Main language: **Taglish**
- Be practical, direct, and easy to understand
- Avoid long academic explanations unless needed
- The user often does **not** have time to read long Deep Research reports
- When Deep Research is used, summarize the useful conclusions instead of asking the user to read the full report
- Current work is **narrowing and research-gap hunting**, not random topic dumping
- Do not jump to a final title too early
- The user wants to understand whether an idea is **actually feasible to implement**
- For groupmate-facing explanations, use **simple Taglish**

---

# BROADER THESIS PROJECT CONTEXT

The group previously completed a large thesis topic-dumping phase across many CS domains.

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

So the **domain topic-dumping phase is already complete**.

The project has now moved into **narrowing**.

---

# CURRENT NARROWING DIRECTION

The user personally narrowed attention to these three cybersecurity research families:

1. **Malware Analysis**
2. **Vulnerability Detection**
3. **Intrusion Detection**

The agreed strategy is:

- Research them **one at a time**
- For each field, identify:
  - current approaches
  - recurring limitations
  - genuine research gaps
  - possible novelty
  - undergraduate feasibility
  - public datasets/test environments
  - prototype potential
  - evaluation metrics
- Only after all three are researched should we compare them side by side

Recommended research order:

1. Vulnerability Detection
2. Malware Analysis
3. Intrusion Detection

Current active focus: **Vulnerability Detection**, specifically implementation-level feasibility validation for a deployed-web DAST thesis.

Current sub-status:
- Security Headers validation: **COMPLETED**
- Cookie Security validation: **NEXT**
- CORS validation: **AFTER COOKIE SECURITY**

---

# CRITICAL CLARIFICATION ABOUT WHAT “VULNERABILITY DETECTION” MEANS TO THE USER

The first Deep Research run misunderstood the user's intent and focused mostly on:

- source-code vulnerability detection
- SAST
- CodeQL/Semgrep
- line-level vulnerability detection
- dependency/package analysis

That is **NOT** the user's intended main idea.

The user clarified that they mean:

> There is already a deployed website. The group's system scans the deployed website using its URL and detects/analyzes vulnerabilities.

So the correct research family is:

- **Dynamic Application Security Testing (DAST)**
- **Black-box Web Vulnerability Scanning**
- **Deployed Web Application Vulnerability Analysis**

The user is interested in this flow:

```text
Authorized Deployed Website
        ↓
Enter URL
        ↓
Scan Running Web Application
        ↓
Detect Possible Vulnerabilities
        ↓
Analyze / Verify / Prioritize Findings
        ↓
Explainable Report
```

Important: all testing must be limited to:

- local lab targets
- intentionally vulnerable applications
- university-controlled test systems
- explicitly authorized websites

Never frame the work as scanning arbitrary public websites.

---

# FIRST DAST RESEARCH CONCLUSION

Deep Research found that simply building another scanner is weak.

Bad framing:

> “We created a web vulnerability scanner.”

Stronger framing:

> “We improve the reliability of deployed web vulnerability scanning by verifying and prioritizing scanner findings.”

The strongest initial research gap identified was:

- false positives / unreliable findings
- weak verification of scanner alerts
- weak prioritization
- limited explanation

A possible direction was:

> Evidence-guided verification and false-positive reduction on top of an existing scanner like OWASP ZAP

But the user correctly worried that this sounded too hard.

---

# FEASIBILITY CORRECTION

The broad version is NOT feasible.

Reject this scope:

> Scan any website, verify every vulnerability type, remove all false positives.

The feasible version is:

> Use an existing scanner as the baseline, then build a verification layer for only 2–3 selected vulnerability categories in a controlled lab.

The group should **not** build:

- a browser engine
- a crawler from scratch
- an exploit framework
- a universal scanner
- a Burp Suite competitor

Use an existing scanner such as **OWASP ZAP** for initial findings.

The thesis contribution should be the layer after scanning.

---

# CURRENT RECOMMENDED ARCHITECTURE

```text
Authorized Test Website
        ↓
OWASP ZAP Scan
        ↓
Raw Vulnerability Alerts
        ↓
Alert Normalizer
        ↓
Evidence Collector
        ↓
Rule-Based Verification / Confidence Engine
        ↓
Confirmed / Likely / Uncertain
        ↓
Prioritized and Explainable Report
```

Potential modules:

1. ZAP integration
2. Alert parser / normalizer
3. Evidence collector
4. Verification scoring engine
5. Results dashboard

Do **rule-based verification first**.

Do not force machine learning unless later evidence shows:

- enough labeled samples exist
- ML clearly improves the research contribution
- the group can support the extra complexity

---

# LATEST DEEP RESEARCH GOAL

The latest Deep Research was focused on:

> Which 2–3 vulnerability categories are the most feasible to verify automatically in a deployed-web DAST thesis?

The categories were evaluated based on:

- safe reproducibility
- ground-truth availability
- automation feasibility
- observable HTTP evidence
- implementation complexity
- compatibility with ZAP
- novelty potential
- evaluation clarity
- thesis usefulness

---

# LATEST RESEARCH CONCLUSION: BEST 3 CATEGORIES

## 1. Security Headers Misconfiguration

Examples:

- missing CSP
- missing HSTS
- missing X-Frame-Options
- missing X-Content-Type-Options
- weak or malformed security headers

Why feasible:

- deterministic HTTP evidence
- easy to inspect automatically
- safe
- repeatable
- clear ground truth

Possible verification logic:

- check whether the header is missing/weak across repeated responses
- check important route classes such as login/account/auth pages
- check redirect response versus final response
- avoid treating static assets the same as sensitive pages
- validate exact header values, not only presence/absence

Feasibility: **Very High**

Warning:

Security headers **alone** may be too simple for a full CS thesis.

---

## 2. Cookie Security Misconfiguration

Examples:

- missing `HttpOnly`
- missing `Secure`
- missing `SameSite`

Why feasible:

- easy to parse from `Set-Cookie`
- repeatable
- clear evidence
- can be made more interesting with session/authentication context

Possible verification logic:

- identify whether the cookie appears session-related
- check whether the weakness persists across repeated logins
- inspect cookie path/domain scope
- downgrade analytics/non-sensitive cookies
- prioritize authentication/session cookies

Feasibility: **Very High**

Warning:

Cookie flags **alone** may also be too simple.

---

## 3. CORS Misconfiguration

This is currently the most technically interesting of the top 3.

Possible verification logic:

- send requests with different `Origin` values
- detect arbitrary-origin reflection
- inspect `Access-Control-Allow-Origin`
- inspect `Access-Control-Allow-Credentials`
- compare preflight and actual response behavior
- check whether the policy is static and restricted versus broadly permissive
- check route sensitivity and context

Feasibility: **High**

Why it matters:

This has more real verification logic than simple presence/absence checks.

---

# CURRENT RECOMMENDED CORE SCOPE

The current recommended combination is:

1. **Security Headers**
2. **Cookie Security**
3. **CORS**

Current thesis logic:

> The existing scanner produces raw findings. The proposed system adds context-aware verification and confidence ranking for selected vulnerability categories.

This combination was recommended because:

- headers give the easiest deterministic category
- cookies add session/authentication context
- CORS adds a more active and technically interesting category

---

# STRETCH CATEGORY

## Reflected XSS

Possible as a later stretch category only.

Why not core yet:

- browser confirmation is harder
- context analysis is harder
- false-positive risk is higher
- implementation becomes more complex

Only consider it after the top 3 are stable.

Do not add SQL injection or access-control/BOLA just for “wow factor” unless the group has strong reason and enough time.

---

# CURRENT TEST ENVIRONMENT RECOMMENDATION

The strongest primary testing setup is:

## 1. Custom Mini Misconfiguration Lab

Best for:

- security headers
- cookie flags
- CORS

Why:

- deterministic ground truth
- easy to intentionally configure weak and secure versions
- repeatable tests
- easy comparison of true positives and false positives

## 2. Secondary / Realism Checks

Possible secondary targets:

- OWASP Juice Shop
- OWASP WebGoat
- DVWA
- OWASP crAPI

Important nuance:

- Juice Shop is excellent for many web vulnerabilities, but may not be the cleanest native target for the top 3 configuration-focused categories
- crAPI is stronger for API-centric issues like BOLA and other API risks
- WebGoat and DVWA are useful for classic web vulnerabilities and possible stretch work

---

# CURRENT EXPERIMENTAL COMPARISON

The thesis should compare:

## Baseline

Raw OWASP ZAP findings

versus

## Proposed System

ZAP findings after the group’s verification/context layer

Main research question pattern:

> Does the proposed verification layer improve the precision of selected DAST findings without causing an unacceptable loss in recall?

Potential metrics:

- Precision
- Recall
- F1-score
- False Positive Rate
- False-positive reduction
- Verification time
- Coverage
- Ranking accuracy, if prioritization is included

---

# CURRENT FEASIBILITY JUDGMENT

## Infeasible version

> Verify all vulnerability types on any website

Verdict: reject

## Feasible version

> Verify selected categories using controlled evidence signals on local/authorized targets

Verdict: strong candidate

## Safest version

> Confidence-based prioritization of selected ZAP alerts using reproducibility, route context, session relevance, and scanner metadata

Verdict: highly feasible, but must still show enough CS contribution

---

# SIMPLE TAGLISH EXPLANATION FOR GROUPMATES

Use this when the user asks for a simple explanation:

> May possible direction tayo sa vulnerability analysis. Instead na source code ang i-scan habang development, deployed website na mismo ang isi-scan gamit ang URL.
>
> Gagamit tayo ng existing scanner like OWASP ZAP para sa initial detection. Tapos yung system natin ang mag-a-analyze ulit ng selected findings para malaman kung alin ang mas likely na valid at relevant based sa additional evidence.
>
> Hindi tayo gagawa ng vulnerability scanner from scratch at hindi rin lahat ng vulnerability types ang iko-cover. Puwede tayong pumili lang ng 2–3 categories at mag-test sa controlled vulnerable websites.
>
> Sa current research, pinaka-feasible ang Security Headers, Cookie Security, at CORS.
>
> So basically: existing scanner detects possible vulnerabilities, tapos system natin ang nagva-validate, nagra-rank, at nag-e-explain ng selected findings.

Shorter version:

> Deployed website vulnerability scanning siya. Mag-iinput ng authorized website URL, then gagamit ng existing scanner for initial findings. Yung contribution natin is a verification and confidence-ranking layer for selected vulnerability categories para maging mas reliable at useful ang results.

---

# WHAT IS NOT FINAL YET

Do not assume the following are already decided:

- final thesis title
- final exact research gap wording
- exact 2 versus 3 categories
- exact scoring weights
- whether to use ML
- exact test applications
- exact rule thresholds
- exact architecture stack
- final adviser-facing proposal wording

Current state is still:

> Feasibility validation and research-gap narrowing

---

# MOST LOGICAL NEXT STEP

The next immediate research task is:

## Implementation-Level Feasibility Validation of Cookie Security

The user has already completed the same focused validation for **Security Headers**.

Do not re-run the Security Headers research unless the user explicitly asks.

The next Deep Research target is:

> **Cookie Security Misconfiguration Verification on Top of OWASP ZAP: implementation-level feasibility assessment**

Research only these questions:

1. What exact OWASP ZAP cookie-related alerts are relevant?
2. How does ZAP currently detect them?
3. What common false positives, low-value alerts, or context problems occur?
4. What extra evidence can the proposed system collect?
5. Can the system distinguish session/authentication cookies from analytics or low-sensitivity cookies?
6. What rule-based verification logic is feasible?
7. What can be automated reliably?
8. How can ground truth be generated in a controlled lab?
9. How should baseline ZAP be compared with the proposed layer?
10. Does Cookie Security provide enough contribution when combined with Security Headers?
11. Final verdict:
    - KEEP
    - DROP
    - KEEP BUT NEEDS PARTNER
    - REPLACE

Expected summary format for the user after research:

- **Paano gagawin?**
- **Ano ang ico-code?**
- **Ano ang extra evidence?**
- **Ano ang novelty?**
- **Gaano kahirap?**
- **Sapat ba kasama ng Security Headers?**
- **Final verdict: KEEP / DROP / NEEDS PARTNER / REPLACE**

Do not make the user read the long report.

After Cookie Security, the next category to validate is **CORS**.

---

# COMPLETED IMPLEMENTATION VALIDATION: SECURITY HEADERS

This focused Deep Research is already complete.

## Final verdict

> **KEEP, but NEEDS PARTNER CATEGORY**

Security Headers is highly feasible and useful as one component, but it is too simple to serve as the entire BS Computer Science thesis by itself.

## Exact ZAP alert families reviewed

### Anti-clickjacking
- `10020-1` Missing Anti-clickjacking Header
- `10020-2` Multiple `X-Frame-Options`
- `10020-3` `X-Frame-Options` via META
- `10020-4` malformed XFO

### MIME sniffing
- `10021` `X-Content-Type-Options` Header Missing

### HSTS
- `10035-1` through `10035-8`
- not set
- disabled
- multiple entries
- present on HTTP
- missing `max-age`
- defined via META
- malformed `max-age`
- malformed content

### CSP
- `10038-1` CSP not set
- `10038-2` obsolete CSP header
- `10038-3` report-only only

## Main research finding

The contribution is not to re-detect missing headers.

The useful thesis angle is:

> **Contextual verification and prioritization of ZAP header alerts using additional live-response evidence.**

## Extra evidence signals identified

The verifier can collect:

- final URL after redirects
- `http` versus `https`
- response `Content-Type`
- status code
- redirect chain
- HTML versus JSON/API versus static asset
- page context
- endpoint type, such as home/login/account/admin
- anonymous versus authenticated state
- consistency across repeated requests

## Example rule-based logic

### Clickjacking

ZAP says:

> Missing `X-Frame-Options`

Verifier checks:

- Is it an HTML page?
- Is CSP `frame-ancestors` already present?
- Is the finding from a redirect or error page?
- Is the page sensitive?

Possible verdict:

- Confirmed
- Needs Review
- Downgraded

### HSTS

Verifier checks:

- Is the response HTTPS?
- Is `max-age=0`?
- Is the value malformed?
- Is the issue on a sensitive authenticated route?

### CSP

Verifier checks:

- Is the target HTML?
- Is the page login/account/admin?
- Is only Report-Only present?
- Is the result from an API JSON response or static asset?

## Minimal implementation flow

```text
Authorized URL
    ↓
ZAP spider / passive scan
    ↓
Raw header alerts
    ↓
Proposed verifier
    ↓
Re-fetch affected response
    ↓
Collect context + consistency evidence
    ↓
Apply rules
    ↓
Confirmed / Needs Review / Downgraded
```

## Ground truth approach

Primary:

- custom controlled mini lab with secure and insecure versions

Examples:

```text
/login-no-csp
/login-with-csp
/https-no-hsts
/page-with-frame-ancestors
/api-json-no-xfo
```

Secondary realism checks:

- OWASP Juice Shop
- OWASP crAPI

## Evaluation

Compare:

### Baseline
Raw OWASP ZAP findings

### Proposed
ZAP + verification layer

Potential metrics:

- Precision
- Recall
- F1-score
- False Positive Rate
- False-positive reduction
- Verification time

## Security Headers decision

| Factor | Assessment |
|---|---|
| Implementation feasibility | Very High |
| Ground truth | Very Easy |
| Automation | Very High |
| Demo potential | Good |
| Research contribution alone | Weak to Medium |
| Value as part of multi-category system | High |
| Final verdict | KEEP, NEEDS PARTNER |

The current intended partner candidates are:

1. Cookie Security
2. CORS

Do not treat Security Headers as a final stand-alone thesis.

---

# RESEARCH WORKFLOW PREFERENCE

When the user says:

`@Deep research go`

The preferred workflow is:

1. Run one focused Deep Research topic at a time
2. Do not make the user read the long report
3. Summarize:
   - strongest findings
   - real gaps
   - feasibility
   - best next step
4. Only create Excel/MD artifacts when the user asks

The user explicitly said they have limited time.

So avoid saying:

> “Please read the full research report.”

Instead:

> “Hindi mo na kailangang basahin yung mahabang report. Ibu-buod ko lang yung findings na kailangan natin.”

---

# LATER RESEARCH TRACKS

After Vulnerability Detection is sufficiently validated, continue one at a time with:

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
- lightweight or edge IDS
- encrypted traffic

Do not research all three simultaneously.

---

# DEFENSIVE CYBERSECURITY SAFETY FRAME

Always keep the work framed as:

- defensive cybersecurity
- authorized testing
- controlled lab evaluation
- detection and validation
- risk assessment
- secure configuration analysis
- intentionally vulnerable training applications

Avoid operational instructions for attacking unauthorized public systems.

---

# THESIS REQUIREMENT REMINDER

The BS Computer Science thesis needs a real computing contribution.

A generic scanner wrapper, dashboard, CRUD system, or report generator is not enough.

The contribution must be something like:

- verification logic
- confidence scoring
- context-aware ranking
- evidence fusion
- algorithmic prioritization
- improved precision
- explainability
- intelligent decision support

Software is only the vehicle for implementing and evaluating the computing contribution.

---

# ONE-LINE CURRENT STATUS

> The group has narrowed into cybersecurity. Current active investigation is a deployed-web DAST thesis where OWASP ZAP provides initial alerts and the proposed system adds context-aware verification and confidence ranking for selected vulnerability categories. Security Headers implementation validation is complete with the verdict KEEP BUT NEEDS PARTNER. The next exact Deep Research task is Cookie Security implementation feasibility, followed by CORS. Final title and exact final scope are not yet locked.
