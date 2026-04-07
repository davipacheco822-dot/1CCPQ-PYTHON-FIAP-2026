# exercicio_2
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("Par")
else:
    print("ímpar")

# exercicio_3
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print("O maior número é:", n1)
elif n1 < n2:
    print("O maior número é:", n2)
else:
    print("Os dois números são iguais")

# exercicio_4
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1+n2+n3+n4) / 4

print("Média" , media)

if media >= 7:
    print("Aprovado!")
elif media >= 5:
    print("Em recuperação")
else:
    print("Reprovado")
# exercicio_5
A = int(input("Digite um número: "))
B = int(input("Digite outro número: "))

if A % B == 0 or B % A == 0:
    print("São múltiplos!!")
else:
    print("Não são múltiplos")