# Screenshot Guide — Demo C

5 screenshot da catturare, tutti anonimizzati prima del commit.

## Convenzioni

- **Formato:** PNG, 1920×1080+
- **Dark mode attivo** (Defender portal supporta dark mode dal menu profilo in alto a destra)
- **Browser zoom 100%** per gli screenshot del repo (in aula proietti al 110-125%)
- **Salvare in:** `demo-c-sentinel/screenshots/`
- **Anonimizzazione:** maschera con redazione PowerPoint, Greenshot, o `redact` di Snip & Sketch:
  - Tutti gli UPN (user principal names)
  - Tenant GUID nella URL bar
  - Display name di dipendenti reali
  - Numeri di telefono, indirizzi email

## Naming convention

```
01_xdr_attack_story.png          — Attack Story view from Defender XDR
02_sentinel_hunting_graph.png    — Hunting / Blast Radius view
03_vscode_notebook.png           — The notebook in VS Code (code visible)
04_custom_graph_defender.png     — Custom graph in Defender portal, query loaded
05_gql_query_result.png          — GQL query result (the killer moment)
```

## Lista screenshot

### 1. `01_xdr_attack_story.png`

**Cosa cattura:** vista Attack Story di un incident multi-asset.

**Cosa anonimizzare:**
- Nome utente reale → "John Doe" o "User-1"
- UPN → `user1@contoso.com`
- Hostname → `WS-001`
- IP esterni → mantenere se pubblici (utile per realismo), oppure mascherare se sono IP malevoli noti

**Tip:** scegli un incident con almeno 4 tipi di entità diverse (Device + User + Mailbox + File/Process). Più ricco è il grafo, più impatto fa.

### 2. `02_sentinel_hunting_graph.png`

**Cosa cattura:** la pagina di management dei grafi auto-provisioned in Sentinel, o un Blast Radius view aperto.

**Path:** Defender portal → Sentinel → Graphs

### 3. `03_vscode_notebook.png`

**Cosa cattura:** VS Code aperto con il custom graph notebook, almeno le celle che importano `MicrosoftSentinelProvider` e quelle che definiscono nodi/archi visibili.

**Tip:** dark theme di VS Code, font grande (Ctrl+`+`), scrolla fino alle celle più "didattiche".

### 4. `04_custom_graph_defender.png`

**Cosa cattura:** la pagina del custom graph nel Defender portal, con:
- Il nome del grafo visibile in alto (`luiss-entra-membership-demo`)
- Lo schema del grafo nel pannello laterale (nodi: User/Group/ServicePrincipal, edge: MemberOf)
- Una query GQL già scritta nell'editor

### 5. `05_gql_query_result.png` (LA PIÙ IMPORTANTE)

**Cosa cattura:** il risultato della query Q2 — il grafo di nested group memberships, con paths multi-hop chiaramente visibili.

**Tip:** scegli un layout (gerarchico o radiale) che mostri *chiaramente* la profondità dei path. Lo screenshot deve "raccontare" che ci sono 4-5 hop in alcuni cammini.

Se hai pochi gruppi con membership profonde nel tuo tenant, considera di crearne qualcuno per la demo (script PowerShell o portale Entra). Investimento 15 min, ritorno enorme.

## Suggerimenti per migliorare la leggibilità

- Nascondi pannelli laterali non rilevanti (chiudi il pannello proprietà se non serve)
- Massimizza l'area del grafo prima di catturare
- Usa labels-visible se i nomi sono leggibili (non sovraffollare)
- Se il grafo è troppo affollato, riduci `LIMIT` nella query e ri-screenshot
