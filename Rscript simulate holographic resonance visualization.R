# RTC Model 3D Simulation: Holographic Resonance Field (Corrected)
# Author: Edward F. Hillenaar, MSc

# Load required library
library(plot3D)

# Define spatial grid
x <- seq(-pi, pi, length.out = 100)
y <- seq(-pi, pi, length.out = 100)
t <- 0  # time snapshot

# Create 2D meshgrid (as matrices)
grid <- mesh(x, y)
X <- grid$x
Y <- grid$y

# Define wave parameters
A_i <- 1.0;  A_e <- 0.8
k_i <- 2;    k_e <- 2.5
l_i <- 1.5;  l_e <- 1.8
omega_i <- 3; omega_e <- 2.7
phi <- pi / 4

# Compute internal and external wavefunctions
psi_i <- A_i * sin(k_i * X + l_i * Y - omega_i * t)
psi_e <- A_e * sin(k_e * X + l_e * Y - omega_e * t + phi)

# Resonant field (integral experience)
psi_r <- psi_i + psi_e + psi_i * psi_e  # interference and coupling term

# 3D surface plot
surf3D(X, Y, psi_r,
       colkey = TRUE, colvar = psi_r,
       main = "Holographic Resonance Field (ψ_r)",
       xlab = "X (spatial dimension)",
       ylab = "Y (spatial dimension)",
       zlab = "Resonant Amplitude",
       border = "black", shade = 0.6, bty = "b2")
