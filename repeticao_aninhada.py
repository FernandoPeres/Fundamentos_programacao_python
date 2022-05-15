'''
Imagine uma estrutura de repetição do tipo while
Considere que, dentro do bloco de comandos desta estrutura, foi inserida outra estrutura de repetição do tipo while

teríamos:

while <condicao1>:
    while <condicao2>:
        <bloco de comandos>

PODERÍAMOS TER OUTRO TIPO DE REPETIÇÃO ANINHADA

for <var1> in range (<inicio1>, <fim1>, <incremento1>):
    for <var2> in range (<inicio2>, <fim2>, <incremento2>):
        <bloco de instruções>

'''

for i in range (3):
    alu=i
    print("Aluno ", alu+1)
    for j in range (2):
        print("Digite a nota ", j+1,": ")
        nota = float(input())

'''
UTILIDADES DAS ESTRUTURAS DE REPETIÇÃO

    CONTADORES
        Variável utilizada em conjunto com um laço para contar o número de vezes que um evento ocorreu
    ACUMULADORES
        Variável para somar uma série de números
    VETORES
        Controlar o índice do vetor
    MATRIZES
        Controlar o acesso a linhas e colunas
    ALGORITMOS ITERATIVOS
    
'''