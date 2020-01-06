# Functions Documentations

This file presents a documentation of the functions presented in the ``thresholdmodeling``package. 

## Threshold Selection
* **``MRL(sample, alpha)``** : It plots the Mean Residual Life function, as it is defined in [@coles]. ``Sample`` is a 1-D array of the observations and ``alpha`` is a float number representing the confidence level.   
* **``Parameter_Stability_Plot(sample, alpha)``** : It plots the two graphics related to the shape and the modified scale parameters stability plot, as they are defined in [@coles].``Sample`` is a 1-D array of the observations and ``alpha`` is a float number representing the confidence level. 

## Model Fit
* **``gpdfit(sample, threshold, fit_method)``** : This function fits the given data to a GPD model. ``Sample`` is a 1-D array of the observations and ``threshold`` is the chosen threshold and ``fit_method`` is one of the following fit methods (string format): 'mle', 'mple', 'moments', 'pwmu', 'pwmb', 'mdpd', 'med', 'pickands', 'lme' and 'mgf' for the maximum likelihood, maximum penalized likelihood, moments, unbiased probability weighted moments, biased probability weigthed moments, minimum density power divergence, medians, Pickands’ likelihood moment and maximum goodness-of-fit estimators respectively.
