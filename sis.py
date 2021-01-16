# 
import datetime as dt
import numpy as np

class SIS():
    def __init__(self, network_size, plambda, iniInfected):
        self.n = network_size
        iniI = 1#iniInfected
        self.Lambda = plambda
        self.myMat = self.net_A2A(self.n)
        self.myStateVec = np.zeros(self.n)
        iniI = np.random.randint(0, self.n)
        self.myStateVec[iniI] = 1
        Ss1 = np.arange(0, iniI)
        Ss2 = np.arange(iniI+1, self.n)
        self.Ss = np.concatenate((Ss1, Ss2), axis=0)
        self.Is = np.array([iniI])
        self.iSizes = []
        self.iSize = 1
        
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
    