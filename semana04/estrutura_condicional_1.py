'''Faça um algoritmo que leia a pontuação de dois times em uma partida. Mostre qual time venceu, qual perdeu ou se houve empate.'''
time1 = int(input("digite a pontuação:"))
time2 = int(input("digite a pontuação:")) 

if time1 > time2:
    print("time 1 venceu:")
    print("time 2 perdeu:")

elif time2 > time1:
    print("time 2 venceu:")
    print("time 1 perdeu:")

else:
    print("empate,vocês são uma vergonha:")