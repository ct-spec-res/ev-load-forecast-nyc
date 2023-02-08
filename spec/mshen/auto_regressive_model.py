# Import Libraries
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg

k_val = 48


# Create a dataframe with the start time, end time, and vehicle counts
df = pd.DataFrame({
    'start_time': pd.date_range(start= '1/1/2020', periods= k_val, freq= '30T'),
    'end_time': pd.date_range(start= '1/1/2020', periods= k_val, freq= '30T') + dt.timedelta(minutes=30),
    'vehicle_count': np.random.randint(1800,size=k_val)
})

df['x_vec'] = np.sqrt(df['vehicle_count'] + 0.25)

ar_model = AutoReg(df['x_vec'] , lags=19).fit()

pred = ar_model.predict(start=19, end=48, dynamic=False)

df['pred'] = pred

df.plot(x='start_time', y=['x_vec','pred'])
plt.show()
# print(df)