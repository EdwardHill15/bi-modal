import streamlit as st
import numpy as np
import plotly.graph_objects as go
from matplotlib import cm
import time

st.title("3D Line Plot with Filled Area Under Curves Workaround")

# Parameters for wave
A_i = st.sidebar.slider("A_i (Amplitude intrinsic)", 0.1, 2.0, 1.0)
A_e = st.sidebar.slider("A_e (Amplitude extrinsic)", 0.1, 2.0, 0.8)
k_i = st.sidebar.slider("k_i (Wave vector intrinsic)", 0.1, 5.0, 2.0)
k_e = st.sidebar.slider("k_e (Wave vector extrinsic)", 0.1, 5.0, 2.5)
l_i = st.sidebar.slider("l_i (Wave vector intrinsic)", 0.1, 5.0, 1.5)
l_e = st.sidebar.slider("l_e (Wave vector extrinsic)", 0.1, 5.0, 1.8)
omega_i = st.sidebar.slider("ω_i (Angular frequency intrinsic)", 0.1, 5.0, 3.0)
omega_e = st.sidebar.slider("ω_e (Angular frequency extrinsic)", 0.1, 5.0, 2.7)
phi = st.sidebar.slider("Phase shift φ (radians)", 0.0, 2*np.pi, np.pi / 4)

# Spatial resolution
n_lines = 30
x = np.linspace(-np.pi, np.pi, n_lines)
y = np.linspace(-np.pi, np.pi, n_lines)

# Animation controls
animate = st.sidebar.checkbox("Animate Wave", value=True)
frame_delay = st.sidebar.slider("Animation speed (ms per frame)", 50, 1000, 200)
plot_placeholder = st.empty()
num_frames = 40
T_seq = np.linspace(0, 2 * np.pi, num_frames)

# Colormaps for distinction
cividis = cm.get_cmap('cividis')
cool = cm.get_cmap('cool')

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

def map_colors_line(Z, cmap):
    colors = []
    for i in range(Z.shape[0]):
        avg_val = np.mean(Z[i, :])
        norm_val = (avg_val - np.min(Z)) / (np.max(Z) - np.min(Z))
        rgb = tuple(int(c*255) for c in cmap(norm_val)[:3])
        colors.append(f'rgb{rgb}')
    return colors

def make_filled_surface_lines_traces(X, Y, Z, colors, name, zbase=0):
    traces = []
    for i in range(X.shape[0]):
        xi = X[i, :]
        yi = Y[i, :]
        zi = Z[i, :]
        # Create vertices for mesh: line and base
        xs = np.concatenate([xi, xi[::-1]])
        ys = np.concatenate([yi, yi[::-1]])
        zs = np.concatenate([zi, np.full_like(zi, zbase)])

        traces.append(go.Mesh3d(
            x=xs,
            y=ys,
            z=zs,
            color=colors[i],
            opacity=0.4,
            name=name if i == 0 else None,
            showscale=False,
            alphahull=0,
            flatshading=True,
            hoverinfo='skip',
            showlegend=(i == 0)
        ))

        traces.append(go.Scatter3d(
            x=xi,
            y=yi,
            z=zi,
            mode='lines',
            line=dict(color=colors[i], width=4),
            showlegend=False
        ))
    return traces

if animate:
    for t in T_seq:
        X, Y, E_exp, E_per = compute_wave(t)
        exp_colors = map_colors_line(E_exp, cividis)
        per_colors = map_colors_line(E_per, cool)

        fig = go.Figure()
        fig.add_traces(make_filled_surface_lines_traces(X, Y, E_exp, exp_colors, 'Experience ψr²'))
        fig.add_traces(make_filled_surface_lines_traces(X, Y, E_per, per_colors, 'Perception |∂ψr/∂t|'))

        fig.update_layout(
            scene=dict(
                xaxis_title='X (spatial)',
                yaxis_title='Y (spatial)',
                zaxis_title='Amplitude / Energy'
            ),
            height=700,
            margin=dict(l=0, r=0, b=0, t=30)
        )
        plot_placeholder.plotly_chart(fig, width='stretch')
        time.sleep(frame_delay / 1000)
else:
    X, Y, E_exp, E_per = compute_wave(T_seq[0])
    exp_colors = map_colors_line(E_exp, cividis)
    per_colors = map_colors_line(E_per, cool)

    fig = go.Figure()
    fig.add_traces(make_filled_surface_lines_traces(X, Y, E_exp, exp_colors, 'Experience ψr²'))
    fig.add_traces(make_filled_surface_lines_traces(X, Y, E_per, per_colors, 'Perception |∂ψr/∂t|'))

    fig.update_layout(
        scene=dict(
            xaxis_title='X (spatial)',
            yaxis_title='Y (spatial)',
            zaxis_title='Amplitude / Energy'
        ),
        height=700,
        margin=dict(l=0, r=0, b=0, t=30)
    )
    plot_placeholder.plotly_chart(fig, width='stretch')

