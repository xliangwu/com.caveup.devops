import glob
from datetime import date
import os

import pandas as pd


def merge_csv():
    today = date.today()
    today_label = today.strftime("%Y%m%d")
    output = "yaozhi_data_{}.csv".format(today_label)

    input_files = "crawler/yaozhi_data_*.csv"
    output = "yaozhi_data_{}.csv".format(today_label)
    csv_list = glob.glob(input_files)

    if os.path.exists(output):
        os.remove(output)

    for i in range(len(csv_list)):
        filepath = csv_list[i]
        print("Read csv file:", filepath)
        df = pd.read_csv(filepath, encoding="utf-8", low_memory=False)
        df = df.to_csv(output, encoding="utf-8", index=False, header=False, mode='a+')


if __name__ == '__main__':
    merge_csv()
