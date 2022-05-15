'''
RECURSIVIDADE
- Definição: O conceito de recursividade está relacionado a algo
  que pode sers definido em termos de si próprio.
    - Em programação: Recursividade é um mecanismmo que permite
      uma função chamar a si mesma direta ou indiretamente

Exemplo:
    1. Pai
    2. Avô - Pai do meu Pai
    3. Bisavô - Pai do meu Avô: Pai do Pai do meu Pai
    4. Trisavô - Pai do meu Bisavô: Pai do Pai do Pai do meu Pai


- O princípio da recursividade consistem em diminuir um problema,
sucessivamente, em problemas menores
    - De tanto diminuir o problema, chega em um ponto que o problma
      pode ser resolvido diretamente (por definição) - Depois,
      combinam-se as soluções!
- A função recursiva precisa ter duas partes:
    - Caso base:  determina que o problema está no menor tamanho 
      possível (não é possível diminuir mais)
        - solução direta
    - Chamada recursiva: que faz uma nova chamada da função transformando 
      o problema atual num problema menor


EXEMPLO:
    - A função Fatorial:
        - Na matemática, a função fatorial de número n, onde n
        pertence a Z+, é o resultado do produto de todos os inteiros
        positivos que são menores ou iguais ao próprio n
        - ou seja:
            n! = n x (n-1) x (n-2) x ... x 3 x 2 x 1
        exemplo:
        fatorial de 5:
            5 x 4 x 3 x 2 x 1 = 120

'''

def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n-1)


print(fat(6))