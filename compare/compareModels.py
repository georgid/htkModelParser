'''
Created on Mar 24, 2014

@author: joro
'''
from htk_converter import HtkConverter
from htk_models import Hmm
from IPython.core.tests.test_formatters import numpy
import matplotlib as plt
from matplotlib.pyplot import plot
from pylab import *

path_to_hmm_defs_before_adapt='/Users/joro/Documents/Phd/UPF/METUdata//model_output/hmmdefs_edited_for_wout'
path_to_hmm_defs_after_adapt='/Users/joro/Documents/Phd/UPF/METUdata//model_output/hmmdefs.gmllrmean_edited_for_wout'
path_to_hmm_defs_after_adapt = '/Users/joro/Documents/Phd/UPF/METUdata/model_output/hmmdefs.gmmlrmean_test'

PATH_TO_HMMLIST='/Users/joro/Documents/Phd/UPF/voxforge/auto/scripts/interim_files/monophones0'




def _computeDiffForaPhonemeModel(means1, means2):
    
    distances = []
      
    ######## find diff. 
    for mean1, mean2 in zip(means1, means2):    
        mean1Array = numpy.asarray(mean1)
        mean2Array = numpy.asarray(mean2)

        euclDist = numpy.linalg.norm(mean1Array - mean2Array)
        norm2meanOriginalModel = numpy.linalg.norm(mean1Array)
        distances.append(euclDist/norm2meanOriginalModel)
   
    # compute ratio to first model    
    return distances


'''
get the means for the three states of a phoneme model
'''

def getMeansForStates(hmmModel1):
    means = []
    
    for i in range(len(hmmModel1.states)):
        currState1 = hmmModel1.states[i][1]
        
        # only one mixture
        mixture = currState1.mixtures[0][2]
        mean1 = mixture.mean.vector
        
        means.append(mean1)
    
    return  means



    '''
    for the two loaded models computes l2-distance between mean of each state
    Can be done for all models or only for a given phoneme. edit in the function the var phonemeName
    '''
def findDiffMean(phonemeName):
    
    hmmModel1, hmmModel2  = loadModelsForGivenPhoneme(phonemeName)
    
    
    # get mean vectors 
    means1 = getMeansForStates(hmmModel1)
    means2 = getMeansForStates(hmmModel2)
   
   
    distances = _computeDiffForaPhonemeModel(means1, means2)
    print "phoneme name: %s"  % phonemeName
    print "distances: " , distances[0], distances[1], distances[2]


    

'''
get the hmm model for a given phoneme from the two trained models 
'''    
def loadModelsForGivenPhoneme(phonemeName):
    # load models
    conv_before = HtkConverter()
    conv_before.load(path_to_hmm_defs_before_adapt, PATH_TO_HMMLIST)
    conv_after = HtkConverter()
    conv_after.load(path_to_hmm_defs_after_adapt, PATH_TO_HMMLIST)
    
    # get models for given phoneme:
   
    hmmModels = [hmm for hmm in conv_before.hmms if hmm.name == phonemeName]
    hmmModel1 = hmmModels[0]
    hmmModels = [hmm for hmm in conv_after.hmms if hmm.name == phonemeName]
    hmmModel2 = hmmModels[0]
    return hmmModel1, hmmModel2


if __name__ == '__main__':
    phonemeName = 'A'
    findDiffMean(phonemeName)
    
    
    
    