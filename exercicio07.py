media1 = float(input("digite a primeira media: "))
media2 = float(input("digite a segunda media: "))
media3 = float(input("digite a terceira media: "))

soma = media1 + media2 + media3 

media = soma / 3

if media >= 7 :
    print("aprovado")
elif media >= 5:
    print("em treinamento") 
else:
     print("reprovado")
