import pandas as pd 
import numpy as np 
from pydp.algorithms import laplacian as dp
import os

#######
# OpenMined-PyDp
#######

def pydp_analysis_count(query, dataset_column, epsilon_value, upper_bound, lower_bound, iterations):
    if query == 'count':
        dp_count_results = []
        dp_MSE_results = []
        dp_scaled_error_results = []
        dp_percentage_error_results = []
        true_count = len(dataset_column)
        for itr in range(iterations):
            x = dp.Count(epsilon=epsilon_value, dtype='float')
            dp_count = (x.quick_result(list(dataset_column)))
            dp_count_results.append(dp_count)
            dp_MSE_results.append(((true_count - dp_count)**2)/iterations)
            dp_scaled_error_results.append(abs(true_count - dp_count)/iterations) 
            dp_percentage_error_results.append(np.square((true_count - dp_count)/true_count))
        print('Report for PyDp (count query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_count_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))   
        #print('Mean Percentage Error: {percent}'.format(percent = np.mean(dp_count_results))) 
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100)) 
        print('===========================')   
    return (np.mean(dp_count_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)
    

def pydp_analysis_sum(query, dataset_column, epsilon_value, upper_bound, lower_bound, iterations):
    if query == 'sum':
        dp_sum_results = []
        dp_MSE_results = []
        dp_scaled_error_results = []
        dp_percentage_error_results = []
        true_sum = np.sum(dataset_column)
        for itr in range(iterations):
            x = dp.BoundedSum(epsilon_value, lower_bound=lower_bound, upper_bound=upper_bound, dtype='float')
            dp_sum = x.quick_result(list(dataset_column))
            dp_sum_results.append(dp_sum)
            dp_MSE_results.append(((true_sum - dp_sum)**2)/iterations)
            dp_scaled_error_results.append(abs(true_sum - dp_sum)/iterations) 
            dp_percentage_error_results.append(np.square((true_sum - dp_sum)/true_sum))
        print('Report for PyDp (sum query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_sum_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))   
        #print('Mean Percentage Error: {percent}'.format(percent = np.mean(dp_sum_results)))  
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100)) 
        print('===========================')
    return (np.mean(dp_sum_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)
    

def pydp_analysis_mean(query, dataset_column, epsilon_value, upper_bound, lower_bound, iterations):
    if query == 'mean':
        dp_mean_results = []
        dp_MSE_results = []
        dp_scaled_error_results = []
        dp_percentage_error_results = []
        true_mean = np.mean(dataset_column)
        for itr in range(iterations):
            x = dp.BoundedMean(epsilon_value, lower_bound=lower_bound, upper_bound=upper_bound, dtype='float')
            dp_mean = x.quick_result(list(dataset_column))
            dp_mean_results.append(dp_mean)
            dp_MSE_results.append(((true_mean - dp_mean)**2)/iterations)
            dp_scaled_error_results.append(abs(true_mean - dp_mean)/iterations) 
            dp_percentage_error_results.append(np.square((true_mean - dp_mean)/true_mean))
        print('Report for PyDp (mean query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_mean_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))   
        #print('Mean Percentage Error: {percent}'.format(percent = np.mean(dp_mean_results))) 
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100)) 
        print('===========================') 
    return (np.mean(dp_mean_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)
    

def pydp_analysis_var(query, dataset_column, epsilon_value, upper_bound, lower_bound, iterations):
    if query == 'var':
        dp_var_results = []
        dp_MSE_results = []
        dp_scaled_error_results = []
        dp_percentage_error_results = []
        true_var = np.var(dataset_column)
        for itr in range(iterations):
            x = dp.BoundedVariance(epsilon_value, lower_bound=lower_bound, upper_bound=upper_bound, dtype='float')
            dp_var = x.quick_result(list(dataset_column))
            dp_var_results.append(dp_var)
            dp_MSE_results.append(((true_var - dp_var)**2)/iterations)
            dp_scaled_error_results.append(abs(true_var - dp_var)/iterations) 
            dp_percentage_error_results.append(np.square((true_var - dp_var)/true_var))
        print('Report for PyDp (var query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_var_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))   
        #print('Mean Percentage Error: {percent}'.format(percent = np.mean(dp_var_results)))  
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100)) 
        print('===========================')
    return (np.mean(dp_var_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)
    

#path = os.path.join('Living_Wage.csv')
#df = pd.read_csv(path)

#pydp_analysis_var(query='var', dataset_column=df.livingwage, epsilon_value=1.01, upper_bound=10.0, lower_bound=5.0, iterations=50)
