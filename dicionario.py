'''
DICIONÁRIOS

    SIMILARES A LISTAS
        - Utilizam termos no lugar dos índices de uma lista
        - cada termo é associado a um conteúdo respectivo
            -assim como em uma lista, cada posição guarda um valor distinto
        - podem armazenar dados de tipos distintos
    
    sintaxe
    <nome_do_dicionario> = {
        '<termo1>':<dado1>,
        '<termo2>':<dado2>,
        ...
        '<termoN>':<dadoN>,
    }
'''

#criando estrutura
produto = {
    'codigo':0,
    'descricao':"",
    'preco':0.0,
    'quantidade':0
}
'''
#inserindo valor
produto['codigo']= int(input("Digite o código do produto: \n"))
produto['descricao']= input("Digite a descrição do produto: \n")
produto['preco']= float(input("Digite o preço do produto: \n"))
produto['quantidade']= float(input("Digite a quantidade em estoque do produto: \n"))
#imprimindo os valores inseridos como nos dicionários

print(produto)'''
# fazendo inserção com valores
produto['codigo']= '2'
produto['descricao']= '2'
produto['preco']= '2'
produto['quantidade']= '2'
#imprimindo depois da outra inserção
print(produto)
print("os valores foram substituídos")
#os valores são substituídos

#VAMOS CRIAR UM DICIONÁRIO COM NOMES E SEUS RESPECTIVOS TELEFONES

telefones = {'fernando':456465456, 'maria': 5677676776, 'joão':68576768}
print(telefones)

#para adicionar outra referência faremos: 
print("telefones['josé']=99999999")
telefones['josé']=99999999
print(telefones)

#retirando uma dessas referências
''' RETORNA ERRO POR NÃO ENCONTRAR O joao SEM ACENTO
print("del telefones[\"joao\"]")
del telefones["joao"]
print(telefones)
'''

print("del telefones[\"joão\"]")
del telefones["joão"]
print(telefones)