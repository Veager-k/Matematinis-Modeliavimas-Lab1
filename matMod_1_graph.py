import numpy as np
import matplotlib.pyplot as plt

#task 1
def func1Solved(x, C):
    return np.exp((C/np.sqrt(x))-1)

x_vals = np.linspace(0.1, 10, 2000)

C1 = [-0.5, 0, 0.5]

plt.plot(x_vals, func1Solved(x_vals, C1[0]), color="blue", label="C = "+str(C1[0]))
plt.plot(x_vals, func1Solved(x_vals, C1[1]), color="orange", label="C = "+str(C1[1]))
plt.plot(x_vals, func1Solved(x_vals, C1[2]), color="red", label="C = "+str(C1[2]))
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

#task 2
def func2Solved(x, C):
    return (x*(1-2*C+2*np.log(x)))/(4*C - 4*np.log(x))

C2 = [-0.5, 0, 0.5]

plt.plot(x_vals, func2Solved(x_vals, C2[0]), color="blue", label="C = "+str(C2[0]))
plt.plot(x_vals, func2Solved(x_vals, C2[1]), color="orange", label="C = "+str(C2[1]))
plt.plot(x_vals, func2Solved(x_vals, C2[2]), color="red", label="C = "+str(C2[2]))
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

#task 3
def func3Solved(x):
    return (3 * np.e / 2) * np.exp(-x**2) + 1/2

x_vals3 = np.linspace(-5, 5, 200)

plt.plot(x_vals3, func3Solved(x_vals3))
plt.plot(1, 2,'bo')
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()