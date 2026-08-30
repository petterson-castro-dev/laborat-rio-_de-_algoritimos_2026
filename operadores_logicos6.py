'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                              Até 5 Kg                 Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã              R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

morango = float(input("Digite os kg de morango: "))
maca = float(input("Digite os kg de maçã: "))

if morango <= 5:
    valor_morango = morango * 2.50
else:
    valor_morango = morango * 2.20

if maca <= 5:
    valor_maca = maca * 1.80
else:
    valor_maca = maca * 1.50

peso = morango + maca
total = valor_morango + valor_maca

if peso > 8 or total > 25:
    desconto = total * 0.10
    total = total - desconto

print("Valor a pagar:", total)