import math
from math import sqrt   
oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = pow(oposto,2) + pow(adjacente,2)
print(f"A hipotenusa vai medir {(sqrt(hipotenusa)):.2f}")