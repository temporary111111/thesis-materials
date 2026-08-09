# FINAL DEEP NOVELTY / DUPLICATION / REAL-WORLD AUDIT
## DHCPv4 Lease-State Effects of MAC Randomization and Client-Identifier Continuity
**Date:** 2026-08-08  
**Decision:** **REVISE / RE-LOCK — DO NOT KILL**

---

## Executive Verdict

The thesis family survives the final audit, but the earlier broad novelty framing was too optimistic.

The following mechanisms are already known in standards, peer-reviewed literature, vendor guidance, and/or patents:

- RCM / randomized MAC behavior can affect DHCP and create address-pool pressure.
- DHCP Client Identifier can preserve identity/lease continuity across changing MAC addresses.
- Privacy-oriented operation may require DHCP identifiers to change together with link-layer identifiers.
- Changing DHCP-visible identities can result in additional address allocations.
- Lease duration materially affects address-pool efficiency and DHCP overhead.
- Shorter leases for randomized-MAC clients have already been proposed.
- Active-leases-versus-active-clients divergence/ratio has already appeared in Cisco prior art.
- DHCP exhaustion has already been related to pool size, lease time, client population, and MAC-rotation frequency.

Therefore, none of the mechanisms above should be claimed as the thesis innovation.

What **survives the audit** is a narrower quantitative contribution:

> **A standards-informed, implementation-validated computational characterization of how persistent versus privacy-synchronized DHCP Client-Identifier behavior changes lease-state overhead, address-pool saturation, and allocation-failure risk under controlled randomized-MAC turnover, lease-duration, and offered-load conditions.**

The novelty is **not** “we discovered RCM affects DHCP.”  
The novelty is **not** “we invented a fix.”  
The novelty is the **replicated operating-region / interaction characterization** of the privacy-versus-continuity choice under controlled resource conditions.

I did not locate an exact peer-reviewed duplicate whose central design jointly manipulates:
1. RCM identity behavior/turnover;
2. persistent versus privacy-synchronized DHCP Client-Identifier behavior;
3. multiple lease durations;
4. exogenous constrained offered physical-client load;
and then estimates interaction/operating regions using replicated computational simulation with implementation-level validation.

That is an absence from the search performed, not proof that no such work exists anywhere.

---

# 1. Audit Question: Are We Repeating an Existing Topic?

## Answer

**If the thesis is framed broadly as “effect of MAC randomization on DHCP leases/pool exhaustion,” then yes — that is substantially already known.**

**If the thesis is reframed around the quantitative operating regions created by persistent versus privacy-synchronized DHCP identity behavior under controlled lease-duration and offered-load conditions, it remains defensible as a BSCS computational-modeling contribution.**

This distinction is now mandatory.

---

# 2. Closest Prior Work / Prior Art

## 2.1 RFC 2131 — DHCP identity is not MAC-only

RFC 2131 already states that if a client supplies a Client Identifier, the server uses that identifier to identify the client; otherwise the server uses `chaddr`. A lease is identified by Client Identifier or `chaddr` together with the network address.

**Effect on novelty:** V0/V1 are implementation validation of standard behavior, not novel findings.

---

## 2.2 RFC 4361 — DHCP Client Identifier can be hardware-independent

RFC 4361 defines DHCPv4 Client Identifiers using IAID + DUID and discusses multiple network identities obtaining different IP addresses.

**Effect on novelty:** separating MAC identity from DHCP logical identity is standards-grounded and not itself novel.

---

## 2.3 RFC 7844 — privacy versus stable DHCP identity is already an explicit trade-off

RFC 7844 says link-layer address, IP address, and DHCP identifier should evolve in synchrony for privacy. It also explains that a stable Client Identifier makes correlation easy and can preserve consistent parameters, while aggressive randomization can increase DHCP request activity and risk IPv4 pool exhaustion.

**Effect on novelty:** the privacy-versus-continuity tension is established. Our contribution must quantify the resource cost under controlled operating conditions, not claim discovery of the trade-off.

---

## 2.4 Bernardos, Zúñiga, and O'Hanlon (IEEE CSCN 2015)

The 2014–2015 IETF/IEEE experiments already examined MAC randomization in operational wireless networks. The published work used DHCP Client Identifier during experiments, observed DHCP/IP allocation behavior, and later introduced shorter DHCP leases for local/randomized MAC addresses.

**Effect on novelty:** a thesis that merely experiments with randomized MAC + Client-ID + DHCP lease duration would be too close to historical work. Our design must clearly go beyond demonstration toward replicated factor-interaction/operating-region characterization.

---

## 2.5 Ficara, Garroppo, and Henry (IEEE Communications Surveys & Tutorials, 2024)

