"""
Author: Breno do Carmo
_version_ = 1.0

"""


def soma_lista(args):
    acumulador = []
    for indice in args:
        if type(indice) == list:
            for valor in indice:
                acumulador.append(valor)
                # continue
        else:
            acumulador.append(indice)

    return sum(acumulador)


if __name__ == "__main__":
    elementos = [[2, 5], 1, [1], [1, 1, 1]]
    """
    elementos = [[2, 5], 1, [1], [1, 1, 1]]
    
    resultado: 12
    """
    soma_lista(args=elementos)
