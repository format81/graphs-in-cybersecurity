# Sentinel Custom Graph — Notebook Cells for Demo C
#
# This file contains the cells of a Jupyter notebook to be run inside the
# Microsoft Sentinel VS Code extension. Each block is a separate cell.
#
# Adapted from the official Microsoft Learn sample:
# https://learn.microsoft.com/en-us/azure/sentinel/datalake/create-custom-graphs
#
# Customized for the LUISS lecture demo: builds a graph of Entra group
# memberships with nested traversal up to 8 levels deep.
#
# Prerequisites: see ../setup.md
#
# Usage: in VS Code, create a new Sentinel notebook. Copy each cell block
# below into a separate notebook cell. The first cell takes ~5 minutes
# to start the Spark session.

# ╔═══════════════════════════════════════════════════════════════════════╗
# ║ CELL 1 — Imports and provider setup                                   ║
# ╚═══════════════════════════════════════════════════════════════════════╝

from pyspark.sql import functions as F
from sentinel_lake.providers import MicrosoftSentinelProvider

lake_provider = MicrosoftSentinelProvider(spark=spark)

# Adjust to your workspace name. "System tables" is the default for Entra
# asset tables.
LOG_ANALYTICS_WORKSPACE = "System tables"


# ╔═══════════════════════════════════════════════════════════════════════╗
# ║ CELL 2 — Resolve the latest snapshot timestamp                        ║
# ╚═══════════════════════════════════════════════════════════════════════╝

snapshot_time = (
    lake_provider.read_table("EntraUsers", LOG_ANALYTICS_WORKSPACE)
    .df.agg(F.max("_SnapshotTime").alias("max_snapshot"))
    .collect()[0]["max_snapshot"]
    .strftime("%Y-%m-%dT%H:%M:%SZ")
)
print(f"Using snapshot_time: {snapshot_time}")

snapshot_filter = (
    F.col("_SnapshotTime") == F.lit(snapshot_time).cast("timestamp")
)


# ╔═══════════════════════════════════════════════════════════════════════╗
# ║ CELL 3 — Load nodes: Groups, Users, Service Principals                ║
# ╚═══════════════════════════════════════════════════════════════════════╝

# Groups
df_groups = (
    lake_provider.read_table("EntraGroups", LOG_ANALYTICS_WORKSPACE)
    .filter(snapshot_filter)
    .df
    .select(
        F.col("id").alias("nodeId"),
        F.col("displayName").alias("name"),
        F.col("description"),
        F.lit("Group").alias("nodeType"),
    )
)

# Users
df_users = (
    lake_provider.read_table("EntraUsers", LOG_ANALYTICS_WORKSPACE)
    .filter(snapshot_filter)
    .df
    .select(
        F.col("id").alias("nodeId"),
        F.col("displayName").alias("name"),
        F.col("userPrincipalName").alias("upn"),
        F.lit("User").alias("nodeType"),
    )
)

# Service Principals
df_sps = (
    lake_provider.read_table("EntraServicePrincipals", LOG_ANALYTICS_WORKSPACE)
    .filter(snapshot_filter)
    .df
    .select(
        F.col("id").alias("nodeId"),
        F.col("displayName").alias("name"),
        F.lit("ServicePrincipal").alias("nodeType"),
    )
)

print(f"Groups loaded: {df_groups.count()}")
print(f"Users loaded: {df_users.count()}")
print(f"Service principals loaded: {df_sps.count()}")


# ╔═══════════════════════════════════════════════════════════════════════╗
# ║ CELL 4 — Load edges: MemberOf relationships                           ║
# ╚═══════════════════════════════════════════════════════════════════════╝

# EntraMembers contains group membership relationships
# sourceType = "group" means the parent is a group
df_members = (
    lake_provider.read_table("EntraMembers", LOG_ANALYTICS_WORKSPACE)
    .filter(
        snapshot_filter
        & (F.col("sourceType") == "group")
    )
    .df
    .select(
        F.col("memberId").alias("startNodeId"),
        F.col("sourceId").alias("endNodeId"),
        F.col("memberType").alias("memberType"),
        F.lit("MemberOf").alias("edgeType"),
    )
)

print(f"MemberOf edges loaded: {df_members.count()}")


# ╔═══════════════════════════════════════════════════════════════════════╗
# ║ CELL 5 — Build the custom graph                                       ║
# ╚═══════════════════════════════════════════════════════════════════════╝

from sentinel_lake.graph import GraphBuilder

graph = GraphBuilder(name="entra-membership-graph")

# Register node types
graph.add_nodes(df_groups, node_type="Group", id_column="nodeId")
graph.add_nodes(df_users, node_type="User", id_column="nodeId")
graph.add_nodes(df_sps, node_type="ServicePrincipal", id_column="nodeId")

# Register edges
graph.add_edges(
    df_members,
    edge_type="MemberOf",
    start_id_column="startNodeId",
    end_id_column="endNodeId",
)

# Materialize for the interactive session
graph.build()

print(f"Graph built: {graph.summary()}")


# ╔═══════════════════════════════════════════════════════════════════════╗
# ║ CELL 6 — Run a sample GQL query in-notebook                          ║
# ╚═══════════════════════════════════════════════════════════════════════╝
# This proves the graph is queryable. The "real" queries during the demo
# happen in the Defender portal — see gql_queries.md

result = graph.query("""
MATCH (n)-[:MemberOf*1..8]->(g:Group)
WHERE g.name CONTAINS 'Admin'
RETURN n.name AS member, n.nodeType AS type, g.name AS targetGroup
LIMIT 20
""")

result.show(truncate=False)


# ╔═══════════════════════════════════════════════════════════════════════╗
# ║ CELL 7 — Schedule a graph job to materialize for the team             ║
# ╚═══════════════════════════════════════════════════════════════════════╝
# In VS Code, with this notebook open, click "Create Scheduled Job" in
# the Sentinel extension panel. Set:
#   - Graph name: "luiss-entra-membership-demo"
#   - Description: "LUISS lecture demo — Entra group memberships graph"
#   - Schedule: Daily at 06:00 UTC
#
# Once the first job run completes, the graph appears in:
#   Defender portal → Sentinel → Graphs → luiss-entra-membership-demo
