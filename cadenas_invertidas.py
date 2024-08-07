def invertir(cadena : str): 
    cadena = list(cadena)
    for i in range(1, len(cadena) // 2 + 1): 
        cadena[-i], cadena[i - 1] = cadena[i - 1], cadena[-i]
    print(''.join(cadena))

def main(): 
    cadena = str(input('Ingrese la cadena que desea invertir: '))
    invertir(cadena)

if __name__ == '__main__': 
    main()