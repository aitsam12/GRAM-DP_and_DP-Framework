from diffprivlib_ana import *
from pydp_ana import *
from smartnoise_ana import *
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
from matplotlib.lines import Line2D

query = 'sum'
dataset_path = 'adult_new.csv' #'Living_Wage.csv'
dataset_column = 'age'
#epsilon_value = 1.0
eps_list = np.arange(0.01, 0.52, 0.02)
iterations = 100


diffprivlib_avg_dp_list=[]
diffprivlib_MSE_list=[]
diffprivlib_M_scaled_E_list=[]
diffprivlib_RMSPE_list=[]

pydp_avg_dp_list=[]
pydp_MSE_list=[]
pydp_M_scaled_E_list=[]
pydp_RMSPE_list=[]

smartnoise_avg_dp_list=[]
smartnoise_MSE_list=[]
smartnoise_M_scaled_E_list=[]
smartnoise_RMSPE_list=[]

def main_DP_analysis(dataset_path, dataset_column, query, epsilon_value, iterations, upper_bound, lower_bound):
    df = pd.read_csv(dataset_path)
    if upper_bound or lower_bound == "None":
        upper_bound = float(max(eval('df.{c}'.format(c=dataset_column))))
        lower_bound = float(min(eval('df.{c}'.format(c=dataset_column))))

    print(len(df[dataset_column]))

    path = os.path.join(dataset_path)
    df_s = pd.read_csv(path)
    if query == 'count':
        d1 = eval('diffprivlib_analysis_{q}'.format(q=query))(query=query, dataset_column=(df[dataset_column]), epsilon_value=epsilon_value, upper_bound=upper_bound, lower_bound=lower_bound, iterations=iterations)
    else:  
        d1 = eval('diffprivlib_analysis_{q}'.format(q=query))(query=query, dataset_column=[eval('df.{c}'.format(c=dataset_column))], epsilon_value=epsilon_value, upper_bound=upper_bound, lower_bound=lower_bound, iterations=iterations)
    p1 = eval('pydp_analysis_{q}'.format(q=query))(query=query, dataset_column=eval('df_s.{c}'.format(c=dataset_column)), epsilon_value=epsilon_value, upper_bound=upper_bound, lower_bound=lower_bound, iterations=iterations)
    s1 = eval('smartnoise_analysis_{q}'.format(q=query))(query=query, dataset_csv=path, dataset_column=dataset_column, actual_column=eval('df.{c}'.format(c=dataset_column)), epsilon_value=epsilon_value, upper_bound=upper_bound, lower_bound=lower_bound, iterations=iterations)

    diffprivlib_avg_dp_list.append(d1[0])
    diffprivlib_MSE_list.append(d1[1])
    diffprivlib_M_scaled_E_list.append(d1[2])
    diffprivlib_RMSPE_list.append(d1[3])

    pydp_avg_dp_list.append(p1[0])
    pydp_MSE_list.append(p1[1])
    pydp_M_scaled_E_list.append(p1[2])
    pydp_RMSPE_list.append(p1[3])

    smartnoise_avg_dp_list.append(s1[0])
    smartnoise_MSE_list.append(s1[1])
    smartnoise_M_scaled_E_list.append(s1[2])
    smartnoise_RMSPE_list.append(s1[3])



for epsilon_value in eps_list: 
    print('calculating results for epsilon = {}'.format(epsilon_value)) 
    main_DP_analysis(dataset_path=dataset_path, dataset_column=dataset_column, query=query, epsilon_value=epsilon_value, upper_bound="None", lower_bound="None", iterations=iterations)


gs1 = gs.GridSpec(nrows=2, ncols=2)
figure = plt.gcf()

ax1 = plt.subplot(gs1[0,0])
ax1.plot(eps_list, diffprivlib_avg_dp_list, color='xkcd:orangish red')
ax1.plot(eps_list, pydp_avg_dp_list, color='xkcd:moss green')
ax1.plot(eps_list, smartnoise_avg_dp_list, color='xkcd:soft blue')
ax1.set_ylabel('Average DP', size=19)

ax2 = plt.subplot(gs1[0,1])
ax2.plot(eps_list, diffprivlib_MSE_list, color='xkcd:orangish red')
ax2.plot(eps_list, pydp_MSE_list, color='xkcd:moss green')
ax2.plot(eps_list, smartnoise_MSE_list, color='xkcd:soft blue')
ax2.set_ylabel('Mean Squared Error \n(MSE)', size=19)

ax3 = plt.subplot(gs1[1,0])
ax3.plot(eps_list, diffprivlib_M_scaled_E_list, color='xkcd:orangish red')
ax3.plot(eps_list, pydp_M_scaled_E_list, color='xkcd:moss green')
ax3.plot(eps_list, smartnoise_M_scaled_E_list, color='xkcd:soft blue')
ax3.set_ylabel('Mean Scaled Error', size=19)

ax4 = plt.subplot(gs1[1,1])
ax4.plot(eps_list, diffprivlib_RMSPE_list, color='xkcd:orangish red')
ax4.plot(eps_list, pydp_RMSPE_list, color='xkcd:moss green')
ax4.plot(eps_list, smartnoise_RMSPE_list, color='xkcd:soft blue')
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


legend_elements_1 = [Line2D([1], [1], color='xkcd:orangish red', label='diffprivlib, IBM'), Line2D([1], [1], color='xkcd:moss green', label='PyDP, OpenMined'), Line2D([1], [1], color='xkcd:soft blue', label='SmartNoise, OpenDP')]
figure.legend(prop={'size': 25},handles=legend_elements_1, loc="lower center", bbox_to_anchor=(0.5, 0.86), frameon=False, ncol=3, handletextpad=0.2, handlelength=1)
plt.show()

print(smartnoise_RMSPE_list)

