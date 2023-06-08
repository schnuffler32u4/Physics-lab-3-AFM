from NSFopen.read import read
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def flatten(data, order=1, mask=[]):
    data_out = np.copy(data)  # create copy of data
    data_in = np.copy(data)
    if np.any(mask):
        data_in[mask] = np.nan
    for idx, (out, line) in enumerate(zip(data_out, data_in)):
        ix = np.isfinite(line)
        
        x = np.arange(len(line))
        p = np.polyfit(x[ix], line[ix], order)  # fit data to polynomial
        y = np.polyval(p, x)
        data_out[idx] = out - y  # subtract fit from data
    return data_out
file = "Measurements/Carbon-nanotubes/Image00005.nid"
afm = read(file)

data = afm.data 
#data = pd.read_csv("Measurements/Carbon-nanotubes/Carbonano1.csv")
data = data[0]
# We begin by making sure that the data starts from 0

data = data - np.ones((len(data), len(data[0])))*np.amin(data)
data = data/np.amax(data)
data = flatten(data)
plt.imshow(data, cmap='gray', vmin=0, vmax=1)
plt.axis('off')  # To remove the axes
plt.show()

print(data)
