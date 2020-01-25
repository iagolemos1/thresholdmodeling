#########################################################################
#Copyright (c) 2019 Iago Pereira Lemos 

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>

##########################################################################

#Two functions for getting the plots for defining the threshold
#in order to model a Generalized Pareto Distribution. 
# 
#MRL Function plots the Mean Residual Life function.
#The Parameter_Stability_plot plots the shape and the modified scale 
#parameters against the threshold values, u.
#
#For both functions it needed the sample array and the significance level. 


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
from rpy2.robjects.packages import importr
import rpy2.robjects.packages as rpackages

base = importr('base')
utils = importr('utils')
utils.chooseCRANmirror(ind=1)
utils.install_packages('POT') #installing POT package

POT = importr('POT') #importing POT package

def MRL(sample, alpha): #MRL function

    #Defining the threshold array and its step
    step = np.quantile(sample, .995)/60
    threshold = np.arange(0, max(sample), step=step) 
    z_inverse = norm.ppf(1-(alpha/2))

    #Initialization of arrays
    mrl_array = [] #mean of excesses intialization
    CImrl = [] #confidence interval for the excesses initialization

    #First Loop for getting the mean residual life for each threshold value and the 
    #second one getting the confidence intervals for the plot
    for u in threshold:
        excess = [] #initialization of the excesses array for each loop
        for data in sample:
            if data > u:
                excess.append(data - u) #adding excesses to the excesses array
        mrl_array.append(np.mean(excess)) #adding the mean of the excesses in the mean excesses array
        std_loop = np.std(excess) #getting standard deviation in the loop
        CImrl.append(z_inverse*std_loop/(len(excess)**0.5)) #getting confidence interval 

    CI_Low = [] #initialization of the low confidence interval array
    CI_High = [] #initialization of the high confidence interval array

    #Loop to add in the confidence interval to the plot arrays
    for i in range(0, len(mrl_array)):
        CI_Low.append(mrl_array[i] - CImrl[i])
        CI_High.append(mrl_array[i] + CImrl[i])

    #Plot MRL
    plt.figure(1)
    sns.lineplot(x = threshold, y = mrl_array)
    plt.fill_between(threshold, CI_Low, CI_High, alpha = 0.4)
    plt.xlabel('u')
    plt.ylabel('Mean Excesses')
    plt.title('Mean Residual Life Plot')
    plt.show()

def Parameter_Stability_plot(sample, alpha): #Parameter stability plot function
    #Defining Threshold array
    step = np.quantile(sample, .995)/45
    threshold = np.arange(0, np.quantile(sample, .999), step = step)

    #Transforming sample in a R array
    rdata = FloatVector(sample)

    #Initialization of some main arrays
    stdshape = [] #standard deviation of the shape parameter initialization
    shape = []  #shape parameter intialization 
    scale = []  #scale paramter initilization 
    mod_scale = [] #modified scale parameter initizaliation 
    CI_shape = [] #confidence interval of the shape parameter
    CI_mod_scale = [] #confidence interval of the modified scale
    z = norm.ppf(1-(alpha/2)) 

    #Getting parameters and CI's for both plots
    for u in threshold:
        fit = POT.fitgpd(rdata, u, est = 'mle')  #fitting distribution using POT package with the MLE method 
        shape.append(fit[0][1]) #adding the shape parameter to the respective array
        scale.append(fit[0][0]) #adding the scale parameter to the respective array
        stdshape.append(fit[1][1]) #adding the shape standard deviation to the respective array
        CI_shape.append(fit[1][1]*z) #getting the values of the confidence interval for plotting
        mod_scale.append(fit[0][0] - (fit[0][1]*u)) #getting the modified scale parameter 
        Var_mod_scale = (fit[3][0] - (u*fit[3][2]) - u*(fit[3][1] - (fit[3][3]*u))) #solving the Delta method 
        #in order to get the variance to the modified scale parameter 
        CI_mod_scale.append((Var_mod_scale**0.5)*z) #getting the confidence interval for the
        #modified scale parameter

    #Plotting shape parameter against u vales   
    plt.figure(2)    
    plt.errorbar(threshold, shape, yerr = CI_shape, fmt = 'o' )
    plt.xlabel('u')
    plt.ylabel('Shape Parameter')
    plt.title('Shape Parameter Stability Plot')

    #Plotting modified scale parameter against u values
    plt.figure(3)
    plt.errorbar(threshold, mod_scale, yerr = CI_mod_scale, fmt = 'o')
    plt.xlabel('u')
    plt.ylabel('Modified Scale Parameter')
    plt.title('Modified Scale Parameter Stability Plot')

    plt.show()

