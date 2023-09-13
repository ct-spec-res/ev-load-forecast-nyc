#### This File Contains Functions Needed to Estimate Range of EVs by Zipcode in NYC ####


### Import Libraries ###
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pyvin
import re


from dotenv import load_dotenv
from shapely.geometry import shape
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sodapy import Socrata
from tqdm.auto import tqdm

def run_client(client_url):
    '''
    Input:
        - Client URL(str)
    Output:
        - Client data for Open Data Socrata API
    '''
    #Load enviroment file
    load_dotenv()
    
    # Login to NYS data with enviornment data
    client = Socrata(client_url,
                     os.getenv('nys_dmv_app_token'),
                     username = os.getenv('nys_dmv_api_key_id'),
                     password = os.getenv('nys_dmv_secret')
                    )
    return client

def api_to_df(endpoint, client_url, query):
    '''
    Input:
        - Client URL(str)
    Output:
        - Dataframe with all vehicle registrations in New York that have not expired two years ago
            - The data frame includes only vehicles from New York City that are electric
    '''
    
    # Get client information
    client = run_client(client_url)
    
    # Pull results from DMV registration that are vehicles
    results = client.get(endpoint, query=query)
    
    # Change results into dataframe
    return pd.DataFrame.from_records(results)

def dmv_vin_data(num_records='max'):
    '''
    Input:
        - N/A
    Output:
        - Dataframe with dmv information
    '''
    # Enpoint for API
    dmv_endpoint = 'w4pv-hbkt'
    
    # NYS open data url
    nys_url = 'data.ny.gov'
    
    # Query for electric vehicles in New York
    query_count = "SELECT COUNT(*)"
    if num_records == 'max':
        NUM_RECORDS = int(client.get(endpoint, query = query_count)[0]['COUNT'])
    else:
        NUM_RECORDS = int(num_records)
    
    
    query = f"""
        SELECT vin, county, zip
        WHERE record_type = 'VEH'
        AND county in ('NEW YORK')
        AND fuel_type = 'ELECTRIC'
        LIMIT {NUM_RECORDS}
    """
    
    return api_to_df(dmv_endpoint,nys_url, query)
    
# print(api_to_df('w4pv-hbkt','data.ny.gov',))

print(dmv_vin_data())