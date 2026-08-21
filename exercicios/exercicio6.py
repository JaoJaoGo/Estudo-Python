# Exercício 1 — Gerenciador de tarefas
# Crie um programa com menu interativo (while True + break) que permita ao usuário: adicionar uma tarefa, remover uma tarefa pelo número, listar todas as tarefas numeradas, 
# sair do programa. Comece com uma lista vazia e use append(), pop() e enumerate().
lista = []

while True:
    print("\n1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        lista.append(tarefa)
    elif opcao == "2":
        if len(lista) == 0:
            print("Não há tarefas para remover!")
        else:
            tarefa = input("Digite o número da tarefa: ")
            lista.pop(int(tarefa) - 1)
    elif opcao == "3":
        for i, tarefa in enumerate(lista):
            print(f"{i + 1}. {tarefa}")
    elif opcao == "4":
        break
    else:
        print("\nOpção inválida!")

# Exercício 2 — Estatísticas de notas
# Peça ao usuário quantos alunos tem a turma. Depois, colete a nota de cada aluno e armazene numa lista. Ao final, exiba: a maior nota, a menor nota, a média da turma, 
# quantos alunos ficaram acima da média e quantos ficaram abaixo.
quantidade = int(input("Quantos alunos tem a turma? "))
notas = []

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")
print(f"Média: {sum(notas) / len(notas)}")

acima_media = 0
abaixo_media = 0

for nota in notas:
    if nota > sum(notas) / len(notas):
        acima_media += 1
    else:
        abaixo_media += 1

print(f"Alunos acima da média: {acima_media}")
print(f"Alunos abaixo da média: {abaixo_media}")

# Exercício 3 — Lista sem duplicatas
# Peça ao usuário 10 números e armazene numa lista. Depois, crie uma nova lista contendo apenas os valores únicos (sem repetições), usando um loop e if valor not in nova_lista.
# Exiba a lista original e a lista sem duplicatas.
numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

nova_lista = []
for numero in numeros:
    if numero not in nova_lista:
        nova_lista.append(numero)

print(f"Lista original: {numeros}")
print(f"Lista sem duplicatas: {nova_lista}")

# Exercício 4 — Ordenação manual
# Peça ao usuário 5 números e armazene numa lista. Sem usar sort() ou sorted(), ordene a lista do menor para o maior usando loops aninhados (algoritmo bubble sort). Exiba a lista
# antes e depois da ordenação.
numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print(f"Lista original: {numeros}")

for i in range(len(numeros)):
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(f"Lista ordenada: {numeros}")

# Exercício 5 — Jogo da forca (simplificado)
# Defina uma palavra secreta no código. Crie uma lista de underlines ["_", "_", "_", ...] com o mesmo tamanho da palavra. Em cada rodada, peça uma letra ao usuário.
# Se a letra existir na palavra, revele ela na posição correta da lista de underlines. Se não existir, conte como erro. O jogo termina quando o usuário acertar toda a palavra
# ou errar 6 vezes. Exiba o estado atual da palavra a cada rodada.
secret_word = "python"
word_display = ["_"] * len(secret_word)
rodada = 0
erros = 0
max_erros = 6

while erros < max_erros and "_" in word_display:
    print(f"Rodada {rodada + 1}")
    print(f"Palavra: {' '.join(word_display)}")
    letra = input("Digite uma letra: ")
    rodada += 1

    if len(letra) != 1:
        print("Digite apenas uma letra.")
        rodada -= 1
        continue
    elif letra in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letra:
                word_display[i] = letra
                print(f"\nLetra '{letra}' encontrada na posição {i + 1}")
    else:
        erros += 1
        print(f"\nLetra '{letra}' não encontrada!")
        print(f"Erros: {erros}/{max_erros}")

if "_" not in word_display:
    print("\nParabéns! Você ganhou!")
else:
    print("\nVocê perdeu!")