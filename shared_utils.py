import pandas as pd
import numpy as np

def read_trip_data(rename_columns=False, parse_dates=True):
    date_columns = ["Start Date", "End Date"] if parse_dates else None
    return read_data("201508_trip_data.csv", rename_columns,
                     date_columns)


def read_station_data(rename_columns=False, parse_dates=True):
    date_columns = ["installation"] if parse_dates else None
    return read_data("201508_station_data.csv", rename_columns,
                     date_columns)


def read_data(file_name, rename_columns=False, parse_dates=None):
    df = pd.read_csv(file_name, parse_dates=parse_dates)
    if rename_columns:
        df.rename(columns=lambda x: x.replace(" ", "_"), inplace=True)
    return df
