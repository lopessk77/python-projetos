dias = int(input("Quantos dias alugados:"))
km = int(input("Quantos Km rodados: "))
d = dias * 60
k = km * 0.15
total = d + k
print(f"O total a pagar é de R${total:.2f}")