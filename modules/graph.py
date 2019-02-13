import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
from collections import Counter  #콜렉션 중요
plt.style.use('ggplot')
import seaborn as sns
import scipy as sp
from matplotlib.ticker import PercentFormatter
from mpl_toolkits.mplot3d import Axes3D

class Graph:

    # 가로로 히스토그램
    def bar(self,data,var):
        count = Counter(data[var])  # 세어줌 ㅜㅜ
        tmp = pd.DataFrame.from_dict(count, orient='index')  # count 는 딕셔너리형태라서,,?
        tmp.plot(kind='bar', legend=None)
        plt.savefig('bar_'+var)
        plt.show()
    # 세로로 누적 한개의 변수
    def bar2(self,data,var):
        count = Counter(data[var])  # 세어줌 ㅜㅜ
        # tmp = pd.DataFrame.from_dict(count, orient=[var])  # count 는 딕셔너리형태라서,,?
        # tmp.plot.barh(stacked=True)
        tmp = pd.DataFrame(dict(count),index=[var])
        tmp.plot.barh(stacked=True)
        plt.savefig('bar2_'+var)
        plt.show()

    #box plot 구현 // 문자열은 float형 또는 int형으로 변환을 해줘야 함.
    def box_plot(self,data,var1,var2):
        df = data[[var1,var2]]
        df = df.astype(float) #float형으로 변환 int형으로 변환해도 되지만 실수값도 포함하기 위해 이걸로

        df.boxplot(column=[var1, var2])
        plt.savefig('boxPlot_'+var1+'&'+var2)
        plt.show()


    # scatter plot 구현
    # def scatter_plot(self, data, var1, var2):
    #     df = data[[var1, var2]]
    #     df = df.astype(float)
    #     N = 50007
    #     colors = np.random.rand(N)
    #     area = (10 * np.random.rand(N)) ** 2  # 0 to 15 point radii
    #     x = df[var1]
    #     y = df[var2]
    #     plt.scatter(x, y, s=area, alpha=0.5)
    #     # plt.savefig('scatterPlot_' + var1 + '&' + var2)
    #     plt.xlabel(var1)
    #     plt.ylabel(var2)
    #     plt.title(var1 + ' and ' + var2 + ' graph')
    #     plt.show()

    def scatter_plot(self, data, var1, var2, var3):
        df = data[0:600]
        df = data[[var1, var2, var3]]
        df = df.dropna(how='all')
        color_list = list(df[var3].unique())
        color_list_filter = []
        for i in color_list:
            if (i != 'nan'):
                color_list_filter.append(i)
        color_dict = {}
        for i in color_list_filter:
            df_filtered_var3 = df[df[var3] == i]
            color_dict[i] = df_filtered_var3

        graph_color = ['orange', 'grey', 'blue', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white']
        tmp = 0
        for i in color_dict:
            df_sort_var3 = color_dict[i].sort_values([var1], ascending=[True])
            x = df_sort_var3[var1]
            df_sort_var3 = color_dict[i].sort_values([var2], ascending=[True])
            y = df_sort_var3[var2]
            plt.scatter(x, y, color=graph_color[tmp], label=var3 + ' = ' + i, alpha=0.3, s=15)
            tmp += 1

        plt.tight_layout()
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.title('직업병 예측')
        plt.xticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
        plt.yticks([1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600])
        plt.legend()
        plt.show()

    # histogram 구현
    # def histogram(self, data, var1):
    #     df = data[[var1]]
    #     df = df.astype(float)
    #     x = df[var1]
    #     n_bins = 20
    #
    #     fig, axs = plt.subplots(1, 2, tight_layout=True)
    #     N, bins, patches = axs[0].hist(x, bins=n_bins)
    #     fracs = N / N.max()
    #     norm = matplotlib.colors.Normalize(fracs.min(), fracs.max())
    #     for thisfrac, thispatch in zip(fracs, patches):
    #         color = plt.cm.viridis(norm(thisfrac))
    #         thispatch.set_facecolor(color)
    #     axs[1].hist(x, bins=n_bins, density=True)
    #     axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))
    #     plt.savefig('histogram_'+var1)
    #     plt.show()

    def histogram(self, data, var, color_var):
        color_list = []
        df = data[0:600]
        df = data[[var, color_var]]
        df = df.dropna(how='all')
        color_list = list(df[color_var].unique())
        color_list_filter = []
        for i in color_list:
            if (i != 'nan'):
                color_list_filter.append(i)
        color_dict = {}
        for i in color_list_filter:
            df_filtered_color_var = df[df[color_var] == i]
            color_dict[i] = df_filtered_color_var

        graph_color = ['orange', 'grey', 'blue', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white']
        tmp = 0
        k = 0
        j = 0
        # 정렬.. 큰것부터..
        max_color_dict = {}
        for i in color_dict:
            df_sort_color_var = color_dict[i].sort_values([var], ascending=[True])
            max_color_dict[i] = len(df_sort_color_var)

        len_sort_value = sorted(max_color_dict, key=lambda k: max_color_dict[k], reverse=True)

        for i in color_dict:
            k = len_sort_value[j]
            df_sort_color_var = color_dict[k].sort_values([var], ascending=[True])
            x = df_sort_color_var[var]
            list_x = list(x)
            plt.hist(list_x, label=color_var + ' = ' + k, rwidth=0.5, color=graph_color[tmp], stacked=True,
                     histtype='stepfilled', align = 'mid', alpha = 0.7, normed=True)
            tmp += 1
            j += 1


        plt.title('직업병 예측')
        plt.xticks([0, 50, 100, 150, 200, 250, 300])
        plt.xlabel(var)
        plt.ylabel('Frequency')
        plt.legend()
        plt.show()


    # 3d projection 구현
    def projection(self, data, var1, var2):
        df = data[[var1, var2]]
        df = df.astype(float)
        x = df[var1]
        y = df[var2]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        colors = ['r', 'g', 'b', 'y']
        yticks = [3, 2, 1, 0]
        for c, k in zip(colors, yticks):
            cs = [c] * len(x)
            cs[0] = 'c'
            ax.bar(x, y, zs=k, zdir='y', color=cs, alpha=0.8)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_yticks(yticks)

        plt.savefig('3DProjection_'+var1+'&'+var2)
        plt.show()

    #정규화 검사 Normalization check
    def normal_check(self, data, var):
        df = data[[var]]
        df = df.astype(float)
        plt.subplot(1, 2, 1)
        sns.distplot(df[var])
        plt.subplot(1, 2, 2)
        sp.stats.probplot(df[var], plot=plt)
        plt.savefig('normal_check'+var)
        plt.show()

        # df = data[[var]]
        # df.astype(float)
        #
        # sns.distplot(df[var])
        # plt.show()
        # sp.stats.probplot(df[var], plot=plt)

    def seaborn(self):
        tips = sns.load_dataset("tips")
        ax = sns.scatterplot(x="total_bill", y="tip", data=tips)
        ax = sns.scatterplot(x="total_bill", y="tip", hue="time", data=tips)

