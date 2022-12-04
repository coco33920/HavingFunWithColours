from matplotlib import pyplot as plot 
import numpy as np
class Operation:
    def __init__(self,file):
        self.file = file
    
    def exist(self):
        try:
            self.matrix = plot.imread(self.file)
            return True
        except:
            return False
        
    