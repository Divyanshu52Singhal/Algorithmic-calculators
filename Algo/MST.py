import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(graph, num_vertices):
    result = []
    i, e = 0, 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []

    for node in range(num_vertices):
        parent.append(node)
        rank.append(0)

    while e < num_vertices - 1:
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)

    return result

st.title("Minimum Spanning Tree")

def graphin(m):
    graph=[]
    for i in range(m):
        st.text_input(label=f"Enter {i+1} Edge Connection Details along with weight with comma separated values", placeholder="Enter the value",
                      key="value" + str(i))
        temp = st.session_state["value" + str(i)]
        if temp:
            temp = temp.split(',')
            graph.append((int(temp[0]),int(temp[1]),int(temp[2])))
    if len(graph)==m:
        return graph

graph = [
    (0, 1, 4),
    (0, 7, 8),
    (1, 7, 11),
    (1, 2, 8),
    (7, 8, 7),
    (6, 7, 1),
    (2, 8, 2),
    (6, 8, 6),
    (2, 3, 7),
    (2, 5, 4),
    (6, 5, 2),
    (3, 5, 14),
    (3, 4, 9),
    (4, 5, 10)
]

st.text_input(label=f"Enter Number of Vertices", placeholder="Enter the value",
                      key="n")

st.text_input(label=f"Enter Number of Edges", placeholder="Enter the value",
                      key="e")

num_vertices = st.session_state["n"]
num_edges = st.session_state["e"]

if num_edges and num_vertices:
    num_vertices=int(num_vertices)
    graph = graphin(int(num_edges))
    try:
        result = kruskal(graph, int(num_vertices))
        G = nx.Graph()
        G.add_weighted_edges_from(graph)

        # Create minimum spanning tree as networkx graph
        T = nx.Graph()
        T.add_weighted_edges_from(result)

        # Plot graphs
        fig, ax = plt.subplots(figsize=(8, 8))
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, ax=ax)
        nx.draw_networkx_edges(G, pos, ax=ax)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), ax=ax)
        nx.draw_networkx_labels(G, pos, labels={i: str(i) for i in range(num_vertices)}, font_size=16, font_color='w', ax=ax)
        nx.draw_networkx_edges(T, pos, edge_color='r', ax=ax)
        nx.draw_networkx_edge_labels(T, pos, edge_labels=nx.get_edge_attributes(T, 'weight'), font_color='r', ax=ax)
        st.write(fig)

        # Display results
        st.write("<h3><b>Minimum Spanning Tree:",unsafe_allow_html=True)
        for u, v, weight in result:
            st.write(f"<h3><b>{u} - {v}: {weight}",unsafe_allow_html=True)
    except TypeError:
        st.write("<h3><b>INCOMPLETE INPUT",unsafe_allow_html=True)