def gpdfit(sample, threshold, fit_method):
    sample = np.sort(sample)  
    sample_excess = []
    sample_over_thresh = []
    for data in sample:
        if data > threshold+0.00001:
            sample_excess.append(data - threshold) #getting an excesses array
            sample_over_thresh.append(data) #getting an array with values over the threshold
    rdata = FloatVector(sample)
    fit = POT.fitgpd(rdata, threshold, est = fit_method) #fit the data to the distribution
    shape = fit[0][1]  
    scale = fit[0][0]
    print(fit) #show gpd fit estimatives  

    return(shape, scale, sample, sample_excess, sample_over_thresh)

def gpdpdf(sample, threshold, fit_method, bin_method, alpha): #get PDF plot with histogram to diagnostic the model
    [shape, scale, sample, sample_excess, sample_over_thresh] = gpdfit(sample, threshold, fit_method) #Fit the data
    x_points = np.arange(0, max(sample), 0.001) #define a range of points for drawing the pdf
    pdf = genpareto.pdf(x_points, shape, loc=0, scale=scale)  #get the pdf values 

    #Plotting PDF
    plt.figure(4)
    plt.xlabel('Data')
    plt.ylabel('PDF')
    plt.title('Data Probability Density Function')
    plt.plot(x_points, pdf, color = 'black', label = 'Theoretical PDF')
    plt.hist(sample_excess, bins = bin_method, density = True) #draw histograms    
    plt.legend()
    plt.show()
    
def qqplot(sample, threshold, fit_method, alpha): #get Quantile-Quantile plot to diagnostic the model
    [shape, scale, sample, sample_excess, sample_over_thresh] = gpdfit(sample, threshold, fit_method) #fit data   
    i_initial = 0
    p = []
    n = len(sample)
    sample = np.sort(sample)
    for i in range(0, n):
        if sample[i] > threshold + 0.0001:
            i_initial = i #get the index of the first observation over the threshold
            k = i - 1
            break

    for i in range(i_initial, n):
        p.append((i - 0.35)/(n)) #using the index, compute the empirical probabilities by the Hosking Plotting Poistion Estimator.

    p0 = (k - 0.35)/(n)    

    quantiles = []
    for pth in p:
       quantiles.append(threshold + ((scale/shape)*(((1-((pth-p0)/(1-p0)))**-shape) - 1))) #getting theorecial quantiles arrays

    n = len(sample_over_thresh)
    y = np.arange(1,n+1)/n #getting empirical quantiles

    #Kolmogorov-Smirnov Test for getting the confidence interval
    K = (-0.5*mt.log(alpha/2))**0.5
    M = (len(p)**2/(2*len(p)))**0.5
    CI_qq_high = []
    CI_qq_low = []
    for prob in y:
        F1 = prob - K/M
        F2 = prob + K/M
        CI_qq_low.append(threshold + ((scale/shape)*(((1-((F1)/(1)))**-shape) - 1)))
        CI_qq_high.append(threshold + ((scale/shape)*(((1-((F2)/(1)))**-shape) - 1)))

    #Plotting QQ
    plt.figure(5)
    sns.regplot(quantiles, sample_over_thresh, ci = None, line_kws={'color':'black','label':'Regression Line'})
    plt.axis('square')
    plt.plot(sample_over_thresh, CI_qq_low, linestyle='--', color='red', alpha = 0.5, lw = 0.8, label = 'Kolmogorov-Smirnov Confidence Bands')
    plt.legend()
    plt.plot(sample_over_thresh, CI_qq_high, linestyle='--', color='red', alpha = 0.5, lw = 0.8)
    plt.xlabel('Theoretical GPD Quantiles')
    plt.ylabel('Sample Quantiles')
    plt.title('Q-Q Plot')
    plt.show()

