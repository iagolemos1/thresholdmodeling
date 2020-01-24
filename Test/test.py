from thresholdmodeling import thresh_modeling
import pandas as pd

url = 'https://raw.githubusercontent.com/iagolemos1/thresholdmodeling/master/dataset/rain.csv'
df =  pd.read_csv(url, error_bad_lines=False)
data = df.values.ravel()


thresh_modeling.MRL(data, 0.05)
thresh_modeling.Parameter_Stability_plot(data, 0.05)
thresh_modeling.gpdfit(data, 30, 'mle')
thresh_modeling.gpdpdf(data, 30, 'mle', 'sturges', 0.05)
thresh_modeling.qqplot(data,30, 'mle', 0.05)
thresh_modeling.ppplot(data, 30, 'mle', 0.05)
thresh_modeling.gpdcdf(data, 30, 'mle', 0.05)
thresh_modeling.return_value(data, 30, 0.05, 365, 36500, 'mle')
thresh_modeling.survival_function(data, 30, 'mle', 0.05)
thresh_modeling.non_central_moments(data, 30, 'mle')
thresh_modeling.lmom_dist(data, 30, 'mle')
thresh_modeling.lmom_sample(data)
thresh_modeling.lmomplot(data, 30)
thresh_modeling.decluster(data, 30, 30)
thresh_modeling.entropy(data, 'e', 30, 'mle')
