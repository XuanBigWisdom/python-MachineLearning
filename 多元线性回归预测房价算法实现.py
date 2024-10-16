##多元线性回归预测房子的价格，构建一个房子价格的模型。
##ex1data2.txt中包含了房子价格的训练组。第一列是房子的尺寸（平方英尺），第二列是卧室的数量，第三列是房子的价格。
#-*- coding: UTF-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt

#加载数据
def load_exdata(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.split(',')
            current = [int(item) for item in line] #根据数据输入的不同确定是int 还是其他类型
            #5.5277,9.1302
            data.append(current)
    return data

data = load_exdata('ex1data2.txt');
data = np.array(data,np.int64)      #根据数据输入的不同确定是int 还是其他类型


#特征缩放
def featureNormalize(X):
    X_norm = X;
    mu = np.zeros((1,X.shape[1]))
    sigma = np.zeros((1,X.shape[1]))
    for i in range(X.shape[1]):
        mu[0,i] = np.mean(X[:,i]) # 均值
        sigma[0,i] = np.std(X[:,i])     # 标准差
#     print(mu)
#     print(sigma)
    X_norm  = (X - mu) / sigma
    return X_norm,mu,sigma
 
#计算损失
def computeCost(X, y, theta):
    m = y.shape[0]
#     J = (np.sum((X.dot(theta) - y)**2)) / (2*m)
    C = X.dot(theta) - y
    J2 = (C.T.dot(C))/ (2*m)
    return J2
 
#梯度下降
def gradientDescent(X, y, theta, alpha, num_iters):
    m = y.shape[0]
    #print(m)
    # 存储历史误差
    J_history = np.zeros((num_iters, 1))
    for iter in range(num_iters):
        # 对J求导，得到 alpha/m * (WX - Y)*x(i)， (3,m)*(m,1)  X (m,3)*(3,1) = (m,1)
        theta = theta - (alpha/m) * (X.T.dot(X.dot(theta) - y))
        J_history[iter] = computeCost(X, y, theta)
    return J_history,theta
     
 
iterations = 10000  #迭代次数
alpha = 0.01    #学习率
x = data[:,(0,1)].reshape((-1,2))
y = data[:,2].reshape((-1,1))
m = y.shape[0]
x,mu,sigma = featureNormalize(x)
X = np.hstack([x,np.ones((x.shape[0], 1))])
# X = X[range(2),:]
# y = y[range(2),:]
 
theta = np.zeros((3, 1))
 
j = computeCost(X,y,theta)
J_history,theta = gradientDescent(X, y, theta, alpha, iterations)
 
 
print('Theta found by gradient descent',theta)

def predict(data):
    testx = np.array(data)
    testx = ((testx - mu) / sigma)
    testx = np.hstack([testx,np.ones((testx.shape[0], 1))])
    price = testx.dot(theta)
    print('price is %d ' % (price))
 
predict([1650,3])
