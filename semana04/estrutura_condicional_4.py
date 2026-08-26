'''Um cinema está automatizando a venda de ingressos.
O sistema deve ler o valor base do ingresso e a opção escolhida pelo cliente:
1- Ingresso normal (valor cheio)
2- Estudante (50% de desconto)
3- Criança até 12 anos (paga 40% do valor)
4- Idoso (paga 60% do valor)
O programa deve calcular e mostrar o valor a ser pago.'''

print("1-ingresso normal: valor cheio")
print("2-Estudante: 50% desconto")
print("3-Criança até 12 anos: paga 40% do valor")
print("4-Idoso: paga 60% do valor")

opcao = int(input("Escolha a opção: "))

valor_base = float(input("Digite o valor base do ingresso: "))

if opcao == 1:
    print("Valor cheio:", valor_base)

elif opcao == 2:
    valor_final = valor_base * 0.50
    print("Valor do ingresso:", valor_final)

elif opcao == 3:
    idade = int(input("Digite a idade: "))

    if idade <= 12:
        valor_final = valor_base * 0.40
        print("Valor do ingresso:", valor_final)
    else:
        print("Essa opção é somente para crianças até 12 anos.")

elif opcao == 4:
    valor_final = valor_base * 0.60
    print("Valor do ingresso:", valor_final)

else:
    print("Opção inválida.")




