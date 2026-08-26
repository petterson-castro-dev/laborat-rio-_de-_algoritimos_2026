'''Uma organização de corrida de rua está oferecendo inscrições para a prova de 10 km com três opções de pagamento:
À vista.
Em 2 vezes.
Em 3 vezes.
O sistema deve ler o valor da inscrição, a opção de
pagamento escolhida pelo atleta e apresentar o 
valor de cada parcela (quando houver).'''

valor_inscrição = int(input("digite o valor:"))
opcao = int(input('''escolha a opção de pagamento:
1-Àvista
2-2vezes
3-3vezes
 Digite a opção'''))

if opcao == 1:
    print("À vista:",valor_inscrição)

elif opcao == 2:
    pagamento = valor_inscrição / 2
    print("em 2 vezes:",pagamento)

elif opcao == 3:
    pagamento = valor_inscrição / 3
    print("em 3 vezes :",pagamento)