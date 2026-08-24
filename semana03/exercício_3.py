'''Um motorista deseja colocar no seu tanque X reais de gasolina.
Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento,
e exibir quantos litros ele conseguiu colocar no tanque.'''

print("~~~~posto de gasolinna~~~~")
valor_abastecer = int(input("valor que deseja abastecer:"))
preco_por_litro = float(input("digite o preco:"))
litros = valor_abastecer / preco_por_litro
print("litros:",litros)
