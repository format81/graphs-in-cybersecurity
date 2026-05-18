# Graphs in Cybersecurity

> Material for the lecture *"Grafi nella Cybersecurity: rappresentare, interrogare, difendere"*  
> Master in Cybersecurity, LUISS Guido Carli — May 29, 2026

[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-lightgrey.svg)](LICENSE-docs)

## What this is

A 2-hour graduate lecture introducing **graph theory as a unifying paradigm for defensive cybersecurity**. The material covers theory, tooling, and four hands-on demos spanning network traffic, identity, SOC platforms, and threat intelligence.

This repository contains everything needed to reproduce the demos and study the topics independently. It is also a reusable teaching kit — feel free to adapt for your own courses, talks, or workshops (please respect the licenses).

## Lecture structure (120 min)

| Block | Duration | Content |
|---|---|---|
| Theory T1-T4 | 35 min | Fundamentals, algorithms, technologies, GNN preview |
| **Demo A** | 12 min | From a PCAP to a graph (Wireshark → networkx → pyvis) |
| **Demo B** | 12 min | Active Directory attack paths with BloodHound CE |
| **Demo C** | 10 min | Investigation graphs in Microsoft Sentinel & Defender XDR |
| **Demo D** | 25 min | TI Mindmap HUB — knowledge graphs from OSINT via LLM |
| Closing | 8 min | Future directions, references, Q&A |

## Quick start

```bash
git clone https://github.com/format81/graphs-in-cybersecurity.git
cd graphs-in-cybersecurity
pip install -r requirements.txt
```

Then pick a demo folder and follow its README.

## Demos at a glance

- **[demo-a-wireshark](./demo-a-wireshark/)** — From a packet capture to an interactive graph in ~30 lines of Python. Three progressive views + PageRank to surface beaconing.
- **[demo-b-bloodhound](./demo-b-bloodhound/)** — BloodHound Community Edition queries for attack-path discovery and defensive tier-0 hardening.
- **[demo-c-sentinel](./demo-c-sentinel/)** — Microsoft Sentinel Investigation Graph + Defender XDR Attack Story as enterprise-scale graph adoption.
- **[demo-d-ti-mindmap-hub](./demo-d-ti-mindmap-hub/)** — A production knowledge graph (929 reports, 60k+ relations) built from OSINT threat reports via LLMs. Live demo platform.

## Theory companion

- **[docs/theory-notes.md](./docs/theory-notes.md)** — accompanying notes on the theoretical part (graph fundamentals, algorithms, GNN intro)
- **[docs/bibliography.md](./docs/bibliography.md)** — academic and industry references
- **[docs/further-reading.md](./docs/further-reading.md)** — pointers for thesis topics and deeper study

## About the author

**Antonio Formato** — Sr. Cybersecurity Solution Engineer @ Microsoft. Independent open-research on AI-powered Cyber Threat Intelligence at [TI Mindmap HUB](https://ti-mindmap-hub.com).

- LinkedIn: [linkedin.com/in/antonioformato](https://linkedin.com/in/antonioformato)
- GitHub: [@format81](https://github.com/format81)

## Citation

If you use this material in academic work or other talks, please cite as:

```
Formato, A. (2026). Graphs in Cybersecurity: a defensive paradigm.
Lecture material, Master in Cybersecurity, LUISS Guido Carli.
https://github.com/format81/graphs-in-cybersecurity
```

## License

- **Code** (notebooks, scripts) — [MIT](LICENSE)
- **Documentation, slides, diagrams** — [CC BY 4.0](LICENSE-docs)

Third-party tools used in the demos (Wireshark, BloodHound CE, Microsoft Sentinel, Neo4j) remain under their respective licenses.
