import unittest

def lmom_dist(shape, scale, threshold):
    #The package function was changed a little just to input given parameters and to don't estimate them from a sample
    #The math is exactly the same.
    t_1 = threshold + scale*(1+shape)
    t_2 = scale/((1+shape)*(2+shape))
    t_3 = (1 - shape)/(3 + shape)
    t_4 = ((1 - shape)*(2 - shape))/((3 + shape)*(4 + shape))
    return (t_1, t_2, t_3, t_4)

class TestFun(unittest.TestCase):
    def test_lmom_dist(self):
        """
        Testing if the function will return the right moments for the given parameters:
        Shape = 1
        Scale = 1
        Threshold = 1 
        """
        result = lmom_dist(1, 1, 1)
        #testing
        self.assertEqual(result[0], 3)
        self.assertEqual(round(result[1],4), 0.1667) 
        self.assertEqual(result[2], 0) 
        self.assertEqual(result[3], 0)  
        

if __name__ == '__main__':
    unittest.main()

