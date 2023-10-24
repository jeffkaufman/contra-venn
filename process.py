#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt

bands = {}
with open("sheet.tsv") as inf:
    for line in inf:
        bits = line.removesuffix("\n").split("\t")
        band, *members = [x for x in bits if x]
        bands[band] = members

# Create a directed graph
G = nx.DiGraph()

# Add nodes for bands
for band in bands:
    G.add_node(band)

# Add edges for intersections
for band1, members1 in bands.items():
    for band2, members2 in bands.items():
        if band1 != band2:
            intersection_size = len(set(members1) & set(members2))
            if intersection_size > 0:
                G.add_edge(band1, band2, weight=intersection_size)

# Draw the graph
pos = nx.spring_layout(G)  # Positions for all nodes
edge_labels = {
    (band1, band2): ", ".join(sorted(set(bands[band1]) & set(bands[band2])))
    for band1, band2, weight in G.edges(data='weight')}
nx.draw(G,
        pos,
        with_labels=True,
        edge_color='black',
        alpha=1)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.savefig("contra-bands-big.png", dpi=180)
plt.clf()
