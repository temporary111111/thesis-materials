# CS 124 – THESIS 1
# THESIS TOPIC PROPOSAL — DRAFT V1

**Status:** Topic locked after implementation-level DHCP mechanism validation.  
**Note:** The Kea V0–V5 results are feasibility/mechanism-validation evidence only and are not the final thesis findings.

---

## I. Proposed Title

**Computational Modeling and Validation of DHCPv4 Lease Utilization under Randomized and Changing MAC Identities and Client-Identifier Continuity in Constrained Guest Networks**

### Required Proposal Classification

| Criterion | Proposed Classification |
|---|---|
| CS / Cross-Cutting Domain | Cybersecurity and Digital Forensics — privacy-aware network identity / privacy-preserving analytics |
| Substantial Computing Component | Computational Modeling and Simulation |
| Computing Contribution | Standards-informed, implementation-validated discrete-event model of DHCPv4 lease-state dynamics and interaction/threshold characterization |
| BU Research Agenda | Institutional Development and Policy Innovation |
| SDG | SDG 9: Industry, Innovation and Infrastructure |
| Primary Beneficiary | Network administrators managing constrained guest/public networks |
| Expected Innovation | Reproducible quantitative characterization of DHCP-visible MAC identity turnover, Client-Identifier continuity, lease duration, and address-pool pressure |

---

# Background of the Study

## Context and Relevance

Wireless networks increasingly use privacy mechanisms that reduce reliance on persistent link-layer identifiers. Randomized and Changing MAC (RCM) address techniques allow devices to use locally generated MAC addresses instead of always presenting a single permanent address. RFC 9724 describes multiple forms of RCM behavior, including per-network, per-period, and per-session generated MAC addresses. These mechanisms improve privacy at the link layer but also change the identifiers visible to network infrastructure.

One network service affected by changing device identity is the Dynamic Host Configuration Protocol for IPv4 (DHCPv4). DHCPv4 dynamically assigns IPv4 addresses for a limited lease period. RFC 2131 specifies that a server must associate a client with its lease through an appropriate identifier. When a DHCP Client Identifier is supplied, it can be used for client identification; when one is not supplied, the server may rely on the client's `chaddr` hardware-address field. RFC 4361 further demonstrates that DHCPv4 Client Identifiers can be constructed independently of a device's MAC address.

This creates an important interaction between privacy and network-state continuity. RFC 7844 explains that, from a privacy perspective, the link-layer address, IP address, and DHCP identifier may need to evolve together to reduce correlation across sessions. However, when both the MAC identity and DHCP-visible logical identity change, a DHCP server may no longer associate a returning physical device with its previous lease. If previous leases remain valid because the client departs silently or the lease has not yet expired, the number of valid leases can exceed the number of currently active physical clients.

The issue is especially relevant to guest or public networks with finite IPv4 address pools. Clients may connect only briefly, disconnect without explicitly releasing their lease, and return later. Increased lease occupancy does not automatically mean service failure: a pool may be fully allocated without rejecting a client until another allocation request occurs. Thus, DHCP resource behavior should distinguish lease utilization, pool saturation, and actual allocation failure.

A controlled implementation-level pre-study validation using Kea DHCPv4 3.2.0 confirmed the core mechanism needed by the proposed model. In an isolated WSL2/Linux environment, changing MAC addresses with a stable Client Identifier retained the same logical lease, while changing both MAC and Client Identifier produced multiple simultaneously valid leases. A three-address pool became saturated after three distinct DHCP-visible identities, and a fourth allocation attempt failed. Proper DHCPRELEASE messages removed the retained lease pressure. These checks establish technical feasibility but do not establish the magnitude or frequency of the effect under realistic guest-network workloads.

## Connection to Sustainable Development Goals, Research Agendas, and Strategic Priorities

The proposed study aligns primarily with **SDG 9: Industry, Innovation and Infrastructure** because it investigates the reliability and efficient utilization of digital network infrastructure under contemporary privacy-oriented identity behavior. Guest and public wireless networks are part of the digital infrastructure used by educational institutions, businesses, public facilities, and community environments. A quantitative understanding of DHCP lease behavior may support more resilient address-pool planning and configuration.

The study is also provisionally aligned with the **Bicol University Research and Development Agenda on Institutional Development and Policy Innovation**. It does not assume deployment on Bicol University's production network. Instead, it develops a computational framework that may support evidence-based network configuration and service-planning decisions in institutional guest-network environments.

