class StaticsClass(object):
    def __init__(self, data):
        self.data_frame = data

    def get_correlation_matrix(self, method):
        return self.data_frame.corr(method=method)

    def get_correlation_matrices(self):
        return self.get_correlation_matrix('pearson'), \
               self.get_correlation_matrix('spearman'), \
               self.get_correlation_matrix('kendall')
