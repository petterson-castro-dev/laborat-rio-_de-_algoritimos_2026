'''Faça um algoritmo para calcular o salário mensal de um funcionário.
Sabe-se que o funcionário recebe R$35,00 por hora,
faça um algoritmo que leia o total de horas trabalhadas no mês e apresente o salário final.
Se o salário for menor que R$1000,00 dê um aumento de R$300,00 no salário recebido,
senão apresente somente o resultado da multiplicação.'''
#if se for <1000 de 300 reais
valor_hora = 35
horas_trabalhadas = float(input("digite as horas:"))
salario = horas_trabalhadas * valor_hora
print("salario:",salario)
if salario < 1000:
    salario = salario + 300
    print("salarioo final:",salario)


