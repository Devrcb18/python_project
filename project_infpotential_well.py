import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import h
from scipy.constants import m_e
l = int(input('length: '))
n = int(input('prinpl Quantum number: '))
a = float(input('Enter A(starting length) : '))
b = float(input('Enter b(ending length): '))
print("space (b-a) is the area of observation of probability")
if(a!=b and (a*b)>=0 and n>0 and l>0 and(b-a)>0 and (a<l and b<=l)):
  po=int(b-a)#space of observation
  k = n * np.pi / l #k
  v = np.sqrt(2.0 / l)
  c=int(po/2)
  x = np.linspace(a, b,c)
  psi = v * np.sin(k * x)#wave_function
  p = psi**2#probability density
  pf = ((b - a) / l) - (1 / (n * np.pi)) * (np.sin(k * b) - np.sin(k * a))#probability appplied over the region of a and b
  E=((n**2)*(h**2))/(8*m_e*l)#energy formula for a quantum particle in a box
else:
    print("your data seems to be invalid for calculations")
plt.subplot(1, 2, 1)    
plt.plot([n],[E],color='yellow',label='Energy',marker="o",markerfacecolor="red")    
plt.xlabel('n')
plt.ylabel('Energy(in j)')
plt.title('Energy')
plt.grid()
plt.legend()
plt.subplot(1, 2, 2)   
plt.plot(x, p, color='green', label='Probability Density',marker='.',markerfacecolor='red')
plt.xlabel('X (m)')
plt.ylabel('Probability Density')
plt.title('Probability density ')
plt.grid()
print(f"Probability of finding the particle between {a} and {b}: {pf:.3f}")
plt.legend()
plt.tight_layout()
plt.show()    
