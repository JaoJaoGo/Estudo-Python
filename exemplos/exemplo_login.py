print("=" * 40)
print("\n== SISTEMA DE LOGIN ==\n")
print("=" * 40)

correct_user = "admin"
correct_password = "123456"

print("Usuário: ")
user = input()
print("\nSenha: ")
password = input()

print('\n')
print("=" * 40)

if not user or not password:
    print("Usuário e senha são obrigatórios!")
elif user == correct_user and password == correct_password:
    print(f"Olá, {user}!")
else:
    print("Usuário ou senha incorretos!")

print("=" * 40)