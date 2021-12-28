from opendp.smartnoise.core.components import index
import pandas as pd 
import numpy as np 
import opendp.smartnoise.core as sn
import os
import math

#######
# OpenDP-Smartnoise
#######

def smartnoise_analysis_count(query, dataset_csv, dataset_column, actual_column, epsilon_value, upper_bound, lower_bound, iterations):
    if query == 'count':
        dp_count_results = []
        dp_MSE_results = []
        dp_scaled_error_results = []
        dp_percentage_error_results = []
        true_count = len(actual_column)
        for itr in range(iterations):
            with sn.Analysis(neighboring='substitute') as analysis:
                var_name = ['dataset_column']
                data_path = dataset_csv
                data = sn.Dataset(path = data_path, column_names = var_name)
                data_in_float = sn.to_float(data['dataset_column'])
                dp = sn.dp_count(data=data_in_float, privacy_usage={'epsilon':epsilon_value})
            analysis.release()
            dp_count = dp.value
            dp_count_results.append(dp_count)
            dp_MSE_results.append(((true_count - dp_count)**2)/iterations)
            dp_scaled_error_results.append(abs(true_count - dp_count)/iterations) 
            dp_percentage_error_results.append(np.square((true_count - dp_count)/true_count))
        print('Report for smartnoise (count query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_count_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))    
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100))
        print('===========================') 
    return (np.mean(dp_count_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)
    

def smartnoise_analysis_sum(query, dataset_csv, dataset_column, actual_column, epsilon_value, upper_bound, lower_bound, iterations):
    if query == 'sum':
        dp_sum_results = []
        dp_MSE_results = []
        dp_scaled_error_results = []
        dp_percentage_error_results = []
        true_sum = np.sum(actual_column)
        for itr in range(iterations):
            with sn.Analysis(neighboring='substitute', protect_floating_point=False, protect_sensitivity=False) as analysis:
                var_name = ['dataset_column']
                data_path = dataset_csv
                dataset = sn.Dataset(path = data_path, column_names = var_name)
                data_in_float = sn.to_float(dataset['dataset_column'])
                data_in_float = sn.impute(data = data_in_float, lower = lower_bound, upper = upper_bound)
                data_in_float = sn.clamp(data_in_float, lower=lower_bound, upper=upper_bound)
                data_in_float = sn.resize(data_in_float, number_rows=len(actual_column), lower=lower_bound, upper=upper_bound)
                dp = sn.dp_sum(data=data_in_float, privacy_usage={'epsilon':epsilon_value}, mechanism="laplace")
            analysis.release()
            dp_sum = dp.value
            dp_sum_results.append(dp_sum)
            dp_MSE_results.append(((true_sum - dp_sum)**2)/iterations)
            dp_scaled_error_results.append(abs(true_sum - dp_sum)/iterations) 
            dp_percentage_error_results.append(np.square((true_sum - dp_sum)/true_sum))
        print('Report for smartnoise (sum query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_sum_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))   
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100)) 
        print('===========================')
    return (np.mean(dp_sum_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)
    

def smartnoise_analysis_mean(query, dataset_csv, dataset_column, actual_column, epsilon_value, upper_bound, lower_bound, iterations):
    if query == 'mean':
        dp_mean_results = []
        dp_MSE_results = []
        dp_scaled_error_results = []
        dp_percentage_error_results = []
        true_mean = np.mean(actual_column)
        for itr in range(iterations):
            with sn.Analysis(neighboring='substitute') as analysis:
                var_name = ['dataset_column']
                data_path = dataset_csv
                dataset = sn.Dataset(path = data_path, column_names = var_name)
                data_in_float = sn.to_float(dataset['dataset_column'])
                data_in_float = sn.impute(data = data_in_float, lower = lower_bound, upper = upper_bound)
                data_in_float = sn.clamp(data_in_float, lower=lower_bound, upper=upper_bound)
                data_in_float = sn.resize(data_in_float, number_rows=len(actual_column), lower=lower_bound, upper=upper_bound)
                dp = sn.dp_mean(data=data_in_float, privacy_usage={'epsilon':epsilon_value})
            analysis.release()
            dp_mean = dp.value
            dp_mean_results.append(dp_mean)
            dp_MSE_results.append(((true_mean - dp_mean)**2)/iterations)
            dp_scaled_error_results.append(abs(true_mean - dp_mean)/iterations) 
            dp_percentage_error_results.append(np.square((true_mean - dp_mean)/true_mean))
        print('Report for smartnoise (mean query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_mean_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))    
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100))
        print('===========================')
    return (np.mean(dp_mean_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)
    

def smartnoise_analysis_var(query, dataset_csv, dataset_column, actual_column, epsilon_value, upper_bound, lower_bound, iterations):
    if query == 'var':
        dp_var_results = []
        dp_MSE_results = []
        dp_scaled_error_results = []
        dp_percentage_error_results = []
        true_var = np.var(actual_column)
        for itr in range(iterations):
            with sn.Analysis(neighboring='substitute') as analysis:
                var_name = ['dataset_column']
                data_path = dataset_csv
                dataset = sn.Dataset(path = data_path, column_names = var_name)
                data_in_float = sn.to_float(dataset['dataset_column'])
                data_in_float = sn.impute(data = data_in_float, lower = lower_bound, upper = upper_bound)
                data_in_float = sn.clamp(data_in_float, lower=lower_bound, upper=upper_bound)
                data_in_float = sn.resize(data_in_float, number_rows=len(actual_column), lower=lower_bound, upper=upper_bound)
                dp = sn.dp_variance(data=data_in_float, privacy_usage={'epsilon':epsilon_value})
            analysis.release()
            dp_var = dp.value
            dp_var_results.append(dp_var)
            dp_MSE_results.append(((true_var - dp_var)**2)/iterations)
            dp_scaled_error_results.append(abs(true_var - dp_var)/iterations) 
            dp_percentage_error_results.append(np.square((true_var - dp_var)/true_var))
        print('Report for smartnoise (var query)')
        print('Results for {it} iterations of your selected column are as follows:'.format(it=iterations))
        print('Average DP: {dp}'.format(dp = np.mean(dp_var_results)))    
        print('Mean Squared Error (MSE): {mse}'.format(mse = np.mean(dp_MSE_results)))    
        print('Mean Scaled Error: {mean_scaled}'.format(mean_scaled = np.mean(dp_scaled_error_results)))    
        print('Root Mean Squared Percentage Error (RMSPE): {percent}'.format(percent = np.sqrt(np.mean(dp_percentage_error_results))*100))
        print('===========================')
    return (np.mean(dp_var_results), np.mean(dp_MSE_results), np.mean(dp_scaled_error_results), np.sqrt(np.mean(dp_percentage_error_results))*100)
    


#path = os.path.join('adult.csv')
#dff = pd.read_csv(path)
#query = 'var'
#col = 'age'
#smartnoise_analysis_var(query=query, dataset_csv=path, dataset_column=col, actual_column=dff[col], epsilon_value=1.01, upper_bound=90.0, lower_bound=5.0, iterations=100)
