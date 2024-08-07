from pprint import pprint

def repeticion(oracion : str): 
    oracion = oracion.strip()
    oracion = oracion.lower()
    for esto in oracion: 
        if not esto.isalpha() and not esto.isspace(): 
            oracion = oracion.replace(esto, '')
    oracion = oracion.split(' ')
    lista = {}
    for i in range(1, len(oracion) // 2 + 1): 
        try: lista[oracion[i - 1]] += 1
        except: lista[oracion[i - 1]] = 1
        try: lista[oracion[-i]] += 1
        except: lista[oracion[-i]] = 1
    pprint(lista)

def main(): 
    oracion = str(input('Introduce la oración a revisar: '))
    repeticion(oracion)

if __name__ == '__main__': 
    main()