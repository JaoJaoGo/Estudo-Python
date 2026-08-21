# Exercício 1 — Tabuada
# Peça ao usuário um número e exiba a tabuada completa dele (de 1 a 10) usando for:
numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

print('\n')

# Exercício 2 — Somador com parada
# Use while para pedir números ao usuário repetidamente. Quando ele digitar 0, pare o loop e exiba a soma de todos os números digitados e quantos números foram inseridos (sem contar o zero).
total = 0
count = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    total += numero
    count += 1

print(f"Total: {total}")
print(f"Count: {count}\n")

# Exercício 3 — FizzBuzz
# Percorra os números de 1 a 30 com for. Para cada número:
 
# Se for múltiplo de 3, exiba "Fizz"
# Se for múltiplo de 5, exiba "Buzz"
# Se for múltiplo de 3 e 5, exiba "FizzBuzz"
# Senão, exiba o próprio número
# Dica: teste a condição de múltiplo de ambos primeiro.
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print('\n')

# Exercício 4 — Maior e menor
# Peça ao usuário 5 números (use for com range). Ao final, exiba qual foi o maior e o menor número digitado. Não use as funções max() e min() — controle com variáveis e if.
menor = 200000
maior = -200000

for i in range(5):
    numero = int(input("Digite um número: "))
    menor = min(menor, numero)
    maior = max(maior, numero)

print(f"Menor: {menor}")
print(f"Maior: {maior}")

# Exercício 5 — Desenho com loops
# Peça ao usuário um número N e desenhe um triângulo de asteriscos com N linhas usando loops aninhados:

# # Exemplo para N = 5:
# # *
# # **
# # ***
# # ****
# # *****
# Desafio extra: depois de funcionar, tente fazer o triângulo invertido (de N asteriscos diminuindo até 1).
numero = int(input("\nDigite um número: "))

for i in range(1, numero + 1):
    print("*" * i)
for i in range(numero - 1, 0, -1):
    print("*" * i)