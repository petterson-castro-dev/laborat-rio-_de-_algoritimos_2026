'''Faça um algoritmo que leia dois números distintos e apresente-os em ordem crescente.
Faça um algoritmo que leia o ano de nascimento de uma pessoa
e verifique se ela pode ou não votar (desconsidere o mês de nascimento).'''

#1°-
print("==ordem crescente==")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 < numero2:
    print(numero1, numero2)
else:
    print(numero2, numero1)


#2°-
print("===votos/politica===")
ano_de_nasc = int(input("digite o ano de nascimento:"))
idade = 2026 - ano_de_nasc

if idade>=18:
    print("pode votar:")

else:
    print("não pode:")
