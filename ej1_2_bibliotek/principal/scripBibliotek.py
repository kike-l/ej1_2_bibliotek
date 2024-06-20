#IMPORTS
from pakages.addBook.addB import aLibro
from pakages.eraseBook.eraseB import bLibro
from pakages.seeAuthor.seeA import mLibA
from pakages.showBibliotek.showB import mBiblio 




# PRINCIPAL
def principal():

    print('\nBienbenido a su biblioteca: \n \tPor favor seleccione una opcion del menu')
    
    flag = True
    while flag:
        print(""" \n\t MENU opciones:
                1 para Añadir libro
                2 para Borrar libro
                3 para Mostrar libros de autor
                4 para Mostrar biblioeca
                5 para Salir de biblioteca""")
    
        try: 
            sel = int(input('\tPor favor seleccione una opcion del menu-->  '))
            print(sel,type(sel))
        except ValueError:
            print('Debe expresar su seleccion con un valor numerico entre 1 y 5')
            
            print(sel,type(sel))
        if sel:
            match sel: 
                case 1:
                    print(f'\n\tSelecciono {sel}.Añadir libro ')
                    aLibro(biblioteca)

                case 2:
                    print(f'\n\tSelecciono {sel}.Borrar libro ')
                    bLibro(biblioteca)
                case 3:
                    print(f'\n\tSelecciono {sel}.Mostrar libros de autor ')
                    mLibA(biblioteca)
                    
                case 4:
                    print(f'\n\tSelecciono {sel}.Mostrar biblioeca ')
                    mBiblio(biblioteca)
                case 5:
                    print(f'\n\tSelecciono {sel}.Salir \n\tSaliendo del programa\n\t\tSoft--flag=false ')
                    flag = False
                case _:
                    print('\n\tAlgo salio muy mal .Saliendo del programa\n\t\tHard --break..')
                    break
            sel = None
        else:
            print(f'La entrada{sel} no puede ser NADA')
    print('Saliendo del programa.....')
    print('computer out')


if __name__=='__main__':
    biblioteca = []
    principal()