def ppplot(sample, threshold, fit_method, alpha):  #probability-probability plot to diagnostic the model
    [shape, scale, sample, sample_excess, sample_over_thresh] = gpdfit(sample, threshold, fit_method) #fit the data
    n = len(sample_over_thresh)
    #Getting empirical probabilities
    y = np.arange(1,n+1)/n 
    #Getting theoretical probabilities 
    cdf_pp = genpareto.cdf(sample_over_thresh, shape, loc=threshold, scale=scale)
    
    #Getting Confidence Intervals using the Dvoretzky–Kiefer–Wolfowitz method
    i_initial = 0
    n = len(sample)
    for i in range(0, n):
        if sample[i] > threshold + 0.0001:
            i_initial = i
            break
    F1 = []
    F2 = []
    for i in range(i_initial,len(sample)):
        e = (((mt.log(2/alpha))/(2*len(sample_over_thresh)))**0.5)  
        F1.append(y[i-i_initial] - e)
        F2.append(y[i-i_initial] + e)

    #Plotting PP
    plt.figure(6)
    sns.regplot(y, cdf_pp, ci = None, line_kws={'color':'black', 'label':'Regression Line'})
    plt.plot(y, F1, linestyle='--', color='red', alpha = 0.5, lw = 0.8, label = 'Dvoretzky–Kiefer–Wolfowitz Confidence Bands')
    plt.plot(y, F2, linestyle='--', color='red', alpha = 0.5, lw = 0.8)
    plt.legend()
    plt.title('P-P Plot')
    plt.xlabel('Empirical Probability')
    plt.ylabel('Theoritical Probability')
    plt.show()

def gpdcdf(sample, threshold, fit_method, alpha): #plot gpd cdf with empirical points
    [shape, scale, sample, sample_excess, sample_over_thresh] = gpdfit(sample, threshold, fit_method) #fit the data

    n = len(sample_over_thresh)
    y = np.arange(1,n+1)/n #empirical probabilities

    i_initial = 0
    n = len(sample)
    for i in range(0, n):
        if sample[i] > threshold + 0.0001:
            i_initial = i 
            break
    
    #Computing confidence interval with the Dvoretzky–Kiefer–Wolfowitz method based on the empirical points
    F1 = []
    F2 = []
    for i in range(i_initial,len(sample)):
        e = (((mt.log(2/alpha))/(2*len(sample_over_thresh)))**0.5)  
        F1.append(y[i-i_initial] - e)
        F2.append(y[i-i_initial] + e)  

    x_points = np.arange(0, max(sample), 0.001) #generating points to apply in the cdf
    cdf = genpareto.cdf(x_points, shape, loc=threshold, scale=scale) #getting theoretical cdf
    
    #Plotting cdf 
    plt.figure(7)
    plt.plot(x_points, cdf, color = 'black', label='Theoretical CDF')
    plt.xlabel('Data')
    plt.ylabel('CDF')
    plt.title('Data Comulative Distribution Function')
    plt.scatter(sorted(sample_over_thresh), y, label='Empirical CDF')
    plt.plot(sorted(sample_over_thresh), F1, linestyle='--', color='red', alpha = 0.8, lw = 0.9, label = 'Dvoretzky–Kiefer–Wolfowitz Confidence Bands')
    plt.plot(sorted(sample_over_thresh), F2, linestyle='--', color='red', alpha = 0.8, lw = 0.9)
    plt.legend()
    plt.show()

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

