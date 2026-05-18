# Further Reading

Pointers for students interested in exploring topics from this lecture in greater depth — including potential thesis directions.

## For graph fundamentals

- **MIT OpenCourseWare** — *Networks*, Prof. Daron Acemoglu — [ocw.mit.edu](https://ocw.mit.edu/)
- **Stanford CS224W** — *Machine Learning with Graphs* (Jure Leskovec). Lectures freely available on YouTube. The reference course for graph ML.

## For attack-path analysis (Demo B context)

- *An ACE Up the Sleeve* — Will Schroeder & Lee Christensen on AD ACL abuse (Black Hat USA 2017)
- *Certified Pre-Owned* — Schroeder et al., AD CS attack surface
- *BloodHound CE official documentation* — [bloodhound.specterops.io](https://bloodhound.specterops.io/)

## For SOC graph analytics (Demo C context)

- *Microsoft Sentinel: User and Entity Behavior Analytics (UEBA)* — official Microsoft Learn docs
- *Defender XDR Attack Disruption* — automated response on the attack graph
- Noel, S. (2018). *A Review of Graph Approaches to Network Security Analytics*. From Database to Cyber Security.

## For threat intelligence and STIX (Demo D context)

- *MITRE ATT&CK as a graph* — community projects mapping ATT&CK techniques into Neo4j
- *OpenCTI documentation* — open-source threat intelligence platform with native graph backend
- TI Mindmap HUB blog — [ti-mindmap-hub.com/blog](https://ti-mindmap-hub.com)

## For Graph Neural Networks (T4)

- Distill.pub interactive primer: [Understanding Convolutions on Graphs](https://distill.pub/2021/understanding-gnns/) (sequel to the GNN intro)
- *Graph Representation Learning Book* — William L. Hamilton — [free PDF](https://www.cs.mcgill.ca/~wlh/grl_book/)
- **PyTorch Geometric** and **DGL** — the two main GNN frameworks

## Potential thesis topics

For students at LUISS or elsewhere interested in graduate research at the intersection of graphs and security:

1. **GNN-based intrusion detection on encrypted traffic** — when payload inspection is unavailable, can graph structure alone classify malicious flows?
2. **Automatic STIX bundle inference from unstructured CTI** — extending TI Mindmap HUB's approach with newer LLMs or fine-tuned models
3. **Knowledge graph completion for threat intelligence** — predicting missing relationships between actors, malware, and infrastructure
4. **Tier-0 hardening with attack-path analytics** — using BloodHound graphs to quantitatively measure exposure reduction from ACL changes
5. **Cross-domain graph fusion for SOC** — unifying network, identity, endpoint, and CTI graphs into a single queryable substrate
6. **Non-traditional STIX applications** — applying threat-intelligence schemas to adjacent domains (fraud, geopolitics, disinformation)

Interested in pursuing one of these or proposing your own? Reach out via the contact information in the [main README](../README.md).
