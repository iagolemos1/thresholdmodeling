# Functions Documentations

This file presents a documentation of the functions presented in the ``thresholdmodeling``package. 

## Threshold Selection
* **``MRL(sample, alpha)``** : It plots the Mean Residual Life function. ``Sample`` is a 1-D array of the observations and ``alpha`` is a float number representing the confidence level.   
* **``Parameter_Stability_Plot(sample, alpha)``** : It plots the two graphics related to the shape and the modified scale parameters stability plot.``Sample`` is a 1-D array of the observations and ``alpha`` is a float number representing the confidence level. 

## Model Fit
* **``gpdfit(sample, threshold, fit_method)``** : This function fits the given data to a GPD model and show the GPD estimatives in the terminal. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold and ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' for the maximum likelihood, maximum penalized likelihood, moments, unbiased probability weighted moments, biased probability weigthed moments, minimum density power divergence, medians, Pickands’ likelihood moment and maximum goodness-of-fit estimators respectively.

## Model Checking
* **``gpdpdf(sample, threshold, fit_method, bin_method, alpha)``**  : This function returns the GPD probability density function plot with the normalized empirical histograms. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold, ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**), ``bin_mehotd`` is one of the following methods to compute the number of bins of a histogram: 'sturges', 'doane', 'scott', 'fd' (Freedman-Diaconis estimator), 'stone', 'rice' and 'sqrt', and ``alpha`` is the confidence level.

* **``gpdcdf(sample, threshold, fit_method, alpha)``**  : This function returns the GPD comulative distribution function plot with the empirical points and the confidence bands based on the Dvoretzky–Kiefer–Wolfowitz method. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold, ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**), and ``alpha`` is the confidence level.

* **``qqplot(sample, threshold, fit_method, alpha)``**  : This function returns the quantile-quantile plot with the confidence bands based on the Kolmogorov-Smirnov two sample test. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold, ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**), and ``alpha`` is the confidence level.

* **``ppplot(sample, threshold, fit_method, alpha)``**  : This function returns the probability-probability plot with the confidence bands based on the Dvoretzky–Kiefer–Wolfowitz method. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold, ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**), and ``alpha`` is the confidence level.

* **``survival_function(sample, threshold, fit_method, alpha)``**  : This function returns the survival function plot (1-CDF) with empirical points and the confidence bands based on the Dvoretzky–Kiefer–Wolfowitz method. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold, ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**), and ``alpha`` is the confidence level.

* **``lmomplot(sample, threshold)``**  : This function returns the L-Skewness against L-Kurtosis plot using the Generalized Pareto normalization. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold. **Warning**: This plot is very difficult to interpret. 

## Model Diagnostics and Return Level Analysis
* **``return_value(sample, threshold, alpha, block_size, return_period, fit_method)``** : This function returns the return level for the given argument ``return_period`` with confidence interval based on the Delta Method. Also, it will draw the return level plot based on the block size (usualy annual) with confidence bands based on the Delta Method and empirical points. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold, ``alpha`` is the confidence level, 'block_size' is represents the number of observations will be a block, for example, if the interest is to conduct an annual analysis, the ``block_size`` should be represent a year, in other words, if the data is daily, ``block_size`` should be 365, ``return_period`` is the exact return period you want to compute the return level and ``fit_mehotd``  is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**).

## Declustering and Data Visualization

* **``decluster(sample, threshold, block_size)``** : This function returns two graphics: The data against the unit of return period (days, for example), and the declustered data based on the block size and the maximum of each block. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold and ``block_size`` is the number of observations that will be part of a cluster, for example: if the dataset is daily and the idea is to cluster based on months, ``block_size`` should be 30. 

## Further Functions for Additional Analysis

* **``non_central_moments(sample, threshold, fit_method)``** : This function returns the non-central moments estimated from the model.
``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold and ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**).

* **``lmom_dist(sample, threshold, fit_method)``** : This function returns the L-moments estimated from the model.
``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold and ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**).

* **``lmom_sample(sample)``** : This function returns the L-moments estimated from the sample. ``Sample`` is a 1-D array of the observations.

* **``entropy(sample, b, threshold, fit_method)``** : This function returns the differential entropy of the model in nats. ``Sample`` is a 1-D array of the observations, ``b`` must be equal to 'e' (changing it does not take any difference in the result, it is just to ilustrate the Euler's number), ``threshold`` is the chosen threshold and ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**).

