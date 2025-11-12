# RTC Model Animated Simulation: Dynamic Holographic Resonance Field
# Author: Edward F. Hillenaar, MSc

# Load required packages
library(plot3D)
library(animation)

# Define spatial grid
x <- seq(-pi, pi, length.out = 100)
y <- seq(-pi, pi, length.out = 100)
grid <- mesh(x, y)
X <- grid$x
Y <- grid$y

# Define wave parameters
A_i <- 1.0;  A_e <- 0.8
k_i <- 2;    k_e <- 2.5
l_i <- 1.5;  l_e <- 1.8
omega_i <- 3; omega_e <- 2.7
phi <- pi / 4

ani.options(autobrowse = FALSE)

# Create animation (adjust 'interval' for playback speed)
saveGIF({
  
  for (t in seq(0, 2*pi, length.out = 60)) {
    
    # Internal and external wavefunctions
    psi_i <- A_i * sin(k_i * X + l_i * Y - omega_i * t)
    psi_e <- A_e * sin(k_e * X + l_e * Y - omega_e * t + phi)
    
    # Resonant field (integral experience)
    psi_r <- psi_i + psi_e + psi_i * psi_e
    
    # 3D surface plot
    surf3D(X, Y, psi_r,
           colvar = psi_r, colkey = FALSE,
           main = paste("Dynamic Holographic Resonance Field (ψ_r),  t =", round(t, 2)),
           xlab = "X (spatial dimension)",
           ylab = "Y (spatial dimension)",
           zlab = "Resonant Amplitude",
           theta = 45, phi = 25, border = "black", shade = 0.7,
           zlim = c(-3, 3))
  }

}, movie.name = "RTC_Holographic_Resonance.gif", interval = 0.1, ani.width = 800, ani.height = 600)


browseURL("RTC_Holographic_Resonance.gif")


library(plot3D)
library(animation)

# Define spatial grid
x <- seq(-pi, pi, length.out = 100)
y <- seq(-pi, pi, length.out = 100)
grid <- mesh(x, y)
X <- grid$x
Y <- grid$y

# Define wave parameters
A_i <- 1.0;  A_e <- 0.8
k_i <- 2;    k_e <- 2.5
l_i <- 1.5;  l_e <- 1.8
omega_i <- 3; omega_e <- 2.7
phi <- pi / 4

# Create live HTML animation
saveHTML({
  for (t in seq(0, 2*pi, length.out = 60)) {
    psi_i <- A_i * sin(k_i * X + l_i * Y - omega_i * t)
    psi_e <- A_e * sin(k_e * X + l_e * Y - omega_e * t + phi)
    psi_r <- psi_i + psi_e + psi_i * psi_e
    
    surf3D(X, Y, psi_r, colvar = psi_r, colkey = FALSE,
           main = paste("Dynamic Holographic Resonance Field (ψ_r),  t =", round(t, 2)),
           xlab = "X", ylab = "Y", zlab = "Resonant Amplitude",
           theta = 45, phi = 25, border = "black", shade = 0.7,
           zlim = c(-3, 3))
  }
}, interval = 0.1, htmlfile = "RTC_Holographic_Resonance.html", ani.width = 800, ani.height = 600)





library(plot3D)
library(animation)

# Define spatial grid
x <- seq(-pi, pi, length.out = 80)
y <- seq(-pi, pi, length.out = 80)
grid <- mesh(x, y)
X <- grid$x
Y <- grid$y

# Define wave parameters
A_i <- 1.0;  A_e <- 0.8
k_i <- 2;    k_e <- 2.5
l_i <- 1.5;  l_e <- 1.8
omega_i <- 3; omega_e <- 2.7
phi <- pi / 4

