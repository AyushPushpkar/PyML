import numpy as np
import matplotlib.pyplot as plt

try:
    # Generate 100 values between 0 and 6π
    x = np.linspace(0, 6 * np.pi, 100)

    # Compute sine and cosine values
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # Create subplots (1 row, 2 columns)
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))

    # First subplot: Sine
    axs[0].plot(x, y_sin, color='blue')
    axs[0].set_title("Sine Wave")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("sin(x)")
    axs[0].grid(True)

    # Second subplot: Cosine
    axs[1].plot(x, y_cos, 'g--')
    axs[1].set_title("Cosine Wave")
    axs[1].set_xlabel("x")
    axs[1].set_ylabel("cos(x)")
    axs[1].grid(True)

    # Adjust layout to prevent overlapping
    plt.tight_layout()

    # Display the plot
    plt.show()

except Exception as e:
    print("Error:", e)
