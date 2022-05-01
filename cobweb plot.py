# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import random
import math

def iterationFunction(x):
    return 3.81*x*(1-x)
function_str = r"$y = 3.81x(1-x)$"
x_0 = 0.6
times = 400
x_range = [0,1]

def arrowp(x_start,y_start,x_end,y_end,ax,fc="blue",ec="red"):
    ax.arrow(x_start,y_start,x_end - x_start,y_end - y_start,length_includes_head = True,head_width = 0.012,head_length = 0.015,fc = fc,ec = ec)
fig = plt.figure(figsize = (15,15*0.618))
ax = fig.add_subplot(111)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x_source_range = np.arange(x_range[0],x_range[1],0.001)
y_source_range = x_source_range*1
# zero_source_range = 0 * x_source_range
for i in range(0,x_source_range.shape[0]):
    y_source_range[i] = iterationFunction(x_source_range[i])
    
ax.set_xlim(x_range[0],x_range[1]) 
ax.set_ylim(np.min(y_source_range)-0.0,np.max(y_source_range)+0.1) 

plt.plot(x_source_range,x_source_range,color = "#33a3dc")
plt.plot(x_source_range,y_source_range,color = "lime")
# plt.plot(x_source_range,zero_source_range,color="grey",linestyle = ":")
plt.title(r"Cobweb plot",fontsize = 25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel(r"$x$",fontsize=20)
plt.ylabel(r"$y$",fontsize=25)
plt.legend([r"$y=x$",function_str],fontsize=20)

x = [[x_0,0]]
for i in range(0,times):
    x_0 = x[-1][0]
    x_1 = iterationFunction(x_0)
    x.append([x_0,x_1])
    x.append([x_1,x_1])

for i in range(0,times-1):
    arrowp(x[i][0],x[i][1],x[i+1][0],x[i+1][1],ax,fc="#843900",ec="#f05b72")
