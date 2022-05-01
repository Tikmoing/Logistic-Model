# -*- coding: utf-8 -*-
'''
Logistic Model x_{n+1} = \mu x_{n} (1 - x_n)
'''
import math
import numpy as np
import matplotlib.pyplot as plt

#the iteration
def logistic(mu,initialValue,times):
    res = [initialValue,]
    for i in range(0,times):
        res.append(mu * res[-1] * (1 - res[-1]))
    return [res[-1],res]

#draw a diagram to represent the iteration
def iterationDiagram(mu,initialValue,times):
    [nouse,valueList] = logistic(mu,initialValue,times)
    iterationNumber = [i for i in range(0,times+1)]
    
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(14,14*0.618))
    
    plt.plot(iterationNumber,valueList,color="red",linewidth=2.0)
    
    plt.title(r"logistic model IterationDiagram ($\mu$=%f,$x_0$ = %f)"%(mu,initialValue),fontsize = 25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel(r"$iterTimes$",fontsize=20)
    plt.ylabel(r"$Value$",fontsize=25)

#bifurcationDiagram
def bifurcationDiagram(muRange = [2.6,4],initialValue = 0.6,times = 250,stepLength = 0.00001,color = 'b'):
    mu = np.arange(muRange[0],muRange[1],stepLength)
    length = mu.shape[0]
    res = np.array( [0.6 for i in range(0,length*(times+1))] )
    res.shape = (times+1,length)
    for i in range(1,times+1):
        res[i,:] = mu * (res[i-1,:] - res[i-1,:]*res[i-1,:]) 

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(14,14*0.618))
    
    for i in range(1,int(times * 0.1)):
        plt.scatter(mu,res[-i,:],color = color,s = 1)

    plt.title(r"logistic model bifurcation diagram initial value = 0.6",fontsize = 25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel(r"$\mu$",fontsize=20)
    plt.ylabel(r"$iteration value$",fontsize=25)

def lyapunovExponent(mu,initialValue,times):
    itervalue = initialValue
    res = 0
    for i in range(0,times):
        itervalue = mu * itervalue * ( 1- itervalue)
        res += math.log( abs( mu - 2 * mu * itervalue ) )
    
    return res / times
    
def lyapunovExponentDiagram(muRange=[3,4],initialValue = 0.6,times = 250 , stepLength = 0.00001 , color = 'b'):
    mu = np.arange(muRange[0],muRange[1],stepLength)
    res = []
    for i in range(0,mu.shape[0]):
        res.append( lyapunovExponent(mu[i],initialValue,times) )
        
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(14,14*0.618))
    
    plt.plot(mu,res,color = color)
    plt.title(r"logistic model lyapunov exponent diagram initial value = 0.6",fontsize = 25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel(r"$\mu$",fontsize=20)
    plt.ylabel(r"$Lyapunov Exponent$",fontsize=25)
