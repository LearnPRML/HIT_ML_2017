import numpy as np
import matplotlib.pyplot as plt
import copy
import random
from functools import reduce

def Sum(f, tms):
	res = [f(each[0], each[1], tms) for each in point]
	return reduce(lambda x, y : x+y, res, 0)

def Dis(x, y):
	res = 0
	for idx, ag in enumerate(theta):
		res += ag * x**idx
	return res - y

def Diff(x, y, tms):
	if tms == 0:
		return Dis(x, y)
	else:
		return Dis(x, y) * (x**tms) * tms

def Err():
	res = 0
	for pt in point:
		res += Dis(pt[0], pt[1])**2
	return res

X = [float(x.strip()) for x in open("q2x.dat").readlines()]
Y = [float(x.strip()) for x in open("q2y.dat").readlines()]


point = list(zip(X, Y))
# theta = [0, 0, 0, 0, 0]
# step = [1e-2, 1e-4, 1e-6, 1e-9, 1e-13]
theta = [0, 0]
step = [1e-4, 1e-4]

for i in range(1000):
	if i % 100 == 0:
		x = np.linspace(min(X), max(X), 1000)
		y = [Dis(each, 0) for each in x]
		plt.plot(x, y, "--b")

	partial = [Sum(Diff, each) for each in range(len(theta))]
	theta = list(map(lambda t, p: t - p, theta, list(map(lambda x, y :x*y, step, partial))))
	print(Err())

plt.scatter(X, Y, c='r', s=10, marker='o')
plt.title("MMMMMua's Graphics")
plt.show()
plt.savefig("MMMMMua.pdf")


