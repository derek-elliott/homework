import numpy as np
import matplotlib.pyplot as plt
class IMRChart:
    def __init__(self, data):
        self.d2 = 1.128
        self.D3 = 0
        self.D4 = 3.267
        self.data = data
        self.mean = sum(data)/float(len(data))
        self.mr = self._setMovingRange()
        self.mrave = sum(self.mr)/float(len(self.mr) - 1)
        self.indlcl = self._findIndividualLCL()
        self.inducl = self._findIndividualUCL()
        self.mrlcl = self._findMrLCL()
        self.mrucl = self._findMrUCL()
        
    def _setMovingRange(self):
        mr = []
        for index, value in enumerate(self.data[1:]):
            mr.append(abs(value - self.data[index - 1]))
        return mr
    
    def _findIndividualLCL(self):
        return max(0, self.mean - 3*(self.mrave/self.d2))
    
    def _findIndividualUCL(self):
        return self.mean + 3*(self.mrave/self.d2)
    
    def _findMrLCL(self):
        return max(0, self.mrave * self.D3)
    
    def _findMrUCL(self):
        return self.mrave * self.D4
    
    def showIChart(self, savefig = True, figtype = 'png'):
        chart = plt.plot(range(len(data)), data.values())
        plt.axhline(y = self.indlcl)
        plt.annotate('LCL = {:.2f}'.format(self.indlcl),
                     xy=(len(data) + 1, self.indlcl),
                     xycoords='data',
                     annotation_clip = False)
        plt.axhline(y = self.mean)
        plt.annotate('CL = {:.2f}'.format(self.mean),
                     xy=(len(data) + 1, self.mean),
                     xycoords='data',
                     annotation_clip = False)
        plt.axhline(y = self.inducl)
        plt.annotate('UCL = {:.2f}'.format(self.inducl),
                     xy=(len(data) + 1, self.inducl),
                     xycoords='data',
                     annotation_clip = False)
        plt.title("Individual Chart")
        if savefig:
            plt.savefig('IChart.{}'.format(figtype), bbox_inches = 'tight')
        plt.show()
        
    def showMRChart(self, savefig = True, figtype = 'png'):
        chart = plt.plot(range(len(self.mr)), self.mr)
        plt.axhline(y = self.mrlcl)
        plt.annotate('lCL = {:.2f}'.format(self.mrlcl),
                     xy=(len(data) + 1, self.mrlcl),
                     xycoords='data',
                     annotation_clip = False)
        plt.axhline(y = self.mrave)
        plt.annotate('UCL = {:.2f}'.format(self.mrave),
                     xy=(len(data) + 1, self.mrave),
                     xycoords='data',
                     annotation_clip = False)
        plt.axhline(y = self.mrucl)
        plt.annotate('UCL = {:.2f}'.format(self.mrucl),
                     xy=(len(data) + 1, self.mrucl),
                     xycoords='data',
                     annotation_clip = False)
        plt.title("Moving Range Chart")
        if savefig:
            plt.savefig('MRChart.{}'.format(figtype), bbox_inches = 'tight')
        plt.show()

data = {"AL":30, "AK":24, "AZ":26, "AR":26, "CA":26, "CO":17, 
        "CT":27,"DE":35, "FL":23, "GA":30, "HI":20, "ID":20, 
        "IL":25, "IN":18, "IA":20, "KS":17, "KY":22, "LA":25, 
        "ME":27, "MD":46, "MA":35, "MI":21, "MN":25, "MS":27, 
        "MO":23, "MT":20, "NE":18, "NV":21, "NH":28, "NJ":30, 
        "NM":28, "NY":27, "NC":30, "ND":20, "OH":20, "OK":23, 
        "OR":29, "PA":24, "RI":31, "SC":30, "SD":18, "TN":23, 
        "TX":24, "UT":16, "VT":27, "VA":22, "WA":21, "WV":27, 
        "WI":18, "WY":17}
chart = IMRChart(data.values())
chart.showIChart(savefig = True)
