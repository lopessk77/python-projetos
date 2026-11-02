preço = float(input("Qual é o preço do produto? R$ "))
desconto = preço * 5 / 100
novo = preço - desconto
print(f"O produto que custava {preço} , na promoção com desconto de 5% vai custar {novo:.2f}")