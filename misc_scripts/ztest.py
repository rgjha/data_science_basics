import pandas as pd
import numpy as np
import scipy.stats as stats
from itertools import combinations
from scipy.stats import ttest_ind

x1 = [70, 80, 65, 42, 39, 92, 81, 54, 34, 56, 78, 92, 10, 95, 63, 55, 52, 58, 50, 61, 72, 73, 81, 82, 90, 42, 34, 42, 95, 82, 70, 70]
x2 = [70, 68, 69, 40, 80, 29, 50, 54, 34, 52, 67, 45, 50, 8, 50, 52, 52, 85, 40, 60, 72, 37, 17, 28, 70, 56, 34, 24, 80, 34, 80, 70]

#print(stats.zscore(x1))

t, p = ttest_ind(x1, x2)
print ("p-value is", p)
print ("t-value is", t)

# Higher values of the t-score indicate that a large difference exists between 
# the two sample sets. The smaller the t-value, the more similarity exists between the two sample sets.

'''
# 1-sample t test

# known population mean 
mu = 5

# Calculate the mean and standard error
mean = np.mean(a)
std_error = np.std(a) / np.sqrt(len(a))

# calculate t statistics
t0 = abs(mean - mu) / std_error
''' 

# From scratch 2-sample t test

# Calculate the mean and standard error
x1_bar, x2_bar = np.mean(x1), np.mean(x2)
n1, n2 = len(x1), len(x2)
var_x1, var_x2= np.var(x1, ddof=1), np.var(x2, ddof=1)

# pooled sample variance
pool_var = ( ((n1-1)*var_x1) + ((n2-1)*var_x2) ) / (n1+n2-2)

# standard error
std_error = np.sqrt(pool_var * (1.0 / n1 + 1.0 / n2))

# calculate t statistics
t2 = abs(x1_bar - x2_bar) / std_error
print ("Direct t2 value comp.", t2) 


if p < 0.05:
	print ("The null must go. Enough evidence to conclude that the scores of students in classA are significantly different from classB scores.")
else:
	print ("Failed to reject the null hypothesis")
