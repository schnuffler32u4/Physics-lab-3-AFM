from NSFopen.read import read
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = "Measurements/Carbon-nanotubes/Image00005.nid"
afm = read(file)

data = afm.data 
#data = pd.read_csv("Measurements/Carbon-nanotubes/Carbonano1.csv")
print(data)
# We begin by making sure that the data starts from 0

data = data - np.ones(len(data), len(data[0]))*np.amin(data)

plt.imshow(luminance_array, cmap='gray')
plt.show()
