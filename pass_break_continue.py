numero = 10
#Utilizando break dentro de um while
while True:
    print(numero)
    numero=numero-1
    if numero ==3:
        print("numero = 3: continue")
        continue
    if numero==2:
        print("numero = 2: break")
        break

#Utilizando break dentro de um while
print("mudando print(numero) para depois do condicional if == 3: continue")
numero = 10
while True:
    numero=numero-1
    if numero ==3:
        print("numero = 3: continue\nObserve que o número 3 não é impresso!")
        continue #faz o loop retornar par o início.
    print(numero)
    if numero==2:
        print("numero = 2: break")
        break #faz o loop parar.


#Utilizando um pass

for i in range(10):
    pass
# não faz nada e permite que a implementação do for seja feita posteriormente
#permitindo que se prossiga com a codificação.
print("foi utilizado o pass dentro de um for")