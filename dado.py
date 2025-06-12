import random

input("Presione o enter para lançar o dado")

reultado = random.randint(1,6)

print(f" O dado rolou : {reultado}" );

if reultado == 6 :
print("Parabéns, você coneguiu")
