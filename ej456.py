import numpy as np
import matplotlib.pyplot as pp
from scipy.optimize import curve_fit

#Creo el set de datos

x = np.array([7.5, 4.48, 8.6, 7.73, 5.28, 4.25, 6.99, 6.31, 9.15, 5.06])
y = np.array([28.66, 20.37, 22.33, 26.35, 22.29, 21.74, 23.11, 23.13, 24.68,
    21.89])

#Reordeno para que pyplot no me haga lío

orden = np.argsort(x)
x = x[orden]
y = y[orden]

#Ajusto un polinomio de grado 3

def ajuste(x,a,b,c,d):
  return a+b*x+c*x**2+d*x**3
popt,pcov = curve_fit(ajuste,x,y)

#Ploteo los datos y el ajuste

pp.figure()
pp.plot(x,y,'ro',label='datos')
pp.plot(x,ajuste(x,popt[0],popt[1],popt[2],popt[3]),label='ajuste')
pp.xlabel('x')
pp.ylabel('y')
pp.legend(loc='best')
pp.show()
pp.close()