The primary contribution remains within Computer Science: the development and evaluation of a standards-informed computational model, controlled simulation experiment, and implementation-level validation framework.

## Existing Challenges, Limitations, and Research Gap

The interaction between MAC randomization and DHCP is not itself new. Earlier Wi-Fi privacy research showed that changing link-layer addresses can create higher-layer service effects, and contemporary standards documents recognize that RCM can disrupt network state and contribute to DHCP address-scope pressure.

DHCP lease management also has an established research literature. Prior studies have examined lease-time optimization, smartphone and transient-client behavior, address utilization, DHCP overhead, large-scale wireless-network DHCP performance, and emulation/modeling of lease behavior. These studies demonstrate that lease duration creates a trade-off between address efficiency and protocol overhead. Therefore, this study does not claim that DHCP lease optimization, pool exhaustion, or RCM-aware DHCP is new.

The 2024 IEEE Communications Surveys & Tutorials article on privacy and RCM identifies DHCP lease management, pool exhaustion, Client Identifier behavior, and lease-duration selection as continuing research challenges associated with randomized and changing MAC addresses. However, the literature reviewed thus far has not revealed a contemporary peer-reviewed study whose central controlled experiment jointly varies DHCP-visible MAC identity turnover, DHCP Client-Identifier continuity, lease duration, and address-pool pressure while quantifying their interaction effects.

### Research Gap

> **Although prior work has established the operational effects of Randomized and Changing MAC addresses on DHCP and separately investigated DHCP lease and address-pool optimization, the literature reviewed thus far does not provide a controlled quantitative characterization of how DHCP-visible MAC identity turnover interacts with DHCP Client-Identifier continuity, lease duration, and address-pool pressure. Consequently, the operating conditions under which identity turnover produces negligible, moderate, or service-impacting DHCPv4 lease amplification remain insufficiently characterized.**

The proposed study therefore focuses not on proving that changing identities can consume additional leases, but on determining **how much**, **under which combinations of conditions**, and **at what operating thresholds** the effect becomes practically significant.

## Opportunities and Proposed Computing Approach

A computational modeling approach is appropriate because the research requires controlled manipulation of factors that are difficult to isolate in a production network. A discrete-event simulator can explicitly represent physical clients, DHCP-visible identities, lease states, session arrivals and departures, renewal timers, release behavior, lease expiration, and finite address-pool capacity.

The model will use standards-informed identity and DHCP lifecycle rules. Five identity profiles will represent stable, periodic, and session-based MAC behavior with persistent or synchronized rotating Client Identifiers. Lease duration and address-pool pressure will be manipulated as additional experimental variables. The simulator will record lease utilization, pool saturation, allocation failure, DHCP message overhead, inactive-but-valid leases, and a valid-lease-to-active-client ratio used to operationalize lease amplification.

The simulation will be validated at two levels. First, deterministic identity-semantic tests will compare modeled behavior with an actual Kea DHCPv4 implementation using programmable Scapy clients. Second, selected quantitative scenarios will be reproduced in the Kea environment and compared with simulator outputs using suitable agreement measures.

## Discussion of Computing Components and Research Areas

### Discrete-Event Computational Model
The primary computing artifact will be a discrete-event model of DHCPv4 lease-state behavior. Events will include client arrival, session start, MAC identity selection, Client-Identifier selection, DHCP acquisition, renewal, rebinding, departure, DHCPRELEASE, silent departure, lease expiration, reclamation, and subsequent sessions.

### DHCP-Visible Identity Model
The model will distinguish physical-client identity from DHCP-visible logical identity. A persistent Client Identifier may preserve lease continuity across changing MAC addresses when the server respects Client-ID matching. When the Client Identifier changes with the MAC, is absent, or is ignored by the server, MAC turnover can result in new DHCP-visible identities.

### Lease-State and Address-Pool Model
The simulated DHCP server will maintain a finite IPv4 address pool and lease state. Proper release returns an allocation to a reusable state under the normative base model, while silent departure allows the lease to remain valid until expiration.

### Experimental Workload Generator
The simulation will use literature-informed public/guest WLAN arrival and session behavior rather than arbitrary traffic. A bursty public-WLAN profile will serve as the reproducible main workload, with a more recent campus DHCP profile used as sensitivity context where appropriate.

