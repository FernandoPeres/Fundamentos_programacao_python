'''
LISTAS
    Dados organizados em sequência
    Vários dados em uma variável de mesmo nome
        índice para acesso de cada posição
    Tipos de dados
        Geralmente são do mesmo tipo
        Permite armazenamento de tipos distintos

SINTAXE:

<nome_da_lista> = [<dado1>, <dado2>, <dado3>]

EXEMPLOS:

    lista1 = []
    lista2 = [10, 20, 30]
    lista3 = [3.14, 999, "teste"]

ADICIONANDO UM ÍTEM AO FINAL DE UMA LISTA

<nome_da_lista>.append(<dado>)

REMOVENDO O ÚLTIMO ELEMENTO DE UMA LISTA

aux = <nome_da_lista>.pop()
aux vai receber o último elemento da lista e esse elemento sairá da lista.


IDENTIFICANDO ELEMENTO QUE TERÁ SEU VALOR SUBSTITUÍDO


<nome_da_lista>[1]=99


'''

lista = [10,20,30]
print(lista)
print("Adicionando um valor ao final da lista: ")
lista.append(99)
print(lista)
print("Removendo valor final da lista: ")
lista.pop()
print(lista)
print("substituindo valor dentro da lista: ")
lista[1]=88
print (lista)
print("descobrindo o tamanho da lista, utlizando len(lista): ")
tamanho = len(lista)
print("tamanho da lista: ", tamanho)
#lista[tamanho]=100 #gera erro, pois o index está fora do range da lista, que nesse caso vai até 2
print (lista)
for i in range (len(lista)):
    print("Elemento da posição ",i, " é: ", lista[i])

del(lista[1])
print(lista)

print("Para acessar o último elemento da list utilizando o index -1")
print(lista[-1])
print("Para acessar o penúltimo elemento da list utilizando o index -2")
print(lista[-2])