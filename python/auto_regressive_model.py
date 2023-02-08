



df['x_vec'] = np.sqrt(df['vehicle_count'] + 0.25)

ar_model = AutoReg(df['x_vec'] , lags=19).fit()

pred = ar_model.predict(start=19, end=48, dynamic=False)

df['pred'] = pred

df.plot(x='start_time', y=['x_vec','pred'])
plt.show()
# print(df)