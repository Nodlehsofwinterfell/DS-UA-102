import numpy as np


# input: a 1D numpy array
# output: the median absolute deviation of the input array
# wrriten at 2021/7/15

def medAbDev(array):
    wriitenBy = "YutingFan"
    md1 = np.median(array)
    temp_list = []
    for i in array:
        temp_list.append(abs(i - md1))
    temp_np_list = np.array(temp_list)
    return np.median(temp_np_list)


if __name__ == '__main__':
    a = np.array([1, 3, 5, 7, 9])
    b = np.array([4.5, 3.2, 1.5, 5.7, 9.3, 2.2, 6.9])
    print(medAbDev(a))
    print(medAbDev(b))
