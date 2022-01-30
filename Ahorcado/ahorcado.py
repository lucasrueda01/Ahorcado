from curses.ascii import isalpha
import os
from palabras_random import get_palabra

def jugar(palabra):
    incognita = len(palabra) * '_'
    Juego = True
    intentos = 10
    letras_erradas = []

    while Juego:
        if incognita.find('_') == -1:
            print('')
            print(f'Felicidades! Encontraste la palabra: {incognita.capitalize()}')
            break
        
        os.system('cls')
        print(f'Tu palabra: {incognita}')
        print('')
        print(f'Te quedan {intentos} intentos')
        if letras_erradas:
            print(f'Letras erradas: {letras_erradas}')
        miLetra = input('Ingrese una letra: ')

        while (miLetra == '') or (len(miLetra) != 1) or (not isalpha(miLetra)):
            print('Error: Debe ingresar una sola letra')
            miLetra = input('Ingrese una letra: ')

        while (incognita.find(miLetra) != -1) or (miLetra in letras_erradas):
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
                letras_erradas.append(miLetra)
                input('Presiona Enter para continuar')
            else:
                print(f'Te quedaste sin intentos! La palabra era: {palabra}')
                break


Menu = True
while Menu:
    os.system('cls')
    print('Bienvenido al juego del ahorcado!'.center(50,'-'))
    print('''
    1. Jugar
    2. Salir
    ''')
    opcion = int(input('Ingrese una opcion: '))
    if opcion == 1:
        opcion2 = 'y'
        while opcion2 == 'y':
            palabra = get_palabra()
            jugar(palabra)  
            print('')
            opcion2 = input('Queres jugar otra vez? (y/n): ')
            while opcion2 != 'y' and opcion2 != 'n':
                print('Entrada Invalida')
                opcion2 = input('Queres jugar otra vez? (y/n): ')
                os.system('cls')
            if opcion2 == 'n':
                print('Saliendo...')
                Menu = False
    elif opcion == 2:
        print('Saliendo...')
        Menu = False
    else:
        print('Entrada invalida')