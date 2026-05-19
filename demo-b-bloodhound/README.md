# Demo B — Active Directory Attack Paths with BloodHound

> Part of the lecture *"Graphs in Cybersecurity"* — LUISS Master in Cybersecurity, May 29, 2026

Active Directory **is** a graph: users, computers, groups, and GPOs are nodes; memberships, sessions, and ACL permissions are edges. BloodHound makes this graph explicit and queryable — born as an offensive tool, today equally adopted by blue teams.

This demo shows the same Active Directory graph from two perspectives — attack and defense — using identical underlying data and visualization, changing only the direction of reading.

## What you'll see (12 min)

1. **AD-as-graph** — how nested group memberships, ACLs, and sessions form a queryable graph
2. **Shortest path to Domain Admins** — the literal application of the algorithm from theory T2 to identity security
3. **Unconstrained Delegation** — a legacy misconfiguration surfaced trivially by graph queries
4. **Defensive reframing** — same graph, blue-team reading: who can take over privileged groups?

## Files

- `setup.md` — quick setup of BloodHound CE on Windows + Docker Desktop
- `queries.cypher` — the 4 main queries used in class + 4 backup queries (all verified against the official BloodHound CE Example Dataset)
- `narrative.md` — minute-by-minute script of what to say during the demo
- `screenshots/` — annotated screenshots of key views (for slides or backup if Neo4j is unavailable)

## Quick start (local reproduction)

```powershell
# Requires: Docker Desktop running
mkdir bloodhound-ce
cd bloodhound-ce
Invoke-WebRequest -Uri https://ghst.ly/getbhce -OutFile docker-compose.yml
docker compose pull
docker compose up -d

# Retrieve the auto-generated admin password
docker compose logs bloodhound | Select-String "Initial Password Set To"
```

Then:
1. Open `http://localhost:8080` and login (`admin` + generated password)
2. Download the **BloodHound CE Example Data** from [SpecterOps documentation](https://bloodhound.specterops.io/)
3. Upload all JSON files via **Administration → File Ingest**
4. Wait for ingestion to complete (~1-3 minutes)
5. Verify in **Explore → Cypher** tab with: `MATCH (n) RETURN count(n)` (should return > 1000)

## Dataset summary

The BloodHound CE Example dataset is a synthetic three-domain forest:

| Domain | Notable property |
|---|---|
| `GHOST.CORP` | DC has unconstrained delegation enabled |
| `PHANTOM.CORP` | Multiple kerberoastable accounts |
| `WRAITH.CORP` | Trust paths into adjacent domains |

No real data, no client information. Safe for public teaching.

## Pre-class checklist

See `narrative.md` for the full pre-class checklist. Key items:
- BloodHound CE running, dataset ingested
- All 4 main queries produce readable graphs
- Browser zoom at 110-125% for projection legibility
- Backup video recorded and offline-accessible

## License

Code in this directory is under MIT. Documentation is under CC BY 4.0. See repository root.
