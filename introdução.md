# 📘 Estrutura Básica de um Programa em Python

## 🎯 Objetivo:
Entender a **estrutura de código Python**, com foco em **indentação**, **blocos de código**, e **particularidades** da linguagem.  

---

## 🧱 1. Estrutura Geral

Diferente de outras linguagens como C, Java ou JavaScript, **Python não usa chaves `{}` para definir blocos de código.**  
Em vez disso, usa **indentação (espaço no início da linha)** para organizar os blocos.

### ✅ Exemplo correto:
```python
idade = 18

if idade >= 18:
    print("Maior de idade")
    print("Pode tirar carteira de motorista")
```

### ❌ Exemplo incorreto (sem indentação):
```python
idade = 18

if idade >= 18:
print("Maior de idade")  # Erro de identação
```

---

## 🔠 2. O que é Indentação?

Indentação é o **espaço ou tabulação** usada no início de uma linha para indicar que ela pertence a um bloco.  
Por padrão, recomenda-se usar **4 espaços** por nível de indentação.

```python
# Bloco dentro do if
if True:
    print("Linha indentada")  # 4 espaços à frente

# Fora do bloco
print("Linha fora do if")
```

---

## ⚙️ 3. Regras de Indentação em Python

1. **Sempre que abrir uma estrutura (como `if`, `for`, `while`, `def`, etc), indente a próxima linha.**
2. **Todos os comandos dentro do mesmo bloco devem ter a mesma indentação.**
3. **Não misture TAB e espaços** – isso gera erro.

---

## 🔄 4. Exemplo com várias estruturas

```python
numero = 5

if numero > 0:
    print("Número positivo")
    for i in range(numero):
        print("Contagem:", i)
else:
    print("Número negativo ou zero")
```

- O `print("Número positivo")` está dentro do `if`
- O `for` também está dentro do `if`
- O `print("Contagem:", i)` está dentro do `for`
- O `print("Número negativo ou zero")` está dentro do `else`

---

## 💡 Dicas 

- Em editores como **VS Code, Thonny ou PyCharm**, a indentação costuma acontecer automaticamente.
- Se aparecer erro de `IndentationError`, revise os espaços no início das linhas.
- Use **somente espaços ou somente tabulação**, nunca os dois misturados no mesmo projeto.

---

## 🧪 Exercício para praticar

```python
# Corrija este código com a indentação correta:

idade = int(input("Digite sua idade:"))

if idade >= 18:
print("Você é maior de idade")
else:
print("Você é menor de idade")
```

### 🔧 Resposta esperada:
```python
idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
```


---




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
