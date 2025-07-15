import matplotlib.pyplot as plt

x = [1, 2, 3]
y1 = [1, 2, 3]
y2 = [3, 2, 1]

plt.plot(x, y1, label='Growth', color='green')
plt.plot(x, y2, label='Decline', color='red')

legend = plt.legend(loc='lower right', title='Trends', fontsize='medium', title_fontsize='large', shadow=True, frameon=True, facecolor='lightgrey', edgecolor='black')
plt.grid(True)

# Optional: change text color
for text in legend.get_texts():
    text.set_color("blue")

plt.show()
