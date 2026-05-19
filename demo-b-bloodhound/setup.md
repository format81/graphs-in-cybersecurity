# Setup BloodHound CE

Tested on Windows 11 + Docker Desktop, May 2026.

## Prerequisites

- Docker Desktop running
- ~3 GB free disk space (container images + Neo4j data)
- PowerShell (not CMD — some commands use PowerShell-specific syntax)

## Install

```powershell
# 1. Create a working directory outside any code repository
mkdir C:\bloodhound-ce
cd C:\bloodhound-ce

# 2. Download the official docker-compose.yml
Invoke-WebRequest -Uri https://ghst.ly/getbhce -OutFile docker-compose.yml

# 3. Pull images (~5 min on first run)
docker compose pull

# 4. Start all services (postgres + neo4j + bloodhound)
docker compose up -d

# 5. Verify all three containers are running
docker compose ps
```

You should see three healthy services: `app-db`, `graph-db`, `bloodhound`.

## First-time login

```powershell
# Retrieve the auto-generated admin password from logs
docker compose logs bloodhound | Select-String "Initial Password Set To"
```

Copy the password, then:
1. Open `http://localhost:8080`
2. Login as `admin` with the retrieved password
3. Change the password on first prompt (any local-only value is fine)

## Import the example dataset

The official BloodHound CE Example Dataset is published by SpecterOps. To find the current download link, see the [BloodHound CE documentation](https://bloodhound.specterops.io/).

Once you have the ZIP file:
1. Extract to a folder — you'll find ~30 JSON files (users, computers, groups, etc.)
2. In BloodHound: **Administration → File Ingest → Upload File(s)**
3. Select **all** JSON files at once
4. Wait for ingestion (~1-3 min). Status appears in the file list ("Success" when done).

## Sanity check

In **Explore → Cypher** tab, run:

```cypher
MATCH (n) RETURN count(n) AS total_nodes
```

You should see at least ~1000 nodes. If you see 0, the ingestion failed — check container logs.

## Daily start/stop

```powershell
cd C:\bloodhound-ce
docker compose start    # daily start
docker compose stop     # daily stop (preserves data)
docker compose down -v  # full reset (deletes all data — use only when needed)
```

## Troubleshooting

**`curl` saves an HTML page instead of YAML**  
Use `Invoke-WebRequest` (PowerShell native, follows redirects) or `curl.exe -L` (Windows curl with explicit `-L` flag for following redirects).

**`Select-Object` not recognized**  
You're in CMD, not PowerShell. Open PowerShell instead.

**Container `bloodhound` starts but UI returns 502**  
Wait 60-90 seconds after `docker compose up -d`. Neo4j needs time to fully initialize before BloodHound can connect.

**File ingest shows "Failed"**  
Check that you uploaded the JSON files inside the ZIP, not the ZIP itself. JSON files are not compressed individually.