### Factorial Experiment and Statistical Analysis
The main experiment will examine five identity profiles, four lease durations, and three pool-pressure levels, for 60 primary configurations. Each configuration will be repeated using independent random seeds. Analysis will emphasize effect sizes, confidence intervals, planned contrasts, and interaction effects.

### Implementation-Level Validation
Kea DHCPv4 will serve as the reference implementation for selected validation scenarios. Scapy will generate exact MAC and Client-Identifier sequences for deterministic tests, while perfdhcp may be used later for controlled load/overhead checks.

## Concluding Synthesis

Randomized and changing MAC addresses improve link-layer privacy but can change identity information visible to network services. DHCPv4 adds another identity layer through the Client Identifier, so MAC turnover does not automatically imply lease turnover. The resulting resource effect depends on whether DHCP-visible identity remains continuous, how long previous leases remain valid, and how much spare capacity exists in the address pool.

Existing work has established the underlying RCM/DHCP issue and separately studied DHCP lease efficiency. The remaining opportunity is to characterize the interaction among identity turnover, Client-Identifier continuity, lease duration, and pool pressure using a reproducible computational experiment. The proposed study addresses this through a standards-informed discrete-event model, controlled factorial simulation, and implementation-level validation.

---

# Introduction of the Proposed Computational Model and Validation Framework

The proposed study will develop a **DHCPv4 Identity and Lease Utilization Simulation Framework**, a research prototype for modeling, executing, measuring, and validating DHCP lease-state dynamics under controlled identity-turnover conditions. The prototype is not intended to replace a DHCP server or serve primarily as a network-management product. Its purpose is to implement and evaluate the computational contribution.

The framework will contain four major components: a workload generator for physical-client sessions; an identity-behavior module for the five experimental profiles; a DHCP state engine for acquisition, lease matching, renewal, rebinding, release, expiration, and reclamation; and an experiment/measurement module for repeated factorial runs and statistical output.

The core computing contribution is not a new DHCP protocol or optimization algorithm. It is a controlled computational representation of DHCP-visible identity continuity that allows interaction and threshold analysis across several known mechanisms. The model explicitly separates physical clients from logical DHCP identities and distinguishes pool saturation from actual allocation failure.

Selected simulator scenarios will be compared with Kea DHCPv4 in an isolated Linux environment. Preliminary V0–V5 mechanism-validation tests have already shown that Kea can reuse a lease across changing MAC addresses when a stable Client Identifier is used, allocate separate leases when both identifiers change, fail a new allocation when a finite pool has no free address, reclaim leases after DHCPRELEASE, and switch to chaddr/MAC-based matching when Client-ID matching is disabled.

---

# General Objective

> **To develop and validate a standards-informed discrete-event computational model for evaluating DHCPv4 lease utilization under randomized and changing MAC identities by quantifying the interactions among DHCP-visible identity behavior, Client-Identifier continuity, lease duration, and constrained address-pool pressure in guest-network environments.**

---

# Specific Objectives

1. **To identify and parameterize** standards- and literature-informed DHCP-visible identity profiles, DHCP Client-Identifier continuity strategies, lease durations, address-pool pressure conditions, release behavior, and guest/public-network workload characteristics for controlled simulation experiments.

2. **To design and implement** a discrete-event computational model that simulates physical-client sessions, DHCP-visible identity selection, DHCPv4 lease acquisition, renewal, rebinding, release, expiration, reclamation, and finite address-pool utilization.

3. **To develop and integrate** an isolated DHCPv4 validation environment using Kea DHCPv4 and programmable client identity generation to verify and reproduce selected identity, lease, renewal, release, saturation, and allocation-failure scenarios generated by the computational model.

4. **To evaluate** the individual and interaction effects of identity profile, Client-Identifier continuity, lease duration, and address-pool pressure using lease utilization, pool saturation probability and duration, allocation-failure rate, time-to-event measures, inactive-but-valid leases, DHCP message overhead, valid-lease-to-active-client ratio, and simulation-to-implementation agreement.

---

# Proposed Research Questions

1. How do different DHCP-visible randomized and changing MAC identity profiles affect DHCPv4 lease utilization under varying address-pool pressure?
2. How does DHCP Client-Identifier continuity influence lease utilization when a physical client presents changing MAC identities?
3. How does lease duration affect the trade-off between address availability and DHCP transaction overhead under different identity-continuity conditions?
4. Under what combinations of identity profile, Client-Identifier continuity, lease duration, and pool pressure do DHCPv4 pool saturation and allocation failures become operationally significant?

