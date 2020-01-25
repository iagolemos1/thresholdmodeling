from thresholdmodeling import thresh_modeling
import pandas as pd
import unittest
from scipy.stats import genpareto
import math as mt

url = 'https://raw.githubusercontent.com/iagolemos1/thresholdmodeling/master/dataset/rain.csv'
df =  pd.read_csv(url, error_bad_lines=False)

def entropy(sample, b, threshold, fit_method): #Get the entropy of the distribution
    [shape, scale, sample, sample_excess, sample_over_thresh] = thresh_modeling.gpdfit(sample, threshold, fit_method)
    h = mt.log(scale) + shape + 1              
    print('The differential entropy is {} nats.'.format(h))
    return (h, shape, scale)

class TestFun(unittest.TestCase):
    def test_entropy(self):
        """
        Testing the diferencial entropy computation
        """
        data = df.values.ravel()
        result = entropy(data, 'e', 30, 'mle')
        #testing 
        self.assertEqual(result[0], genpareto.entropy(result[1], 30, result[2])) 
     

if __name__ == '__main__':
    unittest.main()