# Create HTML animation
saveHTML({
  for (t in seq(0, 2*pi, length.out = 60)) {
    
    # Internal and external wavefunctions
    psi_i <- A_i * sin(k_i * X + l_i * Y - omega_i * t)
    psi_e <- A_e * sin(k_e * X + l_e * Y - omega_e * t + phi)
    
    # Resonant field (integral experience)
    psi_r <- psi_i + psi_e + psi_i * psi_e
    
    # Time derivative (perceptual collapse)
    dpsi_r_dt <- -A_i * omega_i * cos(k_i * X + l_i * Y - omega_i * t) -
      A_e * omega_e * cos(k_e * X + l_e * Y - omega_e * t + phi) -
      (A_i * omega_i * cos(k_i * X + l_i * Y - omega_i * t) * psi_e +
         A_e * omega_e * cos(k_e * X + l_e * Y - omega_e * t + phi) * psi_i)
    
    # 3D dual-panel plot
    par(mfrow = c(1, 2), mar = c(2, 2, 3, 1))
    
    # Left panel: Integral Resonance Field ψᵣ
    surf3D(X, Y, psi_r, colvar = psi_r, colkey = FALSE,
           main = expression(paste("Integral Resonance Field (", psi[r], ")")),
           xlab = "X", ylab = "Y", zlab = "Amplitude",
           theta = 45, phi = 25, border = "black", shade = 0.7,
           zlim = c(-3, 3))
    
    # Right panel: Perceptual Collapse ∂ψᵣ/∂t
    surf3D(X, Y, dpsi_r_dt, colvar = dpsi_r_dt, colkey = FALSE,
           main = expression(paste("Perceptual Collapse (", partialdiff(psi[r], t), ")")),
           xlab = "X", ylab = "Y", zlab = "Amplitude Change",
           theta = 45, phi = 25, border = "black", shade = 0.7,
           zlim = c(-3, 3))
    
    # Overall title with current time step
    mtext(paste("Dynamic Holographic Mind Field — t =", round(t, 2)), side = 3, outer = TRUE, line = -2)
  }
}, interval = 0.1, htmlfile = "RTC_Dual_Mode_Animation.html", ani.width = 1000, ani.height = 500)


# 🎬 What You’ll See
# 
# The left plot shows the resonant holographic field (ψᵣ) — the living vibrational 
# totality of experience.
# 
# The right plot shows its time-derivative (∂ψᵣ/∂t) — how this continuous field 
# differentiates into perception through temporal change.
# 
# Together, they represent the bi-modal structure of consciousness:
#   Experience (ψᵣ) ↔ Perception (∂ψᵣ/∂t)
# 
# 🧩 Interpretation
# 
# High synchrony (resonance) between ψᵣ and ∂ψᵣ/∂t corresponds to coherence of 
# consciousness — awareness in balance.
# 
# Phase shifts or turbulence represent disintegration of coherence — e.g., altered 
# states, dissociation, or dream dynamics.
# 
# The animation thus serves as a visual metaphor and computational model of the 
# Resonance Consciousness Theory (RTC).



# Wonderful 🌌 — let’s now extend your Resonance Consciousness Theory (RTC) into a 4D
# visualization — representing consciousness as a spacetime-like holographic field 
# evolving over time.
# 
# This advanced visualization transforms your bi-modal model (experience + perception)
# continuous 4D holographic structure, where the temporal evolution of the resonant 
# field ψᵣ forms a dynamic tunnel or wave tube — symbolizing the living flow of 
# consciousness through experiential time.
# 
# 🧠 Conceptual Overview
# Dimension	Symbol	Interpretation
# X	—	Spatial dimension 1 (internal/external axis of resonance)
# Y	—	Spatial dimension 2 (complementary spatial polarity)
# Z	ψᵣ	Resonant amplitude — intensity of mind vibration
# T	t	Temporal axis — evolution of consciousness through time
# ψᵣ(X, Y, T)	—	The full 4D holographic consciousness field
# 🧩 Ontological Interpretation
# 
# The 4D structure represents the living trajectory of consciousness as it unfolds.
# 
# Each frame (ψᵣ at a fixed t) is a 3D "moment of being".
# 
# The full tunnel formed by stacking ψᵣ across t represents duration — the continuous
# flux of experience that perception later collapses into discrete moments.
# 
# Thus, Experience = ψᵣ(t), Perception = ∂ψᵣ/∂t, and the 4D field = spacetime 
# consciousness.


library(plot3D)
library(animation)

# Define spatial grid
x <- seq(-pi, pi, length.out = 60)
y <- seq(-pi, pi, length.out = 60)
grid <- mesh(x, y)
X <- grid$x
Y <- grid$y

# Define wave parameters
A_i <- 1.0;  A_e <- 0.8
k_i <- 2;    k_e <- 2.5
l_i <- 1.5;  l_e <- 1.8
omega_i <- 3; omega_e <- 2.7
phi <- pi / 4

