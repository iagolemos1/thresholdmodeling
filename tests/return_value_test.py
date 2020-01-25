#Getting main packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns; sns.set(style = 'whitegrid')
from scipy.stats import genpareto
import pandas as pd
import math as mt
import scipy.special as sm

#Getting main packages from R in order to apply the maximum likelihood function
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import FloatVector

POT = importr('POT') #importing POT package
import unittest


url = 'https://raw.githubusercontent.com/iagolemos1/thresholdmodeling/master/dataset/rain.csv'
df =  pd.read_csv(url, error_bad_lines=False)
data = df.values.ravel()

def return_value(sample_real, threshold, alpha, block_size, return_period, fit_method): #return value plot and return value estimative
    sample = np.sort(sample_real) 
    sample_excess = []
    sample_over_thresh = []
    for data in sample:
        if data > threshold+0.00001:
            sample_excess.append(data - threshold)
            sample_over_thresh.append(data)

    rdata = FloatVector(sample)
    fit = POT.fitgpd(rdata, threshold, est = fit_method) #fit data 
    shape = fit[0][1]  
    scale = fit[0][0]
    
    #Computing the return value for a given return period with the confidence interval estimated by the Delta Method
    m = return_period
    Eu = len(sample_over_thresh)/len(sample)
    x_m = threshold + (scale/shape)*(((m*Eu)**shape) - 1)

    #Solving the delta method    
    d = Eu*(1-Eu)/len(sample)
    e = fit[3][0]
    f = fit[3][1]
    g = fit[3][2]
    h = fit[3][3]
    a = (scale*(m**shape))*(Eu**(shape-1))
    b = (shape**-1)*(((m*Eu)**shape) - 1)
    c = (-scale*(shape**-2))*((m*Eu)**shape - 1) + (scale*(shape**-1))*((m*Eu)**shape)*mt.log(m*Eu)
    CI = (norm.ppf(1-(alpha/2))*((((a**2)*d) + (b*((c*g) + (e*b))) + (c*((b*f) + (c*h))))**0.5))

    print('The return value for the given return period is {} \u00B1 {}'.format(x_m, CI))

        
    ny = block_size #defining how much observations will be a block (usually anual) 
    N_year = return_period/block_size #N_year represents the number of years based on the given return_period

    for i in range(0, len(sample)):
        if sample[i] > threshold + 0.0001:
            i_initial = i 
            break

    p = np.arange(i_initial,len(sample))/(len(sample)) #Getting Plotting Position points
    N = 1/(ny*(1 - p))  #transforming plotting position points to years

    year_array = np.arange(min(N), N_year+0.1, 0.1) #defining a year array 
    
    #Algorithm to compute the return value and the confidence intervals for plotting
    z_N = []
    CI_z_N_high_year = []
    CI_z_N_low_year = [] 
    for year in year_array:
        z_N.append(threshold + (scale/shape)*(((year*ny*Eu)**shape) - 1))
        a = (scale*((year*ny)**shape))*(Eu**(shape-1))
        b = (shape**-1)*((((year*ny)*Eu)**shape) - 1)
        c = (-scale*(shape**-2))*(((year*ny)*Eu)**shape - 1) + (scale*(shape**-1))*(((year*ny)*Eu)**shape)*mt.log((year*ny)*Eu)
        CIyear = (norm.ppf(1-(alpha/2))*((((a**2)*d) + (b*((c*g) + (e*b))) + (c*((b*f) + (c*h))))**0.5))
        CI_z_N_high_year.append(threshold + (scale/shape)*(((year*ny*Eu)**shape) - 1) + CIyear)
        CI_z_N_low_year.append(threshold + (scale/shape)*(((year*ny*Eu)**shape) - 1) - CIyear)
    
    #Plotting Return Value
    plt.figure(8)
    plt.plot(year_array, CI_z_N_high_year, linestyle='--', color='red', alpha = 0.8, lw = 0.9, label = 'Confidence Bands')
    plt.plot(year_array, CI_z_N_low_year, linestyle='--', color='red', alpha = 0.8, lw = 0.9)
    plt.plot(year_array, z_N, color = 'black', label = 'Theoretical Return Level')
    plt.scatter(N, sample_over_thresh, label = 'Empirical Return Level')
    plt.xscale('log')
    plt.xlabel('Return Period')
    plt.ylabel('Return Level')
    plt.title('Return Level Plot')
    plt.legend()
    plt.show()
    return (x_m, CI)

class TestFun(unittest.TestCase):
    def test_return_value(self):
        """
        Testing the return value and its confidence interval based on the values presented by Coles
        """
        data = df.values.ravel()
        result = return_value(data, 30, 0.05, 365, 36500, 'mle')
        #testing return value
        self.assertEqual(round(result[0],1), 106.3) #value took from Coles's book
        #testing confidence interval
        self.assertEqual(round(result[1],1), 40.8) #value took from Coles's book

if __name__ == '__main__':
    unittest.main()