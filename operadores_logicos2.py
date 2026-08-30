'''Um engenheiro quer verificar se três forças podem manter um corpo em equilíbrio.
Faça um programa que leia três valores correspondentes às forças.
O sistema deve verificar se elas obedecem à condição de equilíbrio (a soma de duas deve ser maior que a terceira).
Todas devem ser verdadeiras, A + B > C AND A + C > B AND B + C > A
Caso positivo, classifique o equilíbrio como:
Simétrico → três forças iguais
Parcialmente simétrico → duas forças iguais
Assimétrico → três forças diferentes
Caso contrário, informe que não há equilíbrio.'''

a = float(input("Digite a primeira força: "))
b = float(input("Digite a segunda força: "))
c = float(input("Digite a terceira força: "))

if a + b > c and a + c > b and b + c > a:

    if a == b and b == c:
        print("Equilíbrio simétrico")

    elif a == b or a == c or b == c:
        print("Equilíbrio parcialmente simétrico")

    else:
        print("Equilíbrio assimétrico")

else:
    print("Não há equilíbrio")