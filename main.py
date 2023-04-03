"""
Author: Breno do Carmo
_version_ = 1.0

"""


def soma_lista(lista_de_elemento):
    acumulador = []
    for indice in lista_de_elemento:
        if type(indice) == list:
            for valor in indice:
                acumulador.append(valor)
                # continue
        else:
            acumulador.append(indice)

    return sum(acumulador)
