# step 1
# import libraries
import numpy as np
import pandas as pd

# libraries to grab the stock prices
import pandas_datareader as web
from datetime import datetime

# libraries to visualize the results
import matplotlib.pyplot as plt
import seaborn

# step 2
# set start date for correlation analysis and decide which stocks to correlate
start_date = datetime(2018, 1, 1)
end_date = datetime(2019, 1, 1)
list_of_stocks = ['AAPL', 'TWTR', 'FB', 'AMZN', 'GOOGL', 'MSFT', 'UBER']

# step 3
# create an empty array to store the stock prices in
stocks = []

#pull price for each stock symbol
for stock_ticker in list_of_stocks: 
    r = web.DataReader(stock_ticker, 'yahoo', start_date, end_date)
    # add a symbol column
    r['Stock Symbol'] = stock_ticker 
    stocks.append(r)

# combine data by concatenating into pandas dataframe
data_frame = pd.concat(stocks)
data_frame = data_frame.reset_index()
data_frame = data_frame[['Date', 'Stock Symbol', 'Close']]
data_frame.head()

# pivot the dataframe so that the stock symbols are the columns
data_frame_pivot = data_frame.pivot('Date','Stock Symbol','Close').reset_index()
data_frame_pivot.head()

# step 4
# use corr function to find the Pearson correlation coeffecient between each pair of 
# Pearson correlation: measure of the strength of the linear relationship b/w 2 variables
corr_data_frame = data_frame_pivot.corr(method='pearson')

# reset symbol as index (rather than 0-X)
corr_data_frame.head().reset_index()
del corr_data_frame.index.name
corr_data_frame.head(10)

# step 5
# visualize the data with a heat map
mask = np.zeros_like(corr_data_frame)
mask[np.triu_indices_from(mask)] = True

#generate plot
seaborn.heatmap(corr_df, cmap = 'RdYlGn', vmax = 1.0, vmin = -1.0 , mask = mask, linewidths = 2.5)
plt.yticks(rotation = 0) 
plt.xticks(rotation = 90) 
plt.show()
