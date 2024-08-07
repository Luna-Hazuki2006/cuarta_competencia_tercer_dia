def binario(numero : int): 
    binario = ''
    while numero // 2 != 1: 
        binario = f'{numero % 2}{binario}'
        numero = numero // 2
    else: binario = f'{1}{numero % 2}{binario}'
    print(binario)

def main(): 
    numero = int(input('Inserte el número decimal que desea convertir: '))
    binario(numero)

if __name__ == '__main__': 
    main()