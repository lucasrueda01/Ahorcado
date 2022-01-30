import random

palabras = ['Programacion','Calamar','Teclado','Homosexual','Travesti','Control']

def jugar(palabra):
    incognita = len(palabra) * '_'
    Juego = True
    while Juego:
        if incognita.find('_') == -1:
            print(f'Felicidades! Encontraste la palabra: {incognita}')
            break
        print(f'--------Tu palabra: {incognita} ----------')
        print('')
        miLetra = input('Ingrese una letra: ')
        while not isalpha(miLetra) or len(miLetra) != 1:
            print('Error: Debe ingresar una sola letra')
            miLetra = input('Ingrese una letra: ')
        if palabra.find(miLetra) != -1:
            ocurrencias = []
            i = 1
            ultima_ocurrencia = 0
            while i <= len(palabra):
                ocurrencia = palabra.find(miLetra,ultima_ocurrencia)
                if ocurrencia != -1:
                    ocurrencias.append(ocurrencia)
                    ultima_ocurrencia = ocurrencia + 1
                    i += 1
                else:
                    break
            for j in ocurrencias:
                lista_incognita = list(incognita)
                lista_incognita[j] = miLetra
                incognita = ''.join(lista_incognita)
        else:
            print('La letra no se encuentra en la palabra')


palabra = random.choice(palabras).lower()
jugar(palabra)

    