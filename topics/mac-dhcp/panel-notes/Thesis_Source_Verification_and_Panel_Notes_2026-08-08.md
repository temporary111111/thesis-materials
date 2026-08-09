# Thesis Source Verification and Panel Notes
## DHCPv4 Lease Utilization under MAC Address Randomization and Client-Identifier Continuity

**Date:** 2026-08-08  
**Purpose:** Adviser/panel-facing fact check for Proposal Draft V2.  
**Rule:** This memo distinguishes what authoritative sources directly support from what remains a thesis hypothesis or inference.

---

## 1. Claims that are strongly supported

### DHCP does not identify a client solely by MAC address
RFC 2131 defines an explicit DHCP Client Identifier option. RFC 6842 summarizes RFC 2131's lease identity rule as using a Client Identifier or `chaddr` together with the assigned network address. This supports modeling Client-ID continuity separately from MAC continuity.

### A DHCPv4 Client Identifier can be independent of the interface MAC address
RFC 4361 specifies a DHCPv4 Client Identifier format based on IAID and DUID. This supports the conceptual separation between link-layer MAC identity and DHCP logical identity.

### Privacy-oriented DHCP behavior can require MAC and DHCP identifiers to change together
RFC 7844 explicitly discusses MAC address randomization and DHCP, explaining that link-layer address, IP address, and DHCP identifier should evolve together for stronger unlinkability. It also warns that excessive renewal/change behavior can risk DHCPv4 address-pool exhaustion.

### Modern RCM is not one universal “new MAC every reconnect” behavior
RFC 9724 describes multiple forms of Randomized and Changing MAC behavior rather than a single universal rotation rule. Therefore, the simulator should use controlled standards-informed profiles rather than claim to reproduce every operating system exactly.

### Changing MAC addresses can disrupt network state/services
RFC 9797 documents network impacts and use cases associated with randomized/changing MAC addresses. This supports the general relevance of studying stateful infrastructure such as DHCP.

### DHCP lease duration already has an established optimization literature
Khadilkar et al. (IMC 2007), Papapanagiotou et al. (IMC 2012), Li et al. (IEEE IoT Journal 2018), and Wang et al. (IEEE/ACM ToN 2020) establish that DHCP lease configuration, address utilization, overhead, transient clients, and large-scale WLAN DHCP behavior are existing research areas.

### The RCM literature already recognizes DHCP lease/pool issues
Ficara, Garroppo, and Henry's IEEE Communications Surveys & Tutorials paper identifies DHCP lease management, pool exhaustion, identifier/privacy tension, and lease-duration questions among RCM implications/research challenges. This is the strongest contemporary anchor for why the topic remains relevant while also preventing an overclaim that the basic problem is new.

### Kea's Client-ID behavior matches the thesis mechanism
Kea documentation explains that when Client-ID matching is enabled, a lease found by Client Identifier can remain associated with the client even when the current `chaddr` differs. The user's V1 implementation-level validation reproduced this behavior.

---

## 2. Claims that remain hypotheses, not established facts

Do NOT state these as facts before the main experiment:

- RCM commonly causes DHCP pool exhaustion in real guest networks.
- Session-based MAC turnover is the default behavior of all modern phones.
- A specific lease duration such as 1 h is “best.”
- A particular pool-pressure threshold will always produce service failure.
- Rotating MAC alone necessarily produces a new DHCP lease.
- All DHCP servers behave exactly like Kea.
- Real guest users always leave without DHCPRELEASE.
- The valid-lease-to-active-client ratio is an established standardized networking metric.

These are either scenario assumptions, implementation-dependent behaviors, or quantities the thesis is supposed to investigate.

---

## 3. Best novelty statement

> The study does not claim that RCM affects DHCP for the first time, nor that DHCP lease optimization is new. Its proposed contribution is a controlled, standards-informed, implementation-validated quantitative characterization of the interaction among MAC identity turnover, DHCP Client-Identifier continuity, lease duration, and constrained address-pool pressure.

Use “the literature reviewed thus far” and “insufficiently characterized.” Avoid “no study has ever” unless a formal systematic review can justify it.

---

## 4. Recommended title

### Proposal default
**Computational Modeling and Validation of DHCPv4 Lease Utilization under MAC Address Randomization and Client-Identifier Continuity in Constrained Guest Networks**

