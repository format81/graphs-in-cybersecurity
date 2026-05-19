# Setup — Demo C

This demo requires a Microsoft Sentinel environment with the data lake feature enabled and a few VS Code extensions. The author already has these in a personal lab — these notes are reproducibility guidance for anyone else.

## Prerequisites

### Tenant-side

- **Microsoft Sentinel workspace** in the Defender portal
- **Microsoft Sentinel data lake** onboarded
  - [Onboard to Microsoft Sentinel data lake](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-onboarding)
- **Microsoft Entra ID data connector** enabled, ingesting asset tables (`EntraUsers`, `EntraGroups`, `EntraMembers`, `EntraServicePrincipals`)
  - [Asset data ingestion in Sentinel data lake](https://learn.microsoft.com/en-us/azure/sentinel/datalake/data-ingestion-overview)
- **XDR permissions** in the Sentinel data lake:
  - To create graphs: not be a scoped user
  - To query graphs: read access on the data sources used in the graph

### Client-side (the machine running the demo)

- **Visual Studio Code** (latest stable)
- **Microsoft Sentinel VS Code extension** — provides the Jupyter integration with the data lake and the `sentinel_lake.providers` Python library
  - Install from VS Code marketplace, then sign in with the Microsoft account that has Sentinel access
- **Jupyter extension** for VS Code

### Optional but recommended

- **Defender XDR demo data / lab incidents** to show on the Attack Story view (you can simulate via the Microsoft Defender for Endpoint evaluation lab, or use a real incident from a personal tenant)
- **Backup video** recorded — *strongly recommended* because the Custom Graph experience depends on cloud services that can be slow or temporarily unavailable

## Cost note

Sentinel Custom Graphs are billed under the **Sentinel graph meter** (Security Compute Units, SCU) starting April 1, 2026. For a single demo with a small Entra dataset, costs are negligible (a few cents). Be aware of this if running on a production tenant.

## Sanity check before the demo

1. Open VS Code → Sentinel extension → sign in → confirm workspace visible
2. Open the demo notebook → run the first cell (`MicrosoftSentinelProvider`) → first Spark session takes ~5 min to start, plan accordingly
3. Confirm at least one Entra table returns data: `lake_provider.read_table("EntraUsers", workspace).df.count()` should return > 0
4. In the Defender portal → Sentinel → Graphs → confirm at least one materialized custom graph is visible (run the scheduled job *before* class)

## Day-of checklist

- [ ] Defender portal already logged in (one less auth prompt in front of the audience)
- [ ] VS Code already open with the notebook ready
- [ ] Spark session warmed up (first cell run 10 min before class)
- [ ] Custom graph already materialized via scheduled job
- [ ] Defender XDR incident chosen and reviewed (you know what story to tell)
- [ ] Browser zoom 110-125% for projection
- [ ] Backup video accessible offline
