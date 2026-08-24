'''Leia um número fornecido pelo usuário.
Se esse número for positivo,
apresente o dobro do valor digitado.
Se o número for negativo,
mostre uma mensagem dizendo que o número é inválido.'''
numero = int(input("digite um numero:"))
if numero > 0:
    dobro = numero *2
    print("dobro n° positivo:",dobro)

else:
    print("esse numero é invalido:")

