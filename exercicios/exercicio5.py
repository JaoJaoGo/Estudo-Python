# Exercício 1 — Analisador de texto
# Peça ao usuário uma frase e exiba: quantos caracteres ela tem, quantas palavras, quantas vezes a letra "a" aparece (maiúscula ou minúscula), a frase em maiúsculas, a frase invertida.
frase = input("Digite uma frase: ")
print(f"Quantidade de caracteres: {len(frase)}")
print(f"Quantidade de palavras: {len(frase.split())}")
print(f"Quantidade de vezes que a letra 'a' aparece: {frase.lower().count('a')}")
print(f"Frase em maiúsculas: {frase.upper()}")
print(f"Frase invertida: {frase[::-1]}")

# Exercício 2 — Validador de e-mail simples
# Peça ao usuário um e-mail e verifique se ele é "válido" com as seguintes regras: contém exatamente um @, contém pelo menos um . depois do @, não começa com @, não termina com .. Exiba "E-mail válido" ou "E-mail inválido" com o motivo.
email = input("Digite um e-mail: ")

if email.count("@") != 1 or email.startswith("@") or email.endswith('.'):
    print("E-mail inválido")
else:
    print("E-mail válido")

# Exercício 3 — Formatador de nome
# Peça ao usuário seu nome completo (pode ter espaços extras e letras em qualquer formato). Limpe e formate o nome: remova espaços extras, converta para formato título. Exiba o nome formatado, as iniciais (ex: "J.S." para "João Silva") e o nome abreviado (ex: "João S.").
nome_completo = input("Digite seu nome completo: ")

nome_limpo = nome_completo.strip()
nome_titulo = nome_limpo.title()

partes = nome_titulo.split()
iniciais = "." .join([p[0] for p in partes]) + "."

abreviado = partes[0]
for parte in partes[1:]:
    abreviado += " " + parte[0] + "."

print(f"Nome formatado: {nome_titulo}")
print(f"Iniciais: {iniciais}")
print(f"Abreviado: {abreviado}")

# Exercício 4 — Cifra de César
# Peça uma mensagem e um número de deslocamento ao usuário. Crie uma versão cifrada onde cada letra é substituída pela letra N posições à frente no alfabeto. Exemplo com deslocamento 3: "abc" vira "def", "xyz" vira "abc". Dica: use ord() para obter o código numérico de um caractere e chr() para converter de volta.
mensagem = input("Digite a mensagem: ")
deslocamento = int(input("Digite o deslocamento: "))

cifrada = ""
for caractere in mensagem:
    if caractere.isalpha():
        base = ord("a") if caractere.islower() else ord("A") # 97 ou 65

        #Substrai a base para obter posição 0-25, soma o deslocamento, aplica % 26 para wrap-around, depois soma a base de volta
        novo = chr((ord(caractere) - base + deslocamento) % 26 + base)
        cifrada += novo
    else:
        cifrada += caractere # espaços, pontuação, números: copia sem cifrar

print(f"Mensagem cifrada: {cifrada}")

# Exercício 5 — Gerador de recibo
# Peça ao usuário 3 produtos com seus preços. Exiba um recibo formatado usando f-strings com alinhamento:

# Saída esperada:
# ================================
# TOTAL          R$    479.70
# ================================
produtos = []
for i in range(3):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do {nome}: "))
    produtos.append((nome, preco)) # Tupla: agrupa nome e preço do mesmo produto

total = sum(p[1] for p in produtos)

print("=" * 32)
print("       RECIBO DE COMPRA")
print("=" * 32)
print(f"{'Produto':<15} {'Preço':>10}")
print("-" * 32)
for nome, preco in produtos:
    print(f"{nome:<15} R$ {preco:>8.2f}")
print("-" * 32)
print(f"{'TOTAL':<15} R$ {total:>8.2f}")
print("=" * 32)