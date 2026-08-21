def media(lista):
    if not lista:
        print("A lista está vazia!")
        return None
    return sum(lista) / len(lista)

def mediana(lista):
    if not lista:
        print("A lista está vazia!")
        return None

    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)

    if tamanho % 2 == 1:
        return lista_ordenada[tamanho // 2]
    else:
        return (lista_ordenada[tamanho // 2 - 1] + lista_ordenada[tamanho // 2]) / 2

def moda(lista):
    if not lista:
        print("A lista está vazia!")
        return None

    contador = {}
    for numero in lista:
        contador[numero] = contador.get(numero, 0) + 1

    moda = max(contador, key=contador.get)
    return moda