---

# Provisional Hypotheses

- **H1:** DHCP-visible identity turnover will increase valid lease occupancy when logical DHCP identity changes together with the MAC identity.
- **H2:** Persistent Client-Identifier continuity will reduce lease amplification caused by MAC turnover when the DHCP server respects Client-ID-based matching.
- **H3:** Shorter lease durations will reduce inactive-but-valid lease accumulation and allocation failures but increase DHCP renewal/message overhead.
- **H4:** The effect of identity turnover will become substantially larger as physical client demand approaches address-pool capacity.

---

# Scope and Limitations

## Dataset / Input Scope
No personally identifiable production-user data will be required. Inputs will consist of standards-informed identity behavior, literature-informed session parameters, configured lease durations, finite address-pool conditions, release behavior, and random seeds. Implementation-level validation will use synthetic client identities in an isolated network.

## Computational Model Scope
The model will include DHCPv4 identification, DISCOVER/OFFER/REQUEST/ACK acquisition, T1 renewal, T2 rebinding, DHCPRELEASE, silent departure, lease expiration/reclamation, finite address pools, five identity profiles, four provisional lease durations (1 h, 2 h, 8 h, 24 h), and three provisional pool-pressure levels (50%, 75%, 90%).

The model will not introduce a new DHCP protocol or adaptive RCM-aware lease-allocation algorithm.

## Prototype Scope
The research prototype will support simulation configuration, workload and identity generation, discrete-event execution, DHCP server-state tracking, repeated experiment runs, result aggregation, statistical analysis support, data export/visualization, and selected Kea validation scenarios. A complex end-user GUI is not required.

## Evaluation Scope
Metrics will include peak/mean lease utilization, pool saturation probability, saturation time fraction, allocation failure rate, time to first saturation/failure, inactive-but-valid leases, DHCP message overhead, valid-lease-to-active-client ratio, and selected simulator-to-Kea agreement measures.

## Limitations
The study will not model full IEEE 802.11 PHY/MAC behavior, RF propagation/interference, scanning/roaming details, AP-controller internals, production Android/iOS stacks, device fingerprinting, MAC spoofing attack detection, enterprise 802.1X/RADIUS/NAC, DHCPv6/SLAAC, IPv6 privacy addresses, real-user tracking, or live Bicol University production Wi-Fi.

Identity profiles are controlled standards-informed conditions and should not be interpreted as exact universal behavior of all mobile operating systems. Kea validation establishes implementation-level plausibility but does not imply identical internals across all DHCP server products.

---

# Preliminary Methodology

## Research Design
**Computational modeling and simulation with implementation-level experimental validation.**

## Main Experimental Factors

### Identity Profile
- P0 — stable/per-network MAC + persistent Client-ID
- P1 — periodic MAC turnover + persistent Client-ID
- P2 — periodic MAC turnover + synchronized rotating Client-ID
- P3 — session-based MAC turnover + persistent Client-ID
- P4 — session-based MAC turnover + synchronized rotating Client-ID

### Lease Duration
- 1 hour
- 2 hours
- 8 hours
- 24 hours

### Address-Pool Pressure
- 50%
- 75%
- 90%

**Total main configurations: 5 × 4 × 3 = 60**

## Replication
Each configuration will initially use at least 30 independent random seeds. Additional repetitions may be executed until the primary outcome reaches a predefined confidence-interval precision target.

## Planned Comparisons
- P1 vs P2
- P3 vs P4
- profiles vs P0 where meaningful
- identity profile × lease duration
- identity profile × pool pressure

## Validation
1. **Mechanism validation:** exact identity sequences generated with Scapy and observed in Kea DHCPv4.
2. **Quantitative validation:** selected simulator scenarios reproduced in the Kea lab and compared with server-state/protocol metrics.

---

# Conceptual Framework

