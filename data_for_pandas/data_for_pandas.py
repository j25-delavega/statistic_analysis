import pandas as pd


def get_data_frame(data):
    metric_1 = pd.Series(data[0][:])
    metric_2 = pd.Series(data[1][:])
    metric_3 = pd.Series(data[2][:])
    metric_4 = pd.Series(data[3][:])
    metric_5 = pd.Series(data[4][:])
    metric_6 = pd.Series(data[5][:])

    return pd.DataFrame({'real_dt': metric_1,
                         'euc_dt': metric_2,
                         'b_energy': metric_3,
                         'cross': metric_4,
                         'real_ldi': metric_5,
                         'euc_ldi': metric_6})
