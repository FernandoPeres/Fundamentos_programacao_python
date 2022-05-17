# CONDICIONAL

'''numero=float(input("Digite um número: "))

if (numero < 10):
    print("número menor que 10")
else:
    if (numero > 10):
        print("Número maior que 10")
    else:
        print("Número igual a 10")
'''

numero=int(input("Digite um número: "))

if numero < 0:
    print("Número negativo!")
elif numero == 0:
    print("Número não negativo")
elif numero >= 0 and numero < 10:
    print("Número positivo menor que 10!")
elif numero >=10 and numero <100:
    print("Número positivo >= 10 e <100")
else:
    print("Número positivo >=100")
