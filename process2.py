#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

members = defaultdict(set)
with open("sheet.tsv") as inf:
    for line in inf:
        bits = line.removesuffix("\n").split("\t")
        band, *band_members = [x for x in bits if x]
        for member in band_members:
            members[member].add(band)

G = nx.Graph()

# Add nodes for members
for member in members:
    G.add_node(member)

# Add edges for intersections
for member1, bands1 in members.items():
    for member2, bands2 in members.items():
        if member1 != member2:
            intersection_size = len(set(bands1) & set(bands2))
            if intersection_size > 0:
                G.add_edge(member1, member2, weight=intersection_size)

# Draw the graph
pos = nx.spring_layout(G)  # Positions for all nodes
edge_labels = {
    (member1, member2): ", ".join(sorted(set(members[member1]) &
                                         set(members[member2])))
    for member1, member2, weight in G.edges(data='weight')}
plt.figure(figsize=(30,30))
nx.draw(G,
        pos,
        with_labels=True,
        edge_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Create DOT representation of the graph
dot_data = nx.drawing.nx_pydot.to_pydot(G)

# Save the DOT representation as a DOT file
dot_data.write_dot("graph.dot")

#plt.savefig("contra-members-big.png", dpi=180)
#plt.clf()