Why this version is preferred:
- shorter than the earlier locked title;
- makes the privacy/RMC phenomenon understandable to a panel;
- retains Client-Identifier continuity, which the real Kea validation proved is central;
- states the computing approach and target environment.

### Short fallback
**Computational Modeling of DHCPv4 Lease Utilization under DHCP-Visible Identity Turnover in Constrained Guest Networks**

Use only if the adviser wants a shorter title.

---

## 5. CS classification recommendation

The official BSCS domains guide explicitly lists **Computational Modeling and Simulation** as an acceptable substantial computing component and says software is only a vehicle for implementing/evaluating the computing contribution.

Use:

- **Primary CS Research Area / Computing Component:** Computational Modeling and Simulation
- **Cross-Cutting Application Domain:** Cybersecurity and Digital Forensics — Privacy-Preserving Analytics
- **Computing Contribution:** Standards-informed discrete-event DHCPv4 lease-state model with implementation validation and interaction/threshold analysis

This wording is safer than presenting Cybersecurity as the model itself.

---

## 6. Methodological caveat worth telling the panel

Real operating systems can couple MAC-randomization timing to connection state and DHCP lease timing. For example, current Android platform documentation describes conditions in which non-persistent MAC re-randomization depends partly on DHCP lease expiration and elapsed disconnection time.

Therefore:
> the five identity profiles should be described as controlled, standards-informed experimental abstractions, not exact replicas of every vendor implementation.

That limitation strengthens rather than weakens the simulation design because it explicitly separates interacting factors that may be coupled in real systems.

---

## 7. Pilot validation interpretation

The V0–V5 Kea results support the **mechanism model**, not the final research conclusion.

Validated:
- same logical identity can preserve one lease;
- stable Client-ID can preserve continuity despite MAC change;
- changing DHCP-visible identity can accumulate valid leases;
- retained leases can saturate a constrained pool;
- actual allocation failure occurs when a new request arrives with no free address;
- proper RELEASE can return leased addresses;
- server identity-matching policy changes the effect of MAC turnover.

Not validated by the pilot:
- realistic prevalence;
- long-run probability distributions;
- production-network threshold values;
- generalization across all DHCP server implementations;
- the final 5 × 4 × 3 factorial effect sizes.

---

## 8. Priority references for Chapter 1 and Chapter 2

### Standards / primary technical sources
1. RFC 2131 — Dynamic Host Configuration Protocol.
2. RFC 4361 — Node-specific Client Identifiers for DHCPv4.
3. RFC 7844 — Anonymity Profiles for DHCP Clients.
4. RFC 9724 — State of Affairs for Randomized and Changing MAC Addresses.
5. RFC 9797 — Randomized and Changing MAC Addresses: Context, Network Impacts, and Use Cases.
6. Kea 3.2 Administrator Reference Manual.

### Research literature
7. Ficara, D., Garroppo, R. G., & Henry, J. — A Tutorial on Privacy, RCM and Its Implications in WLAN. IEEE Communications Surveys & Tutorials.
8. Papapanagiotou, I., Nahum, E. M., & Pappas, V. — Configuring DHCP Leases in the Smartphone Era. ACM IMC 2012.
9. Li, F., Wang, X., Cao, J., Wang, R., & Bi, Y. — How DHCP Leases Meet Smart Terminals: Emulation and Modeling. IEEE IoT Journal, 2018.
10. Wang et al. — Squeezing the Gap: An Empirical Study on DHCP Performance in a Large-Scale Wireless Network. IEEE/ACM Transactions on Networking, 2020.
11. Khadilkar et al. — Usage-Based DHCP Lease Time Optimization. ACM IMC 2007.

---

## 9. One-paragraph defense answer

> MAC randomization affecting DHCP is already known, so that is not the novelty claim. The thesis separates physical-device behavior from the logical identity observed by DHCP, especially the role of Client Identifier continuity. It then uses a standards-informed discrete-event model to quantify how identity behavior interacts with lease duration and finite pool pressure. The contribution is the interaction and threshold characterization, with selected scenarios validated against a real Kea DHCPv4 implementation. This is why the study is a computational modeling thesis rather than simply a DHCP configuration project.

