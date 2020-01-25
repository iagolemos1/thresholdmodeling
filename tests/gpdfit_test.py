from thresholdmodeling import thresh_modeling
import pandas as pd
import unittest


url = 'https://raw.githubusercontent.com/iagolemos1/thresholdmodeling/master/dataset/rain.csv'
df =  pd.read_csv(url, error_bad_lines=False)

class TestFun(unittest.TestCase):
    def test_fit(self):
        """
        Test that it can fit the array to a GPD  comparing to the values presented by Coles
        """
        data = df.values.ravel()
        result = thresh_modeling.gpdfit(data, 30, 'mle')
        #testing scale parameter
        self.assertEqual(round(result[0],3), 0.185) 
        #testing shape parameter
        self.assertEqual(round(result[1],2), 7.44) 

if __name__ == '__main__':
    unittest.main()