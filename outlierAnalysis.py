import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=[11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,12,10]
1.#Identifying outliers through z scores
# z_score=(data-mean)/standard deviation.
#the data points having the z score is >=3 are outliers

outliers=[]
def detect_outliers(data):
    threshold=3
    mean=np.mean(data)
    std=np.std(data)
    
    for i in data:
        z_score=(i-mean)/std
        if (np.abs(z_score)>threshold):
            outliers.append(i) 
        
    return outliers

outlier_points=detect_outliers(dataset)
print(outlier_points)


2.#Identifying outliers through interquartile range
#Interquartile range is the range between 2 quartiles of a data
#if any data point falls outside 1.5 times the IQR between the 1st and the 3rd quartile,it is an outlier

sorted(dataset)
q1,q3=np.percentile(dataset,[25,75])
print(q1)
print(q3)

IQR=q3-q1
lower_bound=q1-(1.5*IQR)
upper_bound=q3+(1.5*IQR)
print(lower_bound)
print(upper_bound)

outliers2=[]
def detect_outliers2(data):
    for i in data:
        if (i>upper_bound) or (i<lower_bound):
            outliers2.append(i)
            
        return outliers2
    
outlier_points2=detect_outliers2(dataset)
print(outlier_points2)
