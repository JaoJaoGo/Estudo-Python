# name = input("Enter your name: ")
# age_input = input("Enter your age: ")
# age = int(age_input)
# print(f"Hello {name}, you are {age} years old\n")

# a = 10
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)
# print(a == b)
# print(a != b)
# print(a > b)
# print(a <= b)

# print("\nOperações em textos")
# print("abacaxi" < "banana")
# print("a" < "b")
# print("c" < "b")

# x = 10
# print(f"x = {x}")
# x = x + 5
# print(f"x = {x}")
# x -= 2
# print(f"x = {x}")

# age = 25
# salary = 3000
# print(age >= 18 and salary >= 2000)
# print(age >= 30 and salary >= 2000)
# print(age >= 30 or salary >= 2000)

# rain = True
# print(rain)
# print(not rain)

# age = 20
# is_student = True
# salary = 1500
# print(age >= 18 and (is_student or salary > 2000))
# print(age >= 18 and (not is_student or salary > 2000))

# idade = 20
# if idade < 18:
#     print("Você é menor de idade")
# else:
#     print("Você é maior de idade")

# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade")
#     print("Pode dirigir e votar")
# elif idade >= 16:
#     print("Você é quase maior de idade")
#     print("Pode dirigir, mas não pode votar")
# else:
#     print("Você é menor de idade")
#     print("Não pode dirigir nem votar")

# idade = 20
# tem_carteira = True
# if idade >= 18:
#     print("Você é maior de idade.")
#     if tem_carteira:
#         print("Você pode dirigir.")
#     else:
#         print("Você precisa ter carteira para dirigir.")
# else:
#     print("Você é menor de idade.")

# nome = input("Digite seu nome: ")
# if nome:
#     print(f"Olá, {nome}!")
# else:
#     print("Nome não informado.")

# loop = 1
# while loop <= 100000:
#     print(loop)
#     loop += 1

# i = 0
# for i in range(50000, 100000):
#     print(i)
# i = 0
# for i in range(0, 100000, 1000):
#     print(i)

# for j in range(100):
#     print(j)

#     if j == 50:
#         break

# while True:
#     comando = input("Digite um comando (ou 'sair' para encerrar): ")
#     if comando.lower() == 'sair':
#         print("Encerrando...")
#         break
    
#     print(f"Você digitou: {comando}")

# for i in range(1, 25):
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         continue
#     print("next iteration")

# texto = "banana"
# contador_a = 0
# i = 0
# while i < len(texto):
#     if texto[i] == "a":
#         contador_a += 1
#     i += 1
# print(f"A letra 'a' aparece {contador_a} vezes na palavra '{texto}'")

# soma = 0
# for i in range(1, 11):
#     soma += i
# print("A soma dos números de 1 a 10 é:", soma)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print('\n')

# language = "Python10#@"
# print(language)
# print(language[0])
# print(language[1])
# print(language[2])
# print(language[9])
# print(language[0:6])
# print(language[1:4])
# print(len(language))

# frase = 'php é lindo'
# nova_frase = frase.replace('php', 'python')
# print(nova_frase.capitalize())
# print("python" in frase)
# print("python" in nova_frase)

# frutas = ["maçã", "banana"]
# novas = ["laranja", "uva"]
# frutas.extend(novas)
# print(frutas)


# -- TUPLAS --

# frutas = ["maçã", "banana", "laranja", "uva"]
# tupla_frutas = ("maçã", "banana", "laranja", "uva") # São imutáveis

# lista = ["python", "java", "c++"]
# tupla = tuple(lista)
# print(tupla)
# print(tupla[0])
# print(tupla[-1])
# tupla[0] = "javascript"  # TypeError: 'tuple' objeto não suporta atribuição de item, pois tuplas são imutáveis
# tupla.append("javascript")  # AttributeError: 'tuple' object has no attribute 'append', pois tuplas são imutáveis
# conversao_tupla = list(tupla)
# conversao_tupla.append("javascript")
# print(conversao_tupla)

