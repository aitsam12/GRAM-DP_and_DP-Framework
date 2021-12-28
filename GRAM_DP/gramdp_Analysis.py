import warnings
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from gramdp_count import gramdp_count
from gramdp_mean import gramdp_mean
from gramdp_sum import gramdp_sum
from gramdp_var import gramdp_var
import matplotlib.gridspec as gs
from matplotlib.lines import Line2D

'''
query : string : 'count', 'sum', 'mean', 'std', 'var'
desired_privacy : string : 'very_high', 'high', 'moderate', 'low', 'very_low'
'''
dataset_path = 'adult.csv'
column = 'age'
query = 'var'


df = pd.read_csv(dataset_path)
array = df[column]

Desired_privacy = ['very_high', 'high', 'moderate', 'low', 'very_low']
dp_results_list =[]
std_se_results_list =[]
percent_results_list =[]
true_results_list =[]

MSE_results = []
scaled_error_results = []
percentage_error_results = []

eps_list = []
itr = []

for desired_privacy in Desired_privacy:
  print('Calculating results for {d} privacy.'.format(d=desired_privacy))
  for i in range(1000, 11000, 500):
    iterations =i
    itr.append(i)
    dp_result = eval('gramdp_'+ query)(array=array, desired_privacy=desired_privacy, iterations=iterations)
    eps_list.append(dp_result[0])
    dp_results_list.append(dp_result[1])
    std_se_results_list.append(dp_result[2])
    percent_results_list.append(dp_result[3])   
    MSE_results.append(dp_result[4])
    scaled_error_results.append(dp_result[5])
    percentage_error_results.append(dp_result[6])
    if query == 'count':
      true_results_list.append(len(array))
    else:      
      true_results_list.append(eval('np.{q}'.format(q=query))(array))


gs1 = gs.GridSpec(nrows=2, ncols=2)
figure = plt.gcf()

ax1 = plt.subplot(gs1[0,0])
ax1.plot(eps_list, dp_results_list, color='xkcd:orangish red')
ax1.set_ylabel('Average DP', size=19)

ax2 = plt.subplot(gs1[0,1])
ax2.plot(eps_list, MSE_results, color='xkcd:orangish red')
ax2.set_ylabel('Mean Squared Error (MSE)', size=19)

ax3 = plt.subplot(gs1[1,0])
ax3.plot(eps_list, scaled_error_results, color='xkcd:orangish red')
ax3.set_ylabel('Mean Scaled Error', size=19)

ax4 = plt.subplot(gs1[1,1])
ax4.plot(eps_list, percent_results_list, color='xkcd:orangish red')
ax4.set_ylabel('Root Mean Squared \n Percentage Error (RMSPE) [%]', size=19)

ax1.set_xticks([])
ax2.set_xticks([])

ax3.set_xlabel('Epsilon', size=21)
ax4.set_xlabel('Epsilon', size=21)

plt.subplots_adjust(hspace=0.06)
if query == 'count':
    figure.suptitle('Count Query', fontsize=25)
if query == 'sum':
    figure.suptitle('Sum Query', fontsize=25)
if query == 'mean':
    figure.suptitle('Mean Query', fontsize=25)
if query == 'var':
    figure.suptitle('Variance Query', fontsize=25)

plt.show()


