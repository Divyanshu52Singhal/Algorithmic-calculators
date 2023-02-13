import streamlit as st
import networkx as nx

st.title("Dijkstra's Algorithm Program")
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

def dijkstra(graph, start, end):
    shortest_paths = nx.single_source_dijkstra_path(graph, start)
    return shortest_paths[end]

def plot_graph(graph, path, start, end):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    nx.draw_networkx_nodes(graph, pos, nodelist=[start], node_color='r', node_size=500)
    nx.draw_networkx_nodes(graph, pos, nodelist=[end], node_color='g', node_size=500)
    nx.draw_networkx_edges(graph, pos, edgelist=path, edge_color='b', width=2)
    st.pyplot()

def get_graph():
    num_nodes = st.slider("Number of nodes", 2, 10, 2)
    graph = nx.Graph()
    graph.add_nodes_from(range(num_nodes))
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if st.checkbox(f"Add edge from node {i} to node {j}"):
                weight = st.number_input(f"Weight of edge from node {i} to node {j}", value=1.0)
                graph.add_edge(i, j, weight=weight)
    start = st.selectbox("Start node", list(graph.nodes))
    end = st.selectbox("End node", list(graph.nodes))
    return graph, start, end

graph, start, end = get_graph()
st.set_option('deprecation.showPyplotGlobalUse', False)

if st.button("Find Shortest Path"):
    path = dijkstra(graph, start, end)
    edge_list = [(path[i], path[i+1]) for i in range(len(path) - 1)]

    plot_graph(graph, edge_list, start, end)
    #st.pyplot()
