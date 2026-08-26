'''Durante a inscrição, o atleta pode escolher entre 3 kits diferentes.
Faça um algoritmo que leia a opção escolhida e o valor que o atleta está entregando em R$ e mostre o que ele receberá:
1 → Kit Básico: Número de peito + medalha - R$100,00
2 → Kit Plus: Número de peito + medalha + camiseta - R$120,00
3 → Kit Premium: Número de peito + medalha + camiseta + squeeze + boné - R$150,00
Ao final apresente se o valor foi suficiente, caso foi suficiente,
apresente a categoria do atleta e o troco (se houver),
caso contrário apresente uma mensagem informando a falta do valor.'''

print("1 - Kit Básico: Número de peito + medalha - R$100,00")
print("2 - Kit Plus: Número de peito + medalha + camiseta - R$120,00")
print("3 - Kit Premium: Número de peito + medalha + camiseta + squeeze + boné - R$150,00")

opcao = int(input("Escolha o kit: "))
valor_entregue = float(input("Digite o valor entregue: R$ "))

if opcao == 1:
    valor_kit = 100
    categoria = "Kit Básico"

elif opcao == 2:
    valor_kit = 120
    categoria = "Kit Plus"

elif opcao == 3:
    valor_kit = 150
    categoria = "Kit Premium"

else:
    print("Opção inválida.")
    valor_kit = 0

if valor_kit > 0:
    if valor_entregue >= valor_kit:
        troco = valor_entregue - valor_kit
        print("Valor suficiente!")
        print("Categoria:", categoria)
        print("Troco:", troco)

    else:
        falta = valor_kit - valor_entregue
        print("Valor insuficiente!")
        print("Falta:", falta)