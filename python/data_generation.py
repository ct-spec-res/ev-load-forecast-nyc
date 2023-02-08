# Import Libraries
import datetime as dt
import numpy as np
import pandas as pd

class DataGeneration:
    def __init__ (self, start, periods, freq):
        self.start = start
        self.periods = periods
        self.freq = freq
        
    def start_times(self):
        return pd.date_range(start= self.start, periods= self.periods, freq= self.freq)
    
    def end_times(self):
        return self.start_times + pd.DateOffset(minutes=30)




t1 = DataGeneration('1/1/2020', 48, '30T')

print(t1.end_times())


# Create a dataframe with the start time, end time, and vehicle counts
# df = pd.DataFrame({
#     'start_time': pd.date_range(start= '1/1/2020', periods= k_val, freq= '30T'),
#     'end_time': pd.date_range(start= '1/1/2020', periods= k_val, freq= '30T') + dt.timedelta(minutes=30),
#     'vehicle_count': np.random.randint(1800,size=k_val)
# })