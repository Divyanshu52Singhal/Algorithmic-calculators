from matplotlib import pyplot as plt
import streamlit as st
import numpy as np


def process(M,V,ang,Cd,dt,g):
    t = [0]  # list to keep track of time
    vx = [V * np.cos(ang / 180 * np.pi)]  # list for velocity x and y components
    vy = [V * np.sin(ang / 180 * np.pi)]
    x = [0]  # list for x and y position
    y = [0]

    # Drag force
    drag = Cd * V ** 2  # drag force

    # Acceleration components
    ax = [-(drag * np.cos(ang / 180 * np.pi)) / M]
    ay = [-g - (drag * np.sin(ang / 180 * np.pi) / M)]

    ## Leave this out for students to try
    # We can choose to have better control of the time-step here
    dt = 0.2

    # Use Euler method to update variables
    counter = 0
    while (y[counter] >= 0):  # Check that the last value of y is >= 0
        t.append(t[counter] + dt)  # increment by dt and add to the list of time

        # Update velocity
        vx.append(vx[counter] + dt * ax[counter])  # Update the velocity
        vy.append(vy[counter] + dt * ay[counter])

        # Update position
        x.append(x[counter] + dt * vx[counter])
        y.append(y[counter] + dt * vy[counter])

        # With the new velocity calculate the drag force and update acceleration
        vel = np.sqrt(vx[counter + 1] ** 2 + vy[counter + 1] ** 2)  # magnitude of velocity
        drag = Cd * vel ** 2  # drag force
        ax.append(-(drag * np.cos(ang / 180 * np.pi)) / M)
        ay.append(-g - (drag * np.sin(ang / 180 * np.pi) / M))

        # Increment the counter by 1
        counter = counter + 1

    # Let's plot the trajectory
    fig, ax = plt.subplots()
    ax.plot(x, y, '--')
    plt.ylabel("y (m)")
    plt.xlabel("x (m)")
    st.pyplot(fig)

    st.write(f"<h3><b>Range of projectile is {x[counter]:3.1f} m</h3></b>",unsafe_allow_html=True)


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
st.title("Projectile Motion With Graph")


st.text_input(label="Mass of projectile in kg :",placeholder="Enter the value",
              key="M")
st.text_input(label="Initial velocity in m/s :",placeholder="Enter the value",
              key="V")
st.text_input(label="Angle of initial velocity in degrees :",placeholder="Enter the value",
              key="ang")
st.text_input(label="Drag coefficient :",placeholder="Enter the value",
              key="Cd")
st.text_input(label="time step in s :",placeholder="Enter the value",
              key="dt")

M = st.session_state["M"]
g = 9.8          # Acceleration due to gravity (m/s^2)
V = st.session_state["V"]
ang =st.session_state["ang"]
Cd = st.session_state["Cd"]
dt = st.session_state["dt"]

if M and V and ang and Cd and dt:
    process(float(M),float(V),float(ang),float(Cd),float(dt),float(g))
# Set up the lists to store variables
# Initialize the velocity and position at t=0


   


