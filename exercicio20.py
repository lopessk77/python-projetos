from math import radians,cos,tan,sin
angulo = int(input("Digite o ângulo que deseja: "))
print(f"O ângulo {angulo} tem o seno de {sin(radians(angulo)):.2f}")
print(f"O ângulo {angulo} tem o cosseno de {cos(radians(angulo)):.2f}")
print(f"O ângulo {angulo} tem a tangente de {tan(radians(angulo)):.2f}")