The contemporary RCM survey identifies DHCP lease management, pool exhaustion, identifier/privacy conflict, and lease-duration questions as RCM research challenges.

**Effect on novelty:** the problem remains relevant and research-worthy, but the general problem statement is not new.

---

## 2.6 DHCP lease optimization/modeling literature

Prior literature already covers:
- lease-time optimization;
- smartphone/transient-client DHCP lease configuration;
- emulation/modeling of DHCP lease behavior;
- empirical DHCP performance in large WLANs.

**Effect on novelty:** lease duration is an experimental factor, not our invention; generic DHCP simulation/modeling is also not new.

---

# 3. Patent / Industrial Prior-Art Kill Test

## 3.1 Cisco — US11483283B1
**DHCP resource optimization for randomized and changing MAC address**

The patent describes stable identifiers (including DHCPv4 Option 61) that allow an IP lease to remain bound across MAC rotations.

**Killed novelty claim:** “stable Client-ID preserves lease across MAC rotation.”

---

## 3.2 Cisco — US11962567B2
**Address rotation aware dynamic host control protocol**

The patent explicitly states that DHCP address exhaustion depends on:
- pool size;
- lease time;
- number of clients;
- MAC-rotation frequency.

It also describes a divergence/ratio between active IP addresses/leases and active clients, thresholds that trigger action, and adaptive lowering of lease times.

**Killed novelty claims:**
- active-leases / active-clients ratio as a new metric;
- thresholding that ratio as a new idea;
- general interaction of pool size × lease time × client count × rotation frequency as a new conceptual insight.

Our `valid-lease-to-active-client ratio` can still be used as a descriptive response variable, but it must not be presented as a novel metric.

---

## 3.3 ARRIS — US11765128B2
**DHCP server IP address allocation improvement to nullify the impact of MAC randomization**

This patent identifies randomized MAC clients and proposes shorter-than-default DHCP leases, among other identity/reuse strategies.

**Killed novelty claim:** “shorter DHCP leases for randomized MAC clients.”

---

# 4. Real-World Relevance Audit

## 4.1 Guest/public networks are a legitimate target

RFC 9797 explicitly identifies public guest networks such as malls, hotels, stores, stations, and airports as an environment in which users expect low/zero trust and should not depend on long-lived MAC identities.

Cisco operational guidance also documents temporary DHCP-pool impact from randomized MAC addresses until old-MAC leases expire.

**Verdict:** target environment is real and defensible.

---

## 4.2 Android makes the interaction more complicated than a simple factorial story

Current Android documentation states:
- persistent randomization is the default;
- non-persistent randomization is used only in some conditions;
- one re-randomization condition depends on the DHCP lease having expired plus elapsed disconnect time;
- another depends on MAC age.

**Implication:** MAC turnover and DHCP lease duration can be coupled in a real OS. Treating them as independent experimental factors is acceptable as controlled mechanism isolation, but it is not an exact Android emulator.

---

## 4.3 Apple makes guest/open-network relevance stronger, but aggressive session rotation should not be called universal

Current Apple documentation uses:
- Fixed private address by default on stronger secured networks;
- Rotating private address by default on weak/no-security networks, including captive portals/open networks;
- current user-facing documentation describes rotating addresses on a multi-day period rather than every reconnect.

**Implication:** constrained guest/public networks are a plausible application domain. Per-session turnover should be treated as a standards-informed stress/sensitivity profile, not a claim about default iPhone behavior.

---

# 5. Important Correction to the DHCPRELEASE Story

The Kea V4 pilot demonstrated immediate/near-immediate return of lease pressure in the Kea setup.

RFC 9797 notes that DHCP servers may retain a released IP for some period in case the old client returns.

Therefore:

> **Do not generalize “DHCPRELEASE always immediately returns the address to the pool” across all DHCP implementations.**

Use the Kea behavior as implementation evidence and include release-retention/affinity as a limitation or sensitivity parameter where practical.

---

# 6. Claim-by-Claim Novelty Verdict

