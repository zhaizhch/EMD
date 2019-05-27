import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
from pyhht.emd import EMD
from pyhht.visualization import plot_imfs

data = pd.read_csv('C:\\Users\\ZhaiZhicheng\\Desktop\\AirPassengers.csv')

decomposer = EMD(data.iloc[:,1])               
imfs = decomposer.decompose()

plot_imfs(data.iloc[:,1],imfs,data.index)

#imfs(包括本征模函数（imf）和残差函数)和data原始数据保存在一个excel表中，顺序是第一本征模函数、……、最后本征模函数、残差函数、data原始数据
arr = np.vstack((imfs,data.iloc[:,1]))
dataframe = pd.DataFrame(arr.T)
dataframe.to_csv('G:/imf.csv',index=None,columns=None)