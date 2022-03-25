def get_fractions(valor):
    numero = 0
    try:
        if(isinstance(valor,str)):
            print(valor)
            if "/" in valor:
                arr = valor.split("/")
                numerador = arr[0]
                denominador = arr[1]
                numero = float(numerador) / float(denominador)
            else:
                numero = float(valor) 
        if(isinstance(valor,int) or isinstance(valor,float)):
            numero = valor
    except:
        print("Error de formato de numero")
        return numero