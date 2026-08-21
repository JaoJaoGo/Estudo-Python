# Exercício 1 — Troco da compra
# Peça ao usuário o valor do produto e o valor pago, depois calcule o troco em uma variável e imprima o texto abaixo:

# "Seu troco: R$ {variable}"
preco_produto = float(input("Digite o preço do produto: "))
valor_pago = float(input("Digite o valor pago: "))

troco = valor_pago - preco_produto
print(f"Seu troco: R$ {troco}")


# Exercício 2 — Conversor de tempo
# Converta uma quantidade de minutos em horas (inteiro) e imprima o valor.
minutos = int(input("\nDigite a quantidade de minutos:"))
horas = minutos // 60

print(f"{minutos} minutos equivalem a {horas} horas")


# Exercício 3 — Pode entrar na montanha russa?
# Valide se a pessoa tem pelo menos 12 anos e é maior que 1.50. Peça os dados para o usuário e retorne True ou False.
idade = int(input("\nDigite sua idade: "))
altura = float(input("Digite sua altura: "))

pode_entrar = idade >= 12 and altura > 1.50
print(f"Pode entrar na montanha russa: {pode_entrar}")


# Exercício 4 — Acumulador de gastos
# Acumule em uma variável 3 gastos do usuário (peça usando input) e mostre quanto falta para o orçamento de R$ 500.
total = 0

gasto1 = float(input("\nDigite o primeiro gasto: "))
total += gasto1
gasto2 = float(input("Digite o segundo gasto: "))
total += gasto2
gasto3 = float(input("Digite o terceiro gasto: "))
total += gasto3

orcamento = 500
falta = orcamento - total

print(f"Falta R$ {falta} para atingir o orçamento de R$ 500.")