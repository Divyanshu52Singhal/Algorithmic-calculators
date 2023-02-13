import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

st.title("Huffman Coding Program")

def huffman_coding(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=False)
    nodes = []
    for char, freq in frequency:
        nodes.append({"char": char, "freq": freq, "left": None, "right": None})
    while len(nodes) > 1:
        node1 = nodes.pop(0)
        node2 = nodes.pop(0)
        new_node = {"char": None, "freq": node1["freq"] + node2["freq"], "left": node1, "right": node2}
        nodes.append(new_node)
        nodes = sorted(nodes, key=lambda x: x["freq"], reverse=False)
    codes = {}
    def build_codes(node, code):
        if node is None:
            return
        if node["char"] is not None:
            codes[node["char"]] = code
        build_codes(node["left"], code + "0")
        build_codes(node["right"], code + "1")
    build_codes(nodes[0], "")
    return codes, nodes[0]

text = st.text_input("Enter the text to be encoded:")

if text:
    codes, tree = huffman_coding(text)
    st.write("Huffman Codes:")
    for char, code in codes.items():
        st.write(f"{char}: {code}")

    st.write("Huffman Tree:")

    G = nx.Graph()

    node_labels = {}
    edge_labels = {}

    node_counter = 0
    edge_counter = 0

    def build_graph(node):
        global node_counter
        global edge_counter
        if node is None:
            return
        node_counter += 1
        node_id = node_counter
        node_labels[node_id] = f"{node['char']}\n{node['freq']}"
        if node["left"] is not None:
            build_graph(node["left"])
            edge_counter += 1
            edge_labels[edge_counter] = "0"
            G.add_edge(node_id, node_counter + 1)
        if node["right"] is not None:
            build_graph(node["right"])
            edge_counter += 1
            edge_labels[edge_counter] = "1"
            G.add_edge(node_id, node_counter + 1)


    result=build_graph(tree)

    pos = nx.spring_layout(G)

    plt.figure(figsize=(15, 10))

    nx.draw(G, pos, with_labels=True)
    nx.draw(G, pos, with_labels=True)
    for path in result:
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)
    st.pyplot()


