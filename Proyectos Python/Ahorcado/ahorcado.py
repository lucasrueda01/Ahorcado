#from curses.ascii import isalpha
import random

palabras = ['programacion','calamar','teclado','homosexual','travesti','control','salamandra','juego','cafe']

def jugar(palabra):
    incognita = len(palabra) * '_'
    Juego = True
    intentos = 5

    while Juego:
        if incognita.find('_') == -1:
            print('')
            print(f'Felicidades! Encontraste la palabra: {incognita.capitalize()}')
            break

        print('')
        print(f'      Tu palabra: {incognita}')
        print('')
        miLetra = input('Ingrese una letra: ')

        #while not isalpha(miLetra) or len(miLetra) != 1:
            #print('Error: Debe ingresar una sola letra')
            #miLetra = input('Ingrese una letra: ')

        while incognita.find(miLetra) != -1:
            print('La letra ingresada ya ha sido descubierta')
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
            intentos -= 1
            if intentos > 0:
                print('La letra no se encuentra en la palabra')
                print(f'Te quedan {intentos} intentos')
            else:
                print(f'Te quedaste sin intentos! La palabra era {palabra}')
                break


palabra = random.choice(palabras).lower()
jugar(palabra)

    