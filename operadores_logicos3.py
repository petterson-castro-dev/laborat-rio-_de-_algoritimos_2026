'''Um posto de gasolina deseja calcular descontos para seus clientes:
Se o cliente abastecer 20 litros ou mais e o valor total for maior que R$ 100,00, ele recebe 10% de desconto.
Caso abasteça pelo menos 20 litros mas o valor total seja menor ou igual a R$ 100,00, o desconto é de 5%.
Caso contrário, não há desconto.
O programa deve ler a quantidade de litros e o valor total, e informar o desconto aplicado e o valor final.'''

litros = float(input("Digite a quantidade de litros: "))
valor = float(input("Digite o valor total: "))

if litros >= 20 and valor > 100:
    desconto = valor * 0.10
    valor_final = valor - desconto

    print("Desconto de 10%")
    print("Valor do desconto:", desconto)
    print("Valor final:", valor_final)

elif litros >= 20 and valor <= 100:
    desconto = valor * 0.05
    valor_final = valor - desconto

    print("Desconto de 5%")
    print("Valor do desconto:", desconto)
    print("Valor final:", valor_final)

else:
    print("Não há desconto")
    print("Valor final:", valor)