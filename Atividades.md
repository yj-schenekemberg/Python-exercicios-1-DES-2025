# 🐍 Exercícios de Programação em Python

## Exercício 01 – Comparação de Vendas

Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado.  
Ele registrou a quantidade vendida de dois produtos: maçãs e bananas.  

Agora, ele precisa escrever:  
Um programa que identifique e exiba qual deles teve maior venda.

Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais.  
Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

```python
vendas_macas = int(input("Digite o número de vendas de maçãs: "))
vendas_bananas = int(input("Digite o número de vendas de bananas: "))

if vendas_macas > vendas_bananas:
    print("Maçãs venderam mais.")
elif vendas_bananas > vendas_macas:
    print("Bananas venderam mais.")
else:
    print("Houve um empate nas vendas.")
```

---

## Exercício 02 – Tempo Total de Projeto

Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C.  
No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

```python
dias_a = int(input("Dias para a atividade A: "))
dias_b = int(input("Dias para a atividade B: "))
dias_c = int(input("Dias para a atividade C: "))

if dias_a < 0 or dias_b < 0 or dias_c < 0:
    print("Erro: valores de dias não podem ser negativos.")
else:
    total = dias_a + dias_b + dias_c
    print(f"Tempo total do projeto: {total} dias")
```

---

## Exercício 03 – Alerta de Temperatura

Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C.  
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

```python
temperatura = float(input("Digite a temperatura atual da sala (°C): "))

if temperatura > 25:
    print("Alerta: Temperatura acima do limite permitido!")
else:
    print("Temperatura dentro do limite.")
```

---

## Exercício 04 – Cálculo de IMC

Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas.

```python
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = peso / (altura ** 2)

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso normal.")
else:
    print("Acima do peso.")
```

---

## Exercício 05 – Controle de Orçamento

Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos.  
Ele estabeleceu um limite de R$ 3.000,00.

```python
despesas = float(input("Digite o total de despesas do mês (R$): "))

if despesas > 3000:
    print("Atenção: Você ultrapassou o limite do orçamento!")
else:
    print("Você está dentro do orçamento.")
```

---

## Exercício 06 – Verificação de Acesso

Mariana precisa de um programa que verifique se os funcionários podem entrar no escritório entre 8h e 18h.

```python
hora = int(input("Digite a hora atual (0–23): "))

if 8 <= hora <= 18:
    print("Acesso permitido.")
else:
    print("Acesso negado.")
```

---

## Exercício 07 – Média Final

Uma professora precisa de um programa que ajude a calcular a média final dos alunos.

```python
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média final: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")
```

---

## Exercício 08 – Cálculo de Pedágio

Fernanda quer calcular quanto pagará de pedágio com base na distância percorrida.

```python
distancia = float(input("Digite a distância percorrida (km): "))

if distancia <= 100:
    valor = 10
elif distancia <= 200:
    valor = 20
else:
    valor = 30

print(f"Valor do pedágio: R$ {valor:.2f}")
```

---

## Exercício 09 – Verificação Par ou Ímpar

Lucas está desenvolvendo um jogo e precisa verificar se um número é par ou ímpar.

```python
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

---

## Exercício 10 – Aprovação de Empréstimo

Pedro quer solicitar um empréstimo. As condições são:
- Renda mensal > R$ 2.000,00
- Parcela ≤ 30% da renda

```python
renda = float(input("Digite sua renda mensal (R$): "))
parcela = float(input("Digite o valor da parcela (R$): "))

limite_parcela = renda * 0.3

if renda > 2000 and parcela <= limite_parcela:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado.")
```
