import unittest
import numpy as np
import matplotlib.pyplot as plt

def decluster(sample, threshold, block_size): #function to decluster the dataset toward period blocks 
    period_unit = np.arange(1, len(sample)+1, 1) #period array
    threshold_array = np.ones(len(sample))*threshold 
    nob = int(len(sample)/block_size) #number of blocks
    clust = np.zeros((nob, block_size)) #initialization of the cluster matrix (rows: cluster; columns: observations)
    #Algorithm to cluster 
    k = 0
    for i in range(0, nob):
        for j in range(0, block_size):
            clust[i][j] = sample[j+k]
        k = j + k + 1

    block_max = np.amax(clust, 1) #getting max of each block and declustering 

    period_unit_block = np.arange(0, len(block_max), 1) #array of period for each block
    threshold_block_array = np.ones(len(block_max))*threshold 
    
    #Plot real dataset
    plt.figure(11)
    plt.scatter(period_unit, sample)
    plt.plot(period_unit, threshold_array, label = 'Threshold', color = 'red')
    plt.legend()
    plt.xlabel('Period Unit')
    plt.ylabel('Data')
    plt.title('Sample dataset per Period Unit')
    
    #Plot declustered data
    plt.figure(12)
    plt.scatter(period_unit_block, block_max)
    plt.plot(period_unit_block, threshold_block_array, label = 'Threshold', color = 'red')
    plt.legend()
    plt.xlabel('Period Unit')
    plt.ylabel('Declustered Data')
    plt.title('Declustered dataset per Period Unit')    
    plt.show()

    return(block_max)

class TestFun(unittest.TestCase):
    def test_declustering(self):
        """
        Testing if the function will return exactly the points it should
        """
        data = [1, 1.5, 1.2, 4, 4.5, 4.2, 8, 8.5, 8.2, 12, 12.5, 12.2]
        #The code will cluster the data intro four blocks with size 3 and take the maximum from each one
        # From data, we can say that the resulting array will be [1.5, 4.5, 8.5, 12.5]
        result = decluster(data, 0, 3)
        resultreal = np.array([1.5, 4.5, 8.5, 12.5])
        for i in range(len(result)):
            self.assertEqual(result[i], resultreal[i]) 

      
if __name__ == '__main__':
    unittest.main()

