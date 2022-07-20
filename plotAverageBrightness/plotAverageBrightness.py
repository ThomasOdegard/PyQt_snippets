#Todo: integrate or move plotting to PyQT

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# np.set_printoptions(threshold=sys.maxsize)

# testing on 400x400 checker pattern.
image = Image.open(r"chess.jpg")
left = 0
right = 300 #400
top = 0
bottom = 200 #400


image = image.crop((left, top, right, bottom))
image = image.convert('L')
image.show()
brightness_data = np.asarray(image)

#  Vertical average = 1, Horizontal average = 0.
a_data = np.average(brightness_data, axis=0)

print("integral: ", np.trapz(a_data))


fig, axs = plt.subplots(3)
axs[0].plot(a_data)
axs[0].set_title("avg. brightness")
axs[1].plot(cumulative_trapezoid(
    a_data, list(range(1, len(a_data)+1)), initial=0))
axs[1].set_title(f"integral: {np.trapz(a_data):.3f}")
axs[2].set_title("Histogram")
axs[2].plot(image.histogram())

plt.show()
