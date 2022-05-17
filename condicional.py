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

# TEMOS A OPÇÃO DE UTILIZAR PASS DENTRO DE UM CONDICIONAL 
# PASS NÃO FAZ NENHUMA ALTERAÇÃO.

numero2=int(input("digite outro número: "))
if numero2<0:
    print("pass")
    pass
elif numero2 == 0:
    print("número2 = 0")
else:
    print("número2 >0")