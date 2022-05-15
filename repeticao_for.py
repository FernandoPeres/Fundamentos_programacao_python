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