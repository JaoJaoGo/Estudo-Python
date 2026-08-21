total = 0
operacoes = 0

while True:
    print(f"\nTotal atual: {total}")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Zerar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Encerrando...")
        break
    elif opcao == '1':
        valor = float(input("Digite o valor a somar: "))
        total += valor
        operacoes += 1
    elif opcao == '2':
        valor = float(input("Digite o valor a subtrair: "))
        total -= valor
        operacoes += 1
    elif opcao == '3':
        valor = float(input("Digite o valor a multiplicar: "))
        total *= valor
        operacoes += 1
    elif opcao == '4':
        total = 0
        operacoes = 0
    else:
        print("Opção inválida!")
    
print(f"\nTotal: {total}")
print(f"Operações: {operacoes}")