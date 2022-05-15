'''
Strings

Strings: dados do tipo texto - sequência de caracteres alfanuméricos
    tipo str
    função input()
        retorna um dado do tipo str
            funções úteis para conversão: int() e float()
    Operações úteis sobre str
        Função len(<string>) retorna o tamanho da string
        Concatenação utiliza-se o operador +
        Busca:
            if <substring> in <string>
        Métodos: 
            lower() para modificar as letras para minúsculo
            upper() para modificar as letras para maiúsculo
'''

nome = input("Digite seu primeiro nome: ")
print("tamanho do nome: ", len(nome))
sobrenome = input("Digite seu sobrenome: ")
print("tamanho do sobrenome: ", len(sobrenome))
print("concatenando nome e sobrenome")
nome_completo=nome+" "+sobrenome
print("nome completo: ", nome_completo)
print("tamanho do nome completo: ", len(nome_completo))
if sobrenome in nome_completo:
    print("O sobrenome", sobrenome, " está contido no nome completo", nome_completo)

print("tentando acessar alguma parte da string nome completo")
for i in range (len(nome_completo)):
    print("Elmento ",i," da string nome_completo é: ",nome_completo[i])

for i in nome_completo:
    print(i)