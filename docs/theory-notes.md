# Theory Notes — Graphs in Cybersecurity

> Companion notes for the theoretical portion (35 min) of the lecture.  
> These will be expanded as preparation for the May 29 delivery.

## T1 — Fundamentals (10 min)

- **History**: Euler and the Königsberg bridges (1736), birth of graph theory
- **Definition**: a graph G = (V, E) where V is a set of vertices/nodes and E is a set of edges/links
- **Types**:
  - Directed vs undirected
  - Weighted vs unweighted
  - Simple vs multigraph
  - Labeled/property graph
- **Property graph vs RDF**:
  - *Property graph* — nodes and edges with key-value properties (Neo4j model)
  - *RDF* — subject-predicate-object triples, designed for semantic web
- **Knowledge graph** — a graph with semantics, ontologies, and reasoning capabilities

## T2 — Algorithms Relevant to Cybersecurity (12 min)

- **Shortest path** — Dijkstra/BFS. Application: attack path discovery
- **Centrality**:
  - PageRank — random-walker intuition; identifies "influential" nodes
  - Betweenness — nodes on many shortest paths; chokepoints
  - Degree — simplest measure of connectivity
- **Community detection** — Louvain, Leiden. Maximizes modularity. Application: clustering APT campaigns by shared infrastructure or TTPs
- **Connected components** — disconnected subgraphs. Application: blast radius, segmentation

## T3 — Technologies and Query Languages (7 min)

- **Graph databases**: Neo4j (de facto standard), TigerGraph (extreme scale), Amazon Neptune (managed), Memgraph (in-memory), ArangoDB (multi-model)
- **Query languages**:
  - Cypher (Neo4j-native, declarative, pattern-matching)
  - Gremlin (Apache TinkerPop, traversal-based)
  - SPARQL (for RDF)
- **GQL** — ISO/IEC 39075:2024 — the first international standard for graph query languages, ratified in April 2024. The "SQL moment" for graphs

## T4 — Frontier: Graph Neural Networks (6 min)

- **From query to ML on graphs** — what if the graph itself were input to a model?
- **Message passing intuition** — each node updates its representation by aggregating those of its neighbors, iteratively
- **Cyber applications**:
  - Intrusion detection on graph-of-flows
  - Malware classification on call/dependency graphs
  - Phishing detection on URL/domain graphs
  - Lateral movement prediction
- **Reading**: Distill.pub — *A Gentle Introduction to Graph Neural Networks* (sanchez-lengeling, 2021)

## Pedagogical thread

The "running example" — a 6-node mini-network introduced in T1 — grows progressively:
- T1 introduces it as a generic graph
- T2 demonstrates each algorithm visually on the same graph
- T3 shows a Cypher query against it
- T4 hints at how a GNN would consume it

The bridge to the demos: *"Same mathematical object, different domains — packets in Demo A, identities in Demo B, signals in Demo C, threat reports in Demo D."*
