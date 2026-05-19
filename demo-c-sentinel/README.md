# Demo C — Microsoft Sentinel Graph & Defender XDR Investigation Graphs

> Part of the lecture *"Graphs in Cybersecurity"* — LUISS Master in Cybersecurity, May 29, 2026

Microsoft Sentinel and Defender XDR show three distinct paradigms of *graphs-as-a-service* in a modern SOC platform:

1. **Pre-computed graphs** — Defender XDR Incident Graph / Attack Story, auto-built from multi-source signals (endpoint, identity, mailbox, cloud)
2. **Auto-provisioned interactive graphs** — Sentinel Hunting Graph and Blast Radius, available in the Defender portal when the Sentinel data lake is enabled
3. **Custom graphs with GQL** — Public preview since April 1, 2026: defenders model their own ontology in a Jupyter notebook (Sentinel VS Code extension), materialize the graph, and query it with **Graph Query Language** (ISO/IEC 39075:2024) from the Defender portal

This demo walks through all three, with a special focus on Custom Graphs — the closure of the theory section's GQL discussion.

## What you'll see (10 min)

1. **Defender XDR Attack Story** — a multi-asset incident graph, pre-built by the platform
2. **Sentinel Hunting Graph** — analyst-driven graph traversal at query time
3. **Custom Graph + GQL** — author a graph from Entra group memberships, materialize it, query with GQL in the Defender portal

## Pedagogical thread

> *"In Demo A and Demo B, you constructed the graph from raw data. Here, Microsoft pre-builds graphs for you at enterprise scale. But the most interesting bit is the last one — Sentinel Custom Graphs let you author your own graph, then query it with the same GQL standard we introduced in theory T3. From an ISO standardization document to production security tooling in 18 months."*

## Files

- `setup.md` — prerequisites: Sentinel data lake, VS Code extension, Entra connector, permissions
- `narrative.md` — minute-by-minute script of what to say during the demo (Italian)
- `custom_graph_notebook.py` — the cells of the notebook to run in the Sentinel VS Code extension
- `gql_queries.md` — the GQL queries used in the Defender portal
- `screenshots/` — annotated screenshots of key views (anonymized)

## Key references

- [Microsoft Sentinel graph overview](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-graph-overview)
- [Custom graphs in Microsoft Sentinel (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/custom-graphs-overview)
- [Get started with custom graphs](https://learn.microsoft.com/en-us/azure/sentinel/datalake/create-custom-graphs)
- [Visualize custom graphs in Sentinel graph](https://learn.microsoft.com/en-us/azure/sentinel/datalake/graph-visualization)
- [Announcing public preview of custom graphs in Microsoft Sentinel](https://techcommunity.microsoft.com/blog/microsoft-security-blog/announcing-public-preview-of-custom-graphs-in-microsoft-sentinel/4507410) — April 1, 2026

## Anonymization note

All screenshots and demo data come from a personal Microsoft lab tenant. No customer data. Tenant GUIDs and user principal names are redacted in committed screenshots.

## License

Code in this directory is under MIT. Documentation is under CC BY 4.0. See repository root.
