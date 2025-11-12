import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

st.title("Experience Resonance and Perception Wavefunctions Animation")

# Animation state initialization
if "frame_idx" not in st.session_state:
    st.session_state.frame_idx = 0
if "anim_running" not in st.session_state:
    st.session_state.anim_running = False
if "last_update" not in st.session_state:
    st.session_state.last_update = 0

# Controls
num_external_waves = st.sidebar.slider("Number of External Waves", 1, 10, 3)
A_i = st.sidebar.slider("Intrinsic amplitude A_i", 0.1, 2.0, 1.0)
k_i = st.sidebar.slider("Intrinsic wave number k_i", 0.1, 5.0, 2.0)
omega_i = st.sidebar.slider("Intrinsic angular frequency ω_i", 0.1, 5.0, 3.0)
fps = st.sidebar.slider("Animation FPS", 1, 30, 10)

if st.sidebar.button("Play"):
    st.session_state.anim_running = True
if st.sidebar.button("Pause"):
    st.session_state.anim_running = False
if st.sidebar.button("Reset"):
    st.session_state.frame_idx = 0
    st.session_state.anim_running = False

np.random.seed(42)
A_e = np.linspace(0.5, 1.0, num_external_waves)
k_e = np.linspace(1.5, 3.0, num_external_waves)
omega_e = np.linspace(2.0, 4.0, num_external_waves)
phi_e = np.linspace(0, np.pi, num_external_waves)

x = np.linspace(-np.pi, np.pi, 500)
num_frames = 60
T_seq = np.linspace(0, 2*np.pi, num_frames)

def compute_waves(t):
    psi_i = A_i * np.sin(k_i * x - omega_i * t)
    psi_e_sum = np.zeros_like(x)
    for i in range(num_external_waves):
        psi_e_sum += A_e[i] * np.sin(k_e[i] * x - omega_e[i] * t + phi_e[i])
    psi_r = psi_i + psi_e_sum + psi_i * psi_e_sum
    E_exp = psi_r**2
    dpsi_i_dt = -A_i * omega_i * np.cos(k_i * x - omega_i * t)
    dpsi_e_sum_dt = np.zeros_like(x)
    for i in range(num_external_waves):
        dpsi_e_sum_dt += - A_e[i] * omega_e[i] * np.cos(k_e[i] * x - omega_e[i] * t + phi_e[i])
    dpsi_r_dt = dpsi_i_dt + dpsi_e_sum_dt + dpsi_i_dt * psi_e_sum + dpsi_e_sum_dt * psi_i
    E_per = np.abs(dpsi_r_dt)
    return psi_i, [A_e[i]*np.sin(k_e[i]*x - omega_e[i]*t + phi_e[i]) for i in range(num_external_waves)], E_exp, E_per

def plot_experience(psi_i, external_waves, E_exp, t):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=psi_i, mode='lines', name='Intrinsic', line=dict(color='cyan', dash='dash')))
    for idx, wave in enumerate(external_waves):
        fig.add_trace(go.Scatter(x=x, y=wave, mode='lines', name=f'External {idx+1}', line=dict(color='magenta', dash='dot'), opacity=0.5))
    fig.add_trace(go.Scatter(x=x, y=E_exp, mode='lines', name='Resonance Experience', line=dict(color='blue')))
    fig.update_layout(title=f"Experience Waves at t={t:.2f}", yaxis_range=[min(np.min(E_exp), np.min(psi_i))*1.2, np.max(E_exp)*1.2])
    return fig

def plot_perception(E_per, t):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=E_per, mode='lines', name='Perception', line=dict(color='orange')))
    fig.update_layout(title=f"Perception Wavefunction at t={t:.2f}", yaxis_range=[0, np.max(E_per)*1.1])
    return fig

col_exp, col_per = st.columns(2)

current_time = time.time()
frame_duration = 1.0 / fps

if st.session_state.anim_running and (current_time - st.session_state.last_update > frame_duration):
    st.session_state.frame_idx = (st.session_state.frame_idx + 1) % num_frames
    st.session_state.last_update = current_time

t = T_seq[st.session_state.frame_idx]
psi_i, external_waves, E_exp, E_per = compute_waves(t)

fig_exp = plot_experience(psi_i, external_waves, E_exp, t)
fig_per = plot_perception(E_per, t)

col_exp.plotly_chart(fig_exp, use_container_width=True)
col_per.plotly_chart(fig_per, use_container_width=True)
