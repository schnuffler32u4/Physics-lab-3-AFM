from NSFopen.read import read
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

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


file = "MeasurmentesCalibrationBad/Calibration/Image00006.nid"
afm = read(file)

data = afm.data 
#data = pd.read_csv("Measurements/Carbon-nanotubes/Carbonano1.csv")
# data = data[0]
# We begin by making sure that the data starts from 0
Zaxis = data['Image']['Forward']['Z-Axis'] 
param = afm.param
extents = [param[i][j][0] * 1e6 for i in ['X','Y'] for j in ['min', 'range']]
plt.imshow(Zaxis,extent=extents,  cmap='gray')
plt.axis('off')  # To remove the axes
plt.show()

print(data)
