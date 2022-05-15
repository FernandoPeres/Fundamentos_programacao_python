num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Selecione a opção no seguinte menu: ")
print("Selecione 1 para somar os números.")
print("Selecione 2 para subtrair os números.")
print("Selecione 3 para multiplicar os números.")
print("Selecione 4 para dividir os números.")

opcao = int(input("Digite sua escolha: "))

if (opcao == 1):
    print ("A soma dos dois números é: ", num1+num2)
elif (opcao ==2):
    print ("A subtração dos dois números é: ", num1-num2)
elif (opcao ==3):
    print ("A multiplicação dos dois números é: ", num1*num2)
elif (opcao ==4):
    if(num2!=0):
        print ("A multiplicação dos dois números é: ", num1/num2)
    else:
        print(num1, " não pode ser divido por ", num2)
else:
    print("Opção inválida")