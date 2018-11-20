#Cada termino en la serie de Fibonacci es generado a partir de la suma 
#de los dos terminos previos, empezando por 0 y 1. Los diez primeros 
#terminos seran: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. Considerando los 
#terminos de la serie de Fibonacci que son impares y por debajo de un 
#millon, encuentre la suma de dichos terminos.


n = 1000000
suma = 0
penultimo = 0
ultimo = 1
while ultimo<n:
  if ultimo%2!=0:
    suma += ultimo 
  temp = penultimo + ultimo
  penultimo = ultimo
  ultimo = temp
print(suma)
