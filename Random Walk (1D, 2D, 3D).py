# A drunken sailor, a drunken ant and a drunken bird


import numpy as np 
import random
import matplotlib.pyplot as plt 

# A Durnken sailor (1D)
# Origin-returning Probability Vs the Number of Walkers 

N = 100                        # Number of steps
x0 = 0                         # Let the start of the RW be 2 ( we will consider this as origin)

M = np.arange(1, 10001, 100)   # Number of walkers in the RW
m_ = []
for j in range(len(M)):
    m = 0
    for _ in range(M[j]):
        x = x0
        for i in range(N):
            r = np.random.random()
            if r < 0.5:
                x = x + 1
            elif r > 0.5:
                x = x - 1 

        if x == x0 or x == 1 or x == -1:
            m += 1
    m_.append(m/M[j])

plt.plot(M, m_)
plt.xlabel("M ( Number of Walkers )")
plt.ylabel("P (Probability of returning to origin)")
plt.title(f"1D Random Walk With {N} constant Steps")
plt.grid()
plt.show()


# P (=m/M) approaches a certain value (near 0.08) as we increase M. 
# here, P is the probability if returning to origin.
# M is the number of walkers for that itteration

# Origin-returning Probability Vs the Number of Steps 

x0 = 0     #  Let the start of the RW be 2 ( we will consider this as origin)
M = 100

N = np.arange(1, 1001, 1)  # Number of people in the RW
p = []
for j in range(len(N)):
    m = 0
    for _ in range(M):
        x = x0
        for i in range(N[j]):
            r = np.random.random()
            if r < 0.5:
                x = x + 1
            elif r > 0.5:
                x = x - 1 

        if x == 1 or x == -1 or x == 0:
        # if x == 0:
            m += 1
    p.append(m/M)
# print(sum(p))
plt.plot(N, p)
plt.xlabel("N (Number of steps)")
plt.ylabel("P (Probability of returning to origin)")
plt.title(f"1D Random Walk with {M} Constant Walkers")
plt.xscale("log")
plt.yscale("log")
plt.grid()
plt.show()


# P (=m/N) approaches Zero (0) as we increase N.

# A Drunken Ant (2D)
# Origin-returning Probability Vs the Number of Walkers 

N = 100
x0 = 0     #  Let the start of the RW be 2 ( we will consider this as origin)
y0 = 0

M = np.arange(1, 10001, 100)  # Number of people in the RW
p = []
for j in range(len(M)):
    m = 0
    for _ in range(M[j]):
        x = x0
        y = y0

        for i in range(N):
            r = np.random.random()
            if r < 0.25 and r > 0.0:
                x = x + 1
                
            elif r < 0.5 and r > 0.25:
                x = x - 1 
                
            elif r > 0.5 and r < 0.75:
                y = y + 1
                
            elif r > 0.75 and r < 1.0:
                y = y - 1
               
        if (x == 1 or x == -1 or x == 0) and (y == 1 or y == -1 or y == 0):
            m += 1

    p.append(m/M[j])

plt.plot(M, p)
plt.xlabel("M (Number of Walkers)")
plt.ylabel("P (Probability of returning to origin)")
plt.title(f"2D Random Walk with {N} Constant Steps")
plt.grid()
plt.show()


# Here, while increasing M, P approaches a certain value (near 0.030).

# Origin-returning Probability Vs the Number of Steps 

M = 100
x0 = 0     #  Let the start of the RW be 2 ( we will consider this as origin)
y0 = 0

N = np.arange(1, 1001, 1)  # Number of people in the RW
p = []
for j in range(len(N)):
    m = 0
    for _ in range(M):
        x = x0
        y = y0

        for i in range(N[j]):
            r = np.random.random()
            if r < 0.25 and r > 0.0:
                x = x + 1
                
            elif r < 0.5 and r > 0.25:
                x = x - 1 
                
            elif r > 0.5 and r < 0.75:
                y = y + 1
               
            elif r > 0.75 and r < 1.0:
                y = y - 1
                
        if (x == 1 or x == -1 or x == 0) and (y == 1 or y == -1 or y == 0):
            m += 1
    p.append(m/M)
# print(p)
plt.plot(N, p)
plt.xlabel("N")
plt.ylabel("P (m/M)")
plt.title(f"2D Random Walk with {M} Constant Walkers")
plt.xscale("log")
plt.yscale("log")
plt.grid()
plt.show()


# Again it approaches Zero (0) as we increase the number of steps.

# A Drunken Bird (3D)
# Origin-returning Probability Vs the Number of Walkers 

N = 100
x0 = 6     #  Let the start of the RW be 2 ( we will consider this as origin)
y0 = 10
z0 = 3

M = np.arange(1, 10001, 50)  # Number of people in the RW
p = []
for j in range(len(M)):
    m = 0
    for _ in range(M[j]):
        x = x0
        y = y0
        z = z0

        for i in range(N):
            r = np.random.random()
            if r < 0.167 and r > 0.0:
                x = x + 1
                
            elif r < 0.334 and r > 0.167:
                x = x - 1 
                
            elif r > 0.334 and r < 0.501:
                y = y + 1
                
            elif r > 0.501 and r < 0.668:
                y = y - 1
                
            elif r > 0.668 and r < 0.835:
                z = z + 1
                
            elif r > 0.835 and r < 1.0 :
                z = z - 1
                    
        if (x == 1 or x == -1 or x == 0) and (y == 1 or y == -1 or y == 0) and (z == 0 or z == 1 or z == -1):
            m += 1

    p.append(m/M[j])

plt.plot(M, p)
plt.xlabel("M (Number of Walkers)")
plt.ylabel("P (Probability of returning to origin)")
plt.title(f"3D Random Walk with {N} Constant Steps")
plt.grid()
plt.show()


# Here the Probability reaches a value in between 0.0005 and 0.0015

# Origin-returning Probability Vs the Number of Steps

M = 100
x0 = 0     #  Let the start of the RW be 2 ( we will consider this as origin)
y0 = 0
z0 = 0

N = np.arange(0, 1001, 1)  # Number of people in the RW
p = []
for j in range(len(N)):
    m = 0
    for _ in range(M):
        x = x0
        y = y0
        z = z0

        for i in range(N[j]):
            r = np.random.random()
            if  r > 0.0 and r < 0.167:
                x = x + 1
                
            elif r > 0.167 and r < 0.334:
                x = x - 1 
                
            elif  r < 0.501 and r > 0.334:
                y = y + 1
                
            elif r < 0.668 and r > 0.501:
                y = y - 1
                
            elif r < 0.835 and r > 0.668:
                z = z + 1
                
            elif r < 1.0 and r > 0.835:
                z = z - 1
                    
        if (x == 1 or x == -1 or x == 0) and (y == 1 or y == -1 or y == 0) and (z == 0 or z == 1 or z == -1):
            m += 1

    p.append(m/M)
# print(p)
plt.plot(N, p)
plt.xlabel("N (Number of Steps)")
plt.ylabel("P (Probability of returning to origin)")
plt.title(f"3D Random Walk with {M} Constant Walkers")
plt.xscale("log")
plt.yscale("log")
plt.grid()
plt.show()