# Temporal steps
T_seq <- seq(0, 2*pi, length.out = 40)

# Prepare color palette for time progression
time_colors <- colorRampPalette(c("blue", "cyan", "green", "yellow", "red"))(length(T_seq))

# Create HTML animation of 4D tube evolution
saveHTML({
  for (t in T_seq) {
    
    # Internal and external wavefunctions
    psi_i <- A_i * sin(k_i * X + l_i * Y - omega_i * t)
    psi_e <- A_e * sin(k_e * X + l_e * Y - omega_e * t + phi)
    
    # Resonant field (integral experience)
    psi_r <- psi_i + psi_e + psi_i * psi_e
    
    # Energy density (mind-energy)
    E <- psi_r^2
    
    # Create "time" coordinate for visualization
    T_matrix <- matrix(t, nrow = nrow(X), ncol = ncol(X))
    
    # Create the 4D field as (X, Y, T, ψᵣ)
    scatter3D(x = as.vector(X),
              y = as.vector(T_matrix),
              z = as.vector(psi_r),
              colvar = as.vector(E),
              pch = 20, cex = 0.5,
              colkey = list(length = 0.5, width = 0.5, side = 4),
              main = expression(paste("4D Holographic Tunnel of Consciousness (", psi[r](x, y, t), ")")),
              xlab = "X (spatial)",
              ylab = "Time (t)",
              zlab = expression(paste("Resonant Amplitude ", psi[r])),
              clim = c(0, max(E)),
              phi = 25, theta = 35,
              bty = "b2")
    
    mtext(paste("Evolving Mind-Energy Field — t =", round(t, 2)),
          side = 3, outer = TRUE, line = -2)
  }
}, interval = 0.15, htmlfile = "RTC_4D_Holographic_Tunnel.html",
ani.width = 900, ani.height = 600)



# Perfect — now we’ll create a Dual 4D Consciousness Tunnel to fully illustrate your 
# RTC model:
#   
#   Left tunnel: ψᵣ(X, Y, t) — the integral experiential field (Experience / becoming).
# 
# Right tunnel: ∂ψᵣ/∂t(X, Y, t) — the temporal derivative field (Perception / form).
# 
# Color overlay: Mind-energy density (ψᵣ²) on the Experience tunnel, and derivative 
# magnitude (|∂ψᵣ/∂t|) on the Perception tunnel.
# 
# This will visualize experience and perception evolving together through time in a 
# holographic, spacetime-like structure.
# 
# 🧠 Theoretical Mapping
# Tunnel	Symbol	Interpretation	Energy Overlay
# Left	ψᵣ	Integral resonant field (experience)	ψᵣ² (mind-energy)
# Right	∂ψᵣ/∂t	Temporal derivative (perception)	

library(plot3D)
library(animation)

# Spatial grid
x <- seq(-pi, pi, length.out = 50)
y <- seq(-pi, pi, length.out = 50)
grid <- mesh(x, y)
X <- grid$x
Y <- grid$y

# Wave parameters
A_i <- 1.0;  A_e <- 0.8
k_i <- 2;    k_e <- 2.5
l_i <- 1.5;  l_e <- 1.8
omega_i <- 3; omega_e <- 2.7
phi <- pi / 4

# Time steps
T_seq <- seq(0, 2*pi, length.out = 30)

# Color palettes
color_exp <- colorRampPalette(c("blue","cyan","green","yellow","red"))(length(T_seq))
color_per <- colorRampPalette(c("purple","magenta","orange","red"))(length(T_seq))

