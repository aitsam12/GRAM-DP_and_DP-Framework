import warnings
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from gramdp_count import gramdp_count
from gramdp_mean import gramdp_mean
from gramdp_sum import gramdp_sum
from gramdp_var import gramdp_var


dataset_path = '/home/path_to_your_csv_file'
column = 'your_column_header'
query = 'sum'                  # query : string : 'count', 'sum', 'mean', 'std', 'var'
desired_privacy = 'very_low'   # desired_privacy : string : 'very_high', 'high', 'moderate', 'low', 'very_low'
iterations = 5                 # number of iterations

######### calculations ##########
df = pd.read_csv(dataset_path)
array = df['your_column_header']
dp_result = eval('gramdp_'+ query)(array=array, desired_privacy=desired_privacy, iterations=iterations)
print('Average DP result: {r}'.format(r=dp_result[0]))
print('Average std of Scaled Error: {r}'.format(r=dp_result[1]))
print('Average Percentage Error: {r}'.format(r=dp_result[2]))