def survival_function(sample, threshold, fit_method, alpha): #Plot the survival function, (1 - cdf)
    [shape, scale, sample, sample_excess, sample_over_thresh] = gpdfit(sample, threshold, fit_method)

    n = len(sample_over_thresh)
    y_surv = 1 - np.arange(1,n+1)/n

    i_initial = 0

    n = len(sample)
    for i in range(0, n):
        if sample[i] > threshold + 0.0001:
            i_initial = i 
            break
    #Computing confidence interval with the Dvoretzky–Kiefer–Wolfowitz
    F1 = []
    F2 = []
    for i in range(i_initial,len(sample)):
        e =  (((mt.log(2/alpha))/(2*len(sample_over_thresh)))**0.5)  
        F1.append(y_surv[i-i_initial] - e)
        F2.append(y_surv[i-i_initial] + e)  

    x_points = np.arange(0, max(sample), 0.001)
    surv_func = 1 - genpareto.cdf(x_points, shape, loc=threshold, scale=scale)

    #Plotting survival function
    plt.figure(9)
    plt.plot(x_points, surv_func, color = 'black', label='Theoretical Survival Function')
    plt.xlabel('Data')
    plt.ylabel('Survival Function')
    plt.title('Data Survival Function Plot')
    plt.scatter(sorted(sample_over_thresh), y_surv, label='Empirical Survival Function')
    plt.plot(sorted(sample_over_thresh), F1, linestyle='--', color='red', alpha = 0.8, lw = 0.9, label = 'Dvoretzky–Kiefer–Wolfowitz Confidence Bands')
    plt.plot(sorted(sample_over_thresh), F2, linestyle='--', color='red', alpha = 0.8, lw = 0.9)
    plt.legend()
    plt.show()

def non_central_moments(sample, threshold, fit_method): #Getting non-central moments using the genpareto package
    [shape, scale, sample, sample_excess, sample_over_thresh] = gpdfit(sample, threshold, fit_method)
    [Mean, Variance, Skewness, Kurtosis]= genpareto.stats(shape, threshold, scale, moments = 'mvsk')
    print('Non-Central Moments estimated from the distribution:\nMean: {} \nVariance: {} \nSkewness: {} \nKurtosis: {} \n'.format(Mean, Variance, Skewness, Kurtosis))
    return (Mean, Variance, Skewness, Kurtosis)

def lmom_dist(sample, threshold, fit_method): #Getting the l-moments from the distribution
    [shape, scale, sample, sample_excess, sample_over_thresh] = gpdfit(sample, threshold, fit_method)
    t_1 = threshold + scale*(1+shape)
    t_2 = scale/((1+shape)*(2+shape))
    t_3 = (1 - shape)/(3 + shape)
    t_4 = ((1 - shape)*(2 - shape))/((3 + shape)*(4 + shape))
    print('L-Moments estimated from the distribution:\nL-Mean: {} \nL-Variance: {} \nL-Skewness: {} \nL-Kurtosis: {} \n'.format(t_1, t_2, t_3, t_4))
    return (t_1, t_2, t_3, t_4)

def lmom_sample(sample): #Algorithm to compute the fourth l-moments from the sample
    sample = np.sort(sample)
    n = len(sample)

    #first moment
    l1 = np.sum(sample) / sm.comb(n, 1, exact=True)
    
    #second moment
    comb1 = range(n)
    coefl2 = 0.5 / sm.comb(n, 2, exact=True)
    sum_xtrans = sum([(comb1[i] - comb1[n - i - 1]) * sample[i] for i in range(n)])
    l2 = coefl2 * sum_xtrans
    
    #third moment
    comb3 = [sm.comb(i, 2, exact=True) for i in range(n)]
    coefl3 = 1.0 / 3.0 / sm.comb(n, 3, exact=True)
    sum_xtrans = sum([(comb3[i] - 2 * comb1[i] * comb1[n - i - 1] + comb3[n - i - 1]) * sample[i] for i in range(n)])
    l3 = coefl3 * sum_xtrans / l2
    
    #fourth moment
    comb5 = [sm.comb(i, 3, exact=True) for i in range(n)]
    coefl4 = 0.25 / sm.comb(n, 4, exact=True)
    sum_xtrans = sum(
        [(comb5[i] - 3 * comb3[i] * comb1[n - i - 1] + 3 * comb1[i] * comb3[n - i - 1] - comb5[n - i - 1]) * sample[i]
         for i in range(n)])
    l4 = coefl4 * sum_xtrans / l2

    print('L-Moments estimated from the sample:\nL-Mean: {} \nL-Variance: {} \nL-Skewness: {} \nL-Kurtosis: {} \n'.format(l1, l2, l3, l4))
    
    return(l1, l2, l3, l4)