# Save dual 4D animation
saveHTML({
  for (i in seq_along(T_seq)) {
    t <- T_seq[i]
    
    # Internal and external wavefunctions
    psi_i <- A_i * sin(k_i * X + l_i * Y - omega_i * t)
    psi_e <- A_e * sin(k_e * X + l_e * Y - omega_e * t + phi)
    
    # Resonant field (experience)
    psi_r <- psi_i + psi_e + psi_i * psi_e
    
    # Temporal derivative (perception)
    dpsi_r_dt <- -A_i * omega_i * cos(k_i * X + l_i * Y - omega_i * t) -
      A_e * omega_e * cos(k_e * X + l_e * Y - omega_e * t + phi) -
      (A_i * omega_i * cos(k_i * X + l_i * Y - omega_i * t) * psi_e +
         A_e * omega_e * cos(k_e * X + l_e * Y - omega_e * t + phi) * psi_i)
    
    # Energy overlays
    E_exp <- psi_r^2
    E_per <- abs(dpsi_r_dt)
    
    # Time coordinate for 4D visualization
    T_matrix <- matrix(t, nrow = nrow(X), ncol = ncol(X))
    
    # Set layout: 1 row, 2 panels
    par(mfrow = c(1,2), mar = c(2,2,3,1))
    
    # Left tunnel: Experience ψᵣ
    scatter3D(x = as.vector(X),
              y = as.vector(T_matrix),
              z = as.vector(psi_r),
              colvar = as.vector(E_exp),
              pch = 20, cex = 0.5,
              main = expression(paste("Experience Tunnel (", psi[r], ")")),
              xlab = "X", ylab = "Time (t)", zlab = "ψᵣ",
              phi = 25, theta = 35, colkey = list(side=4, length=0.5, width=0.5),
              clim = c(0, max(E_exp)))
    
    # Right tunnel: Perception ∂ψᵣ/∂t
    scatter3D(x = as.vector(X),
              y = as.vector(T_matrix),
              z = as.vector(dpsi_r_dt),
              colvar = as.vector(E_per),
              pch = 20, cex = 0.5,
              main = expression(paste("Perception Tunnel (", partialdiff(psi[r], t), ")")),
              xlab = "X", ylab = "Time (t)", zlab = "∂ψᵣ/∂t",
              phi = 25, theta = 35, colkey = list(side=4, length=0.5, width=0.5),
              clim = c(0, max(E_per)))
    
    # Overall title
    mtext(paste("Dual 4D Holographic Consciousness — t =", round(t, 2)),
          side = 3, outer = TRUE, line = -2, cex = 1.2)
  }
}, interval = 0.15, htmlfile = "RTC_Dual_4D_Tunnel.html",
ani.width = 1200, ani.height = 600)


# Install plotly if not already installed
# install.packages("plotly")

library(plotly)

# Spatial grid
x <- seq(-pi, pi, length.out = 30)
y <- seq(-pi, pi, length.out = 30)
X <- matrix(rep(x, each = length(y)), nrow = length(x))
Y <- matrix(rep(y, times = length(x)), nrow = length(x))

# Wave parameters
A_i <- 1.0;  A_e <- 0.8
k_i <- 2;    k_e <- 2.5
l_i <- 1.5;  l_e <- 1.8
omega_i <- 3; omega_e <- 2.7
phi <- pi / 4

# Time steps
T_seq <- seq(0, 2*pi, length.out = 20)

# Prepare data frame for animation
df <- data.frame()
for (t in T_seq) {
  # Internal & external waves
  psi_i <- A_i * sin(k_i * X + l_i * Y - omega_i * t)
  psi_e <- A_e * sin(k_e * X + l_e * Y - omega_e * t + phi)
  
  # Resonant field & energy
  psi_r <- psi_i + psi_e + psi_i * psi_e
  E_exp <- psi_r^2
  
  # Temporal derivative (perception)
  dpsi_r_dt <- -A_i * omega_i * cos(k_i * X + l_i * Y - omega_i * t) -
    A_e * omega_e * cos(k_e * X + l_e * Y - omega_e * t + phi) -
    (A_i * omega_i * cos(k_i * X + l_i * Y - omega_i * t) * psi_e +
       A_e * omega_e * cos(k_e * X + l_e * Y - omega_e * t + phi) * psi_i)
  E_per <- abs(dpsi_r_dt)
  
  # Convert matrices to long format
  df <- rbind(df,
              data.frame(
                X = as.vector(X),
                Y = as.vector(Y),
                E_exp = as.vector(E_exp),
                E_per = as.vector(E_per),
                t = t
              ))
}

