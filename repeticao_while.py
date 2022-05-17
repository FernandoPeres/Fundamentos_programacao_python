'''
Sintaxe de utilização básica do while

while <condicao>: #enquanto essa condição for verdadeira, ele vai repetir o bloco de comandos
    <bloco de comandos>
'''

i =0
print ("com incremento após a impressão")
while i<10:
    print("Aguarde", i)
    i=i+1
print ("com incremento antes da impressão")
i=0
while i<10:
    i=i+1
    print("Aguarde", i)

soma=0
print("repetir while enquanto a soma <= 100")
while soma<=100:
    numero=int(input("Digite um número para adicionar à soma: "))
    soma = soma + numero
    print("A soma é: ", soma)

