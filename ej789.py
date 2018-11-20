import numpy as np
import matplotlib.pyplot as pp

#Defino un dominio mas chico  que el del enunciado, 
#para que quede mejor el grafico

x = np.arange(-3,3.1,0.1)

#Defino f, y encuentro su derivada y extremos

f = np.poly1d([1,1,-4,4])
fprima = np.polyder(f)
extremos = np.roots(fprima)

#Grafico

pp.figure()
pp.plot(x,f(x),label='y=f(x)')
pp.plot(x,fprima(x),label='y=df/dx')
pp.plot(extremos,f(extremos),'C0o',label='extremos de f')
pp.xlabel('x')
pp.ylabel('y')
pp.legend(loc='best')
pp.grid(alpha=0.5)
pp.show()
pp.close()

#Creo un archivo y guardo la tabla de valores de f

archivo = open('tabla.txt','w')
tabla = np.c_[x,f(x)]
np.savetxt(archivo,tabla,fmt='%f',delimiter='\t',header='x # f(x)')
archivo.close()
