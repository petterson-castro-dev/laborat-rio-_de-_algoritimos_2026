'''Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas
(onde  h corresponde a altura): 
Homens: (72.7 ∗ h) − 58
Mulheres: (62, 1 ∗ h) − 44, 7'''

h = float(input("digite a altura:"))
genero = input("digite seu genero:")

if genero == "homem":
    resultado = 72.7 * h -58
    print("seu peso ideal é:",resultado)

elif genero == "mulher":
    resultado = 62.1 * h -44.7
    print("seu peso ideal é:",resultado)

else:
    print("genero invalido")

   



