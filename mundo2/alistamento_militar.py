from datetime import datetime
ano = int(input("Ano de nascimento: "))

atual = datetime.now().year
idade = atual - ano

print(f"Quem nasceu em {ano} tem {idade} anos em {atual}")

if idade < 18:
    falta = 18 - idade
    alistamento = atual + falta
    print(f"Ainda falta {falta} anos para o alistamento")
    print(f"Você deve se alistar em {alistamento}")

elif idade == 18:
    print("Você deve se alistar esse ano")

else:
    passou = idade - 18
    alistamento = atual - passou
    print(f"Você deveria ter se alistado a {passou} anos atrás")
    print(f"Seu alistamento foi em {alistamento}")