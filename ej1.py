#Si hacemos una lista de todos los numeros naturales debajo de 10 que 
#sean multiplos de 3 o 5 obtendriamos 3, 5, 6 y 9. La suma de los 
#multiplos es 23. Encuentre la suma de todos los multiplos de 3 o 5 
#debajo de 1000.

multiplos3 = range(0,1000,3)
multiplos5 = range(0,1000,5)
multiplos3y5 = range(0,1000,15)
suma=sum(multiplos3)+sum(multiplos5)-sum(multiplos3y5)
print(suma)
