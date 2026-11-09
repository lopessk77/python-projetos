distancia = int(input("Qual é a distância da sua viagem:"))
print(f"Você está prestes a começar uma viagem de {distancia :.1f}")

if distancia <= 200:
    preço = distancia * 0.50
    print(f"")