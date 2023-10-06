import numpy as np


# input: A -> a 2D array (with predictions in the column 1 and measurements in column 2)
#        power -> a flag by which power to normalize the error, for instance 1 for the mean absolute error, 2 for the
#                 RMSE, 3 for the cubic root mean cubed error and so on.
# output: The output of this calculation should be a single scalar, real number.
# wrriten at 2021/7/21 by Yuting Fan

def normalizedError(A, power):
    rows = A.shape[0]
    dif_sum = 0
    for i in A:
        dif = i[0] - i[1]
        dif_sum += pow(abs(dif), power)
    ne = pow(dif_sum / rows, 1 / power)
    return ne


if __name__ == '__main__':
    caseA = [[1, 2], [2, 4], [3, 1], [4, 6], [5, 2]]
    caseB = [[0, 50], [10, 5], [5, 10]]
    npA = np.array(caseA)
    npB = np.array(caseB)
    print(normalizedError(npA, 1))
    print(normalizedError(npA, 2))
    print(normalizedError(npA, 3))
    print(normalizedError(npB, 1))
    print(normalizedError(npB, 2))
    print(normalizedError(npB, 3))
