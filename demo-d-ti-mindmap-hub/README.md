# Demo D — TI Mindmap HUB Knowledge Graph

> Part of the lecture *"Graphs in Cybersecurity"* — LUISS Master in Cybersecurity, May 29, 2026

**Status:** Coming soon. Material will be added before the lecture.

## What this demo covers

A live production knowledge graph for Cyber Threat Intelligence, built from OSINT reports via Large Language Models.

**Current production stats** (as of May 2026):
- 929 ingested OSINT reports
- 21,601 canonical entities (threat actors, malware families, TTPs, infrastructure)
- 59,783 observed relationships extracted from text
- 46 inferred cross-report relationships

## Architecture highlights

- Two-layer graph: **Mention layer** (raw extractions per report) + **Canonical layer** (resolved entities)
- Three-level entity resolution pipeline
- IOC protection gate (prevents whitelisting-induced data loss)
- Differentiated edge types: `:OBSERVED_REL` (in text) vs `:INFERRED_REL` (cross-report)
- Neo4j on Azure, secured with bolt+s

## Main project repositories

The core implementation lives in dedicated repos under the TI Mindmap HUB organization:

- **Knowledge graph engine**: [TI-Mindmap-HUB-Org/ti-kg](https://github.com/TI-Mindmap-HUB-Org/ti-kg)
- **MCP server (25 tools, 6 KG-specific)**: [TI-Mindmap-HUB-Org/ti-mindmap-mcp](https://github.com/TI-Mindmap-HUB-Org/ti-mindmap-mcp)
- **Platform website**: [ti-mindmap-hub.com](https://ti-mindmap-hub.com)

## Files (planned)

- `cypher_queries.md` — Cypher queries used in the live demo
- `architecture.md` — diagram and walkthrough of the two-layer design