def lmomplot(sample, threshold): #Plotting the l-skewnes and l-kurtosis empirical against theoretical to 
#diagnostic the u choice. 
    def lmom_sample2(sample): 
        sample = np.sort(sample)
        n = len(sample)

        #first moment
        l1 = np.sum(sample) / sm.comb(n, 1, exact=True)
    
        #second moment
        comb1 = range(n)
        coefl2 = 0.5 / sm.comb(n, 2, exact=True)
        sum_xtrans = sum([(comb1[i] - comb1[n - i - 1]) * sample[i] for i in range(n)])
        l2 = coefl2 * sum_xtrans
    
        #third moment
        comb3 = [sm.comb(i, 2, exact=True) for i in range(n)]
        coefl3 = 1.0 / 3.0 / sm.comb(n, 3, exact=True)
        sum_xtrans = sum([(comb3[i] - 2 * comb1[i] * comb1[n - i - 1] + comb3[n - i - 1]) * sample[i] for i in range(n)])
        l3 = coefl3 * sum_xtrans / l2
    
        #fourth moment
        comb5 = [sm.comb(i, 3, exact=True) for i in range(n)]
        coefl4 = 0.25 / sm.comb(n, 4, exact=True)
        sum_xtrans = sum(
            [(comb5[i] - 3 * comb3[i] * comb1[n - i - 1] + 3 * comb1[i] * comb3[n - i - 1] - comb5[n - i - 1]) * sample[i]
             for i in range(n)])
        l4 = coefl4 * sum_xtrans / l2
        return(l1, l2, l3, l4)

    threshold_array = np.arange(0, threshold + (threshold/3), 0.5) #defining a threshold array to compute the 
    #different l-moments from the sample
    sample = np.sort(sample)
    skewness_sample = []
    kurtosis_sample =[]
    #Algorithm to compute the l-moments for each threshold
    for u in threshold_array:
        sample_over_thresh = []
        for data in sample:
            if data > u+0.00001:
                sample_over_thresh.append(data)
        [l1, l2, l3, l4] = lmom_sample2(sample_over_thresh)
        skewness_sample.append(l3)
        kurtosis_sample.append(l4)

    skewness_theo = np.arange(0,1+0.1,0.1) #defining theoretical l-skewness
    kurtosis_theo = (skewness_theo*(1 + 5*skewness_theo))/(5 + skewness_theo) #theoretical kurtosis of the gpd  
    
    #Plotting l-moments
    plt.figure(10)
    plt.scatter(skewness_sample, kurtosis_sample, label = 'Empirical')
    plt.plot(skewness_theo, kurtosis_theo, color = 'black', label = 'Theoretical')
    plt.legend()
    plt.xlabel('L-Skewness')
    plt.ylabel('L-Kurtosis')
    plt.title('L-Moments Plot')
    plt.show()
    
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

def entropy(sample, b, threshold, fit_method): #Get the entropy of the distribution
    [shape, scale, sample, sample_excess, sample_over_thresh] = gpdfit(sample, threshold, fit_method)
    h = mt.log(scale) + shape + 1              
    print('The differential entropy is {} nats.'.format(h))

