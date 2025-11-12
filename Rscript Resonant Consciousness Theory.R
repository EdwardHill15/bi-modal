# RTC Model Simulation: Resonant Interference and Perceptual Collapse
# Author: Edward F. Hillenaar, MSc

# Time domain
t <- seq(0, 4 * pi, length.out = 1000)

# Internal (ψ_i) and External (ψ_e) wavefunctions
freq_i <- 3       # internal frequency (Hz)
freq_e <- 2.5     # external frequency (Hz)
amp_i  <- 1.0     # amplitude of internal wave
amp_e  <- 0.8     # amplitude of external wave

psi_i <- amp_i * sin(freq_i * t)
psi_e <- amp_e * sin(freq_e * t + pi/4)  # phase-shifted external wave

# Resonant interaction (integral experience)
psi_r <- psi_i + psi_e + psi_i * psi_e   # resonance term represents interference coupling

# Perceptual collapse (derivative)
phi <- c(0, diff(psi_r))                 # simple discrete derivative

# Plot the wavefunctions
par(mfrow = c(3,1), mar = c(4,4,2,1))
plot(t, psi_i, type="l", col="blue", lwd=2,
     main="Internal and External Wavefunctions",
     ylab="Amplitude", xlab="Time")
lines(t, psi_e, col="red", lwd=2, lty=2)
legend("topright", legend=c("Internal ψ_i", "External ψ_e"), col=c("blue","red"), lty=c(1,2))

plot(t, psi_r, type="l", col="purple", lwd=2,
     main="Resultant Resonance Wavefunction (ψ_r)",
     ylab="Amplitude", xlab="Time")

plot(t, phi, type="l", col="darkgreen", lwd=2,
     main="Perceptual Collapse (Derivative of ψ_r)",
     ylab="Collapsed Signal (φ)", xlab="Time")
