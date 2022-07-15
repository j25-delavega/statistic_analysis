import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class StaticsClass(object):
    def __init__(self, data):
        self.data_frame = data

    def get_correlation_matrix(self, method):
        return self.data_frame.corr(method=method).round(2)

    def get_correlation_matrices(self):
        return self.get_correlation_matrix('pearson'), \
               self.get_correlation_matrix('spearman'), \
               self.get_correlation_matrix('kendall')

    def heatmap_graphic(self, method):
        if method == 'pearson':
            legend = 'Pearson Correlation Coefficient'
        elif method == 'spearman':
            legend = 'Spearman Correlation Coefficient'
        else:
            legend = 'Kendall Correlation Coefficient'
        heat = sns.heatmap(self.get_correlation_matrix(method), annot=True, vmax=1, vmin=-1, center=0, cmap='Blues')
        heat.set_xlabel(legend)
        plt.show()

    def heatmap_graphics(self):
        self.heatmap_graphic('pearson')
        self.heatmap_graphic('spearman')
        self.heatmap_graphic('kendall')

    def scatter_matrix_graphics(self):
        pd.plotting.scatter_matrix(self.data_frame, diagonal='hist')
        plt.show()
