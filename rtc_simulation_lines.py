import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Experience Resonance and Perception Wavefunctions Animation")

# Controls
num_external_waves = st.sidebar.slider("Number of External Waves", 1, 10, 3)
A_i = st.sidebar.slider("Intrinsic amplitude A_i", 0.1, 2.0, 1.0)
k_i = st.sidebar.slider("Intrinsic wave number k_i", 0.1, 5.0, 2.0)
omega_i = st.sidebar.slider("Intrinsic angular frequency ω_i", 0.1, 5.0, 3.0)
animation_running = st.sidebar.checkbox("Play Animation", value=False)
animation_fps = st.sidebar.slider("Animation FPS", 1, 30, 10)

# External waves params fixed for demo
np.random.seed(42)
A_e = np.linspace(0.5, 1.0, num_external_waves)
k_e = np.linspace(1.5, 3.0, num_external_waves)
omega_e = np.linspace(2.0, 4.0, num_external_waves)
phi_e = np.linspace(0, np.pi, num_external_waves)

x = np.linspace(-np.pi, np.pi, 500)
num_frames = 60
T_seq = np.linspace(0, 2*np.pi, num_frames)

if "frame_idx" not in st.session_state:
    st.session_state.frame_idx = 0

def compute_waves(t):
    psi_i = A_i * np.sin(k_i * x - omega_i * t)
    psi_e_sum = np.zeros_like(x)
    for i in range(num_external_waves):
        psi_e_sum += A_e[i] * np.sin(k_e[i] * x - omega_e[i] * t + phi_e[i])
    psi_r = psi_i + psi_e_sum + psi_i * psi_e_sum
    E_exp = psi_r ** 2
    
    dpsi_i_dt = - A_i * omega_i * np.cos(k_i * x - omega_i * t)
    dpsi_e_sum_dt = np.zeros_like(x)
    for i in range(num_external_waves):
        dpsi_e_sum_dt += - A_e[i] * omega_e[i] * np.cos(k_e[i] * x - omega_e[i] * t + phi_e[i])
    dpsi_r_dt = dpsi_i_dt + dpsi_e_sum_dt + dpsi_i_dt * psi_e_sum + dpsi_e_sum_dt * psi_i
    E_per = np.abs(dpsi_r_dt)
    return psi_i, psi_e_sum, E_exp, E_per

# Compute current frame's waves
t = T_seq[st.session_state.frame_idx]
psi_i, psi_e_sum, E_exp, E_per = compute_waves(t)

# Setup two columns for side by side plots
col1, col2 = st.columns(2)

with col1:
    fig_exp = go.Figure()
    fig_exp.add_trace(go.Scatter(x=x, y=psi_i, mode='lines', name='Intrinsic Wave', line=dict(color='cyan', dash='dash')))
    for i in range(num_external_waves):
        ext_wave = A_e[i] * np.sin(k_e[i] * x - omega_e[i] * t + phi_e[i])
        fig_exp.add_trace(go.Scatter(x=x, y=ext_wave, mode='lines', name=f'External Wave {i+1}', 
                                     line=dict(color='magenta', dash='dot'), opacity=0.5))
    fig_exp.add_trace(go.Scatter(x=x, y=E_exp, mode='lines', name='Resonance Experience Wave', line=dict(color='blue')))
    fig_exp.update_layout(title=f'Experience Wave Patterns at t={t:.2f}', yaxis_range=[min(np.min(E_exp), np.min(psi_i))*1.2, np.max(E_exp)*1.2])
    st.plotly_chart(fig_exp, use_container_width=True)

with col2:
    fig_per = go.Figure()
    fig_per.add_trace(go.Scatter(x=x, y=E_per, mode='lines', name='Perception Wavefunction (Derivative)', line=dict(color='orange')))
    fig_per.update_layout(title=f'Perception Wavefunction at t={t:.2f}', yaxis_range=[0, np.max(E_per)*1.1])
    st.plotly_chart(fig_per, use_container_width=True)

# Update frame index if animation is playing
if animation_running:
    st.session_state.frame_idx = (st.session_state.frame_idx + 1) % num_frames
    # Rerun script after delay to animate
    st.experimental_rerun()














