import pandas as pd
import numpy as np

def empiricalSampleBounds(data, n):
    try:
        df = pd.read_csv(data, header = None)
        data = df.values.reshape(-1)
    except:
        pass
    threshold_1 = (100 - n) / 200
    threshold_2 = 1 - (100 - n) / 200
    data = np.sort(data)
    (sum_,) = data.shape
    bound_1 = None
    bound_2 = None
    for i in range(len(data)):
        if bound_1 is None and (i+1)/sum_ >= threshold_1:
            bound_1 = data[i]
        if bound_2 is None and (i+1)/sum_ >= threshold_2:
            bound_2 = data[i]
    return round(bound_1,3), round(bound_2,3)
print(empiricalSampleBounds('sampleInput1.csv', 95))
print(empiricalSampleBounds('sampleInput1.csv', 99))
print(empiricalSampleBounds('sampleInput1.csv', 50))
print(empiricalSampleBounds('sampleInput2.csv', 95))
print(empiricalSampleBounds('sampleInput2.csv', 99))
print(empiricalSampleBounds('sampleInput2.csv', 50))