def binario(numero : int): 
    if numero < 0: 
        print('Disculpa, pero solo aceptamos números naturales enteros (ﾉ*ФωФ)ﾉ')
        return
    if numero == 1 or numero == 0: 
        print(numero)
        return
    binario = ''
    while numero // 2 != 1: 
        binario = f'{numero % 2}{binario}'
        numero = numero // 2
    else: binario = f'{1}{numero % 2}{binario}'
    print(binario)

def main(): 
    try: 
        numero = int(input('Inserte el número decimal natural entero que desea convertir: '))
        binario(numero)
    except: 
        print('Disculpa, pero solo aceptamos números (´。＿。｀)')

if __name__ == '__main__': 
    main()