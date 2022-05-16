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
#somar uma string a outra - concatenar as strings

nome_completo=nome+" "+sobrenome

print("nome completo: ", nome_completo)

print("tamanho do nome completo: ", len(nome_completo))

#verificar se há alguma sequencia de caracteres dentro de uma string
pesquisar=str(input("digite para pesquisar: "))
if pesquisar in nome_completo:
    print("A string: ", pesquisar, " está contido no nome completo", nome_completo)

#verificação direta 
print("há a letra a no nome_completo?")
print("a" in nome_completo)# retorna true se houver a no nome_completo

#multiplicação de strings
nome="fernando"
print(nome*2)

'''
print("tentando acessar alguma parte da string nome completo")
for i in range (len(nome_completo)):
    print("Elemento ",i," da string nome_completo é: ",nome_completo[i])

for i in nome_completo:
    print(i)
#'''