| Candidate Claim | Audit Verdict | Thesis Treatment |
|---|---|---|
| RCM affects DHCP | **NOT NOVEL** | background only |
| RCM can contribute to DHCP pool exhaustion | **NOT NOVEL** | background/problem relevance |
| stable Client-ID can preserve lease despite MAC change | **NOT NOVEL** | mechanism/input assumption |
| different DHCP-visible identities can obtain multiple leases | **NOT NOVEL** | mechanism/input assumption |
| short lease mitigates retained-address pressure | **NOT NOVEL** | known trade-off / factor |
| lease duration affects utilization and overhead | **NOT NOVEL** | known trade-off / factor |
| lease-to-active-client ratio | **NOT NOVEL AS A CONCEPT** | descriptive response metric only |
| thresholds based on active leases vs clients | **NOT NOVEL** | do not claim invention |
| pool size × lease time × clients × rotation frequency | **NOT NOVEL AS A GENERAL RELATION** | prior-art-backed factors |
| privacy vs persistent identity continuity | **NOT NOVEL** | central known tension |
| controlled comparison of persistent vs privacy-synchronized CID under the same RCM behavior | **SURVIVES** | primary planned contrast |
| replicated response-surface / operating-region characterization across CID behavior × lease duration × exogenous offered load | **SURVIVES SEARCH** | primary contribution |
| simulation + deterministic real DHCP implementation validation of that operating-region model | **SURVIVES SEARCH AS A COMBINED DESIGN** | validation contribution |
| exact “first-ever” claim | **UNSUPPORTED** | never use |

---

# 7. Revised Novelty — Recommended Final Form

> **The study will provide a standards-informed and implementation-validated computational characterization of the operating regions created by persistent versus privacy-synchronized DHCP Client-Identifier behavior under randomized MAC turnover. By systematically varying lease duration and exogenous offered physical-client load, the study will estimate when the additional DHCP lease-state cost of privacy-preserving identity rotation remains negligible, becomes operationally significant, or leads to address-pool saturation and allocation failure.**

A shorter defense version:

> **The known mechanism is not our novelty. Our contribution is quantifying its operating regions and interaction effects.**

---

# 8. Revised Research Gap — Audit-Safe

> **Prior standards, operational studies, vendor work, and patents already establish that randomized and changing MAC behavior can affect DHCP lease state, that persistent Client Identifiers can preserve continuity across MAC changes, and that lease time, pool capacity, client population, and MAC-rotation frequency influence address exhaustion. However, the literature reviewed thus far does not provide a replicated controlled characterization of the operating regions produced by persistent versus privacy-synchronized DHCP identity behavior under standards-informed MAC turnover across multiple lease-duration and exogenous offered-load conditions, with implementation-level validation. Consequently, the quantitative resource cost of choosing privacy-preserving identifier rotation over identity continuity, and the conditions under which that cost shifts from negligible to service-impacting, remain insufficiently characterized.**

This is substantially safer than the previous gap.

---

# 9. Methodology Changes Required After the Audit

## 9.1 Make Client-ID continuity the scientific center

The primary contrast should be:
- same MAC-turnover process + persistent CID
versus
- same MAC-turnover process + privacy-synchronized rotating CID.

This isolates the privacy/continuity choice.

## 9.2 Rename “pool pressure”

Do **not** define the experimental factor using current lease utilization, because utilization is an outcome.

Recommended independent factor:

> **Offered physical-client load = offered active physical-client demand / DHCP pool capacity**

Use 50%, 75%, 90% only after the workload definition makes this quantitatively reproducible.

## 9.3 Keep lease-to-active-client ratio descriptive

Preferred label:
> **valid-lease-to-active-client ratio**

Do not call it a new metric or algorithm.

## 9.4 Reclassify P3/P4 per-session profiles

Per-session behavior remains legitimate under the RFC taxonomy, but it is implementation-dependent and is not a universal Android/iOS default.

Recommended treatment:
> **stress/sensitivity or upper-bound profiles**

## 9.5 Add release-retention sensitivity or limitation

At minimum, document that Kea's release behavior is not universal. If practical, model:
- immediate reuse;
- short post-release retention/affinity.

## 9.6 Strong optional upgrade: second DHCP implementation

A second DHCP implementation for a small subset of deterministic tests would reduce the argument that the model is “Kea-specific.”

This is optional for feasibility, but academically valuable if low-cost and stable.

## 9.7 Main deliverable should be an operating-region map

The thesis output should be framed as:
- response surfaces;
- interaction effects;
- safe/transition/service-impacting regions;
- uncertainty/confidence intervals.

Do not frame it as a new DHCP optimizer or mitigation algorithm.

---

# 10. Recommended Experimental Focus

A scientifically cleaner primary design is:

### Primary inferential experiment
- P0 baseline: stable/per-network MAC + persistent CID
- P1 periodic MAC turnover + persistent CID
- P2 same periodic MAC turnover + privacy-synchronized rotating CID
- 4 lease durations
- 3 offered-load levels

This is:
> **3 × 4 × 3 = 36 primary configurations**

### Sensitivity experiment
Use P3/P4 session-based turnover at selected representative operating points to test a more aggressive/upper-bound RCM condition.

The original 60 configurations remain computationally feasible, but the 36-config primary + selected sensitivity design provides a clearer novelty story and less risk of presenting vendor-nondefault behavior as co-equal with the primary real-world scenario.

---

# 11. BSCS Acceptability Audit

