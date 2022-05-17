# utilizando for

''' 
for é uma forma de repetição por contagem.
forma:
    for <variavel> in range (<inicio>, <fim>, <passo>):
        <bloco de comandos>

OBS.: <passo> pode ser incremento ou decremento, de acordo com a necessidade
'''


print("Com incremento: ")
for i in range(0, 10, 1):
    print("Aguarde!", i)

print("Com decremento: ")
for j in range (10, 0, -1):
    print("Aguarde! ", j)

'''
Por padrão a função range():
tem 0 como valor de início da variável 
tem +1 como valor da variável de incremento.
'''

print("Com incremento, usando valor padrão para início e incremento: ")
for i in range(10):
    print("Aguarde!", i)

#Utilizando o for para percorrer e imprimir cada letra de uma string
nome = "fernando"
print(nome)

# inprimindo a letra de acordo com o indice atribuído
print("for i in range(len(nome)):")
print("     print(nome[i])")
for i in range(len(nome)):
    print(nome[i])

# utilizando o for de outra maneira
print("for letra in nome):")
print("     print(letra)")
for letra in nome:
    print(letra)

# utilizando o for para percorrer e imprimir uma lista
lista=['a', 'e', 'i', 'o', 'u']
print("lista=['a', 'e', 'i', 'o', 'u']")

print("for i in range(len(lista)):")
print("     print(lista[i])")
for i in range (len(lista)):
    print(lista[i])
# podemos fazer referencia direta aos elementos da lista
print("for valor in lista):")
print("     print(lista)")
for valor in lista:
    print(valor)