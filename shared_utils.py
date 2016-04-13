import pandas as pd
import numpy as np

def read_trip_data():
    return pd.read_csv("201508_trip_data.csv")


def read_station_data():
    return pd.read_csv("201508_station_data.csv")