The official BSCS thesis guide explicitly accepts **Computational Modeling and Simulation** as a substantial computing component and requires the primary contribution to remain computational rather than merely being a software application.

The course materials also state that originality is required but that confirmation or rejection of previous findings may itself be meaningful when that is the research purpose.

Therefore, this thesis does **not** require a world-first mechanism to be acceptable. It does require:
- a clear computational contribution;
- a nontrivial research question;
- rigorous methodology;
- well-supported gap positioning;
- original analysis/results rather than simple reproduction.

The revised topic satisfies those requirements more strongly than the old broad framing.

---

# 12. Risk Assessment

| Dimension | Final Audit Assessment | Reason |
|---|---|---|
| Basic-mechanism novelty | **Weak / none** | standards, experiments, patents already cover mechanism |
| Exact-duplicate risk after reframe | **Low-to-moderate** | no exact peer-reviewed factorial/operating-region duplicate located |
| BSCS originality | **Moderate-to-strong if rigorously executed** | original quantitative interaction/operating-region analysis |
| Real-world relevance | **Strong** | current standards/vendor/OS behavior make guest-network case credible |
| Technical feasibility | **Very strong** | real Kea V0–V5 mechanism validation already passed |
| Cost/implementation burden | **Low** | simulation + local open-source DHCP lab |
| Panel-defense risk if old framing retained | **High** | easy to attack as known RCM/DHCP issue |
| Panel-defense risk after revised framing | **Manageable** | contribution becomes specific and falsifiable |
| Publication-level novelty | **Moderate, not breakthrough** | useful characterization, not new protocol/mechanism |
| “First ever” support | **None** | do not claim |

---

# 13. Recommended Re-Locked Title

### Preferred
**Computational Characterization of DHCPv4 Lease-State Effects of Client-Identifier Continuity under Randomized MAC Behavior in Constrained Guest Networks**

### Alternative, more trade-off oriented
**Computational Modeling of DHCPv4 Lease-State Trade-offs under Randomized MAC and Client-Identifier Continuity in Constrained Guest Networks**

The first title is preferred because it states exactly what survived the novelty audit: characterization of Client-Identifier continuity effects under randomized MAC behavior.

---

# 14. Final Kill / Keep Decision

## DO NOT KILL THE TOPIC.

But also:

## DO NOT KEEP THE OLD NOVELTY CLAIM UNCHANGED.

The correct decision is:

> **REVISE / RE-LOCK.**

The research is strongest when its contribution is a **controlled quantitative operating-region characterization**, not discovery of the underlying DHCP/RCM mechanism and not invention of a mitigation.

---

# 15. Source Set Used in the Final Audit

### Standards / authoritative technical sources
- RFC 2131 — Dynamic Host Configuration Protocol.
- RFC 4361 — Node-specific Client Identifiers for DHCPv4.
- RFC 7844 — Anonymity Profiles for DHCP Clients.
- RFC 9724 — State of Affairs for Randomized and Changing MAC Addresses.
- RFC 9797 — Randomized and Changing MAC Addresses: Context, Network Impacts, and Use Cases.
- Android Open Source Project — MAC randomization behavior.
- Apple Platform Security / Apple Support — Private Wi-Fi Address behavior.
- Cisco — DNA Center Q&A for Randomized MAC Addresses.
- Cisco — Randomized and Changing MAC Deployment Guide.

### Peer-reviewed / scholarly literature
- Bernardos, Zúñiga, O'Hanlon (IEEE CSCN 2015), *Wi-Fi Internet Connectivity and Privacy: Hiding Your Tracks on the Wireless Internet*.
- Ficara, Garroppo, Henry (IEEE Communications Surveys & Tutorials, 2024), RCM/WLAN privacy tutorial.
- Khadilkar et al. (ACM IMC 2007), DHCP lease time optimization.
- Papapanagiotou et al. (ACM IMC 2012), smartphone-era DHCP leases.
- Li et al. (IEEE IoT Journal 2018), DHCP lease emulation/modeling.
- Wang et al. (IEEE/ACM Transactions on Networking 2020), large-scale wireless DHCP performance.

### Patent / industrial prior art
- Cisco US11483283B1.
- Cisco US11962567B2.
- ARRIS US11765128B2.

### Search coverage
Targeted searches included:
- exact combinations of MAC randomization + DHCP + Client Identifier + lease duration + pool exhaustion;
- IEEE / ACM;
- theses/dissertations;
- patents;
- 2025–2026 recent work;
- DHCP simulation/modeling;
- “lease amplification” / active lease vs active-client concepts;
- current OS/vendor behavior.

No exact peer-reviewed duplicate matching the narrowed full controlled design was located. This is a search result, not a universal proof of absence.
