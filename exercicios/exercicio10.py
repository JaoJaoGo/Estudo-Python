# Exercício 1 — Classe Retângulo
# Crie uma classe Retangulo com atributos largura e altura. Adicione métodos calcular_area() e calcular_perimetro(). 
# Crie dois objetos, calcule e exiba a área e o perímetro de cada um.
print("<<--===//| Exercício 1 |\\===-->>")

class Retangulo:
    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self) -> float:
        return self.largura * self.altura
    
    def calcular_perimetro(self) -> float:
        return 2 * (self.largura + self.altura)

# Criar dois objetos
retangulo1 = Retangulo(10, 5)
retangulo2 = Retangulo(8, 6)

# Calcular e exibir área e perímetro de cada um
print(f"Retângulo 1 - Área: {retangulo1.calcular_area()}, Perímetro: {retangulo1.calcular_perimetro()}")
print(f"Retângulo 2 - Área: {retangulo2.calcular_area()}, Perímetro: {retangulo2.calcular_perimetro()}")

print("\n")
# Exercício 2 — Classe Conta Bancária
# Crie uma classe ContaBancaria com atributos titular (público) e _saldo (protegido). Implemente métodos: depositar(valor), sacar(valor) e exibir_saldo(). O saque só deve ser
# permitido se houver saldo suficiente. Crie uma conta, faça operações de depósito e saque, e exiba o saldo final.
print("<<--===//| Exercício 2 |\\===-->>")

class ContaBancaria:
    def __init__(self, titular: str, saldo: float) -> None:
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self._saldo += valor
        else:
            print("Valor inválido")

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            print("Valor inválido")
        elif self._saldo >= valor:
            self._saldo -= valor
        else:
            print("Saldo insuficiente")

    def exibir_saldo(self) -> None:
        print(f"Saldo: {self._saldo}")

conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(200)
conta.exibir_saldo()

print("\n")

# Exercício 3 — Herança — Funcionários
# Crie uma classe Funcionario com nome e salario_base. Crie uma classe Vendedor que herde de Funcionario e adicione o atributo comissao. Implemente um método 
# calcular_salario_total() que retorne salario_base + comissao. Crie um funcionário comum e um vendedor, e exiba os dados de ambos.
print("<<--===//| Exercicio 3 |\\===-->>")

class Funcionario:
    def __init__(self, nome: str, salario_base: float) -> None:
        self.nome = nome
        self.salario_base = salario_base

    def exibir_dados(self) -> None:
        print(f"{self.nome} - R$ {self.salario_base:2f}")
    
class Vendedor(Funcionario):
    def __init__(self, nome: str, salario_base: float, comissao: float) -> None:
        super().__init__(nome, salario_base)
        self.comissao = comissao
    
    def calcular_salario_total(self) -> float:
        return self.salario_base + self.comissao

    def exibir_dados(self) -> None:
        total = self.calcular_salario_total()
        print(f"{self.nome} (Vendedor) — R$ {total:.2f}")

funcionario = Funcionario("João", 1000)
vendedor = Vendedor("Maria", 1000, 500)

funcionario.exibir_dados()
vendedor.exibir_dados()

print("\n")

# Exercício 4 — Classe Produto com desconto
# Crie uma classe Produto com nome, preco e _estoque. Adicione métodos: aplicar_desconto(porcentagem) que reduz o preço, vender(quantidade) que diminui o estoque 
# (se houver quantidade suficiente) e exibir_dados() que mostra nome, preço atual e estoque. Teste criando um produto, aplicando desconto, vendendo e exibindo os dados.
print("<<--===//| Exercicio 4 |\\===-->>")

class Produto:
    def __init__(self, nome: str, preco: float, estoque: int) -> None:
        self.nome = nome
        self.preco = preco
        self._estoque = estoque
    
    def aplicar_desconto(self, porcentagem: float) -> None:
        if porcentagem < 0 or porcentagem > 100:
            print("Porcentagem inválida")
            return
        self.preco -= self.preco * (porcentagem / 100)

    def vender(self, quantidade: int) -> None:
        if quantidade <= 0:
            print("Quantidade inválida")
            return
        elif self._estoque >= quantidade:
            self._estoque -= quantidade
        else:
            print("Estoque insuficiente")
        
    def exibir_dados(self) -> None:
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Estoque: {self._estoque}")

# Teste
produto = Produto("Notebook", 1000, 10)
produto.aplicar_desconto(10)
produto.vender(5)
produto.exibir_dados()

print("\n")

# Exercício 5 — Agenda de contatos
# Crie uma classe Contato com nome, telefone e email. Crie uma classe Agenda que tenha uma lista de contatos e métodos: adicionar(contato), remover(nome), buscar(nome) e
# listar_todos(). Implemente um menu interativo (while True) que permita ao usuário gerenciar a agenda.
print("<<--===//| Exercicio 5 |\\===-->>")

class Contato:
    def __init__(self, none: str, telefone: str, email: str) -> None:
        self.nome = none
        self.telefone = telefone
        self.email = email

class Agenda:
    def __init__(self) -> None:
        self.contatos = []

    def adicionar(self, contato: Contato) -> None:
        self.contatos.append(contato)
    
    def remover(self, nome: str) -> None:
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                return
    
    def buscar(self, nome: str) -> Contato | None:
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def listar_todos(self) -> None:
        for contato in self.contatos:
            print(f"Nome: {contato.nome}")
            print(f"Telefone: {contato.telefone}")
            print(f"Email: {contato.email}")
            print("\n")

