# addB 

def aLibro(biblioteca):
    print('\n\tBienvenido a: ----> Añadir Libros\n\t\tIntroduzca salir para terminar')
    autL = None
    flagA = True
    while flagA:
        autL = input('Introduzca el nombre del autor o salir para terminar:').title()
        if not autL:
            print('El campo no puede quedar vacio')
        elif autL == 'Salir':
            flagA = False
            print(flagA, '\t\tSaliendo totalmente  de opcion')
            return None
        else:

            flagT = True
            while flagT:

                titL = input('Introduzca el titulo del libro').title()
                if not titL:
                    print('El campo no puede quedar vacio')
                if titL:
                    for lib in biblioteca:
                        if lib.get('titulo') == titL and lib.get('autor') == autL:
                            print(f'El libro introducido {titL} del autor {autL} ya existe en la biblioteca como puede ver\n\t{lib}')
                            flagT = False
                 
                    else:
                        print('Saliendo parcialmente')
                        flagT = False
                
            flagP = True
            while flagP:
                if autL=='Salir':
                    flagP = False
                try:
                    aPubL = int(input('Introduzca el año de publicacion del libro'))
                except ValueError:
                        print('el año de publicacion debe ser numerico como--> 1356')
                else:
                    if aPubL<= 2024:
                        biblioteca.append({'autor': autL, 'title': titL, 'año publicacion': aPubL })
                        flagP = False
                    else:
                        print(f'La fecha de publicacion{aPubL} esta en el futuro\n\t\t!!¡·$~Eso crearia una brecha esspacio temporal !!McFly¡¡')
        iA = 0
        print('Saliendo de la opcion Añadir libros: Esta es su biblioteca')
        for libro in biblioteca:
            print(f'libro-numero:{iA}')
            iA += 1
            for k,v in libro.items():
                print(f'\n\n \t\t[{k}]|---:---|{v}\n')
        return None

if __name__=='__main__':
    aLibro()
    


