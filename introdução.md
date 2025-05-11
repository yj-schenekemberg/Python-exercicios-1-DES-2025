# 🧠 Aula: Fundamentos da Programação com Python

## 🎯 Objetivos:
- Compreender o conceito de variáveis em Python.
- Utilizar operadores aritméticos e lógicos.
- Escrever estruturas de repetição (`for`, `while`).
- Aplicar estruturas de controle (`if`, `else`, `elif`).

---

## 📝 1. Variáveis

### Conceito:
Variáveis armazenam valores na memória.

### Exemplos:
```python
nome = "Maria"
idade = 17
altura = 1.65
```

> 💡 Observação:
> - Python não exige declaração de tipo.
> - O tipo é inferido automaticamente.

---

## ➕ 2. Operadores

### Aritméticos:
```python
a = 10
b = 3
print(a + b)  # Soma
print(a - b)  # Subtração
print(a * b)  # Multiplicação
print(a / b)  # Divisão
print(a % b)  # Módulo
print(a ** b) # Exponenciação
```

### Relacionais:
```python
print(a > b)   # True
print(a == b)  # False
print(a != b)  # True
```

### Lógicos:
```python
x = True
y = False
print(x and y) # False
print(x or y)  # True
print(not x)   # False
```

---

## 🔁 3. Estruturas de Repetição

### `while`:
```python
contador = 0
while contador < 5:
    print("Contando:", contador)
    contador += 1
```

### `for`:
```python
for i in range(5):
    print("Passo", i)
```

---

## 🔀 4. Estruturas de Controle (Condicionais)

### `if`, `elif`, `else`:
```python
nota = 7

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

---

## 🧪 Exercícios

1. Crie um programa que peça a idade do usuário e diga se ele é maior de idade.
2. Escreva um programa que peça dois números e mostre a média.
3. Faça um contador de 1 a 10 usando `for`.
4. Monte uma calculadora simples com `if` e operadores (`+`, `-`, `*`, `/`).

---
