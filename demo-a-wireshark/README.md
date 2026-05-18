# Demo A — From PCAP to Graph

> Part of the lecture *"Graphs in Cybersecurity"* — LUISS Master in Cybersecurity, May 29, 2026

Build an interactive graph from a network packet capture in ~30 lines of Python, and apply the same algorithms introduced in the theory section (PageRank, connected components) to surface anomalous traffic patterns such as C2 beaconing.

## Pipeline

```
PCAP ─► tshark ─► CSV ─► pandas ─► networkx ─► pyvis ─► interactive HTML
```

## What you'll see

Three progressive views of the **same** packet capture, each adding a layer of meaning:

1. **Naive view** — every flow as an edge. Visual chaos. *Pedagogical point: this is why aggregation matters.*
2. **Weighted view** — same nodes, edge weight = number of flows. Hubs emerge.
3. **External-only view** — internal hosts (RFC1918) → public destinations. Potential C2/exfiltration candidates.

Plus a **bonus**: PageRank applied to the live graph, demonstrating that the same abstract algorithm from the theory section identifies the most "central" IPs in real traffic.

## Files

- `wireshark_to_graph.ipynb` — the full notebook, 24 cells, drop-in ready
- `smoke_test.py` — synthetic-data test to verify install (and prove the pipeline works without a real PCAP)
- `preview/preview_pagerank_view.html` — pre-generated preview of the final visualization

## Setup

```bash
pip install -r ../requirements.txt
tshark --version   # verify tshark is on PATH
```

**Windows:** tshark ships with Wireshark — add `C:\Program Files\Wireshark` to PATH.  
**macOS:** `brew install wireshark`.  
**Ubuntu:** `apt install tshark`.

## Which PCAP to use

Three options, ranked by teaching impact:

### 1. Malware-Traffic-Analysis.net (recommended)
[malware-traffic-analysis.net](https://www.malware-traffic-analysis.net/) — pick a recent case labeled "Cobalt Strike", "IcedID", or "Qakbot". Real malware traffic with beaconing patterns the bonus PageRank section will surface. Zip password: `infected`.

### 2. Wireshark Sample Captures
[wiki.wireshark.org/SampleCaptures](https://wiki.wireshark.org/SampleCaptures) — clean, no malware, good if you prefer a benign example.

### 3. Synthetic fallback
Uncomment the "Synthetic data" cell in the notebook. Generates 700 flows including a simulated C2 that PageRank correctly identifies. Zero technical risk for in-class delivery.

## Suggested in-class timing (12 min)

| Time | Action |
|---|---|
| 0:00-1:30 | Setup: "I have a PCAP from a customer engagement, let's see what's inside" |
| 1:30-3:00 | `tshark` extraction cell — 1 command, 4 fields, 30 seconds |
| 3:00-5:00 | **View 1 (naive)** — open HTML, show the chaos. *"This is useless."* |
| 5:00-7:30 | **View 2 (weighted)** — hubs emerge. *Aggregation is what makes the graph useful.* |
| 7:30-9:30 | **View 3 (external)** — only public destinations. Suspect IPs cluster. |
| 9:30-11:30 | **Bonus PageRank** — *"Remember the algorithm from T2? Here it is, live."* |
| 11:30-12:00 | Bridge: *"Same paradigm — but instead of IP packets, identities in AD..."* → Demo B |

## Pre-rehearsal checklist

- [ ] Notebook runs end-to-end with your chosen PCAP
- [ ] All three output HTMLs render correctly in browser
- [ ] HTMLs pre-loaded in browser tabs before class
- [ ] Backup video recorded (~6 min)
- [ ] If using MTA.net: zip extracted, no leftover executables

## Notes

- **Performance:** for PCAPs >500MB, tshark extraction takes 30-60s. Pre-generate `output/flows.csv` before class to skip the wait.
- **Anonymization:** for customer PCAPs, run `tcprewrite --pnat=...` or `bittwiste` first. Not needed for MTA.net captures.
- **Network requirement:** pyvis HTML loads `vis-network.js` from `cdnjs.cloudflare.com` on first open. Pre-load with Wi-Fi or you'll have an awkward moment in class.
