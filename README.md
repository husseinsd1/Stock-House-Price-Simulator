# Stock-House-Price-Simulator
Uses linear regression to predict house prices in Boston and Monte Carlo simulations to simulate stock movements.

More on linear regression and Monte Carlo simulations can be read here: 

https://machinelearningmastery.com/linear-regression-for-machine-learning

https://www.investopedia.com/terms/m/montecarlosimulation.asp


# Dependencies
- Python 3: https://www.python.org/downloads/
- Pandas: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
- NumPy: https://numpy.org/install/
- SciKit-Learn: https://scikit-learn.org/stable/install.html
- Pandas-DataReader: https://pypi.org/project/pandas-datareader/
- DateTime: https://pypi.org/project/DateTime/
- MatPlotLib: https://matplotlib.org/stable/users/installing.html

# Download
Download *stock.py* for Monte Carlo simulations on stocks, and *house.py* for linear regression on house prices. 

# Stock.py
Once you've downloaded the file, run it.

- - - -

```Enter the stock code: ```

Enter the code of the stock you would like to run simulations on. A list of stock codes can be found here: https://stockanalysis.com/stocks/

- - - -


```Enter the number of simulations (higher numbers will take longer to run): ```

Depending on your device, too high of a number might take a long time to run. I recommend you start with 1000, and add or decrease depending on how long it took to run.

- - - -

```How many days into the future do you want the simulation to be: ```

This controls how far into the future the simulation will be. Note that there are approximately 253 trading days in a year, so to simulate 1 year into the future, you would enter 253. 

- - - -

The program will output a simulation plot and a frequency distribution. 

### Here's a sample trial

```Enter the stock code: tsla```

```Enter the number of simulations (higher numbers will take longer to run): 1000```

```How many days into the future do you want the simulation to be: 253```

##### Output:
https://imgur.com/a/3xCJXcf

*The red line in both graphs represent the current price of the stock*


# House.py
The linear regression model uses data on house prices in Boston extracted from scikit-learn toy datasets (https://scikit-learn.org/stable/datasets/toy_dataset.html).

Data was split into 67% training and 33% testing. 

To view results simply run the file. 

