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

#inserindo valor
produto['codigo']= int(input("Digite o código do produto: \n"))
produto['descricao']= input("Digite a descrição do produto: \n")
produto['preco']= float(input("Digite o preço do produto: \n"))
produto['quantidade']= float(input("Digite a quantidade em estoque do produto: \n"))

'''
#mostrando valor
print("Código: ", produto['codigo'])
print("Descrição: ", produto['descricao'])
print("Preço: ", produto['preco'])
print("Quantidade em estoque: ", produto['quantidade'])
'''
print(produto.values)