# Exercício 1 — Cadastro fixo
# Crie uma tupla com os 12 meses do ano. Peça ao usuário um número de 1 a 12 e exiba o nome do mês correspondente. Trate o caso de número fora do intervalo.
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

numero = int(input("Digite um número de 1 a 12: "))

if numero < 1 or numero > 12:
    print("Número inválido")
else:
    print(meses[numero - 1])


# Exercício 2 — Desempacotamento
# Crie uma tupla com 5 notas de um aluno. Desempacote a primeira e a última em variáveis separadas, e o restante em uma variável com *. Exiba a primeira nota, a última nota e a 
# média das notas do meio.
notas = (8.5, 7.0, 9.0, 6.5, 8.0)

primeira, *resto, ultima = notas

print(f"Primeira nota: {primeira}")
print(f"Última nota: {ultima}")
print(f"Média das notas do meio: {sum(resto) / len(resto)}")


# Exercício 3 — Conversão ida e volta
# Peça ao usuário 5 nomes e armazene numa lista. Converta para tupla e exiba. Depois peça qual nome deseja alterar (pelo índice) e qual o novo nome. Converta para lista, faça a
# alteração, converta de volta para tupla e exiba a tupla final.
nomes = []

for i in range(5):
    nomes.append(input("Digite um nome: "))

tupla_nomes = tuple(nomes)
print(tupla_nomes)

indice = int(input("Digite o índice do nome que deseja alterar: "))
novo_nome = input("Digite o novo nome: ")

lista_nomes = list(tupla_nomes)
lista_nomes[indice] = novo_nome
tupla_nomes = tuple(lista_nomes)
print(tupla_nomes)