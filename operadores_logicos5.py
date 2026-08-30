'''A cidade está prestes a sediar a Corrida Anual dos Campeões, e os organizadores precisam saber se você está preparado para participar.
Um programa fará 5 perguntas sobre sua preparação:
Você treinou regularmente nas últimas semanas?
Participou de treinos longos (acima de 10 km)?
Seguiu uma dieta especial para a corrida?
Já competiu em provas oficiais neste ano?
Conta com acompanhamento de treinador ou equipe?
De acordo com suas respostas "Sim" ou "Não", o sistema deve classificá-lo:
2 respostas positivas → Você é classificado como Participante Casual (ainda precisa de mais treino).
3 ou 4 respostas positivas → Você é classificado como Atleta Competitivo (tem boas chances de se destacar).
5 respostas positivas → Você é classificado como Atleta de Elite (pronto para o pódio!).
Menos de 2 respostas positivas → Você é classificado como Não Preparado (talvez seja melhor assistir da arquibancada este ano).'''

resposta1 = input("Você treinou regularmente nas últimas semanas? ")
resposta2 = input("Participou de treinos longos acima de 10 km? ")
resposta3 = input("Seguiu uma dieta especial para a corrida? ")
resposta4 = input("Já competiu em provas oficiais neste ano? ")
resposta5 = input("Conta com acompanhamento de treinador ou equipe? ")

positivas = 0

if resposta1 == "Sim" or resposta1 == "sim":
    positivas = positivas + 1

if resposta2 == "Sim" or resposta2 == "sim":
    positivas = positivas + 1

if resposta3 == "Sim" or resposta3 == "sim":
    positivas = positivas + 1

if resposta4 == "Sim" or resposta4 == "sim":
    positivas = positivas + 1

if resposta5 == "Sim" or resposta5 == "sim":
    positivas = positivas + 1


if positivas < 2:
    print("Não Preparado")
    print("Talvez seja melhor assistir da arquibancada este ano.")

elif positivas == 2:
    print("Participante Casual")
    print("Ainda precisa de mais treino.")

elif positivas == 3 or positivas == 4:
    print("Atleta Competitivo")
    print("Tem boas chances de se destacar.")

else:
    print("Atleta de Elite")
    print("Pronto para o pódio!")