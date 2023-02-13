import streamlit as st
import networkx as nx
from collections import defaultdict as ddc

#COMPLETED


page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
    background-color:#E5B8F4;
    padding:none;
    margin:none;
    background-image: linear-gradient(0deg,#E5B8F4 ,#810CA8 );
    }
    </style>
    """
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Finding If there is Path Existing")

def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_vertex in graph[vertex] - set(path):
            if next_vertex == end:
                yield path + [next_vertex]
            else:
                queue.append((next_vertex, path + [next_vertex]))

def display_bfs_result(graph, start, end):
    result = list(bfs(graph, start, end))
    if not result:
        st.write("No path found between", start, "and", end)
    else:
        st.write("Path found between", start, "and", end, ":")
        st.write(result)
        G = nx.Graph(graph)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        for path in result:
            edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)
        st.pyplot()

def process(graph):
    start = st.selectbox("Select the starting node", list(graph.keys()))
    end = st.selectbox("Select the ending node", list(graph.keys()))
    display_bfs_result(graph, start, end)

def graphin(m):
    zz = ddc(set)
    for i in range(m):
        st.text_input(label=f"Enter {i+1} Edge Connection Details", placeholder="Enter the value",
                      key="value" + str(i))
        temp = st.session_state["value" + str(i)]
        temp = temp.split()
        if temp:
            zz[temp[0]].add(temp[1])
            zz[temp[1]].add(temp[0])
    return process(zz)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.text_input(label="Number Of Edges", placeholder="Enter the value",
                      key="e")
e=st.session_state["e"]
if e:
    graphin(int(e))