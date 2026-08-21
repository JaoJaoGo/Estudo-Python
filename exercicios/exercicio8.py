# Exercício 1 — Removedor de duplicatas
# Peça ao usuário 8 números (podem repetir). Armazene numa lista. Depois, use set para criar uma versão sem duplicatas. Exiba: a lista original, o set sem duplicatas, quais
# números eram repetidos e quantas duplicatas havia.
numeros = []
numeros_repetidos = []
quantas_duplicatas = 0

for i in range(8):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)
    
    # se o número já estiver na lista, é duplicata
    if numero in numeros[:-1]:
        quantas_duplicatas += 1
        numeros_repetidos.append(numero)

numero_set = set(numeros)

print(f"Lista original: {numeros}")
print(f"Números repetidos: {numeros_repetidos}")
print(f"Quantas duplicatas: {quantas_duplicatas}")
print(f"Set sem duplicatas: {numero_set}")


# Solução do professor
numeros = []
for i in range(8):
    n = int(input(f"Digite o número {i + 1}: "))
    numeros.append(n)

unicos = set(numeros)

for n in numeros:
    if numeros.count(n) > 1:
        repetidos.add(n)

total_duplicada = len(numeros) - len(unicos)

print(f"Lista original: {numeros}")
print(f"Set sem duplicatas: {unicos}")
print(f"Números repetidos: {repetidos}")
print(f"Total de duplicatas: {total_duplicada}")