# tupla = ("python", "java", "c++", "python", "python")
# print(tupla.count("python"))
# print(tupla.index("c++"))
# print(tupla.index("python"))

# tupla1 = (1, 2, 3)
# tupla2 = (4, 5, 6)
# tupla3 = tupla1 + tupla2
# print(tupla3)
# print(1 in tupla1)
# print(1 in tupla2)

# frutas = ("maçã", "banana", "uva")
# for fruta in frutas:
#     print(fruta)
# for i in range(len(frutas)):
#     print(frutas[i])
# for i, fruta in enumerate(frutas):
#     print(f"Índice: {i}, Fruta: {fruta}")

# coordenadas = (10, "Cliente X", "25/06/2026")

# soma_total, cliente, comemoracao = coordenadas
# print(soma_total)
# print(cliente)
# print(comemoracao)


# -- SET --

# Semelhantes a listas e tuplas, mas não existe índices e não permite valores duplicados
# lista = [1, 2, 3, 2, 1]
# print(lista)
# conjunto = {1, 2, 3, 2, 1}
# conjunto = set(lista)
# print(conjunto)

# frutas = {"maçã", "banana", "laranja", "uva", "abacaxi"}
# conjunto = set(frutas)
# print(conjunto)
# conjunto.add("manga")
# print(conjunto)
# frutas.update(["pera", "kiwi"])
# print(frutas)
# frutas.remove("pera")
# frutas.discard("uva") # Não gera erro se o elemento não existir
# print(frutas)
# item_removido = frutas.pop()
# print(item_removido)
# print(frutas)
# frutas.clear()
# print(frutas)


# -- FUNÇÃO --

# def soma(a = 2, b = 2):
#     print("Olá! Bem-vindo ao meu estudo de Python!")

#     resultado = a + b
#     print(f"O resultado da soma é: {resultado}")

#     return resultado is not None
# somou = soma(b = 3)
# print(somou)


# -- CLASSES --

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    
#     def apresentar(self):
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
# pessoa1 = Pessoa("João", 23)
# pessoa2 = Pessoa("Ellen", 24)
# pessoa1.apresentar()
# pessoa2.apresentar()

# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self._velocidade = 0 # Convenção: atributo privado

#     def acelerar(self, velocidade_adicional = 10):
#         self._velocidade += velocidade_adicional
#         print(f"{self.modelo} acelerou para {self._velocidade}km/h")
    
#     def frear(self, velocidade_reduzida = 10):
#         self._velocidade -= velocidade_reduzida
#         print(f"{self.modelo} freou para {self._velocidade}km/h")

#     def informacoes(self):
#         print(f"{self.marca} {self.modelo} {self.ano}")
#         print(f"Velocidade: {self._velocidade}km/h")

# carro1 = Carro("Toyota", "Corolla", 2020)
# carro1.informacoes()
# carro1.acelerar()
# carro1.acelerar(30)
# carro1.frear()
# carro1.informacoes()

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, nome):
#         self.nome = nome

#     @abstractmethod
#     def fazer_som(self):
#         print(f"{self.nome} faz um som.")

# class Cachorro(Animal):
#     def __init__(self, nome, mordida):
#         super().__init__(nome)
#         self.mordida = mordida

#     def fazer_som(self):
#         print(f"{self.nome} late.")

# class Gato(Animal):
#     def fazer_som(self):
#         print(f"{self.nome} mia.")

# dog = Cachorro("Rex", "Forte")
# cat = Gato("Mimi")

# dog.fazer_som()
# cat.fazer_som()

# animais: list[Animal] = [dog, cat]

# for animal in animais:
#     animal.fazer_som()

# class Pessoa:
#     total_alunos: int = 0

#     def __init__(self, nome: str, idade: int) -> None:
#         self.nome = nome
#         self.idade = idade
#         Pessoa.total_alunos += 1

