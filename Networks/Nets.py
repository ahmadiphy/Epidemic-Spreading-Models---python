# Complex networks
import numpy as np


class net():
    #base class of networks
    def __init__(self):
        pass


class A2A(net):
    # all to all network
    def __init__(self, n):
        self.N = n

    def net_A2A(self):
        if self.N > 1:
            myMatrix = []
            for i in range(N):
                myRow = []
                for j in range(N):
                    myRow.append(1)
                myRow = np.array(myRow)
                myRow[i] = 0
                myMatrix.append(myRow)
            myMatrix = np.array(myMatrix)
            return myMatrix
        else:
            print("Error! (N < 2)")


class ER(net):
    #ER network
    def __init__(self):
        pass


class SF(net):
    # SF network
    def __init__(self):
        pass
