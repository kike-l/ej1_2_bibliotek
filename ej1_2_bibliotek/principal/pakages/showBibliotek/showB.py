# showB
from pakages.addBook.addB import aLibro

def mBiblio(biblioteca):
    iBiblio = len(biblioteca)
    
    match iBiblio:
        case 0:
            try:
                rAdd =  input('la biblioteca esta vacia: Desea introducir un libro?¿:-->\n\t\t < SI >--o--< NO > \n\t Introduzca salir para cancelar').lower()
                rAdd == 'si' or rAdd == 'no' or rAdd == 'salir'
            except ValueError:
                print('\n\nDebe contestar [si o no]  o salir para cancelar')

            else:
                while True:
                    if not rAdd:
                        print('\n\nDebe contestar [si o no]  o salir para cancelar')
                    if rAdd == 'si':
                        print('\n\nRedirigiendo a opcion 1- Añadir libro')
                        aLibro(biblioteca)
                    elif rAdd == 'no':
                        print('\t\t Saliendo opcion |mostrar biblioteca |--->>')
                        return None
                    else:
                        print('\t\t NON CAPITO NIENTE CATZZO!!! && COMPUTER SAYS NO!¿¡ BY THE WAY!!\n\tSaliendo opcion |mostrar biblioteca |--->>')
                        return None
                
        case iBiblio if iBiblio >=1:
                
                print('\n\tBienvenido a: ----> Mostrar biblioteca')
                print('Aqui tiene su biblioteca ')
                iA = 0
                for libro in biblioteca:
                    print(f'libro-numero:{iA}')
                    iA += 1
                    for k,v in libro.items():
                        print(f'\n\n \t\t[{k}]|---:---|{v}\n')
                return None
if __name__=='__main__':
    mBiblio()