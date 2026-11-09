from random import randint
from time import sleep
print("-=--=" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
num = int(input("Em que número eu pensei? "))
compu = randint(0,5)
print("PROCESSANDO...")
sleep(2)
if num == compu:
    print("Você acertou")
else:
    print(f"Eu ganhei, pensei no {compu} e não no {num}")