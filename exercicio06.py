# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e inform
acesso_plataforma = int(input("digite o horario que você esta tentamdo acessar a plataforma: "))
if acesso_plataforma  == 9:
    print("horario autorizado. ")
elif acesso_plataforma == 21:
    print("horario autorizado. ")
else:
    print("horario não autorizado.")
    
