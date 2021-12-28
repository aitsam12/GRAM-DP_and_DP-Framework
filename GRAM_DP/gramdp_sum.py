import warnings
from numbers import Integral
import numpy as np
from numpy.core import multiarray as mu
from numpy.core import umath as um
import random

# Gram-DP focus on un-bounded Differential Privacy.

def gramdp_sum(array, desired_privacy, iterations):
    r"""Compute the differentially private arithmetic sum along the specified axis.

    Returns the sum of the array elements with differential privacy. Noise is added using np.Laplace` to satisfy differential
    privacy, where sensitivity is calculated automatically. Noise is also added to the true bounds. But user still have choice
    to add bounds manually according to the situation (upper, lower).

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
    sum : int or array of int
        Differentially private sum of an array along a given axis.
    """
    maximum = np.max(array) * 1.01
    minimum = np.min(array) * 0.99
    sensitivity = (maximum - minimum)
    true_sum = np.sum(array)
    DP_result = []
    std_se_error = []
    percentage_error = []
    
    dp_MSE_results = []
    dp_scaled_error_results = []
    dp_percentage_error_results = []
    
    eps = []
    
    for itr in range(iterations):
        epsilon = []
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
        dp_result = true_sum + noise
        DP_result.append(dp_result)
        percentage_error.append(abs(((true_sum - dp_result)/true_sum)*100))
        std_se_error.append(abs((true_sum - dp_result)/len(array)))
        
        dp_MSE_results.append(((true_sum - dp_result)**2)/iterations)
        dp_scaled_error_results.append(abs(true_sum - dp_result)/iterations)
        dp_percentage_error_results.append(np.square((true_sum - dp_result)/true_sum))
        
    avg_eps = np.mean(eps)
    avg_DP_result = np.mean(DP_result)
    avg_std_se_error = np.std(std_se_error)
    avg_percentage_error = np.mean(percentage_error)
    
    avg_dp_MSE_results = np.mean(dp_MSE_results)
    avg_dp_scaled_error_results = np.mean(dp_scaled_error_results)
    avg_dp_percentage_error_results = np.sqrt(np.mean(dp_percentage_error_results))*100
    
    return avg_eps, avg_DP_result, avg_std_se_error, avg_percentage_error, avg_dp_MSE_results, avg_dp_scaled_error_results, avg_dp_percentage_error_results

#print(gramdp_sum(array=[10,23,45,76,8,2,34,65], desired_privacy='very_high', iterations=500))

