import pandas as pd
import numpy as np

SF_ZIP_CODES = ["94102", "94103", "94104", "94105", "94107", "94108",
                "94109", "94110", "94111", "94112", "94114", "94115",
                "94116", "94117", "94118", "94121", "94122", "94123",
                "94124", "94127", "94128", "94129", "94130", "94131",
                "94132", "94133", "94134", "94143", "94158", "94188"]

def read_trip_data(parse_dates=True):
    date_columns = ["Start Date", "End Date"] if parse_dates else None
    return read_data("201508_trip_data.csv", date_columns)


def read_station_data(parse_dates=True):
    date_columns = ["installation"] if parse_dates else None
    return read_data("201508_station_data.csv", date_columns)

def read_zip_code_data():
    return read_data("zip_code_database.csv")


def read_data(file_name, parse_dates=None):
    '''Read in named data file'''
    df = pd.read_csv(file_name, parse_dates=parse_dates)
    df.rename(columns=lambda x: x.replace(" ", "_"), inplace=True)
    return df



def clean_zip_codes(df):
    '''Creates new column "Clean_Zip_Code". Replaces "nil" with NaN. 
    Only uses values before the "-". Any Zip code that is then not
    exactly five digits long is replaced by NaN.'''
    def replace_nonsense_value(x):
        if x == 'nil':
            x = np.NaN
        elif isinstance(x, str):
            if "-" in x:
                x = x.split("-")[0]
            if len(x) != 5:
                x = np.NaN

        return x
    df["Clean_Zip_Code"] = df.Zip_Code.map(replace_nonsense_value)
    
