import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

st.title("Convex Hull Program")

def plot_hull(points):
    hull = ConvexHull(points)
    plt.plot(points[:,0], points[:,1], 'o')
    for simplex in hull.simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

def get_points():
    st.text_input(label="ENTER NUMBER OF COORDINATES",placeholder="Enter the Value",key="n")
    num_points = st.session_state["n"]
    points = []
    if num_points:
        for i in range(int(num_points)):
            x = st.number_input(f"x{i+1}")
            y = st.number_input(f"y{i+1}")
            points.append([x, y])
        return np.array(points)

points = get_points()
st.set_option('deprecation.showPyplotGlobalUse', False)

if st.button("Plot Convex Hull"):
    plot_hull(points)
    #plt.show()
    st.pyplot()