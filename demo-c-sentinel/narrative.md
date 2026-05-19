# Demo C — Narrative (10 minuti)

> Script operativo di cosa dire e quando.
> Le query GQL sono in `gql_queries.md`.
> Il notebook è in `custom_graph_notebook.py` (da incollare cella per cella nella Sentinel VS Code extension).

---

## 0:00 — 1:00 · Apertura e bridge da Demo B

**Cosa fai:** chiudi BloodHound, apri una slide-titolo "Demo C — Microsoft Sentinel Graph".

**Cosa dici:**

> "Nelle prime due demo siete voi a costruire il grafo. Dai pacchetti grezzi di Wireshark, dagli oggetti AD via BloodHound. È un esercizio didattico bello, ma in un SOC enterprise reale non avete il tempo di costruire grafi a mano per ogni indagine.
>
> Adesso vediamo il livello industriale: cosa succede quando un grande vendor — Microsoft — vi mette a disposizione **i grafi pre-costruiti** sul vostro patrimonio di telemetria di sicurezza.
>
> Quello che vi mostro nei prossimi 10 minuti sono tre paradigmi diversi, tutti nello stesso prodotto: grafi *pre-computati* dal vendor, grafi *interattivi auto-provisioned* che voi traversate, e — l'ultima frontiera, rilasciata in public preview solo il 1° aprile — grafi *custom* che voi modellate e interrogate con un linguaggio standard internazionale che vi suonerà familiare."

---

## 1:00 — 3:30 · Defender XDR Attack Story (Incident Graph)

**Cosa fai:** vai sul Defender portal (`security.microsoft.com`) → Incidents → apri un incident multi-asset che hai pre-selezionato dal tuo lab → click sulla tab **Attack Story** (o "Graph").

**Cosa l'audience vede:** un grafo con nodi eterogenei — un device compromesso, l'identità dell'utente, una mailbox, un file/processo malevolo, eventualmente una sessione cloud. Tutti connessi dalla logica dell'incident.

**Cosa dici:**

> "Questo è un incident reale del mio lab. Vedete che Defender XDR ha **già costruito** un grafo che mette insieme segnali da fonti diverse: dall'endpoint che dice 'ho rilevato un file malevolo', dall'identità che dice 'questo utente ha fatto sign-in da un IP anomalo', dalla mailbox che dice 'è arrivato un email di phishing'.
>
> Punto chiave: nessun analista ha disegnato questo grafo. Defender XDR lo costruisce *automaticamente* in tempo reale, correlando segnali multi-prodotto. Questo è il modello 'pre-computed graph': il vendor sa cosa volete vedere — utenti, dispositivi, email, file, processi — e costruisce in anticipo il grafo standard per l'investigazione.
>
> Vantaggio: zero tempo di setup per l'analista, vedete subito la storia. Svantaggio: l'ontologia è fissata dal vendor — vedete solo le entità che Microsoft ha deciso di reificare nel grafo."

**Tempo cuscinetto:** click su un nodo per mostrare il pannello delle proprietà laterali, fai vedere come la timeline degli eventi è sincronizzata col grafo.

---

## 3:30 — 5:30 · Sentinel Hunting Graph (auto-provisioned)

**Cosa fai:** Defender portal → Sentinel → Graphs. Mostri la pagina di management dei grafi. Selezioni il **Hunting Graph** (auto-provisioned quando hai data lake) o il **Blast Radius**.

**Cosa l'audience vede:** un'esperienza in cui scegli un'entità (es. un utente) e fai *traversal* dei suoi vicini con un click. Ogni hop espande il grafo.

**Cosa dici:**

> "Sallendo di un gradino: questo è il Sentinel Hunting Graph, anch'esso auto-provisioned quando avete il data lake.
>
> La differenza con l'Attack Story è che qui *voi guidate l'investigazione*. Non aspettate che il vendor decida cosa è collegato a cosa. Partite da un'entità — magari il vostro utente sospetto — e fate traversal interattivo del grafo. Click. Vedete chi sono i suoi vicini. Click. Andate al next hop.
>
> Questo è il modello 'query-time graph': il grafo non esiste fino al momento in cui voi lo interrogate, e quello che vedete è esattamente la slice del dato che vi serve in quel momento.
>
> Pedagogicamente: notate che *gli stessi dati sottostanti* — gli stessi log nel data lake — possono essere visti come tabelle KQL **o** come grafo Hunting **o** come incident graph multi-asset. Non sono tre dati diversi, sono tre *rappresentazioni* dello stesso dato. La rappresentazione a grafo è quella giusta quando la domanda è 'cosa è connesso a cosa'."

---

## 5:30 — 9:00 · Custom Graphs + GQL — IL MOMENTO CLOU

Questo è il pezzo più importante della demo C, prepara bene la transizione.

**Cosa fai:**
1. Pausa di 2-3 secondi
2. Apri VS Code → notebook custom graph già pronto e Spark già caldo
3. Mostri rapidamente il codice del notebook (NON lo esegui, è già stato materializzato prima)
4. Passi al Defender portal → Sentinel → Graphs → selezioni il tuo custom graph
5. Esegui una query GQL live

