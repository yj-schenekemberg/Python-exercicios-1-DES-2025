#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.

dias_01 = int(input("dias para o curdo 01"))
dias_02 = int(input("dias para o curso 02"))
dias_03 = int(input("dias para o curso 03"))

if dias_01 <0 or dias_02 <0 or dias_03 <0:
    print("erro números negativo")
else:
    soma = dias_01 + dias_02 + dias_03
    print(f"tempo total do projeto: {soma} dias")