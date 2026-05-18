"""Smoke test: esegue la logica del notebook con dati sintetici."""
import random
import ipaddress
from pathlib import Path
import pandas as pd
import networkx as nx
from pyvis.network import Network

random.seed(42)
OUTPUT_DIR = Path("output_test")
OUTPUT_DIR.mkdir(exist_ok=True)
FLOWS_CSV = OUTPUT_DIR / "flows.csv"

# Synthetic flows con un "C2" beaconing
internal_hosts = [f"10.0.0.{i}" for i in range(1, 8)]
external_hosts = [f"203.0.113.{i}" for i in [10, 25, 42, 77]] + ["8.8.8.8"]
c2 = "203.0.113.42"
rows = []
for _ in range(500):
    src = random.choice(internal_hosts)
    dst = random.choice(external_hosts + internal_hosts)
    dport = random.choice([80, 443, 53, 22, 3389])
    rows.append((src, dst, dport, ""))
for _ in range(200):
    rows.append((random.choice(internal_hosts), c2, 443, ""))
pd.DataFrame(rows, columns=["src","dst","tcp_dport","udp_dport"]).to_csv(
    FLOWS_CSV, index=False, header=False)

# Load
df = pd.read_csv(FLOWS_CSV, names=["src","dst","tcp_dport","udp_dport"], dtype=str)
df["dport"] = df["tcp_dport"].fillna(df["udp_dport"])
df = df.dropna(subset=["src","dst"])
print(f"Flussi totali: {len(df)}, src unici: {df['src'].nunique()}, dst unici: {df['dst'].nunique()}")

# View 1
G1 = nx.from_pandas_edgelist(df, "src", "dst", create_using=nx.DiGraph())
print(f"View 1 — Nodi: {G1.number_of_nodes()}, Archi: {G1.number_of_edges()}")
net1 = Network(notebook=False, directed=True, height="650px", width="100%")
net1.from_nx(G1)
net1.write_html(str(OUTPUT_DIR / "view1.html"), open_browser=False, notebook=False)

# View 2 weighted
weighted = df.groupby(["src","dst"]).size().reset_index(name="weight")
G2 = nx.from_pandas_edgelist(weighted, "src", "dst", edge_attr="weight", create_using=nx.DiGraph())
print(f"View 2 — Nodi: {G2.number_of_nodes()}, Archi: {G2.number_of_edges()}")

# View 3 external
RFC1918 = [ipaddress.ip_network(n) for n in
           ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16")]

def is_internal(ip):
    try:
        addr = ipaddress.ip_address(ip)
        return any(addr in net for net in RFC1918)
    except ValueError:
        return False

ext = weighted[weighted["src"].apply(is_internal) & ~weighted["dst"].apply(is_internal)]
print(f"View 3 — Host interni→esterni: {ext['src'].nunique()}, dest esterne: {ext['dst'].nunique()}")

# Bonus PageRank
pr = nx.pagerank(G2, weight="weight")
top = sorted(pr.items(), key=lambda x: -x[1])[:5]
print(f"\nTop 5 PageRank:")
for ip, score in top:
    tipo = "interno" if is_internal(ip) else "ESTERNO"
    print(f"  {ip:20s}  {score:.4f}  ({tipo})")

# Components
G2u = G2.to_undirected()
comps = list(nx.connected_components(G2u))
print(f"\nComponenti connesse: {len(comps)}")
print(f"Dimensione max: {max(len(c) for c in comps)}")

print("\n✓ Tutta la logica del notebook funziona correttamente.")
