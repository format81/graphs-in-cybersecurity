# Screenshot Guide — Demo B

5 screenshot da catturare durante la prova della demo. Servono per:
- Backup nelle slide (se Neo4j non parte in aula)
- Documentazione del repository
- Materiale post-lezione condivisibile

## Convenzioni

- **Formato:** PNG, full-screen del browser (1920×1080 minimo)
- **Dark mode attivo** — più leggibile su slide e GitHub dark theme
- **Browser zoom 100%** per gli screenshot (in aula userai 110-125%, ma per docs è meglio standard)
- **Salvare in:** `demo-b-bloodhound/screenshots/`

## Naming convention

```
01_membership_tree.png       — Q1
02_shortest_path_to_da.png   — Q2 (LA SLIDE PIÙ IMPORTANTE)
03_unconstrained_delegation.png  — Q3
04_defensive_view.png        — Q4
05_dataset_overview.png      — vista d'insieme (opzionale)
```

## Lista screenshot

### 1. `01_membership_tree.png` — Q1

**Cosa cattura:** il risultato di Q1 — tre gruppi DOMAIN ADMINS con membri visibili attorno.

**Come prepararlo:**
1. Esegui Q1
2. Aspetta che il layout si stabilizzi (~2 secondi)
3. Click **Layout** → prova "Sequential" o "Standard" — scegli quello più leggibile
4. Zoom out finché vedi tutti e tre i gruppi
5. Screenshot

### 2. `02_shortest_path_to_da.png` — Q2 (PIÙ IMPORTANTE)

**Cosa cattura:** cammini d'attacco verso Domain Admins.

**Come prepararlo:**
1. Esegui Q2
2. Vuoi catturare un *cammino multi-hop chiaro* — se vedi solo membership dirette, prova ad aumentare `LIMIT` o togliere il filtro `u.enabled`
3. Layout "Sequential" tende a rendere i path più leggibili (sorgenti a sinistra, destinazione a destra)
4. Se possibile, evidenzia visivamente UN cammino specifico (click sui nodi del path)
5. Screenshot

### 3. `03_unconstrained_delegation.png` — Q3

**Cosa cattura:** i computer con unconstrained delegation, in particolare `GHOST-DC01`.

**Come prepararlo:**
1. Esegui Q3
2. Click sul nodo `GHOST-DC01` per espandere il pannello proprietà a destra
3. Lo screenshot deve mostrare *sia* il nodo nel canvas *sia* le sue proprietà laterali (con `unconstraineddelegation: true` visibile)
4. Screenshot

### 4. `04_defensive_view.png` — Q4

**Cosa cattura:** gruppo DOMAIN ADMINS con archi entranti di GenericAll, WriteDacl, ecc.

**Come prepararlo:**
1. Esegui Q4
2. Layout "Standard" per questa
3. Evidenziare visualmente alcuni archi pericolosi (passa con mouse sopra per vedere il tipo)
4. Screenshot

### 5. `05_dataset_overview.png` (opzionale)

**Cosa cattura:** schermata "Administration → File Ingest" mostrando i 31 file importati con status Success.

Utile per documentare cosa contiene il dataset, ma non essenziale.

## Suggerimenti per migliorare la leggibilità

- **Hide Labels** non andrebbe attivo: lasciali visibili
- Se i nodi si sovrappongono: trascinali manualmente prima dello screenshot
- Se hai troppi nodi: riduci `LIMIT` nella query e ri-screenshot
- Per cammini multi-hop, **non** usare layout circolare — usa Sequential/Hierarchical
