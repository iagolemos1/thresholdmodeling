---
title: 'thresholdmodeling: A Python package for modeling excesses over a threshold using the Peak-Over-Threshold Method and the Generalized Pareto Distribution'
tags:
  - Python
  - Threshold Models
  - Peak-Over-Threshold Method
  - Generalized Pareto Distribution
  - Estatistical Modeling
authors:
  - name: Iago Pereira Lemos
    orcid: 0000-0002-5829-7711
    affiliation: "1, 2, 3"
    
  - name: Antônio Marcos Gonçalves Lima
    orcid: 0000-0003-0170-6083
    affiliation: "4, 2, 3"
    
  - name: Marcus Antônio Viana Duarte
    orcid: 0000-0002-8166-5666
    affiliation: "4, 1, 2, 3"
affiliations:
 - name: Acoustics and Vibration Laboratory
   index: 1
 - name: School of Mechanical Engineering
   index: 2
 - name: Federal University of Uberlândia
   index: 3
 - name: Associate Professor
   index: 4

date: 06 January, 2020
bibliography: paper.bib
---

# Summary

Extreme value analysis has been emerged as one of the most important disciplines
for the applied sciences when dealing with reduced datasets and when the main idea is to
extrapolate the observations over a given time. By using a threshold model with an asymptotic characterization, it is posible to work with the Generalized Pareto Distribution (GPD) [@coles] and use it to model the stochastic behavior of a process at an unusual level, which can be of maximum or minimum. For example, suppose that it is available a large dataset of wind velocity in Florida, USA, during a given time period. It is possible to model this process and to quantify the probability of having extreme events, like hurricanes, which are maximums observations of wind velocity, in a given time period of interest using the return value analysis tool.

In this context, this package provides a complete toolkit to conduct a threshold model analysis, from the beginning phase of selecting the threshold, going through the model fit, model checking and return value analysis. Moreover, statistical moments functions are provided. In case of extremes of dependences sequences it is also possible to conduct a declustering analysis.   

Into a software context, it is possible to see a strong community working with ``R`` packages like ``POT`` [@POT],``evd`` [@evd] and ``extRemes`` [@extremes], that are used for a complete extreme value modeling. 
Otherwise, in ``Python``, it is possible to find the ``scikit-extremes`` [@kiko], which does not contain the threshold models yet. In addition, another package is ``scipy``, with the ``genpareto`` [@scipy] functions, which also does not provide any Peak-Over-Threshold modeling functions since it is not possible to define a threshold using this package. Moreover, this package allows the community of scientists, engineers and any other interested person and programmer the possibility to conduct an extreme value analysis using a strong, consolidated and high-level programming language given the importance of the extreme value theory approach for statistical analysis in corrosion engineering [see @scarf; and @tan], hydrology [see @katz], enviromental data analysis [see @max; and @esther] and many other fields of natural sciences and engineering [for a massive number of other applications see @coles p. 1] 

Hence, the ``thresholdmodeling`` package presents numerous functions to model the stochastic behavior of an extreme process. For a complete introduction of the complete fifteen package functions it is crucial to go to the [Functions Documentation](https://github.com/iagolemos1/thresholdmodeling/blob/master/Functions%20Documentation.md), on the [GitHub page](https://github.com/iagolemos1/thresholdmodeling). 

# Package Features

## Threshold Selection
* **Mean Residual Life Plot** : It is possible to plot the Mean Residual Life function, as it is defined in @coles;

* **Parameter Stability Plot** : Also, it is possible to obtain the two parameter stability plots of the GPD: the Shape Parameter Stability Plot and the Modified Scale Parameter Stability Plot, which is defined from a reparametrization of the GPD scale parameter [see @coles from a complete theoretical introduction about these two plots].

## Model Fit
* **Fit the GPD Model** : Fitting a given dataset to a GPD model using some methods (see [**Model Fit**](https://github.com/iagolemos1/thresholdmodeling/blob/master/Functions%20Documentation.md#model-fit)).

## Model Checking
* **Probability Density Function, Cumulative Distribution Function, Quantile-Quantile and Probability-Probability Plots** : Plots the theoretical probability density function with the normalized empirical histograms for a given dataset, using some bin methods (see [``gpdpdf``](https://github.com/iagolemos1/thresholdmodeling/blob/master/Functions%20Documentation.md#model-fit)).
Also, the theoretical CDF in comparison to the empirical one with the Dvoretzky–Kiefer–Wolfowitz confidence bands can be drawn. 
In addition, The QQ and PP plots, comparing the sample and the theoretical values can be obtained, where the first one uses the Kolmogorov-Smirnov Two Sample Test for getting the confidence bands while the second one uses the Dvoretzky–Kiefer–Wolfowitz method;

* **L-Moments Plots** : L-Skewness against L-Kurtosis plot for a given threshold values using the Generalized Pareto parametrization. As warning, L-Moments plots are really difficult to interpret. See @POT and @hosking for more details.

## Model Diagnostics and Return Level Analysis
* **Return Level Computation and Plot** : Computing a return value for a given return period is also possible, with a confidence interval obtained by the Delta Method [@coles]. Furthermore, a return level plot is provided, using the Delta Method in order to obtain the confidence bands. In order to compare, the empirical return level plot is provided. 

## Declustering and Data Visualization
It is possible to visualize the data during the unit of a return period. In case of extreme dependences sequences, for a given empirical rule (number of days, for example), it is possible to cluster the dataset and, taking the maximum observation of each cluster, a declustering of maximums is done. 

## Further Functions
It is also possible to compute sample L-Moments, model L-Moments, non-central moments, differential entropy and the survival function plot. 

## Installation 

For installation instructions, go to [README](https://github.com/iagolemos1/thresholdmodeling/blob/master/README.md).

# Reproducibility and User's Guide

In the repository on [GitHub page](https://github.com/iagolemos1/thresholdmodeling) is possible
to get the dataset: Daily Rainfall in the South-West of England from 1914 to 1962. 
Using it is a way of testing the software in order to verify its results and compare it with the forseen ones in @coles. For a more detailed tutorial of the using of each function, go to the [Test](https://github.com/iagolemos1/thresholdmodeling/blob/master/Test/test.py) folder.

A minimal simple example on how to use the software and get some of the results presented by @coles is given below. For information about the functions employed see the [Functions Documentation](https://github.com/iagolemos1/thresholdmodeling/blob/master/Functions%20Documentation.md) and for more detailes of reproducibility see the [README](https://github.com/iagolemos1/thresholdmodeling/blob/master/README.md).

```python
from thresholdmodeling import thresh_modeling 
import pandas as pd 

url = 'https://raw.githubusercontent.com/iagolemos1
/thresholdmodeling/master/dataset/rain.csv'
df = pd.read_csv(url, error_bad_lines=False) 
data = df.values 

thresh_modeling.MRL(data, 0.05)   
thresh_modeling.return_value(data, 30, 0.05, 365, 36500, 'mle') 
``` 
![](result_MRL.png)

**Fig. 1:** Mean Residual Life Plot for the daily rainfall dataset.

![](result_retlvl.png)

**Fig. 2:** Return level plot with the empirical estimatives of the return level and the confidence bands based on the Delta Method.

Also, for the given return period (100 years), the software presentes the following results in the terminal:
```
The return value for the given return period is 106.3439 ± 40.8669
```

For more details, the documentation is up-to-date on the [GitHub page](https://github.com/iagolemos1/thresholdmodeling).

# Acknowledgements

The authors would like to thanks the School of Mechanical Engineering at Federal University of Uberlândia and CNPq and CAPES for the financial support to this research.

# References

