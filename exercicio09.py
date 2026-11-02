largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
print(f"sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².")
litro = area / 2
print(f"para pintar essa parede, voce precisará de {litro:.2f}L de tinta")
