from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import FloatVector
from thresholdmodeling import thresh_modeling
import pandas as pd
import unittest


url = 'https://raw.githubusercontent.com/iagolemos1/thresholdmodeling/master/dataset/rain.csv'
df =  pd.read_csv(url, error_bad_lines=False)

class TestFun(unittest.TestCase):
    def test_lmom_sample(self):
        """
        Testing L-moments from sample
        """
        data = df.values.ravel()
        POT = importr('POT') #importing POT package
        POTLmonsample = POT.samlmu(FloatVector(data), 4)
        result = thresh_modeling.lmom_sample(data)
        #testing 
        self.assertEqual(round(result[0],4), round(POTLmonsample[0],4)) 
        self.assertEqual(round(result[1],4), round(POTLmonsample[1],4)) 
        self.assertEqual(round(result[2],4), round(POTLmonsample[2],4)) 
        self.assertEqual(round(result[3],4), round(POTLmonsample[3],4)) 

if __name__ == '__main__':
    unittest.main()