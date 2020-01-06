# Functions Documentations

This file presents a documentation of the functions presented in the ``thresholdmodeling``package. 

## Threshold Selection
* **``MRL(sample, alpha)``** : It plots the Mean Residual Life function. ``Sample`` is a 1-D array of the observations and ``alpha`` is a float number representing the confidence level.   
* **``Parameter_Stability_Plot(sample, alpha)``** : It plots the two graphics related to the shape and the modified scale parameters stability plot.``Sample`` is a 1-D array of the observations and ``alpha`` is a float number representing the confidence level. 

## Model Fit
* **``gpdfit(sample, threshold, fit_method)``** : This function fits the given data to a GPD model. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold and ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' for the maximum likelihood, maximum penalized likelihood, moments, unbiased probability weighted moments, biased probability weigthed moments, minimum density power divergence, medians, Pickands’ likelihood moment and maximum goodness-of-fit estimators respectively.

## Model Checking
* **``gpdpdf(sample, threshold, fit_method, bin_method, alpha)``**  : This function returns the GPD probability density function plot with the normalized empirical histograms. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold, ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**), ``bin_mehotd`` is one of the following methods to compute the number of bins of a histogram: 'sturges', 'doane', 'scott', 'fd' (Freedman-Diaconis estimator), 'stone', 'rice' and 'sqrt', and ``alpha`` is the confidence level.

* **``gpdcdf(sample, threshold, fit_method, alpha)``**  : This function returns the GPD comulative distribution function plot with the empirical points and the confidence bands based on the Dvoretzky–Kiefer–Wolfowitz method. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold, ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**), and ``alpha`` is the confidence level.

* **``qqplot(sample, threshold, fit_method, alpha)``**  : This function returns the quantile-quantile plot with the confidence bands based on the Kolmogorov-Smirnov two sample test. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold, ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**), and ``alpha`` is the confidence level.

* **``ppplot(sample, threshold, fit_method, alpha)``**  : This function returns the probability-probability plot with the confidence bands based on the Dvoretzky–Kiefer–Wolfowitz method. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold, ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**), and ``alpha`` is the confidence level.

* **``survival_function(sample, threshold, fit_method, alpha)``**  : This function returns the survival function plot (1-CDF) with empirical points and the confidence bands based on the Dvoretzky–Kiefer–Wolfowitz method. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold, ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' (for more information see **Model Fit**), and ``alpha`` is the confidence level.

* **``lmomplot(sample, threshold)``**  : This function returns the L-Skewness against L-Kurtosis plot using the Generalized Pareto normalization. ``Sample`` is a 1-D array of the observations, ``threshold`` is the chosen threshold. **Warning**: This plot is very difficult to interpret. 




