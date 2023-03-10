import pandas as pd
import requests
from io import StringIO
import pyvin


# Load electric vehicle registration into a dataframe
url = "https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/ChargeNY/ny_ev_registrations.csv"# New York State Energy Research and Development Authority(NYSERDA) electric vehicle registration
def url_to_df(url):
    '''
    Input: url that downloads to a csv from online
    Output: dataframe with data url/csv
    '''
    bytes_data = requests.get(url).content# Request data into bytes format
    clean_bytes = str(bytes_data,'utf-8')# Adjust bytes data into utf-8
    data_file = StringIO(clean_bytes)# Read string into a new file
    return pd.read_csv(data_file)# Load data into pandas

# Manhattan:10001-10282. Staten Island :10301-10314. Bronx: 10451-10475. Queens:11004-11109, 11351-11697.

df = url_to_df(url)

print(df.sort_values(by = ['Valid Date']))

# print(df['VIN Prefix'][1])

# single_vin = df['VIN Prefix'][1] + '0000000'

# veh = pyvin.VIN(single_vin, error_handling=pyvin.RAISE)

# print(veh.Make, veh.Model, veh.ModelYear)

# print(df.head())