```text
Physical Client Population
        |
        v
Arrival / Session Workload
        |
        v
DHCP-Visible Identity Profile
(P0, P1, P2, P3, P4)
        |
        v
DHCP Identity Matching
(Client-ID continuity / chaddr dependence)
        |
        v
Lease Lifecycle
Acquisition -> Renewal -> Rebinding
          -> Release / Expiration
        |
        v
Finite Address-Pool State
        |
        +------------------+--------------------+
        |                  |                    |
        v                  v                    v
 Lease Utilization   Pool Saturation     DHCP Overhead
        |                  |
        +------------------+
                 |
                 v
        Allocation Failure Risk
                 |
                 v
Interaction / Threshold Characterization

Moderators:
- Lease duration
- Address-pool pressure
- Release behavior / workload assumptions
```

---

# Initial RRL / Source Map

## Protocol and Standards
1. Droms, R. (1997). **RFC 2131: Dynamic Host Configuration Protocol.**
2. Lemon, T., & Sommerfeld, B. (2006). **RFC 4361: Node-specific Client Identifiers for DHCPv4.**
3. Mrugalski, T., et al. (2016). **RFC 7844: Anonymity Profiles for DHCP Clients.**
4. Zúñiga, J. C., Bernardos, C. J., & Andersdotter, A. (2025). **RFC 9724: State of Affairs for Randomized and Changing MAC Addresses.**
5. **RFC 9797 (2025): Randomized and Changing MAC Addresses: Context, Network Impacts, and Use Cases.**

## RCM / Privacy Literature
6. Ficara, D., Garroppo, R. G., & Henry, J. (2024). **A Tutorial on Privacy, RCM and Its Implications in WLAN.** IEEE Communications Surveys & Tutorials, 26(2), 1003–1040. DOI: 10.1109/COMST.2023.3345746.
7. O'Hanlon, P., Bernardos, C. J., & Zúñiga, J. C. (2015). **Wi-Fi Internet Connectivity and Privacy: Hiding Your Tracks on the Wireless Internet.** IEEE CSCN. DOI: 10.1109/CSCN.2015.7390443.

## DHCP Lease / Resource Literature
8. Khadilkar, M., Feamster, N., Sanders, M., & Clark, R. (2007). **Usage-Based DHCP Lease Time Optimization.** ACM IMC. DOI: 10.1145/1298306.1298315.
9. Papapanagiotou, I., Nahum, E. M., & Pappas, V. (2012). **Configuring DHCP Leases in the Smartphone Era.** ACM IMC, 365–370. DOI: 10.1145/2398776.2398814.
10. Li, F., Wang, X., Cao, J., Wang, R., & Bi, Y. (2018). **How DHCP Leases Meet Smart Terminals: Emulation and Modeling.** IEEE Internet of Things Journal, 5(1), 56–68. DOI: 10.1109/JIOT.2017.2771219.
11. Wang, H., Wang, J. H., Wang, J., Dang, W., Xue, J., Li, F., & Shan, J. (2020). **Squeezing the Gap: An Empirical Study on DHCP Performance in a Large-Scale Wireless Network.** IEEE/ACM Transactions on Networking, 28(2), 832–845. DOI: 10.1109/TNET.2020.2971551.

## Validation Platform
12. Internet Systems Consortium. **Kea DHCP 3.2 documentation.**
13. Scapy Project. **Scapy BOOTP/DHCP documentation.**

---

# Novelty Boundaries — Do Not Claim

Do not claim that:
- MAC randomization is new;
- RCM affecting DHCP is new;
- DHCP scope exhaustion is new;
- DHCP lease optimization is new;
- shorter leases for randomized clients are new;
- Client-ID continuity under MAC changes is new;
- RCM-aware DHCP is new;
- this is the “first ever” study.

Defensible contribution:

> **A controlled, standards-informed, implementation-validated quantitative characterization of the interaction among DHCP-visible identity turnover, Client-Identifier continuity, lease duration, and address-pool pressure.**

---

# Preliminary Feasibility Note

A real Kea DHCPv4 mechanism-validation lab has already been executed successfully in WSL2. V0–V5 deterministic tests supported all six core identity/lease assumptions. These tests should be retained as technical feasibility evidence and later documented appropriately in the methodology or pilot-validation subsection, but should not be presented as final thesis findings.

---

# Draft Status

This is **Proposal Draft V1**. The next review pass should focus on:
- adviser-preferred title length;
- confirmation of the BU Agenda alignment;
- final literature-backed workload parameters;
- final lease-duration rationale;
- department-required citation style;
- exact wording of “lease amplification” in the manuscript;
- whether a separate Statement of the Problem section is required outside the topic-proposal template.
