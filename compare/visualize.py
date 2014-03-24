'''
Created on Mar 24, 2014

@author: joro
'''

from pylab import *
from compare.compareModels import loadModelsForGivenPhoneme, getMeansForStates

 
def plotMfccs(mfcc1, mfcc2):
    figure()
    plot(mfcc1, 'r')
    plot(mfcc2, 'g')
    show()
    

if __name__ == '__main__':
        phonemeName ='AA'
        hmmModel1, hmmModel2  = loadModelsForGivenPhoneme(phonemeName)
        
           # get mean vectors 
        means1 = getMeansForStates(hmmModel1)
        means2 = getMeansForStates(hmmModel2)
        
        whichState = 2
        plotMfccs(means1[whichState], means2[whichState])
        
