def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for char in texto if char in vogais)

def inverter_texto(texto):
    return texto[::-1]

def eh_palindromo(texto):
    return texto.lower() == texto[::-1].lower()