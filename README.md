# Signal Analysis with DFT and Phase Difference

This Python program analyzes two noisy signals (voltage and current) sampled at 10 kHz. It performs the following tasks:

1. Loads the data from the "twoNoisySignals.txt" file.
2. Plots the voltage and current signals over time.
3. Calculates the fundamental frequency for each signal using the Discrete Fourier Transform (DFT).
4. Finds the phase difference between the two signals in radians.

## Instructions

1. **Data File**: Ensure the "twoNoisySignals.txt" file is in the specified file path (you can modify the `file_path` variable in the code to match your file's location).

2. **Dependencies**: Make sure you have the necessary libraries installed, including NumPy and Matplotlib. You can install them using pip:
   
   ```bash
   pip install numpy matplotlib
