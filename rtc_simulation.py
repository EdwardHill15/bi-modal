import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from matplotlib import cm
import time

st.title("Animated Interactive Dual Holographic Energy Tubes")

# Parameters adjustable via sidebar
A_i = st.sidebar.slider("A_i (Amplitude intrinsic)", 0.1, 2.0, 1.0)
A_e = st.sidebar.slider("A_e (Amplitude extrinsic)", 0.1, 2.0, 0.8)
k_i = st.sidebar.slider("k_i (Wave vector intrinsic)", 0.1, 5.0, 2.0)
k_e = st.sidebar.slider("k_e (Wave vector extrinsic)", 0.1, 5.0, 2.5)
l_i = st.sidebar.slider("l_i (Wave vector intrinsic)", 0.1, 5.0, 1.5)
l_e = st.sidebar.slider("l_e (Wave vector extrinsic)", 0.1, 5.0, 1.8)
omega_i = st.sidebar.slider("ω_i (Angular frequency intrinsic)", 0.1, 5.0, 3.0)
omega_e = st.sidebar.slider("ω_e (Angular frequency extrinsic)", 0.1, 5.0, 2.7)
phi = st.sidebar.slider("Phase shift φ (radians)", 0.0, 2*np.pi, np.pi / 4)

# Spatial grid
x = np.linspace(-np.pi, np.pi, 30)
y = np.linspace(-np.pi, np.pi, 30)
X, Y = np.meshgrid(x, y)

# Animation control
animate = st.sidebar.checkbox("Animate Wave", value=True)
frame_delay = st.sidebar.slider("Animation speed (ms per frame)", 50, 1000, 200)

# Prepare Plotly chart container
plot_placeholder = st.empty()

# Number of frames in animation
num_frames = 40
T_seq = np.linspace(0, 2 * np.pi, num_frames)

n_colors = 100
viridis = cm.get_cmap('viridis', n_colors)
plasma = cm.get_cmap('plasma', n_colors)

def get_colors(Z, cmap):
    Z_norm = (Z - Z.min()) / (Z.max() - Z.min())
    return [f'rgb{tuple(int(c*255) for c in cmap(val)[:3])}' for val in Z_norm]

def create_figure(t):
    psi_i = A_i * np.sin(k_i * X + l_i * Y - omega_i * t)
    psi_e = A_e * np.sin(k_e * X + l_e * Y - omega_e * t + phi)
    psi_r = psi_i + psi_e + psi_i * psi_e
    E_exp = psi_r ** 2
    dpsi_r_dt = (-A_i * omega_i * np.cos(k_i * X + l_i * Y - omega_i * t)
                 - A_e * omega_e * np.cos(k_e * X + l_e * Y - omega_e * t + phi)
                 - (A_i * omega_i * np.cos(k_i * X + l_i * Y - omega_i * t) * psi_e +
                    A_e * omega_e * np.cos(k_e * X + l_e * Y - omega_e * t + phi) * psi_i))
    E_per = np.abs(dpsi_r_dt)

    df_exp = pd.DataFrame({'X': X.ravel(), 'Y': Y.ravel(), 'Z': E_exp.ravel()})
    df_per = pd.DataFrame({'X': X.ravel(), 'Y': Y.ravel(), 'Z': E_per.ravel()})

    df_exp['color'] = get_colors(df_exp['Z'], viridis)
    df_per['color'] = get_colors(df_per['Z'], plasma)

    fig = go.Figure()

    fig.add_trace(go.Scatter3d(
        x=df_exp['X'], y=df_exp['Y'], z=df_exp['Z'],
        mode='markers',
        marker=dict(size=3, color=df_exp['color']),
        name='Experience ψr²'
    ))

    fig.add_trace(go.Scatter3d(
        x=df_per['X'], y=df_per['Y'], z=df_per['Z'],
        mode='markers',
        marker=dict(size=3, color=df_per['color']),
        name='Perception |∂ψr/∂t|'
    ))

    fig.update_layout(
        scene=dict(
            xaxis_title='X (spatial)',
            yaxis_title='Y (spatial)',
            zaxis_title='Amplitude / Energy'
        ),
        height=700,
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig

if animate:
    for t in T_seq:  # Loop through time frames
        fig = create_figure(t)
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        time.sleep(frame_delay / 1000)
else:
    # Static plot at initial frame
    fig = create_figure(T_seq[0])
    plot_placeholder.plotly_chart(fig, use_container_width=True)

