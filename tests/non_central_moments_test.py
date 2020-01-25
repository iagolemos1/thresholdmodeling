from thresholdmodeling import thresh_modeling
import pandas as pd
import unittest
from scipy.stats import genpareto


url = 'https://raw.githubusercontent.com/iagolemos1/thresholdmodeling/master/dataset/rain.csv'
df =  pd.read_csv(url, error_bad_lines=False)

class TestFun(unittest.TestCase):
    def test_entropy(self):
        """
        Testing the non-central moments computation
        """
        data = df.values.ravel()
        result = thresh_modeling.non_central_moments(data, 30, 'mle')
        par = thresh_modeling.gpdfit(data, 30, 'mle')
        #testing 
        self.assertEqual(result[0], genpareto.stats(par[0], 30, par[1], 'mvsk')[0]) 
        self.assertEqual(result[1], genpareto.stats(par[0], 30, par[1], 'mvsk')[1]) 
        self.assertEqual(result[2], genpareto.stats(par[0], 30, par[1], 'mvsk')[2]) 
        self.assertEqual(result[3], genpareto.stats(par[0], 30, par[1], 'mvsk')[3]) 
    
     

if __name__ == '__main__':
    unittest.main()