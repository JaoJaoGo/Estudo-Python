# Exercício 1 — Saudação personalizada
# Crie uma função saudar(nome, horario) que receba um nome e um horário ("manhã", "tarde" ou "noite"). Retorne a saudação
# apropriada: "Bom dia, [nome]!", "Boa tarde, [nome]!" ou "Boa noite, [nome]!". Se o horário não for reconhecido, retorne "Olá, [nome]!".
print("<<--===//| Exercício 1 |\\===-->>")
def saudar(nome, horario):
    if horario == "manhã":
        return f"Bom dia, {nome}!"
    elif horario == "tarde":
        return f"Boa tarde, {nome}!"
    elif horario == "noite":
        return f"Boa noite, {nome}!"
    else:
        return f"Olá, {nome}!"

print(saudar("João", "manhã"))
print(saudar("João", "tarde"))
print(saudar("João", "noite"))
print(saudar("João", "madrugada"))


# Exercício 2 — Calculadora simples
# Crie quatro funções: somar(a, b), subtrair(a, b), multiplicar(a, b) e dividir(a, b). A função dividir deve retornar "Erro: divisão por zero!" se b for 0. Depois, peça ao usuário
# dois números e uma operação (+, -, *, /), chame a função correta e exiba o resultado.
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

print("\n")
print("<<--===//| Exercício 2 |\\===-->>")

print(somar(1, 2))
print(subtrair(1, 2))
print(multiplicar(1, 2))
print(dividir(1, 2))
print(dividir(1, 0))


# Exercício 3 — Verificador de número primo
# Crie uma função eh_primo(n) que receba um número inteiro e retorne True se ele for primo, ou False caso contrário. Um número é primo se for maior que 1 e divisível apenas por 1 e por ele mesmo. Teste a função com vários números.
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("\n")
print("<<--===//| Exercício 3 |\\===-->>")

print(eh_primo(2))
print(eh_primo(3))
print(eh_primo(4))
print(eh_primo(5))
print(eh_primo(6))
print(eh_primo(7))
print(eh_primo(8))
print(eh_primo(9))
print(eh_primo(10))


# Exercício 4 — Estatísticas de lista
# Crie uma função estatisticas(lista) que receba uma lista de números e retorne uma tupla com quatro valores: (soma, média, maior, menor). Não use as funções built-in sum(), max() e min() — calcule tudo manualmente com loops.
def estatisticas(lista):
    soma = 0
    maior = lista[0]
    menor = lista[0]
    
    for i in lista:
        soma += i

        if i > maior:
            maior = i
        
        if i < menor:
            menor = i
    
    media = soma / len(lista)

    return (soma, media, maior, menor)

print("\n")
print("<<--===//| Exercício 4 |\\===-->>")

print(estatisticas([1, 2, 3, 4, 5]))
print(estatisticas([10, 20, 30, 40, 50]))
print(estatisticas([100, 200, 300, 400, 500]))

    
# Exercício 5 — Conversor de temperatura com funções
# Crie três funções: celsius_para_fahrenheit(c), fahrenheit_para_celsius(f) e celsius_para_kelvin(c). Depois, crie um menu interativo (while True) que permita ao usuário escolher
# a conversão desejada, digitar a temperatura e ver o resultado. Inclua uma opção para sair.
def celsius_para_fahrenheit(c):
    return c * 1.8 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) / 1.8

def celsius_para_kelvin(c):
    return c + 273.15

while True:
    print("\n")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Sair")
    print("=" * 20)
    opcao = int(input("Opção: "))

    if opcao == 1:
        c = float(input("\nDigite a temperatura em Celsius: "))
        print(f"{c}°C = {celsius_para_fahrenheit(c)}°F")
    elif opcao == 2:
        f = float(input("\nDigite a temperatura em Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_para_celsius(f)}°C")
    elif opcao == 3:
        c = float(input("\nDigite a temperatura em Celsius: "))
        print(f"{c}°C = {celsius_para_kelvin(c)}°K")
    elif opcao == 4:
        break
    else:
        print("Opção inválida!")