#     def __str__(self) -> str:
#         return f"Pessoa(nome={self.nome}, idade={self.idade})"

#     def ano_nascimento(self) -> int:
#         return 2026 - self.idade

# print(Pessoa.total_alunos)
# pessoa1 = Pessoa("João", 24)
# print(pessoa1)
# print(Pessoa.total_alunos)
# pessoa2 = Pessoa("Maria", 25)
# print(pessoa2)
# print(Pessoa.total_alunos)
# print(pessoa1.ano_nascimento())

# class Calculadora:
#     @staticmethod
#     def somar(a: int, b: int) -> int:
#         return a + b
    
#     @staticmethod
#     def eh_par(numero: int) -> bool:
#         return numero % 2 == 0

# calc = Calculadora()
# print(Calculadora.somar(1, 2))
# print(Calculadora.eh_par(3))

# class Aluno:
#     total_alunos: int = 0

#     def __init__(self, nome: str) -> None:
#         self.nome = nome
#         Aluno.total_alunos += 1

#     @classmethod
#     def obter_total_alunos(cls) -> int:
#         return cls.total_alunos

#     @classmethod
#     def criar_aluno(cls, nome: str) -> 'Aluno':
#         return cls(nome)

# aluno1 = Aluno.criar_aluno("João")
# print(aluno1.nome)
# aluno2 = Aluno.criar_aluno("Maria")
# print(aluno2.nome)
# print(Aluno.obter_total_alunos())

"""
+-----------------+--------------------+
| Decorator       | Recebe             |
| (sem decorator) | `self` (instância) |
| `@staticmethod` | nada               |
| `@classmethod`  | `cls` (classe)     |
+-----------------+--------------------+
"""


# -- DICIONÁRIOS --

# estoque = {}
# produto = {"name": "Coca-cola", "price": 5.0, "quantity": 10}
# contato = {
#     "name": "João",
#     "email": "teste@teste.com.br",
#     "phones": ["11999999999", "11988888888"],
#     "address": {
#         "street": "Rua A",
#         "number": 123,
#         "city": "São Paulo"
#     }
# }

# print(contato["name"])
# print(contato.get("email", 0))
# print(contato["phones"])
# print(contato["address"]["street"])
# print(contato["address"]["number"])
# print(contato["address"]["city"])

# produto["name"] = "Pepsi"
# produto["soda"] = True
# print(produto)

# produto.pop("soda") # Ou del produto["soda"]
# print(produto)

# for chave in produto:
#     print(chave, ":", produto[chave])

# for chave, valor in produto.items():
#     print(chave, ":", valor)

# dados = {"a": 1, "b": 2, "c": 3}

# print("a" in dados)
# print("z" in dados)
# print(len(dados))

# chave_lista = list(dados.keys())
# print(chave_lista)

# valor_lista = list(dados.values())
# print(valor_lista)

# dados.clear()
# print(dados)

# turma = [
#     {"nome": "João", "nota": 8},
#     {"nome": "Maria", "nota": 9},
#     {"nome": "Pedro", "nota": 7},
#     {"nome": "Ana", "nota": 6}
# ]

# for aluno in turma:
#     if aluno["nota"] >= 7:
#         print(f"{aluno['nome']} passou com nota {aluno['nota']}.")
#     else:
#         print(f"{aluno['nome']} reprovado com nota {aluno['nota']}.")


# -- MÓDULOS --
# import utilidades
# from utilidades import formatar_moeda
# import utilidades as util # Alias
# from utilidades import formatar_moeda as fm
# import datetime

# preco = 50.0

# print(utilidades.dobro(preco))
# print(utilidades.metade(preco))
# print(utilidades.formatar_moeda(preco))
# print90(formatar_moeda(preco))
# print(fm(preco))
# print(datetime.date.today())


from matematica.operacao import somar
from strings.formatacao import apresentacao

print(somar(5, 10))
print(apresentacao("João"))