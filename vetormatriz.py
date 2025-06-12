alunos = ["Alice", "Bruno", "Carla" ]

dias = ["Seg", "Ter", "Quar", "Qui"]

reservas = [["Ausente"for _ in dias]for _ in alunos ]

print("preencha com 'S' para presença e'X'para a ausência:")

for i, aluno in enumerate (alunos):
    print(f"\nAluno: {aluno}")
    for j, dia in enumerate(dias):
        entrada  = input(f"{dia}: ")  