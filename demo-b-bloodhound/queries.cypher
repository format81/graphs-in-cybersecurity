// ═══════════════════════════════════════════════════════════════════════════
// Demo B — BloodHound CE Cypher Queries
// LUISS Master Cybersecurity — 29 maggio 2026
// Dataset: BloodHound CE Example Data
//   Forest: GHOST.CORP, PHANTOM.CORP, WRAITH.CORP
// ═══════════════════════════════════════════════════════════════════════════

// ───────────────────────────────────────────────────────────────────────────
// Q1 — APERTURA: AD è un grafo
// ───────────────────────────────────────────────────────────────────────────
// Mostra i membri (diretti e indiretti) dei gruppi Domain Admins
// in tutto il forest. Usata come "intro visiva" alla struttura.
//
// Cosa l'audience vede: i gruppi DOMAIN ADMINS@<dominio> con utenti collegati
// via MemberOf, e sotto-gruppi nidificati.
// ───────────────────────────────────────────────────────────────────────────
MATCH p = (u:User)-[:MemberOf*1..]->(g:Group)
WHERE g.name STARTS WITH "DOMAIN ADMINS"
RETURN p
LIMIT 100;


// ───────────────────────────────────────────────────────────────────────────
// Q2 — CLOU OFFENSIVE: Shortest Path to Domain Admins
// ───────────────────────────────────────────────────────────────────────────
// La query "regina" di BloodHound. Letteralmente shortestPath()
// l'algoritmo della slide T2 applicato al problema d'attacco.
//
// Per ogni utente attivo, trova il cammino più breve verso un gruppo
// DOMAIN ADMINS — anche multi-step via MemberOf, AdminTo, HasSession,
// GenericAll, GenericWrite, WriteDacl, ecc.
//
// Cosa l'audience vede: cammini d'attacco non banali — un utente
// "qualsiasi" che, attraverso 3-4 hop, può prendere DA.
// ───────────────────────────────────────────────────────────────────────────
MATCH p = shortestPath((u:User)-[*1..]->(g:Group))
WHERE g.name STARTS WITH "DOMAIN ADMINS"
  AND u.enabled = true
RETURN p
LIMIT 25;


// ───────────────────────────────────────────────────────────────────────────
// Q3 — OFFENSIVE: Unconstrained Delegation
// ───────────────────────────────────────────────────────────────────────────
// Mostra computer con unconstrained delegation abilitata.
// Sono server in cui un attaccante può catturare credenziali Kerberos
// di chiunque vi si autentichi — anche Domain Admin.
//
// Nel dataset esempio: GHOST-DC01 ha questa proprietà (visibile dal JSON
// importato — campo "unconstraineddelegation": true).
//
// Cosa l'audience vede: pochi nodi (i DC e qualche server), ma è il
// modo per parlare di una vera misconfiguration AD comune.
// ───────────────────────────────────────────────────────────────────────────
MATCH (c:Computer {unconstraineddelegation: true})
RETURN c;


// ───────────────────────────────────────────────────────────────────────────
// Q4 — REFRAME DIFENSIVO: chi può prendere il controllo di Domain Admins?
// ───────────────────────────────────────────────────────────────────────────
// La stessa struttura a grafo, ma letta dal blue team:
// "Quali entità hanno permessi diretti pericolosi sui gruppi DA?"
// Una sola modifica ACL nel posto sbagliato apre tutto.
//
// Cosa l'audience vede: oltre ai membri del gruppo, eventuali entità
// con GenericAll/GenericWrite/WriteDacl/WriteOwner/Owns sul gruppo DA.
// Ognuno di questi archi è un controllo di sicurezza che il blue team
// deve auditare.
//
// Punto pedagogico: "Stesso grafo. Cambiamo solo la direzione di lettura."
// ───────────────────────────────────────────────────────────────────────────
MATCH p = (n)-[r:GenericAll|GenericWrite|WriteDacl|WriteOwner|Owns]->(g:Group)
WHERE g.name STARTS WITH "DOMAIN ADMINS"
RETURN p
LIMIT 50;


// ═══════════════════════════════════════════════════════════════════════════
// QUERY DI BACKUP (per Q&A o se una delle sopra non rende bene)
// ═══════════════════════════════════════════════════════════════════════════

// B1 — Kerberoastable users con path verso target high-value
// Utenti con SPN (vulnerabili a kerberoasting) che hanno anche
// un cammino verso Domain Admins. Doppia vulnerabilità.
MATCH (u:User {hasspn: true})
MATCH p = shortestPath((u)-[*1..]->(g:Group))
WHERE g.name STARTS WITH "DOMAIN ADMINS"
RETURN p
LIMIT 10;


// B2 — Sessioni di Domain Admin su computer non-DC
// Utenti DA con sessioni attive su macchine "normali" = target prioritari
// per lateral movement (credential dump).
MATCH (u:User)-[:MemberOf*1..]->(g:Group)
WHERE g.name STARTS WITH "DOMAIN ADMINS"
MATCH (c:Computer)-[:HasSession]->(u)
WHERE NOT c.name CONTAINS "DC"
RETURN u.name, c.name
LIMIT 20;


// B3 — Cross-domain attack: PHANTOM users con path a GHOST DA
// Sfruttando i trust del forest, utenti di un dominio possono raggiungere
// DA di un altro dominio. Dimostra perché i trust sono superficie d'attacco.
MATCH p = shortestPath(
  (u:User)-[*1..]->(g:Group {name: "DOMAIN ADMINS@GHOST.CORP"})
)
WHERE u.domain = "PHANTOM.CORP"
  AND u.enabled = true
RETURN p
LIMIT 10;


// B4 — Inventario rapido del dataset
// Utile per sanity check pre-lezione. Mostra quanti nodi per tipo.
MATCH (u:User)        RETURN "User"     AS tipo, count(u) AS quanti
UNION
MATCH (c:Computer)    RETURN "Computer" AS tipo, count(c) AS quanti
UNION
MATCH (g:Group)       RETURN "Group"    AS tipo, count(g) AS quanti
UNION
MATCH (gpo:GPO)       RETURN "GPO"      AS tipo, count(gpo) AS quanti
UNION
MATCH (ou:OU)         RETURN "OU"       AS tipo, count(ou) AS quanti
UNION
MATCH (d:Domain)      RETURN "Domain"   AS tipo, count(d) AS quanti;
