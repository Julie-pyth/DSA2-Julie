# Task 2 (ekstra): To nye grafer for Kruskal
# Minimum Spanning Tree with Kruskal's Algorithm (samme kode, ulike grafer)

import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(G, pos, title, mst_edges=None, filename=None):
    plt.figure(figsize=(6, 6))
    nx.draw_networkx(G, pos, with_labels=True, node_size=700, font_size=12, width=1.5)
    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    if mst_edges:
        nx.draw_networkx_edges(
            G, pos,
            edgelist=[(u, v) for (u, v, _) in mst_edges],
            width=5.0
        )
    plt.title(title)
    plt.axis("off")
    if filename:
        plt.savefig(filename, bbox_inches="tight", dpi=160)
        print(f"Saved figure: {filename}")
    plt.show()

def run_kruskal_for_graph(nodes, edges, layout_fn, layout_kwargs, tag):
    # a) Lag og tegn sammenhengende graf
    G = nx.Graph()
    G.add_nodes_from(nodes)
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = layout_fn(G, **layout_kwargs) if layout_kwargs is not None else layout_fn(G)

    draw_graph(G, pos, f"[{tag}] Initial Connected Graph", filename=f"{tag}_a_initial_graph.png")

    # b) Algoritmen
    print(f"[{tag}] MST algorithm: Kruskal's algorithm (Greedy).")
    print("Idea: sort edges by non-decreasing weight and add an edge if it does not create a cycle (Union-Find).")

    # c) Kruskal med Union-Find
    parent = {v: v for v in G.nodes()}
    rank = {v: 0 for v in G.nodes()}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
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

    sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]["weight"])

    print(f"\n[{tag}] Sorted edges by weight:")
    for (u, v, d) in sorted_edges:
        print(f"  ({u}, {v}) weight {d['weight']}")

    mst_edges = []
    total_weight = 0
    step = 1

    print(f"\n[{tag}] Kruskal step-by-step:")
    for (u, v, d) in sorted_edges:
        w = d["weight"]
        if find(u) == find(v):
            print(f"Consider ({u}, {v}) w={w}: SKIP (cycle)")
            continue

        union(u, v)
        mst_edges.append((u, v, w))
        total_weight += w
        print(f"Consider ({u}, {v}) w={w}: TAKE")

        draw_graph(
            G, pos,
            title=f"[{tag}] MST Progress (step {step}): added ({u}, {v}) w={w}",
            mst_edges=mst_edges,
            filename=f"{tag}_c_progress_step_{step}.png"
        )
        step += 1

        if len(mst_edges) == len(G.nodes()) - 1:
            break

    print(f"\n[{tag}] Selected MST edges in order:")
    for (u, v, w) in mst_edges:
        print(f"  ({u}, {v}) weight {w}")
    print(f"[{tag}] Total MST weight = {total_weight}")

    # d) Endelig MST
    draw_graph(
        G, pos,
        title=f"[{tag}] Final Minimum Spanning Tree (Kruskal)",
        mst_edges=mst_edges,
        filename=f"{tag}_d_final_mst.png"
    )

def main():
    # ---------- Graph 2 (6 noder, 9 kanter) ----------
    nodes_g2 = range(1, 7)
    edges_g2 = [
        (1, 2, 4),
        (1, 3, 3),
        (2, 3, 5),
        (2, 4, 6),
        (3, 5, 7),
        (4, 5, 2),
        (4, 6, 9),
        (5, 6, 4),
        (2, 5, 8),
    ]
    run_kruskal_for_graph(
        nodes_g2,
        edges_g2,
        layout_fn=nx.spring_layout,
        layout_kwargs={"seed": 42},
        tag="g2"
    )

    # ---------- Graph 3 (8 noder, 13 kanter) ----------
    nodes_g3 = range(1, 9)
    edges_g3 = [
        (1, 2, 10),
        (1, 3, 1),
        (1, 4, 4),
        (2, 4, 3),
        (2, 5, 2),
        (3, 6, 8),
        (4, 6, 7),
        (4, 7, 6),
        (5, 7, 5),
        (6, 7, 9),
        (6, 8, 11),
        (7, 8, 12),
        (3, 5, 13),
    ]
    run_kruskal_for_graph(
        nodes_g3,
        edges_g3,
        layout_fn=nx.shell_layout,
        layout_kwargs=None,
        tag="g3"
    )


if __name__ == "__main__":
    main()

