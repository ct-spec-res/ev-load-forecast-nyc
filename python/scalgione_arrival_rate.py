# Import Libraries
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg


# Set up initial variables
k_val = 48 # number of epochs we are looking at in a 24 hr period
j_val = 5 # days into the future we are observing

# Create fake data
np.random.seed(0) # set consistent seed


# Create a dataframe with the start time, end time, and vehicle counts
df = pd.DataFrame({
    'start_time': pd.date_range(start= '1/1/2020', periods= k_val, freq= '30T'), # start times every 30 min
    'end_time': pd.date_range(start= '1/1/2020', periods= k_val, freq= '30T') + dt.timedelta(minutes=30), # end time is 30 min after the start times
    'vehicle_count': np.random.randint(1800,size=k_val) # random integer that is less than a single lane recommendation from AASHTO
})

df['x_vec'] = np.sqrt(df['vehicle_count'] + 0.25)

ar_model = AutoReg(df['x_vec'] , lags=19).fit()

pred = ar_model.predict(start=19, end=48, dynamic=False)

df['pred'] = pred

df.plot(x='start_time', y=['x_vec','pred'])
plt.show()
# print(df)