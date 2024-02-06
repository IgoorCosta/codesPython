import math

print("Adicione os valores a, b e c da equação de segundo grau:")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

x = (b**2 - (2*a*c))

if (x >= 0):
  delta = math.sqrt(x)
  print("As duas raizes da equação são", ((-b + delta)/2*a), "e", ((-b - delta)/2*a))

else: 
  print("Não tem raiz real")