**Cosa dici:**

> "Adesso il pezzo nuovo. Il 1° aprile di quest'anno — sei settimane fa — Microsoft ha rilasciato in public preview una feature chiamata **Sentinel Custom Graphs**.
>
> Vi ricordate cosa abbiamo detto nella slide T3, settantacinque minuti fa? Vi ho parlato di GQL, **Graph Query Language**, standard ISO/IEC 39075 ratificato nel 2024 — l'ho chiamato 'il momento SQL dei grafi'. Sembrava una nota di colore accademica. Bene.
>
> [transizione a VS Code]
>
> Questo è un notebook Jupyter che gira dentro la Sentinel VS Code extension. In trenta righe di Python definisco la mia ontologia di security: prendo le tabelle del data lake — qui sto usando `EntraUsers`, `EntraGroups`, `EntraMembers` — e dichiaro: questi sono i miei nodi, queste sono le mie relazioni di tipo MemberOf.
>
> [scorrimento veloce del codice, non leggi tutto]
>
> Il notebook ha definito un grafo che traversa la membership annidata dei gruppi Entra ID fino a 8 livelli di profondità. L'ho materializzato stamattina con uno scheduled job, ora vive sul tenant e posso interrogarlo.
>
> [passi al Defender portal → Sentinel → Graphs → il tuo grafo]
>
> Ecco il grafo nel Defender portal. Non ci sono dati di clienti — è il mio tenant lab. Adesso lo interrogo.
>
> [PAUSA di 2 secondi, poi]
>
> MATCH (n:Group)-[r:MemberOf*1..8]->(g:Group)  
> WHERE g.displayName = 'Privileged Access'  
> RETURN n, r, g
>
> [esegui, mostra il risultato]
>
> Notate la sintassi: non è KQL, non è SQL. È GQL — il linguaggio standard ISO. È esattamente quello che vi ho detto. Microsoft, dal 1° aprile, lo usa in produzione. Per fare security. Sui dati di telemetria reale del vostro tenant.
>
> Il punto di chiusura del percorso teorico della lezione: abbiamo iniziato con Eulero e i ponti di Königsberg. Abbiamo passato i pacchetti grezzi, abbiamo passato Active Directory, abbiamo visto i grafi pre-costruiti. E adesso vi sto mostrando uno standard internazionale del 2024, implementato da uno dei più grandi vendor mondiali, sei settimane fa, per la cybersecurity."

**Pedagogical anchor:** se ti accorgi che l'audience sta seguendo, dedica 30 secondi a fare un *traversal interattivo* — click su un nodo del risultato, espandi i vicini, fai vedere come Defender portal supporta la traversal "next hop".

---

## 9:00 — 10:00 · Chiusura e bridge a Demo D

**Cosa fai:** torni a una slide-chiusura.

**Cosa dici:**

> "Tre takeaway dalla Demo C:
>
> Primo: la stessa piattaforma offre tre paradigmi di grafo diversi — pre-computed, auto-provisioned, custom. Sono complementari. Servono problemi diversi.
>
> Secondo: lo standard GQL non è un esercizio accademico astratto. È in produzione, in uno dei sei prodotti SIEM più usati al mondo, dal 1° aprile.
>
> Terzo, il più importante: il pattern che avete visto qui — modellare la propria ontologia di security, materializzarla come grafo, interrogarla con un linguaggio dichiarativo — non è esclusivo di Microsoft. È un pattern emergente. Lo vediamo in OpenCTI, in MISP, in molte piattaforme di CTI moderne, e nella prossima demo lo vediamo applicato a un dominio molto diverso dalla SOC enterprise: la threat intelligence open-source.
>
> Adesso vi mostro come *io* — fuori da Microsoft, come ricerca indipendente — ho costruito un knowledge graph di threat intelligence usando esattamente questo paradigma. Si chiama TI Mindmap HUB. Trenta minuti, ultima demo della lezione."

---

## Note per la registrazione del backup video

- **Durata target:** 7-8 minuti (più stretto dei 10 in aula)
- **Punti critici da registrare con attenzione:**
  - Transizione VS Code → Defender portal (il momento clou)
  - Esecuzione live della query GQL (cattura sia il codice che il risultato visivo)
- **Camtasia/OBS** vanno bene. Su Windows anche **Xbox Game Bar** (Win+G).
- **Voiceover:** registra una passata mentre fai le azioni in silenzio, poi voiceover in post. È più pulito.

## Checklist pre-lezione

- [ ] Defender XDR incident scelto e screenshottato come backup
- [ ] Notebook custom graph già materializzato (scheduled job eseguito)
- [ ] Spark session VS Code testata
- [ ] Query GQL testata e produce output leggibile
- [ ] Tutti gli IP/UPN sensibili anonimizzati o redatti negli screenshot
- [ ] Backup video registrato e accessibile offline
- [ ] Slide di apertura/chiusura pronte
