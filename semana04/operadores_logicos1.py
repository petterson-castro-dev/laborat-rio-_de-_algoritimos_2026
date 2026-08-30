'''Uma equipe de corrida deseja premiar seus treinadores.
Faça um programa que leia o nome do treinador, seu salário atual e o tempo de serviço na equipe (em anos).
Se o treinador tem 5 anos ou mais de experiência e recebe até R$ 2.000,00, ele terá um aumento de 10%.
Nos demais casos, o aumento será de 5%.
Exiba o nome do treinador, o aumento concedido e o novo salário.'''

treinador = input("Digite o nome do treinador: ")
salario = float(input("Digite o salário atual do treinador: "))
tempo_servico = int(input("Digite o tempo de serviço na equipe (em anos): "))
if tempo_servico >= 5 and  salario <= 2.000:
    aumento = salario * 0.10
else:
    aumento= salario * 0.5
novo_salario = salario + aumento
print("nome do treinador:",treinador)
print("aumento consedido:",aumento)
print("novo salario R$:", novo_salario)