agenda = Agenda()

while True:
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Listar todos")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")

        contato = Contato(nome, telefone, email)

        agenda.adicionar(contato)
    elif opcao == 2:
        nome = input("Nome: ")
        agenda.remover(nome)
    elif opcao == 3:
        nome = input("Nome: ")
        contato = agenda.buscar(nome)

        if contato:
            print(f"Nome: {contato.nome}")
            print(f"Telefone: {contato.telefone}")
            print(f"Email: {contato.email}")
        else:
            print("Contato não encontrado")
    elif opcao == 4:
        agenda.listar_todos()
    elif opcao == 5:
        break
    else:
        print("Opção inválida")

print("\n")

# Exercício 6 — __str__ na prática
# Crie uma classe Livro com atributos titulo, autor e ano. Implemente o método __str__ para que print(livro) exiba algo como "Dom Casmurro, de Machado de Assis (1899)". Crie 
# dois livros e imprima com print().
print("<<--===//| Exercicio 6 |\\===-->>")

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def __str__(self):
        return f"{self.titulo}, de {self.autor} ({self.ano})"
    
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("1984", "George Orwell", 1948)

print(livro1)
print(livro2)

print("\n")

# Exercício 7 — Atributo de classe (contador)
# Crie uma classe Usuario com atributos nome e email. Adicione um atributo de classe total_usuarios que conta quantos usuários foram criados. Toda vez que um novo Usuario for
# instanciado, o contador deve incrementar automaticamente. Crie alguns usuários e imprima o total usando Usuario.total_usuarios.
print("<<--===//| Exercicio 7 |\\===-->>")

class Usuario:
    total_usuarios: int = 0

    def __init__(self, nome: str, email: str) -> None:
        self.nome = nome
        self.email = email
        Usuario.total_usuarios += 1

usuario1 = Usuario("João", "joao@gmail.com")
usuario2 = Usuario("Ellen", "ellen@gmail.com")
usuario3 = Usuario("Pedro", "pedro@gmail.com")
usuario4 = Usuario('Nathália', 'nathalia@gmail.com')

print(Usuario.total_usuarios)

print("\n")

# Exercício 8 — @staticmethod e @classmethod
# Crie uma classe ConversorTemperatura com:

# @staticmethod celsius_para_fahrenheit(celsius) — converte e retorna o valor em Fahrenheit
# @staticmethod fahrenheit_para_celsius(fahrenheit) — converte e retorna o valor em Celsius

# @classmethod descongelar_agua(cls) — retorna uma temperatura de 0°C em Fahrenheit (use o static method)
# @classmethod ferver_agua(cls) — retorna uma temperatura de 100°C em Fahrenheit (use o static method)

# Teste todos os métodos sem instanciar a classe.
print("<<--===//| Exercicio 8 |\\===-->>")

class ConversorTemperatura:
    @staticmethod
    def celsius_para_fahrenheit(celsius: float) -> float:
        return celsius * 9/5 + 32
    
    @staticmethod
    def fahrenheit_para_celsius(fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5/9
    
    @classmethod
    def descongelar_agua(cls) -> float:
        return cls.celsius_para_fahrenheit(0)

    @classmethod
    def ferver_agua(cls) -> float:
        return cls.celsius_para_fahrenheit(100)

print(ConversorTemperatura.descongelar_agua())
print(ConversorTemperatura.ferver_agua())

print("\n")

# Exercício 9 — Polimorfismo com formas geométricas
# Crie uma classe FormaGeometrica com método area() que retorna 0. Crie as subclasses:

# Circulo — recebe raio no construtor. area() retorna 3.14 * raio ** 2.
# Retangulo — recebe largura e altura. area() retorna largura * altura.
# Triangulo — recebe base e altura. area() retorna (base * altura) / 2.

# Crie uma lista com uma instância de cada forma e itere com for imprimindo a área de cada uma — sem usar if para verificar o tipo.
print("<<--===//| Exercicio 9 |\\===-->>")
class FormaGeometrica:
    def area(self) -> float:
        return 0
        
class Circulo(FormaGeometrica):
    def __init__(self, raio: float) -> None:
        self.raio = raio
    
    def area(self) -> float:
        return 3.14 * self.raio ** 2
        
class Retangulo(FormaGeometrica):
    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura
    
    def area(self) -> float:
        return self.largura * self.altura
        
class Triangulo(FormaGeometrica):
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura
    
    def area(self) -> float:
        return (self.base * self.altura) / 2
        
formas = [Circulo(5), Retangulo(5, 10), Triangulo(5, 10)]

for forma in formas:
    print(forma.area())

print("\n")

# Exercício 10 — Type hints em classes
# Retome a classe ContaBancaria do Exercício 2 e reescreva-a adicionando type hints em todos os parâmetros, atributos e retornos de métodos. Depois, crie uma nova classe Banco com:
 
# Atributo de classe contas: list[ContaBancaria] = []

# @classmethod abrir_conta(cls, titular: str, saldo_inicial: float) -> ContaBancaria — cria uma conta, adiciona na lista e retorna

# @classmethod total_contas(cls) -> int — retorna a quantidade de contas
# Use type hints em TODOS os métodos e parâmetros. Teste abrindo contas e consultando o total.
print("<<--===//| Exercicio 10 - JÁ FEITO!!! |\\===-->>")
