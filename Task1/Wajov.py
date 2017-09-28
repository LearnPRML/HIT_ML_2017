import numpy as np
import matplotlib.pyplot as plt
global a, b
def f(x):
	return a * x + b
def sum1():
	ans = 0
	for i in range(100):
		ans += x[i] * (f(x[i]) - y[i])
	return ans / 100
def sum2():
	ans = 0
	for i in range(100):
		ans += f(x[i]) - y[i]
	return ans / 100
f1 = open('q2x.dat', 'r')
f2 = open('q2y.dat', 'r')
x = np.array(map(float, f1.read().split()))
y = np.array(map(float, f2.read().split()))
plt.figure(figsize = (10, 6), dpi = 80)
plt.xlim(-8, 14)
plt.ylim(-3, 3)
plt.title("Wajov's Graph for Task1")
for i in range(100):
	plt.scatter(x[i], y[i])
xpos = np.linspace(-7, 13, 1000)
step = 0.05
a = b = 0.0
c = a - step * sum1()
d = b - step * sum2()
plt.plot(xpos, f(xpos), color = 'red', linewidth = 0.5)
while (abs(a - c) > 1e-3 or abs(b - d) > 1e-3):
	a = c
	b = d
	plt.plot(xpos, f(xpos), color = 'red', linewidth = 0.5)
	c = a - step * sum1()
	d = b - step * sum2()
plt.plot(xpos, f(xpos), color = 'yellow', linewidth = 2.0, label = 'Target Function')
plt.legend(loc = 'upper left', frameon = True)
plt.savefig('Wajov.png')
