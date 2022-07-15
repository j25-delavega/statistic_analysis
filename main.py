from reader.reader import DataClass
from printer.data_printer import data_printer
from data_for_pandas.data_for_pandas import get_data_frame
from statics.statics import StaticsClass
import pandas as pd

if __name__ == '__main__':

    path = "file_for_reading/"
    file_name = path + "data.dat"

    reader = DataClass(file_name)
    reader.reader()
    data = reader.get_data_to_analyze()

    data_frame = get_data_frame(data)

    statics = StaticsClass(data_frame)

    pearson_matrix, spearman_matrix, kendall_matrix = statics.get_correlation_matrices()

    print(pearson_matrix, spearman_matrix, kendall_matrix)

