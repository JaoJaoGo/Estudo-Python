# Exercício 1 — Classificador de idade
# Peça a idade do usuário e classifique:

# 0 a 12: "Criança"
 
# 13 a 17: "Adolescente"
 
# 18 a 59: "Adulto"
 
# 60 ou mais: "Idoso"
# Use if/elif/else e trate o caso de idades negativas com a mensagem "Idade inválida".
idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")


# Exercício 2 — Calculadora com menu
# Peça ao usuário dois números e uma operação (+, -, *, /). Realize a operação escolhida e exiba o resultado. Se a operação for / e o segundo número for 0, exiba "Erro: divisão por zero!". Se a operação não for reconhecida, exiba "Operação inválida".
print("Calculadora\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    if num2 == 0:
        print("Erro: divisão por zero!")
    else:
        print(num1 / num2)
else:
    print("Operação inválida")


# Exercício 3 — Triângulo válido
# Peça ao usuário três valores (lados de um triângulo). Verifique se eles formam um triângulo válido (cada lado deve ser menor que a soma dos outros dois). Se for válido, classifique: "Equilátero" (3 lados iguais), "Isósceles" (2 lados iguais) ou "Escaleno" (todos diferentes).
lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não é um triângulo válido")

# Exercício 4 — Faixa salarial de imposto
# Peça ao usuário seu salário bruto e calcule o desconto de imposto simplificado com base nas faixas abaixo. Exiba o salário bruto, o percentual aplicado, o valor do desconto e o salário líquido:

# Até R$ 1.900,00: isento (0%)
 
# De R$ 1.900,01 a R$ 2.800,00: 7,5%
 
# De R$ 2.800,01 a R$ 3.750,00: 15%
 
# De R$ 3.750,01 a R$ 4.600,00: 22,5%
 
# Acima de R$ 4.600,00: 27,5%

salario = float(input("Digite seu salário bruto: "))

if salario <= 1900:
    print("Isento")
elif salario <= 2800:
    print("7,5%")
elif salario <= 3750:
    print("15%")
elif salario <= 4600:
    print("22,5%")
else:
    print("27,5%")

