import pandas_datareader.data as web
import pandas as pd
import datetime as dt
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from pandas_datareader._utils import RemoteDataError

style.use('dark_background')

# Set start and end date for time series
start = dt.datetime(2017, 1, 3)
end = date.today()

# Get stock prices
try:
    stock_code = input('Enter the stock code: ')
    prices = web.DataReader(stock_code, 'yahoo', start, end)['Close']
except (RemoteDataError, KeyError):
    stock_code = input('Enter a valid stock code: ')
    prices = web.DataReader(stock_code, 'yahoo', start, end)['Close']

# Gets number of simulations
try:
    num_sims = int(input('Enter the number of simulations (higher numbers will take longer to run): '))
except ValueError:
    print("Enter a valid number.")
    num_sims = int(input('Enter the number of simulations (higher numbers will take longer to run): '))

# Gets duration of simulation
try:
    num_days = int(input('How many days into the future do you want the simulation to be: '))
except ValueError:
    print("Enter a valid number.")
    num_days = int(input('How many days into the future do you want the simulation to be: '))

returns = prices.pct_change()

# Extract last price
last_price = prices[-1]

# Create dataframe for simulation
sim_df = pd.DataFrame()

# Perform simualtion
for x in range(num_sims):
    count = 0

    # Daily volatility
    daily_vol = returns.std()

    price_series = []

    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == num_days - 1:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    sim_df[x] = price_series

# Plot simulation outcome
fig = plt.figure()
fig.suptitle(f'Monte Carlo Simulation: {stock_code.upper()}')
plt.plot(sim_df)
plt.axhline(y=last_price, color='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price (USD)')
plt.show()

# Plot frequency distribution
fig2 = plt.figure()
fig2.suptitle(f'Frequency Distribution: {stock_code.upper()}')
plt.hist(sim_df.iloc[num_days - 1])
plt.axvline(last_price, color='r')
plt.xlabel('Price (USD)')
plt.ylabel('Frequency')
plt.show()