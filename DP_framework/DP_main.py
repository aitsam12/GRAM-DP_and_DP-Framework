from diffprivlib_ana import *
from pydp_ana import *
from smartnoise_ana import *
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

query = 'mean'
dataset_path = 'adult.csv'
dataset_column = 'age'
epsilon_value = 0.1
iterations = 10


def main_DP_analysis(dataset_path, dataset_column, query, epsilon_value, iterations, upper_bound, lower_bound):

    df = pd.read_csv(dataset_path)
    if upper_bound or lower_bound == "None":
        upper_bound = float(max(eval('df.{c}'.format(c=dataset_column))))
        lower_bound = float(min(eval('df.{c}'.format(c=dataset_column))))


    path = os.path.join(dataset_path)
    df = pd.read_csv(path)

    d1 = eval('diffprivlib_analysis_{q}'.format(q=query))(query=query, dataset_column=[eval('df.{c}'.format(c=dataset_column))], epsilon_value=epsilon_value, upper_bound=upper_bound, lower_bound=lower_bound, iterations=iterations)
    p1 = eval('pydp_analysis_{q}'.format(q=query))(query=query, dataset_column=eval('df.{c}'.format(c=dataset_column)), epsilon_value=epsilon_value, upper_bound=upper_bound, lower_bound=lower_bound, iterations=iterations)
    s1 = eval('smartnoise_analysis_{q}'.format(q=query))(query=query, dataset_csv=path, dataset_column=dataset_column, actual_column=eval('df.{c}'.format(c=dataset_column)), epsilon_value=epsilon_value, upper_bound=upper_bound, lower_bound=lower_bound, iterations=iterations)
    print(d1)
    print(p1)
    print(s1)
    
    x = ['diffprivlib', 'PyDp', 'Smartnoise']
    x_pos = [i for i, _ in enumerate(x)]
    
    val0 = [d1[0], p1[0], s1[0]]
    val1 = [d1[1], p1[1], s1[1]]
    val2 = [d1[2], p1[2], s1[2]]
    val3 = [d1[3], p1[3], s1[3]]
    
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].bar(x_pos, val0, color=['xkcd:orangish red', 'xkcd:moss green', 'xkcd:soft blue'])
    axs[0, 0].set_ylabel('Average DP', size=15)
    axs[0, 1].bar(x_pos, val1, color=['xkcd:orangish red', 'xkcd:moss green', 'xkcd:soft blue'])
    axs[0, 1].set_ylabel('Mean Squared Error (MSE)', size=15)
    axs[1, 0].bar(x_pos, val2, color=['xkcd:orangish red', 'xkcd:moss green', 'xkcd:soft blue'])
    axs[1, 0].set_ylabel('Mean Scaled Error', size=15)
    axs[1, 1].bar(x_pos, val3, color=['xkcd:orangish red', 'xkcd:moss green', 'xkcd:soft blue'])
    axs[1, 1].set_ylabel('Root Mean Squared \n Percentage Error (RMSPE) [%]', size=15)

    axs[1, 0].set_xlabel('Epsilon', size=15)
    axs[1, 1].set_xlabel('Epsilon', size=15)
    if query == 'count':
        fig.suptitle('Count Query', fontsize=19)

    if query == 'sum':
        fig.suptitle('Sum Query', fontsize=19)

    if query == 'mean':
        fig.suptitle('Mean Query', fontsize=19)

    if query == 'var':
        fig.suptitle('Variance Query', fontsize=19)

    plt.subplots_adjust(wspace=0.27)
    legend_elements_1 = [Line2D([1], [1], color='xkcd:orangish red', label='diffprivlib, IBM'), Line2D([1], [1], color='xkcd:soft blue', label='PyDP, OpenMined'), Line2D([1], [1], color='xkcd:moss green', label='SmartNoise, OpenDP')]
    fig.legend(prop={'size': 16},handles=legend_elements_1, loc="lower center", bbox_to_anchor=(0.5, 0.88), frameon=False, ncol=3, handletextpad=0.2, handlelength=1)
    plt.show()
    
    
main_DP_analysis(dataset_path=dataset_path, dataset_column=dataset_column, query=query, epsilon_value=epsilon_value, upper_bound="None", lower_bound="None", iterations=iterations)
