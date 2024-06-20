# eraseB
from pakages.addBook.addB import aLibro

def bLibro(biblioteca):
    print('\n\tBienvenido a: ----> Borrar Libros')
    while True:
        lib = input('\t\tIntroduzca el titulo del libro...a borrar o...\n\t\t salir para abandonar la opcion').title()
        if not lib:
            print('El campo no puede quedar.....')
        if lib:
            if len(biblioteca) == 0:
                try:
                    rbAdd =  input('la biblioteca esta vacia y triste:( |: Desea introducir un libro?¿:):-->\n\t\t < SI >--o--< NO > \n\t Introduzca salir para cancelar').lower()
                    rbAdd == 'si' or rbAdd == 'no' or rbAdd == 'salir'
                except ValueError:
                    print('\n\nDebe contestar [si o no]  o salir para cancelar')

                else:
                    while True:
                        if not rbAdd:
                            print('\n\nDebe contestar [si o no]  o salir para cancelar')
                        if rbAdd == 'si':
                            print('\n\nRedirigiendo a opcion 1- Añadir libro')
                            aLibro(biblioteca)
                        elif rbAdd == 'no':
                            print('\t\t Saliendo opcion |borrar libro de biblioteca |--->>')
                            return None
                        else:
                            print('\t\t NON CAPITO NIENTE CATZZO!!! && COMPUTER SAYS NO!¿¡ BY THE WAY!!\n\tSaliendo opcion |mostrar biblioteca |--->>')
                            return None
                
            else:
                for libro in biblioteca:
                    if libro['title'] == lib:
                        print(f'Se borrara{libro}')
                        biblioteca.remove(libro)
                if libro.get(lib) == None:
                    print(f'El libro que desea borrar{lib} no existe en la biblioteca')

if __name__=='__main__':
    bLibro()