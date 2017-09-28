import numpy as np
import matplotlib.pyplot as plt
import random as rand
L2_size = 3
alpha = 0.01
# 读取数据
def splitx(str):
    return list(map(float, str.split()[1:3]))
def splity(str):
    return float(str.split()[3:] == ['是'])
X = np.array(list(map(splitx, open('watermelon.txt').readlines()[1:])))
Y = np.mat(np.array(list(map(splity, open('watermelon.txt').readlines()[1:]))))
# 分类绘图
positive_x = []
negative_x = []
for x, y in zip(X, Y.T):
    if y:
        positive_x.append(x)
    else:
        negative_x.append(x)
positive_x = np.array(positive_x)
negative_x = np.array(negative_x)
plt.scatter(positive_x[:, 0], positive_x[:, 1], c='b', marker='o', s=15)
plt.scatter(negative_x[:, 0], negative_x[:, 1], c='r', marker='x', s=15)
# 实现算法
def Sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))
def calc_L(matrix):
    (x, y) = np.shape(matrix)
    return np.row_stack((np.mat(np.ones((1, y))), Sigmoid(matrix)))
def calc_A(matrix):
    return Sigmoid(matrix)
X1 = X[:, 0]
X2 = X[:, 1]
matrix_X = np.mat(X).T
(m, n) = np.shape(matrix_X)   # n为数据个数
X0 = np.mat(np.ones((1, n)))
matrix_L1 = np.row_stack((X0, matrix_X))  # 计算L1矩阵           (每组数据元素数+1) * n
Theta1 = np.mat(([rand.random(), rand.random(), rand.random()], [rand.random(), rand.random(), rand.random()] ,[rand.random(), rand.random(), rand.random()]))  # 初始化Theta1矩阵     L2_size * (每组数据元素数+1)
Theta2 = np.mat((rand.random(), rand.random(), rand.random(), rand.random()))  # 初始化Theta2矩阵     1 * L2_size+1
for i in range(100000):
    matrix_L2 = calc_L(Theta1 * matrix_L1)  # 计算L2矩阵           L2_size+1 * n
    A = calc_A(Theta2 * matrix_L2)
    E3 = A - Y   # 1 * n
    E2 = np.multiply((Theta2.T[1:,:] * E3), np.multiply(matrix_L2[1:,:], (1-matrix_L2[1:,:])))  # L2_size * n
    Theta2 = Theta2 - alpha * E3 * matrix_L2.T
    Theta1 = Theta1 - alpha * (E2 * matrix_L1.T)
x1 = np.arange(0, 0.8, .01)
x2 = np.arange(0, 0.6, .01)
x1, x2 = np.meshgrid(x1, x2)
f = Theta2[0,0] + Theta2[0,1]*Sigmoid(Theta1[0,0]+Theta1[0,1]*x1+Theta1[0,2]*x2) + \
    Theta2[0,2]*Sigmoid(Theta1[1,0]+Theta1[1,1]*x1+Theta1[1,2]*x2) + \
    Theta2[0,3]*Sigmoid(Theta1[2,0]+Theta1[2,1]*x1+Theta1[2,2]*x2)
plt.contour(x1, x2, f, 0)
plt.show()
