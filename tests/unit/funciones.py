
def get_fractions(valor):
    """

    Args:
      valor: valor de entrada, puede ser una fracción o un número entero.

    Returns:La fucnion regresa un valor entero o flotante en caso de que el valor sea fracción

    """
    numero = 0
    try:
        if(isinstance(valor, str)):
            print(valor)
            if "/" in valor:
                arr = valor.split("/")
                numerador = arr[0]
                denominador = arr[1]
                numero = float(numerador) / float(denominador)
            else:
                numero = float(valor)
        if(isinstance(valor, int) or isinstance(valor, float)):
            numero = valor
    except:
        print("Error de formato de numero")
    return numero

def multiplica(a, b):
    """

    Args:
      a: valor del multiplicando
      b: valor del multiplicador

    Returns: la fucnión arroja la multiplicación del multiplicando y el multplicador, sin importar si el valor introducido es una fracción

    """
    multiplicando = get_fractions(a)
    multiplicador = get_fractions(b)
    return multiplicando * multiplicador
