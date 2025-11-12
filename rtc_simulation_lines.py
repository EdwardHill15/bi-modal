import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from matplotlib import cm
import time

st.title("Animated Interactive Dual Holographic Energy Tubes with Lines")

# Sidebar parameters
A_i = st.sidebar.slider("A_i (Amplitude intrinsic)", 0.1, 2.0, 1.0)
A_e = st.sidebar.slider("A_e (Amplitude extrinsic)", 0.1, 2.0, 0.8)
k_i = st.sidebar.slider("k_i (Wave vector intrinsic)", 0.1, 5.0, 2.0)
k_e = st.sidebar.slider("k_e (Wave vector extrinsic)", 0.1, 5.0, 2.5)
l_i = st.sidebar.slider("l_i (Wave vector intrinsic)", 0.1, 5.0, 1.5)
l_e = st.sidebar.slider("l_e (Wave vector extrinsic)", 0.1, 5.0, 1.8)
omega_i = st.sidebar.slider("ω_i (Angular frequency intrinsic)", 0.1, 5.0, 3.0)
omega_e = st.sidebar.slider("ω_e (Angular frequency extrinsic)", 0.1, 5.0, 2.7)
phi = st.sidebar.slider("Phase shift φ (radians)", 0.0, 2*np.pi, np.pi / 4)

# Spatial grid resolution for lines
n_lines = 30
x = np.linspace(-np.pi, np.pi, n_lines)
y = np.linspace(-np.pi, np.pi, n_lines)

# Animation control
animate = st.sidebar.checkbox("Animate Wave", value=True)
frame_delay = st.sidebar.slider("Animation speed (ms per frame)", 50, 1000, 200)

plot_placeholder = st.empty()
num_frames = 40
T_seq = np.linspace(0, 2 * np.pi, num_frames)

viridis = cm.get_cmap('viridis')
plasma = cm.get_cmap('plasma')

def compute_wave(t):
    X, Y = np.meshgrid(x, y)
    psi_i = A_i * np.sin(k_i * X + l_i * Y - omega_i * t)
    psi_e = A_e * np.sin(k_e * X + l_e * Y - omega_e * t + phi)
    psi_r = psi_i + psi_e + psi_i * psi_e
    E_exp = psi_r ** 2
    dpsi_r_dt = (-A_i * omega_i * np.cos(k_i * X + l_i * Y - omega_i * t)
                 - A_e * omega_e * np.cos(k_e * X + l_e * Y - omega_e * t + phi)
                 - (A_i * omega_i * np.cos(k_i * X + l_i * Y - omega_i * t) * psi_e +
                    A_e * omega_e * np.cos(k_e * X + l_e * Y - omega_e * t + phi) * psi_i))
    E_per = np.abs(dpsi_r_dt)
    return X, Y, E_exp, E_per

def color_line(Z, cmap):
    norm = (Z - Z.min()) / (Z.max() - Z.min())
    return [f'rgb{tuple(int(c*255) for c in cmap(val)[:3])}' for val in norm]

def make_lines_trace(X, Y, Z, colors, name):
    traces = []
    # We create lines along rows (i.e., y fixed) for better visualization
    for i in range(X.shape[0]):
        traces.append(go.Scatter3d(
            x=X[i, :],
            y=Y[i, :],
            z=Z[i, :],
            mode='lines',
            line=dict(color=colors[i], width=4),
            name=name if i==0 else None,  # Show legend only once
            showlegend=(i==0)
        ))
    return traces

if animate:
    for t in T_seq:
        X, Y, E_exp, E_per = compute_wave(t)
        # Color by average line value for each line (row)
        exp_colors = []
        per_colors = []
        for i in range(n_lines):
            exp_colors.append(tuple(int(c*255) for c in viridis(np.mean(E_exp[i,:]))[:3]))
            per_colors.append(tuple(int(c*255) for c in plasma(np.mean(E_per[i,:]))[:3]))
        exp_colors_str = [f'rgb{c}' for c in exp_colors]
        per_colors_str = [f'rgb{c}' for c in per_colors]

        fig = go.Figure()
        fig.add_traces(make_lines_trace(X, Y, E_exp, exp_colors_str, 'Experience ψr²'))
        fig.add_traces(make_lines_trace(X, Y, E_per, per_colors_str, 'Perception |∂ψr/∂t|'))

        fig.update_layout(
            scene=dict(
                xaxis_title='X (spatial)',
                yaxis_title='Y (spatial)',
                zaxis_title='Amplitude / Energy'
            ),
            height=700,
            margin=dict(l=0,r=0,b=0,t=30)
        )
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        time.sleep(frame_delay / 1000)
else:
    X, Y, E_exp, E_per = compute_wave(T_seq[0])
    exp_colors = []
    per_colors = []
    for i in range(n_lines):
        exp_colors.append(tuple(int(c*255) for c in viridis(np.mean(E_exp[i,:]))[:3]))
        per_colors.append(tuple(int(c*255) for c in plasma(np.mean(E_per[i,:]))[:3]))
    exp_colors_str = [f'rgb{c}' for c in exp_colors]
    per_colors_str = [f'rgb{c}' for c in per_colors]

    fig = go.Figure()
    fig.add_traces(make_lines_trace(X, Y, E_exp, exp_colors_str, 'Experience ψr²'))
    fig.add_traces(make_lines_trace(X, Y, E_per, per_colors_str, 'Perception |∂ψr/∂t|'))

    fig.update_layout(
        scene=dict(
            xaxis_title='X (spatial)',
            yaxis_title='Y (spatial)',
            zaxis_title='Amplitude / Energy'
        ),
        height=700,
        margin=dict(l=0,r=0,b=0,t=30)
    )
    plot_placeholder.plotly_chart(fig, use_container_width=True)
