# Task 2, Kruskals algorithm
# Minimum Spanning Tree with Kruskal's Algorithm


# a) Create and depict connected graph

import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(G, pos, title, mst_edges=None, filename=None):
  
    plt.figure(figsize=(6, 6))
    # base graph
    nx.draw_networkx(G, pos, with_labels=True, node_size=700, font_size=12, width=1.5)
    # edge labels (weights)
    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    # highlight current MST edges if any
    if mst_edges:
        nx.draw_networkx_edges(
            G, pos,
            edgelist=[(u, v) for (u, v, _) in mst_edges],
            width=5.0  # thicker to make them stand out
        )

    plt.title(title)
    plt.axis("off")
    if filename:
        plt.savefig(filename, bbox_inches="tight", dpi=160)
        print(f"Saved figure: {filename}")
    plt.show()

def main():
 
#Create the connected graph

    G = nx.Graph()
    nodes = range(1, 8)  # 7 nodes labeled 1..7
    G.add_nodes_from(nodes)

    # 11 weighted edges (u, v, weight)
    edges = [
        (1, 2, 7),
        (1, 3, 5),
        (2, 3, 9),
        (2, 4, 8),
        (2, 5, 7),
        (3, 5, 15),
        (4, 5, 5),
        (4, 6, 6),
        (5, 6, 8),
        (5, 7, 9),
        (6, 7, 11),
    ]
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    # fixed layout so figures look consistent
    pos = nx.circular_layout(G)

    # Draw initial graph
    draw_graph(G, pos, "Initial Connected Graph (7 nodes, 11 edges)", filename="a_initial_graph.png")

   
#b) Algorithm used
    print("MST algorithm: Kruskal's algorithm (Greedy).")
    print("Idea: sort edges by non-decreasing weight and add an edge if it does not create a cycle (Union-Find).")

 
#c) Kruskal step-by-step using Union-Find
    parent = {v: v for v in G.nodes()}
    rank = {v: 0 for v in G.nodes()}

    def find(x):
        # path compression
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        # union by rank
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    # sort edges by weight
    sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]["weight"])

    print("\nSorted edges by weight:")
    for (u, v, d) in sorted_edges:
        print(f"  ({u}, {v}) weight {d['weight']}")

    mst_edges = []
    total_weight = 0
    step = 1

    print("\nKruskal step-by-step:")
    for (u, v, d) in sorted_edges:
        w = d["weight"]
        if find(u) == find(v):
            print(f"Consider ({u}, {v}) w={w}: SKIP (cycle)")
            continue

        # take the edge
        union(u, v)
        mst_edges.append((u, v, w))
        total_weight += w
        print(f"Consider ({u}, {v}) w={w}: TAKE")

        # draw progress after each TAKE
        draw_graph(
            G, pos,
            title=f"MST Progress (step {step}): added ({u}, {v}) w={w}",
            mst_edges=mst_edges,
            filename=f"c_progress_step_{step}.png"
        )
        step += 1

        if len(mst_edges) == len(G.nodes()) - 1:
            break

    print("\nSelected MST edges in order:")
    for (u, v, w) in mst_edges:
        print(f"  ({u}, {v}) weight {w}")
    print(f"Total MST weight = {total_weight}")


#d) Final MST figure

    draw_graph(
        G, pos,
        title="Final Minimum Spanning Tree (Kruskal)",
        mst_edges=mst_edges,
        filename="d_final_mst.png"
    )

if __name__ == "__main__":
    main()

