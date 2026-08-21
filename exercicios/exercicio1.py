""" Exercício 1 — Criando variáveis e investigando tipos
Crie quatro variáveis (uma de cada tipo: int, float, str, bool) que descrevam você (nome, idade, altura, se é estudante). Use print() e type() para exibir o valor e o tipo de cada
uma."""

nome = "João Víctor"
idade = 23
altura = 1.75
is_estudante = False

print(f"Nome: {nome} - Tipo: {type(nome)}")
print(f"Idade: {idade} - Tipo: {type(idade)}")
print(f"Altura: {altura} - Tipo: {type(altura)}")
print(f"É estudante: {is_estudante} - Tipo: {type(is_estudante)}")


""" Exercício 2 — Converta e corrija
Dadas as variáveis abaixo (ambas são strings), converta-as para os tipos numéricos adequados, some-as e exiba o resultado:

valor1 = "50"
valor2 = "23.75"
Depois, corrija o código abaixo para que funcione sem erros de tipo:

nome = "Ana"
idade = 30
altura = 1.65

print("Nome: " + nome)
print("Idade: " + idade + " anos")
print("Altura: " + altura + "m")"""

valor1 = "50"
valor2 = "23.75"

nome = "Ana"
idade = 30
altura = 1.65

print(f"\nNome: {nome}")
print(f"idade: {idade}")
print(f"altura: {altura}\n")


""" Exercício 3 — Verdadeiro ou Falso?
Sem rodar o código, adivinhe o resultado de cada bool() abaixo. Depois confira:

print(bool(42)) -> True
print(bool("")) -> False
print(bool(" ")) -> True
print(bool(0)) -> False
print(bool("False")) -> True
print(bool(-1)) -> True
print(bool(None)) -> False

Exercício 4 — Formulário completo
Peça ao usuário nome, idade e profissão. Exiba tudo numa frase usando f-string: "Meu nome é [nome], tenho [idade] anos e trabalho como [profissão]."""
nome = input("Digite seu nome:" )
idade = int(input("Digite sua idade: "))
profissao = input("Digite sua profissão:")

print(f"\nMeu nome é {nome}, tenho {idade} anos e trabalho como {profissao}")