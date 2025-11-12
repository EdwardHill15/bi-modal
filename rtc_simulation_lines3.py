import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

st.title("Animated Experience and Perception Wave Patterns")

# Sidebar input sliders
num_external_waves = st.sidebar.slider("Number of External Waves", 1, 10, 3)
A_i = st.sidebar.slider("Intrinsic Amplitude", 0.1, 2.0, 1.0)
k_i = st.sidebar.slider("Intrinsic Wave Number", 0.1, 5.0, 2.0)
omega_i = st.sidebar.slider("Intrinsic Angular Frequency", 0.1, 5.0, 3.0)
fps = st.sidebar.slider("FPS (frames per second)", 1, 30, 10)

# Play/Pause/Reset buttons
col1, col2, col3 = st.sidebar.columns(3)
if col1.button("Play"):
    st.session_state['playing'] = True
if col2.button("Pause"):
    st.session_state['playing'] = False
if col3.button("Reset"):
    st.session_state['frame_index'] = 0
    st.session_state['playing'] = False

# Initialize session state variables
if 'frame_index' not in st.session_state:
    st.session_state['frame_index'] = 0
if 'playing' not in st.session_state:
    st.session_state['playing'] = False
if 'last_time' not in st.session_state:
    st.session_state['last_time'] = time.time()

# Constants and arrays
x = np.linspace(-np.pi, np.pi, 500)
num_frames = 60
T_seq = np.linspace(0, 2*np.pi, num_frames)

np.random.seed(42)
A_e_arr = np.linspace(0.5, 1.0, num_external_waves)
k_e_arr = np.linspace(1.5, 3.0, num_external_waves)
omega_e_arr = np.linspace(2.0, 4.0, num_external_waves)
phi_e_arr = np.linspace(0, np.pi, num_external_waves)

# Compute waveforms for a given time t
def compute_waveforms(t):
    psi_i = A_i * np.sin(k_i * x - omega_i * t)
    psi_e_sum = np.zeros_like(x)
    for i in range(num_external_waves):
        psi_e_sum += A_e_arr[i] * np.sin(k_e_arr[i] * x - omega_e_arr[i] * t + phi_e_arr[i])
    psi_r = psi_i + psi_e_sum + psi_i * psi_e_sum
    E_exp = psi_r ** 2
    dpsi_i_dt = -A_i * omega_i * np.cos(k_i * x - omega_i * t)
    dpsi_e_sum_dt = np.zeros_like(x)
    for i in range(num_external_waves):
        dpsi_e_sum_dt += -A_e_arr[i] * omega_e_arr[i] * np.cos(k_e_arr[i] * x - omega_e_arr[i] * t + phi_e_arr[i])
    dpsi_r_dt = dpsi_i_dt + dpsi_e_sum_dt + dpsi_i_dt * psi_e_sum + dpsi_e_sum_dt * psi_i
    E_per = np.abs(dpsi_r_dt)
    ext_waves = [A_e_arr[i]*np.sin(k_e_arr[i]*x - omega_e_arr[i]*t + phi_e_arr[i]) for i in range(num_external_waves)]
    return psi_i, ext_waves, E_exp, E_per

# Update frame index if playing and time elapsed exceeds interval
current_time = time.time()
interval = 1.0 / fps
if st.session_state['playing'] and (current_time - st.session_state['last_time'] > interval):
    st.session_state['frame_index'] = (st.session_state['frame_index'] + 1) % num_frames
    st.session_state['last_time'] = current_time

t = T_seq[st.session_state['frame_index']]
psi_i, ext_waves, E_exp, E_per = compute_waveforms(t)

# Layout columns for experience and perception plots
col_exp, col_per = st.columns(2)

with col_exp:
    fig_exp = go.Figure()
    fig_exp.add_trace(go.Scatter(x=x, y=psi_i, mode='lines', name='Intrinsic Wave', line=dict(color='cyan', dash='dash')))
    for idx, wv in enumerate(ext_waves):
        fig_exp.add_trace(go.Scatter(x=x, y=wv, mode='lines', name=f'External {idx+1}', line=dict(color='magenta', dash='dot'), opacity=0.5))
    fig_exp.add_trace(go.Scatter(x=x, y=E_exp, mode='lines', name='Resonance Wave', line=dict(color='blue')))
    fig_exp.update_layout(title=f'Experience Waves at t={t:.2f}', yaxis=dict(range=[min(np.min(E_exp), np.min(psi_i)) * 1.2, np.max(E_exp) * 1.2]))
    st.plotly_chart(fig_exp, use_container_width=True)

with col_per:
    fig_per = go.Figure()
    fig_per.add_trace(go.Scatter(x=x, y=E_per, mode='lines', name='Perception Wavefunction', line=dict(color='orange')))
    fig_per.update_layout(title=f'Perception Wavefunction at t={t:.2f}', yaxis=dict(range=[0, np.max(E_per) * 1.1]))
    st.plotly_chart(fig_per, use_container_width=True)

