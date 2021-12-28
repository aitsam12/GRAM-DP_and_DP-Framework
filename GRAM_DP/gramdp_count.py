import warnings
from numbers import Integral
import numpy as np
from numpy.core import multiarray as mu
from numpy.core import umath as um
import random

# Gram-DP focus on un-bounded Differential Privacy for count query.

def gramdp_count(array, desired_privacy, iterations):
    r"""Counts the number of elements in the array ``array`` with differential privacy.

    Parameters
    ----------
    array : array_like
        The array for which to count.

    desired_privacy : string
        Choose the level of privacy.
        1) very_high
        2) high
        3) moderate
        4) low
        5) very_low
    * higher privacy leads to lower utility and vice versa.

        Epsilon selection will be according to the selected privacy level.
        1) epsilon: 0.01 - 0.10 (very_high)
        2) epsilon: 0.1 - 0.25 (high)
        3) epsilon: 0.25 - 0.50 (moderate)
        4) epsilon: 0.50 - 0.75 (low)
        5) epsilon: 0.75 - 1.0 (very_low)

    Returns
    -------
    count : int or array of int
        Differentially private number of non-zero values in the array along a given axis.  Otherwise, the total number
        of non-zero values in the array is returned.

    """
    sensitivity = 1
    true_count = len(array)
    DP_result = []
    std_se_error = []
    percentage_error = []
    
    dp_MSE_results = []
    dp_scaled_error_results = []
    dp_percentage_error_results = []
    
    eps = []
    
    for itr in range(iterations):
        if desired_privacy == "very_high":
            epsilon = round(random.uniform(0.01, 0.1), 2)
        if desired_privacy == "high":
            epsilon = round(random.uniform(0.1, 0.25), 2)      
        if desired_privacy == "moderate":
            epsilon = round(random.uniform(0.25, 0.50), 2)
        if desired_privacy == "low":
            epsilon = round(random.uniform(0.51, 0.75), 2)
        if desired_privacy == "very_low":
            epsilon = round(random.uniform(0.75, 1.0), 2)

        eps.append(epsilon)
        beta = sensitivity/epsilon
        noise = np.random.laplace(0, beta, 1)
        dp_result = true_count + noise
        DP_result.append(dp_result)
        percentage_error.append(abs(((true_count - dp_result)/true_count)*100))
        std_se_error.append(abs((true_count - dp_result)**2/len(array)))
        
        dp_MSE_results.append(((true_count - dp_result)**2)/iterations)
        dp_scaled_error_results.append(abs(true_count - dp_result)/iterations)
        dp_percentage_error_results.append(np.square((true_count - dp_result)/true_count))
        
    avg_eps = np.mean(eps)
    avg_DP_result = np.mean(DP_result)
    avg_std_se_error = np.mean(std_se_error)
    avg_percentage_error = np.mean(percentage_error)
    
    avg_dp_MSE_results = np.mean(dp_MSE_results)
    avg_dp_scaled_error_results = np.mean(dp_scaled_error_results)
    avg_dp_percentage_error_results = np.sqrt(np.mean(dp_percentage_error_results))*100
    
    return avg_eps, avg_DP_result, avg_std_se_error, avg_percentage_error, avg_dp_MSE_results, avg_dp_scaled_error_results, avg_dp_percentage_error_results



#print(gramdp_count(array=[10,23,45,76,8,2,34,65], desired_privacy='very_high', iterations=50))
