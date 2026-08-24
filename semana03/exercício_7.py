'''Peça o valor de uma compra.
Se o valor for maior que R$100,
aplique 10% de desconto.
Senão, não aplique desconto.'''
valor_compra = float(input("digite o valor:"))
if valor_compra >100:
    valor_final = valor_compra * 0.90
    print("valorCom_desc:",valor_final)

else:
    print("valor a pagar:",valor_compra)
