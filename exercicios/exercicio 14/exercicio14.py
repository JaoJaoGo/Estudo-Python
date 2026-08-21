import csv

# Exercício 1 — Criar CSV de produtos
# Crie um programa que peça ao usuário o nome, a quantidade e o preço de 4 produtos. Salve os dados em produtos.csv com cabeçalho nome,quantidade,preco. Use DictWriter.
print("<<--===//| Exercicio 1 |\\===-->>")

with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["nome", "quantidade", "preco"])
    escritor.writeheader()

    for i in range(4):
        nome = input("\nDigite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        preco = float(input("Digite o preço do produto: "))

        escritor.writerow({"nome": nome, "quantidade": quantidade, "preco": f"R$ {preco:.2f}"})

print('\n')

# Exercício 2 — Ler e filtrar
# Leia o arquivo produtos.csv criado no exercício anterior e exiba apenas os produtos com preço acima de 50 reais. Use DictReader. Lembre-se de converter o preço para float.
print("<<--===//| Exercicio 2 |\\===-->>")

with open("produtos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        if float(linha['preco'].replace("R$", "")) > 50:
            print(linha)

print('\n')

# Exercício 3 — Relatório de turma
# Crie um programa que peça o nome e a nota de 5 alunos e salve em turma.csv. Depois, leia o arquivo e exiba: quantos foram aprovados (nota ≥ 7), quantos foram reprovados e a 
# média da turma.
print("<<--===//| Exercicio 3 |\\===-->>")

with open("turma.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["nome", "nota"])
    escritor.writeheader()

    for i in range(5):
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        escritor.writerow({"nome": nome, "nota": nota})

print('\n')

with open('turma.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    aprovados = 0
    reprovados = 0
    soma_notas = 0

    for linha in leitor:
        if float(linha["nota"]) >= 7:
            aprovados += 1
        else:
            reprovados += 1
        
        soma_notas += float(linha["nota"])

    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}")
    print(f"Média da turma: {(soma_notas / (aprovados + reprovados)):.2f}")

print('\n')

# Exercício 4 — Adicionar ao CSV
# Usando o arquivo turma.csv do exercício anterior, crie um programa que peça o nome e a nota de um novo aluno e acrescente o registro ao CSV sem apagar os existentes.
# Exiba a turma completa ao final.

with open("turma.csv", "a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["nome", "nota"])

    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    escritor.writerow({"nome": nome, "nota": nota})

print('\n')

with open("turma.csv", "r", encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)