import numpy as np
import pandas as pd


# We want to define a function such that  it allows us to load a specific csv files and then it averages one of the columns that is also predefined in the function 



def average(file, column):
    averaging = np.array()
    for datafile in file:
        data = pd.read_csv(datafile)
        data.rename(columns={column:"column"},inplace=True) # this is done in order to allow for files whose columns might have weird names
        intermediate = np.array(data.column)
        np.append(averaging, intermediate) 
    return str(np.average(averaging)) + "±" + str(np.std(averaging))