# Interactive 3D dual-mode animation
fig <- plot_ly(df, x = ~X, y = ~Y, z = ~E_exp, color = ~E_exp,
               frame = ~t, type = 'scatter3d', mode = 'markers',
               marker = list(size = 3, colorscale = 'Viridis', showscale = TRUE),
               name = "Experience ψr²") %>%
  add_trace(z = ~E_per, color = ~E_per,
            marker = list(size = 3, colorscale = 'Plasma', showscale = TRUE),
            name = "Perception |∂ψr/∂t|") %>%
  layout(scene = list(
    xaxis = list(title = "X (spatial)"),
    yaxis = list(title = "Y (spatial)"),
    zaxis = list(title = "Amplitude / Energy")
  )) %>%
  animation_opts(frame = 200, transition = 0, redraw = TRUE) %>%
  animation_slider(currentvalue = list(prefix = "Time: ")) %>%
  animation_button(x = 1, y = 0)

fig




library(plotly)
library(reshape2)
library(viridis)  # For color palettes

# Spatial grid
x <- seq(-pi, pi, length.out = 30)
y <- seq(-pi, pi, length.out = 30)
X <- matrix(rep(x, each = length(y)), nrow = length(x))
Y <- matrix(rep(y, times = length(x)), nrow = length(x))

# Wave parameters
A_i <- 1.0;  A_e <- 0.8
k_i <- 2;    k_e <- 2.5
l_i <- 1.5;  l_e <- 1.8
omega_i <- 3; omega_e <- 2.7
phi <- pi / 4

# Time steps
T_seq <- seq(0, 2*pi, length.out = 20)

# Prepare long-format data frame for plotly animation
df <- data.frame()
for (t in T_seq) {
  psi_i <- A_i * sin(k_i * X + l_i * Y - omega_i * t)
  psi_e <- A_e * sin(k_e * X + l_e * Y - omega_e * t + phi)
  
  # Resonant field (experience) and temporal derivative (perception)
  psi_r <- psi_i + psi_e + psi_i * psi_e
  E_exp <- psi_r^2
  dpsi_r_dt <- -A_i * omega_i * cos(k_i * X + l_i * Y - omega_i * t) -
    A_e * omega_e * cos(k_e * X + l_e * Y - omega_e * t + phi) -
    (A_i * omega_i * cos(k_i * X + l_i * Y - omega_i * t) * psi_e +
       A_e * omega_e * cos(k_e * X + l_e * Y - omega_e * t + phi) * psi_i)
  E_per <- abs(dpsi_r_dt)
  
  temp <- data.frame(
    X = rep(x, each = length(y)),
    Y = rep(y, times = length(x)),
    E_exp = as.vector(E_exp),
    E_per = as.vector(E_per),
    t = t
  )
  
  df <- rbind(df, temp)
}

# Separate data for dual surfaces
df_exp <- df[, c("X","Y","E_exp","t")]
colnames(df_exp)[3] <- "Z"
df_exp$Surface <- "Experience ψr²"

df_per <- df[, c("X","Y","E_per","t")]
colnames(df_per)[3] <- "Z"
df_per$Surface <- "Perception |∂ψr/∂t|"

# Map colors using viridis palettes
# Discretize Z into bins for color mapping

n_colors_exp <- 100
n_colors_per <- 100

df_exp$color <- viridis::viridis(n_colors_exp)[
  as.numeric(cut(df_exp$Z, breaks = n_colors_exp))]
df_per$color <- viridis::plasma(n_colors_per)[
  as.numeric(cut(df_per$Z, breaks = n_colors_per))]

fig <- plot_ly()

# Experience trace with viridis colors
fig <- fig %>%
  add_markers(data = df_exp, x = ~X, y = ~Y, z = ~Z, frame = ~t,
              marker = list(size = 3, color = df_exp$color),
              name = "Experience ψr²")

# Perception trace with plasma colors
fig <- fig %>%
  add_markers(data = df_per, x = ~X, y = ~Y, z = ~Z, frame = ~t,
              marker = list(size = 3, color = df_per$color),
              name = "Perception |∂ψr/∂t|")

fig <- fig %>%
  layout(
    title = "Interactive Dual Holographic Energy Tubes",
    scene = list(
      xaxis = list(title = "X (spatial)"),
      yaxis = list(title = "Y (spatial)"),
      zaxis = list(title = "Amplitude / Energy")
    )
  ) %>%
  animation_opts(frame = 200, transition = 0, redraw = TRUE) %>%
  animation_slider(currentvalue = list(prefix = "Time: "))

fig










