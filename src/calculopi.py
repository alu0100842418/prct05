#!/usr/bin/python
PI = 3.1415926535897931159979634685441852
n = int(raw_input('Numero de intervalos: '))
suma = 0
while n <= 0:
  print 'El numero debe ser mayor que 0'
  n = int(raw_input('Numero de intervalos: '))
for i in range (1,n+1):
  a = float(i-1)/n
  b = float(i)/n
  xi = (i-0.5)/n
  fxi = 4.0/(1.0 + xi*xi)
  print a, b, xi, fxi
  suma += fxi
  pi = float (suma)/n
print 'El resultado de la aproximacion es: ', pi
print 'La constante pi con 35 decimales: %1.35g' % PI