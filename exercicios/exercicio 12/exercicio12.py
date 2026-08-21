# Exercício 1 — Criando um módulo de matemática
# Crie um arquivo chamado matematica_simples.py com três funções: soma(a, b), subtracao(a, b) e multiplicacao(a, b). Depois, crie um arquivo programa.py que importe essas funções
# e peça ao usuário dois números e uma operação. Execute a operação usando a função do módulo.
print("<<--===//| Exercício 1 |\\===-->>")

from matematica_simples import somar, subtrair, multiplicar

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))

operacao = input("Digite a operação (+, -, *): ")

if operacao == "+":
    print(somar(num1, num2))
elif operacao == '-':
    print(subtrair(num1, num2))
elif operacao == '*':
    print(multiplicar(num1, num2))
else:
    print("Operação inválida!")

print("\n")

# Exercício 2 — Módulo de conversões
# Crie um arquivo conversoes.py com funções para converter entre unidades: km_para_milhas(km), celsius_para_fahrenheit(c) e kg_para_libras(kg). Em outro arquivo, importe as
# funções e crie um menu interativo (while True) que permita ao usuário escolher a conversão desejada.
print("<<--===//| Exercício 2 |\\===-->>")

from conversoes import km_para_milhas, celsius_para_fahrenheit, kg_para_libras

while True:
    print("1. km para milhas")
    print("2. celsius para fahrenheit")
    print("3. kg para libras")
    print("4. Sair")
    print ('=' * 20)

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        km = float(input("Digite a distância em km: "))
        print(km_para_milhas(f"{km} m\n"))
    elif opcao == '2':
        celsius = float(input("Digite a temperatura em celsius: "))
        print(celsius_para_fahrenheit(f"{celsius} F\n"))
    elif opcao == '3':
        kg = float(input("Digite o peso em kg: "))
        print(kg_para_libras(f"{kg} lbs\n"))
    elif opcao == '4':
        break
    else:
        print("Opção inválida!\n")

print("\n")

# Exercício 3 — if __name__ == "__main__"
# Crie um módulo validadores.py com funções: eh_par(numero) que retorna True se o número for par, e eh_positivo(numero) que retorna True se for positivo. Adicione um bloco 
# if __name__ == "__main__": com testes para verificar se as funções funcionam corretamente. Depois, importe o módulo em outro arquivo e confirme que os testes não rodam na
# importação.
print("<<--===//| Exercício 3 |\\===-->>")

from validadores import eh_par, eh_positivo

print("\n")

#Exercício 4 — Importando de uma pasta
# Crie a seguinte estrutura de pastas:
# 
# projeto/
# |
# |__ utilidades/
# |   |
# |   |__ texto.py
# |
# |__ main.py
# 
# Dentro de texto.py, crie funções: contar_vogais(texto), inverter_texto(texto) e eh_palindromo(texto). Em main.py, importe essas funções e peça ao usuário uma frase. Exiba a
# quantidade de vogais, o texto invertido e se é um palíndromo.
print("<<--===//| Exercício 4 |\\===-->>")

from utilidades.texto import contar_vogais, inverter_texto, eh_palindromo

frase = input("Digite uma frase: ")
print(f"Quantidade de vogais: {contar_vogais(frase)}")
print(f"Texto invertido: {inverter_texto(frase)}")
print(f"É palíndromo: {eh_palindromo(frase)}")

print("\n")

# Exercício 5 — Módulo de estatísticas
# Crie um módulo estatisticas.py com funções: media(lista), mediana(lista) e moda(lista). A função mediana deve ordenar a lista e retornar o valor do meio 
# (ou a média dos dois do meio, se a lista tiver tamanho par). A função moda deve retornar o valor que mais aparece na lista. Todas as funções devem retornar None e exibir uma 
# mensagem de aviso se a lista estiver vazia. Em outro arquivo, peça ao usuário 7 números, armazene em uma lista e exiba a média, mediana e moda usando o módulo.
print("<<--===//| Exercício 5 |\\===-->>")

from estatisticas import media, mediana, moda

numeros = []
for i in range(7):
    numeros.append(int(input(f"Digite o {i + 1}º número: ")))

print(f"Média: {media(numeros)}")
print(f"Mediana: {mediana(numeros)}")
print(f"Moda: {moda(numeros)}")

print("\n")