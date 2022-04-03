# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:54:11 2021

@author: Preethi Abraham
"""


import random;
import numpy as np;
import math;

population=list(range(0,10001)) #define the population
population[10000] #accessing the 10000th element in the array

n=[10, 20, 50, 100, 200, 500, 1000, 5000] #an array which contains number of samples

for i in range(len(n)):
    sample= random.sample(population, n[i]);
    mean=sum(sample)/n[i]
    std_dev=np.std(sample)
    std_error=std_dev/math.sqrt(n[i])
    #print('The sample', i+1, 'is', sample)
    print('sample',i+1,'mean=',mean, 'standard error=', std_error)