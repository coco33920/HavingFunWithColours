from matplotlib import pyplot as plot 
import numpy as np
import os
class Operation:
    def __init__(self,file):
        self.file = file
        self.name = os.path.basename(file)

    
    def exist(self):
        try:
            self.matrix = plot.imread(self.file)
            print(self.matrix)
            return True
        except:
            return False
    
    def prints(self):
        plot.imshow(self.matrix)
        plot.imsave("results/"+self.name,self.matrix)