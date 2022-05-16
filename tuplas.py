tuplas=("fernando","python", "estudo")
print(tuplas)

#acessando por index
print("tuplas[0]:",tuplas[0])
print("tuplas[1]:",tuplas[1])
print("tuplas[2]:",tuplas[2])

''' RETORNA ERRO POIS NÃO HÁ INDICE 3 NA NOSSA TUPLA
print("tuplas[3]:",tuplas[3])
'''
# imprimindo sequência de index das tuplas
print("tuplas[0:-1] ",tuplas[0:-1])
print("tuplas[0:2] ",tuplas[0:2])
print("tuplas[0:3] ",tuplas[0:3])
print("tuplas[0:len(tuplas)] ",tuplas[0:len(tuplas)])
#imprimindo soma de tuplas
print("tuplas+tuplas",tuplas+tuplas)
#imprimindo tuplas n vezes
print("tuplas*5",tuplas*5)

#verificando se há alguma ocorrencia dentro de tuplas
print("fernando" in tuplas) #retorna True
print("maria" in tuplas) #retorna False

#convertendo lista para tuplas

lista = [1,2,3,4,5,6]#lista formada de inteiros
print(lista)
tupla2=tuple(lista)#convertendo lista em tupla2
print("tupla2: ",tupla2)

print(tupla2.count("2")) #verificando quantos "2" existem na tupla
print(tupla2.count(2)) #verificando quantos 2 existem na tupla
#a tupla foi convertida de uma lista com inteiros, logo a tupla será de inteiros.

tupla4=(1,"3",3,3,4,5,"6")
print (tupla4)
print("print(tupla4.count(\"3\"))")
print(tupla4.count("3"))
print("print(tupla4.count('3'))")
print(tupla4.count('3'))
print("print(tupla4.count(1))")
print(tupla4.count(1))
print("print(tupla4.count(2))")
print(tupla4.count(2))
print("print(tupla4.count(3))")
print(tupla4.count(3))
#tentativa de impressão de um termo só
print("imprimindo termo por index")
print(tupla4[0])
print(tupla4[1])