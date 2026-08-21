# Exercício 1 — Cadastro de pessoa
# Crie um dicionário com os dados de uma pessoa: nome, idade, cidade e profissão. Exiba cada informação no formato "Campo: Valor" usando .items(). Depois, peça ao usuário uma
# chave e exiba o valor correspondente usando .get(), mostrando "Campo não encontrado." se a chave não existir.
print("<<--===//| Exercício 1 |\\===-->>")

pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo",
    "profissao": "Desenvolvedor"
}

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

chave = input("Digite uma chave: ")
print(pessoa.get(chave, "Campo não encontrado."))

print('\n')

# Exercício 2 — Contador de palavras
# Peça ao usuário uma frase. Percorra cada palavra da frase e use um dicionário para contar quantas vezes cada palavra aparece. Exiba o resultado ao final. 
# (Dica: use .get(palavra, 0) + 1 para incrementar o contador.)
print("<<--===//| Exercício 2 |\\===-->>")

frase = input("Digite uma frase: ")
palavras = frase.split()
contador = {}

for palavra in palavras:
    contador[palavra] = contador.get(palavra, 0) + 1

print(contador)

print("\n")

# Exercício 3 — Agenda de contatos
# Crie um programa com um menu (while True) que permita: (1) adicionar contato (nome e telefone), (2) buscar contato pelo nome, (3) listar todos os contatos, (0) sair.
# Use um dicionário onde a chave é o nome e o valor é o telefone.
print("<<--===//| Exercício 3 |\\===-->>")

agenda = {}

while True:
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Listar contatos")
    print("0 - Sair")
    print('=' * 30)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("\nDigite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        print("Contato adicionado com sucesso!")
    elif opcao == 2:
        nome = input("\nDigite o nome do contato: ")
        print(agenda.get(nome, "Contato não encontrado..."))
    elif opcao == 3:
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")
    elif opcao == 0:
        print("Saindo...\n")
        break
    else:
        print("Opção inválida!")

    print("\n")