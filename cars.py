# Cars
import pandas as pd
# Importing the dataset
car = pd.read_csv("C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\ProbCLT\\probability dataset\\Cars.csv")

# Graphical Representation
import matplotlib.pyplot as plt # mostly used for visualization purposes 
import numpy as np
plt.hist(car.MPG) #histogram
plt.boxplot(car.MPG) #boxplot
plt.bar(height = car.MPG, x = np.arange(len(car)))# initializing the parameter

# Normal Quantile-Quantile Plot
import scipy.stats as stats
import pylab
stats.probplot(car.MPG, dist="norm",plot=pylab)

# z-distribution
# cdf => cumulative distributive function; # similar to pnorm in R
stats.norm.cdf(740,711,29)  # given a value, find the probability

# ppf => Percent point function; # similar to qnorm in R
stats.norm.ppf(0.975,0,1) # given probability, find the Z value

#t-distribution
stats.t.cdf(1.98,139) # given a value, find the probability; # similar to pt in R
stats.t.ppf(0.975, 139) # given probability, find the t value; # similar to qt in R

