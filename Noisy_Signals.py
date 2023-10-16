import numpy as np
import matplotlib.pyplot as plt
import os


# Load the data from the file
file_path = "Destination/To/twoNoisySignals.txt"
data = np.loadtxt(file_path)

#data = np.loadtxt("twoNoisySignals.txt")

# Split the data into voltage and current signals
voltage_signal = data[:, 0]
current_signal = data[:, 1]

# Create a time array based on the sampling rate (10 kHz)
sampling_rate = 10000
time = np.arange(len(voltage_signal)) / sampling_rate

# Plot the voltage and current signals
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, voltage_signal)
plt.title("Voltage Signal")
plt.subplot(2, 1, 2)
plt.plot(time, current_signal)
plt.title("Current Signal")
plt.xlabel("Time (s)")
plt.tight_layout()
plt.show()

def calculate_dft(signal):
    N = len(signal)
    dft = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(N, 1 / sampling_rate)
    return frequencies, dft

# Calculate the DFT for voltage and current signals
frequencies_v, dft_voltage = calculate_dft(voltage_signal)
frequencies_c, dft_current = calculate_dft(current_signal)

# Find the fundamental frequency for each signal
fundamental_frequency_v = frequencies_v[np.argmax(np.abs(dft_voltage))]
fundamental_frequency_c = frequencies_c[np.argmax(np.abs(dft_current))]

print(f"Fundamental Frequency (Voltage): {fundamental_frequency_v} Hz")
print(f"Fundamental Frequency (Current): {fundamental_frequency_c} Hz")


def calculate_phase_difference(dft_signal1, dft_signal2):
    convolution = np.fft.ifft(dft_signal1 * np.conj(dft_signal2))
    max_index = np.argmax(np.abs(convolution))
    phase_difference = np.angle(convolution[max_index])
    return phase_difference

# Calculate the phase difference between voltage and current signals
phase_difference_rad = calculate_phase_difference(dft_voltage, dft_current)

print(f"Phase Difference (Radians): {phase_difference_rad}")
