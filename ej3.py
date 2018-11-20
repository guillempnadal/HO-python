#Los factores primos en 13195 son 5, 7, 13 y 29. Cual es el factor primo mas 
#grande en el numero 600851475143?

n = 600851475143
factoresprimos = []

while n>1:
  factorprimo=2
  while n%factorprimo!=0:
    factorprimo += 1
  factoresprimos.append(factorprimo)
  n=n/factorprimo

factormax=max(factoresprimos)

print(factoresprimos)
print(factormax)
