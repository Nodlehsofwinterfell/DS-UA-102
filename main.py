 """
Created on Thu Aug 12 15:18:02 2021

@author: ***
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# the function slideWinDescStats takes in 3 input arguments,  in this order: 
# 1) An input dataset (make it a 1- or 2D numpy array), 
# 2) a flag for which parameter to calculate, where 1 = mean, 2 = SD and 3 = correlation 
# 3) the window size (the subset of how many numbers of the dataset to compute the parameter indicated in 2)
# For the mean, use np.sum(data)/window_size to calculate
# For the SD, use np.std(data, 2), where parameter 2 represents the sample standard deviation
# For the correlation, Pearson correlation coefficient needs to be calculated, use np.corrcoef(x,y) to calculate
# The function was written on 2021/08/12 by ***
def slidWinDescStats(data, type, window_size):
    ret = []
    for i in range(data.shape[0] - window_size + 1):
        if type == 1:
            ret.append(round(np.sum(data[i:i+window_size])/window_size,2))
        elif type == 2:
            ret.append(round(np.std(data[i:i+window_size], ddof=1),2))
        else:
            ret.append(round(np.corrcoef(data[i:i+window_size,0],data[i:i+window_size,1])[0,1],3))
    return np.array(ret)

# input/output example one
A = np.array([1,3,5,7,9])
print(slidWinDescStats(A,1,3))
print(slidWinDescStats(A,1,4))
print(slidWinDescStats(A,2,3))
print(slidWinDescStats(A,2,4))
B = np.array([[1,1],[3,2],[5,4],[7,3],[9,5]])
print(slidWinDescStats(B,3,3))
print(slidWinDescStats(B,3,4))

# input/output example two(load inputArrayExample.csv)
df = pd.read_csv('outputArrayExample50.csv')
data = df.values
plt.plot(range(data.shape[0]), data,color='black',linewidth=2.0)
plt.title('outputArrayExample50_raw_data')
plt.show()
plt.close()
index = np.array(range(data.shape[0]))
data = np.array([index,data.reshape(-1,)]).T
y = slidWinDescStats(data, 3, 50)
plt.plot(range(y.shape[0]), y,color='black',linewidth=2.0)
plt.title('Windows size 50')
plt.show()
plt.close()

df = pd.read_csv('outputArrayExample300.csv')
data = df.values
plt.plot(range(data.shape[0]), data,color='black',linewidth=2.0)
plt.title('outputArrayExample300_raw_data')
plt.show()
plt.close()
index = np.array(range(data.shape[0]))
data = np.array([index,data.reshape(-1,)]).T
y = slidWinDescStats(data, 3, 300)
plt.plot(range(y.shape[0]), y,color='black',linewidth=2.0)
plt.title('Windows size 300')
plt.show()