# Exercício 1 — Lista de compras
# Crie um programa que peça ao usuário itens de uma lista de compras (um por vez, até digitar "sair"). Salve todos os itens em um arquivo chamado compras.txt, um por linha.
# Ao final, leia o arquivo e exiba todos os itens na tela.
print("<<--===//| Exercício 1 |\\===-->>")

itens = []

while True:
    item = input("Digite um item (ou 'sair' para finalizar): ")
    if item == 'sair':
        break
    itens.append(item)

with open("compras.txt", "w") as file:
    for item in itens:
        file.write(item + "\n")
    
with open("compras.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\n")

#Exercício 2 — Contador de linhas
# Crie um programa que leia o arquivo compras.txt criado no exercício anterior e exiba: o número total de linhas, o primeiro item e o último item da lista.
print("<<--===//| Exercício 2 |\\===-->>")

with open("compras.txt", "r") as file:
    lines = file.readlines()

    print("Total de linhas: ", len(lines))
    print("Primeiro item: ", lines[0].strip())
    print("Último item: ", lines[-1].strip())

    print("\n")

# Exercício 3 — Diário
# Crie um programa de diário simples. Cada vez que rodar, ele pergunta o que o usuário quer escrever e acrescenta a entrada no arquivo diario.txt, precedida pela data atual
# (use from datetime import date e date.today()). Ao final, exiba todo o diário na tela.
print("<<--===//| Exercício 3 |\\===-->>")

from datetime import date

while True:
    entry = input("Digite uma entrada (ou 'sair' para finalizar): ")
    if entry == 'sair':
        break
    with open("diario.txt", "a") as file:
        file.write(f"{date.today()}: {entry}\n")
        
with open("diario.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\n")

# Exercício 4 — Copiar arquivo
# Crie um programa que leia o conteúdo de compras.txt e salve uma cópia em compras_backup.txt, adicionando a linha "--- Backup ---" no início do arquivo de destino.
print("<<--===//| Exercício 4 |\\===-->>")

with open("compras.txt", "r") as file:
    content = file.read()

with open("compras_backup.txt", "w") as file:
    file.write("--- Backup ---\n")
    file.write(content)

print("Backup criado com sucesso!\n")

# Exercício 5 — Registro de notas
# Crie um programa que peça o nome e a nota de 3 alunos e salve em notas.txt no formato Nome: X.X. Depois, leia o arquivo, some todas as notas e exiba a média da turma.
print("<<--===//| Exercício 5 |\\===-->>")

nota_sum = 0

for i in range(3):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))

    nota_sum += nota

    with open("notas.txt", "a") as file:
        file.write(f"{nome}: {nota:.1f}\n")

media = nota_sum / 3

with open("notas.txt", 'a') as file:
    file.write(f"Media da turma: {media:.1f}\n")

with open("notas.txt", 'r') as file:
    for line in file:
        print(line.strip())

print('\n')