# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.
consumo = int(input("Digite o consumo diário"))
if consumo >=100 :
    print("Alerta! seu consumo passou os 100gb")
else:
    print("Consumo adequado.")