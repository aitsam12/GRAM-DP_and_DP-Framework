import pandas as pd 
import os
import numpy as np 
from diffprivlib.mechanisms import Laplace
import diffprivlib.tools as dpt


#######
# Diffprivlib
#######

def diffprivlib_analysis_count(query, dataset_column, epsilon_value, upper_bound, lower_bound, iterations): 
    dp_count_results = []
    dp_MSE_results = []
    dp_scaled_error_results = []
    dp_percentage_error_results = []
    
    true_count = len(dataset_column)
    if query == 'count':
        for itr in range(iterations):
            dp_count = dpt.count_nonzero(dataset_column, epsilon_value)
            dp_count_results.append(dp_count)
            dp_MSE_results.append(((true_count - dp_count)**2)/iterations)
            dp_scaled_error_results.append(abs(true_count - dp_count)/iterations) 
            dp_percentage_error_results.append(np.square((true_count - dp_count)/true_count))
        print('Report for diffprivlib (count query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_count_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))   
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100))
        print('===========================') 
    return (np.mean(dp_count_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)

def diffprivlib_analysis_sum(query, dataset_column, epsilon_value, upper_bound, lower_bound, iterations):
    if query == 'sum':
        dp_sum_results = []
        dp_MSE_results = []
        dp_scaled_error_results = []
        dp_percentage_error_results = []
        true_sum = np.sum(dataset_column)
        for itr in range(iterations):
            dp_sum = dpt.sum(dataset_column, epsilon_value, bounds=(lower_bound, upper_bound))
            dp_sum_results.append(dp_sum)
            dp_MSE_results.append(((true_sum - dp_sum)**2)/iterations)
            dp_scaled_error_results.append(abs(true_sum - dp_sum)/iterations) 
            dp_percentage_error_results.append(np.square((true_sum - dp_sum)/true_sum))
        print('Report for diffprivlib (sum query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_sum_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))   
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100)) 
        print('===========================')
    return (np.mean(dp_sum_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)
    

def diffprivlib_analysis_mean(query, dataset_column, epsilon_value, upper_bound, lower_bound, iterations):
    if query == 'mean':
        dp_mean_results = []
        dp_MSE_results = []
        dp_scaled_error_results = []
        dp_percentage_error_results = []
        true_mean = np.mean(dataset_column)
        for itr in range(iterations):
            dp_mean = dpt.mean(dataset_column, epsilon_value, bounds=(lower_bound, upper_bound))
            dp_mean_results.append(dp_mean)
            dp_MSE_results.append(((true_mean - dp_mean)**2)/iterations)
            dp_scaled_error_results.append(abs(true_mean - dp_mean)/iterations) 
            dp_percentage_error_results.append(np.square((true_mean - dp_mean)/true_mean))
        print('Report for diffprivlib (mean query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_mean_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))   
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100))  
        print('===========================')
    return (np.mean(dp_mean_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)
    

def diffprivlib_analysis_var(query, dataset_column, epsilon_value, upper_bound, lower_bound, iterations):
    if query == 'var':
        dp_var_results = []
        dp_MSE_results = []
        dp_scaled_error_results = []
        dp_percentage_error_results = []
        true_var = np.var(dataset_column)
        for itr in range(iterations):
            dp_var = dpt.var(dataset_column, epsilon_value, bounds=(lower_bound, upper_bound))
            dp_var_results.append(dp_var)
            dp_MSE_results.append(((true_var - dp_var)**2)/iterations)
            dp_scaled_error_results.append(abs(true_var - dp_var)/iterations) 
            dp_percentage_error_results.append(np.square((true_var - dp_var)/true_var))
        print('Report for diffprivlib (var query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_var_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))   
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100))
        print('===========================')
    return (np.mean(dp_var_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)
    

path = os.path.join('//home//aitsam//Documents//my_publication//DP_framework//business.csv')
df = pd.read_csv(path)

#diffprivlib_analysis_sum(query='sum', dataset_column=[df.col], epsilon_value=0.01, upper_bound=10.0, lower_bound=5.0, iterations=50)
