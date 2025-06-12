distancia = input(input("Digite a distancia: "))
tempo = int(input("DIgite o tempo:"))

velocidade = distancia / tempo

if velocidade < 5 :
    print("lento")
elif velocidade >=5 <=10:
    print("MOderado")
else:
    print("VElocidade rápida")