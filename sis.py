# SIS model
import datetime as dt
import numpy as np
import Nets as network

class SIS():
    def __init__(self, size, lambda_p, iniInfected, net):
        self.N = size
        self.myStateVec = np.zeros(self.n)
        self.Lambda = lambda_p
        iniIs = []
        if size < iniInfected:
            print("Warning! Trivial result.")
            iniInfected = size
            iniIs = np.arange(0, size, 1)
            for i in range(0, self.n):
                self.myStateVec[i] = 1
        elif iniInfected > 0:
            iniIs = np.random.choice(0, self.n, size=iniInfected, replace=False)
            for i in iniIs:
                self.myStateVec[i] = 1
        else:
            print('ERROR!')
            return None

        self.Ss = []
        self.Is = []
        for i in range(self.n):
            if self.myStateVec[i] == 0:
                self.Ss.append(i)
            elif self.myStateVec[i] == 1:
                self.Is.append(i)
        self.iSizes = []
        self.iSize = 1
        self.myMat = None

    def mynet(self):
        self.myMat = network.net_A2A(self.n)
    
    def dynamics(self):
        print('dynamics started at:')
        print(dt.datetime.now())
        step = 0
        while self.iSize > 0:
            step = step + 1
            self.iSizes.append(self.iSize/self.n)
            new_Is = []
            for i in self.Is:
                for j in range(len(self.myMat[i])):
                    if self.myMat[i][j] == 1 and self.myStateVec[j] == 0:
                        rNij = np.random.uniform(0.0, 1.0)
                        if rNij <= self.Lambda:
                            new_Is.append(j)
                            self.myStateVec[j] = 1
            for i in self.Is:
                self.myStateVec[i] = 0

            self.Is = np.array(new_Is)
            self.Is.sort()
            self.iSize = self.Is.size
        else:
            print('dynamic has finished at:')
            print(dt.datetime.now())
            return self.iSizes
    