# Exercício 1 — Calculadora segura
# Crie uma calculadora que peça dois números e uma operação (+, -, *, /). Trate os erros de: entrada não numérica (ValueError) e divisão por zero (ZeroDivisionError). Exiba o 
# resultado ou uma mensagem de erro adequada.
print("<<--===//| Exercicio 1 |\\===-->>")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        raise Exception("Operação inválida!")
        
    print(f"Resultado: {resultado}\n")
except ValueError:
    print("Entrada inválida! Digite apenas números.\n")
except ZeroDivisionError:
    print("Divisão por zero não é permitida!\n")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}\n")

# Exercício 2 — Leitor de arquivo
# Crie um programa que peça o nome de um arquivo ao usuário e exiba seu conteúdo. Trate FileNotFoundError com uma mensagem amigável. Use finally para sempre exibir
# "Operação finalizada." ao terminar.
print("<<--===//| Exercicio 2 |\\===-->>")

nome_arquivo = input("Digite o nome do arquivo: ")

print('\n')

try:
    with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado!")
finally:
    print("Operação finalizada.\n")

# Exercício 3 — Conversão segura
# Crie uma função converter_para_inteiro(texto) que tente converter o texto recebido para inteiro. Se não conseguir, retorne None em vez de travar o programa. Teste a função com 
# os valores: "42", "abc", "7.5", "100".
print("<<--===//| Exercicio 3 |\\===-->>")

def converter_para_inteiro(texto):
    try:
        return int(texto)
    except:
        return None

testes = ["42", "abc", "7.5", "100"]
for valor in testes:
    resultado = converter_para_inteiro(valor)
    if resultado is not None:
        print(f"'{valor}' -> {resultado}")
    else:
        print(f"'{valor}' -> não foi possível converter")

print("\n")

# Exercício 4 — Validador de nota
# Crie uma função validar_nota(nota) que lança um ValueError se a nota for menor que 0 ou maior que 10. No programa principal, peça uma nota ao usuário em um loop, tratando tanto
# o ValueError da conversão quanto o da validação, e só saia do loop quando receber uma nota válida.
print("<<--===//| Exercicio 4 |\\===-->>")

def validar_nota(nota):
    if nota < 0 or nota > 10:
        raise ValueError("Nota deve ser entre 0 e 10")
    
    return True

while True:
    try:
        nota = float(input("Digite uma nota: "))
        validar_nota(nota)
        break
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        print("\n")

# Exercício 5 — Agenda com erros tratados
# Crie um programa de agenda que salva contatos em agenda.txt. O programa deve:
# (a) tentar ler os contatos existentes ao iniciar, sem travar se o arquivo não existir;
# (b) permitir adicionar um novo contato;
# (c) salvar o contato no arquivo, tratando possíveis erros de escrita.
print("<<--===//| Exercicio 5 |\\===-->>")

try:
    with open("agenda.txt", "r", encoding="utf-8") as arquivo:
        contatos = arquivo.readlines()
        
        print("Contatos existentes:")
        print("-" * 20)

        for contato in contatos:
            print(" -", contato.strip())
        
        print("-" * 20)
except FileNotFoundError:
    print("Nenhum contato encontrado. Iniciando agenda vazia.")

# Adiciona novo contato
nome = input("\nNome do novo contato: ")
telefone = input("Telefone: ")

try:
    with open("agenda.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}: {telefone}\n")
    print("Contato salvo com sucesso!")
except OSError as erro:
    # OSError cobre FileNotFoundError, PermissionError e erros de disco
    print(f"Erro ao salvar contato: {erro}")