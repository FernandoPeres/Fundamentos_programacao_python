'''
MATRIZES
Até aqui aprendemos a manipular apenas listas (arrays) simples:
    estrutura de dados unidimensinal
    contrada através de um único índice
Consegue imaginar as situações em que é necessário mais de um índice?
    tabelas, gráficos 3D, aplicações contábeis, processamento de imagens e visão computacional, 
    jogos, aplicações científicas, projetos de engenharia etc...

DEFINIÇÃO
    matrizes são estruturas de dados multidimensionais que necessitam de mais de um índice para serem manipuladas.
    são parecidas com listas
        semelhanças: os elementos de uma matriz são referenciados por um mesmo nome
        diferença: possuem dois ou mais índices
        Bidimensionais: um índice para linhas e outro índice para colunas
        multidimensionais: podem possuir 2, 3, ... k índices.

Definição matemática: uma matriz é um arranjo tabular de M x N valores, onde M é o número de linhas e N é o número de colunas.
Os elementos de uma matriz são acessados por dois índices:
    i - geralmente associado às linhas
    j - geralmente associado às colunas
    acesso a elementos: 
        <matriz>[<linha>][<coluna>]
        índices normalmente iniciam no zero
'''

mat = [] #inicializando minha matriz
print("adicionando primeira linha")
mat.append([1,2,3])
print(mat)
print("adicionando segunda linha")
mat.append([4,5,6])
print(mat)
print("adicionando terceira linha")
mat.append([7,8,9])
print(mat)

print("imprimindo valor separadamente, acessado pelos índices")
for i in range (3):
    for j in range (3):
        print("elemento mat[",i,"][",j,"]: ",mat[i][j])

matriz=[]
for i in range(3):
    linha=[]
    for j in range(3):
        print("Digite o elemento da linha ",i," coluna ",j)
        dado = int(input())
        linha.append(dado)
    matriz.append(linha)

print("imprimindo valor separadamente, acessado pelos índices")
for i in range (3):
    for j in range (3):
        print("elemento matriz[",i,"][",j,"]: ",matriz[i][j])
