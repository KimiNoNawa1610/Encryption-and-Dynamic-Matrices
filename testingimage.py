import numpy as np
import matplotlib
import matplotlib.pyplot as plt

Y = ["j = h-1", ".",".", ".", "j = y",
              ".", ".", ".", "j = 0"]
X = ["i = 0", ".", ".",
           ".", "i = x", ".",".", "i = w-1"]

pixels = np.array([[10, 20, 30, 40, 50, 60, 80, 100],
                    [110, 120, 130, 140, 150, 160, 170, 180],
                    [190, 200, 210, 220, 230, 240, 250, 255],
                    [10, 20, 30, 40, 50, 60, 80, 100],
                    [110, 120, 130, 140, 150, 160, 170, 180],
                    [190, 200, 210, 220, 230, 240, 250, 255],
                    [10, 20, 30, 40, 50, 60, 80, 100],
                    [110, 120, 130, 140, 150, 160, 170, 180],
                    [190, 200, 210, 220, 230, 240, 250, 255]])


fig, ax = plt.subplots()
im = ax.imshow(pixels,cmap = "gray")

ax.set_xticks(np.arange(len(X)))
ax.set_yticks(np.arange(len(Y)))
ax.set_xticklabels(X)
ax.set_yticklabels(Y)

plt.setp(ax.get_xticklabels(), ha="center", rotation_mode="anchor")

for i in range(len(Y)):
    for j in range(len(X)):
        ax.text(j, i, pixels[i, j], ha="center", va="center", color="black")

ax.set_title("Image Data")
fig.tight_layout()
plt.show()
