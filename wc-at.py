# WC
import pandas as pd
# Importing the data 
wc = pd.read_csv("C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\ProbCLT\\probability dataset\\wc-at.csv")

#Graphical Representation
import matplotlib.pyplot as plt # mostly used for visualization purposes 
import numpy as np

plt.hist(wc.Waist) #histogram
plt.hist(wc.AT) #histogram

plt.boxplot(wc.Waist) #boxplot
plt.boxplot(wc.AT) #boxplot
plt.bar(height = wc.Waist, x = np.arange(len(wc)))# initializing the parameter
plt.bar(height = wc.AT, x = np.arange(len(wc)))# initializing the parameter

#Normal Quantile-Quantile Plot
import scipy.stats as stats
import pylab
# Checking Whether data is normally distributed
stats.probplot(wc.Waist, dist="norm",plot=pylab)
stats.probplot(wc.AT, dist="norm",plot=pylab)

