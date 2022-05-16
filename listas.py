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
#deletando um elemento usando o index 
del(lista[1])

print(lista)
lista = [10,20,30,40,50,60,10]
print("Para acessar o último elemento da list utilizando o index -1")
print(lista[-1])
print("Para acessar o penúltimo elemento da list utilizando o index -2")
print(lista[-2])
print("Para acessar o ante-penúltimo elemento da list utilizando o index -3")
print(lista[-3])
print("Para acessar o quarto elemento do final da lista para o início utilizando o index -4")
print(lista[-4])
#retornando o index se houver o elemento pesquisado dentro da lista
print("index do elemento 50:",lista.index(50))
try:
    print("index do elemento 90:",lista.index(90))
except:
    print("erro ao pesquisar elemento 90 na lista")

#Retornará o index se houver o termo pesquisado
print("index do número 10:",lista.index(10))
#retorna a quantidade de termos encontrados na lista
print("Quantidade de 10 encontrados na lista",lista.count(10))
# Para adicionar um elemento
lista.append(10)
print(lista)
# removendo da lista
print("removendo 10 da lista")
lista.remove(10) #remove a primeira ocorrência
print("Lista: ",lista)
print("removendo 10 da lista")
lista.remove(10)
print("Lista: ",lista)

# invertendo a lista
lista = [10,20,30,40,50,60]
print("Lista: ",lista)
print("Invertendo a ordem da lista: lista.reverse()")
lista.reverse()
print("Lista: ",lista)

# ordenando uma lista
lista2=[1,5,8,6,4,9,7,13,15964654]
print("lista2: ", lista2)
print("ordenando a lista com lista2.sort()")

lista3=lista2.sort()#lista2.sort() não retorna nenhum valor, apenas coloca a lista em ordem

print("lista2: ", lista2)
print("lista3: ", lista3)#retorna none pq não foi criado uma lista3 por .sort() não retorna valores

#ordenando letras - números entram em ordem se forem lidos como str
lista4=['a','d','j','ui','9','fg','1','sdfg','h','w','r','h']
print("lista4: ", lista4)
lista4.sort()# só coloca em ordem listas com mesmo tipo de variável
print("lista4: ", lista4)
