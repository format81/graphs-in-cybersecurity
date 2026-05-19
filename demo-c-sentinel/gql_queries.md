# GQL Queries — Demo C

> Queries to run in the **Defender portal → Sentinel → Graphs** during the live demo.  
> Custom graph name: `luiss-entra-membership-demo`

## How to access

1. Browse to `security.microsoft.com`
2. Left navigation → **Microsoft Sentinel** → **Graphs**
3. Click on the `luiss-entra-membership-demo` tile → **Query graph**
4. Paste the GQL into the editor
5. Click **Run GQL query**

## Q1 — Quick exploration: show me the schema

The first query helps the audience understand what's in the graph. Use this as a "lightweight intro" — output is small, just shows the structure.

```gql
MATCH (n)-[r]->(m)
RETURN n, r, m
LIMIT 20
```

**Expected output:** ~20 nodes (Users, Groups, ServicePrincipals) connected by `MemberOf` edges. Default starter query suggested by the Defender portal itself.

---

## Q2 — Nested group membership traversal (THE KEY QUERY)

This is the query that demonstrates the *real power* of the graph paradigm. Find all members (direct + nested, up to 8 levels) of admin-related groups.

```gql
MATCH p = (n)-[:MemberOf*1..8]->(g:Group)
WHERE g.name CONTAINS 'Admin'
RETURN p
LIMIT 50
```

**What the audience sees:** a forest of paths converging on admin groups. Notice how some users are reached via 4-5 hops — that's a *nested-group privilege escalation chain* that would be invisible in a flat table view.

**Talking point:** *"This is the kind of query you cannot write naturally in KQL. The variable-length path `MemberOf*1..8` is native graph syntax — and it's standard GQL, not a Microsoft proprietary extension."*

---

## Q3 — Service Principal access (the security-relevant scenario)

Service Principals are non-human identities (apps, automations) and are increasingly the target of OAuth abuse. Find all SPs that are members of any group.

```gql
MATCH (sp:ServicePrincipal)-[:MemberOf]->(g:Group)
RETURN sp.name AS servicePrincipal,
       g.name AS group
ORDER BY sp.name
LIMIT 30
```

**Talking point:** *"In a real attack scenario, an attacker who compromises an OAuth app inherits the privileges of the SPs that own it. This kind of query becomes part of the daily hunting routine."*

---

## Q4 — Interactive traversal (do this last, click-driven)

After running Q2 or Q3, click on a specific node in the visualization. The Defender portal offers a **"Expand to next hop"** action — use it. The audience sees the graph extending one hop at a time, query-time.

**Talking point:** *"This is what 'interactive graph traversal' means in practice — you don't write a new query for every step. You navigate the graph the way you'd navigate a website."*

---

## Backup queries

In case one of the above doesn't render well in your specific lab data:

### B1 — All direct group memberships (simple, always works)

```gql
MATCH (u:User)-[:MemberOf]->(g:Group)
RETURN u.name AS user, g.name AS group
LIMIT 25
```

### B2 — Find groups with many members (interesting structure)

```gql
MATCH (n)-[:MemberOf]->(g:Group)
RETURN g.name AS group, count(n) AS members
ORDER BY members DESC
LIMIT 10
```

### B3 — Visualize a specific group's full neighborhood

Replace `'<group-name>'` with an actual group name from your tenant.

```gql
MATCH (n)-[r:MemberOf*1..3]-(g:Group)
WHERE g.name = '<group-name>'
RETURN n, r, g
```

## Notes on GQL syntax

Quick reference for the audience, in case someone asks during Q&A:

- `MATCH` declares a pattern — like SQL `FROM` for graphs
- `(n:Label)` matches a node with optional label
- `[r:RelType]` matches a relationship with optional type
- `*1..N` is the variable-length-path operator — *only graph languages have this*
- `WHERE` filters, like SQL
- `RETURN` projects, like SQL `SELECT`
- `LIMIT` is identical to SQL

GQL ISO standard reference: [ISO/IEC 39075:2024](https://www.iso.org/standard/76120.html)
