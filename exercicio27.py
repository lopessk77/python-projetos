frase = str(input("Digite uma frase: ")).strip().upper()
print(f"A letra A aparece {frase.count("A")} na frase")
print(f"A primeira letra apareceu na posição {frase.find("A")+1}")
print(f"A ultima letra apaereceu na posição {frase.rfind("A")+1}")