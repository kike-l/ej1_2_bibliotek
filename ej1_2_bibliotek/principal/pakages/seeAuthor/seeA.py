# seeA
from pakages.addBook.addB import aLibro


def mLibA(biblioteca):
    aut = input('Indique el autor que desea buscar ').title()
    if not aut:
        print('el campo no puede estar...')
    elif aut:
        aL = [libro for libro in biblioteca if libro['autor']==aut]
        print('Espere --...--..recopilando datos')
        if len(aL)==0:
            try:
                raAdd =  input(f'\nEl autor que busca: {aut} no tiene actualmente libros en esta biblioteca.\n\t Desea introducir un libro del autor?¿:-->\n\t\t < SI >--o--< NO > \n\t Introduzca salir para cancelar').lower()
                raAdd == 'si' or raAdd == 'no' or raAdd == 'salir'
            except ValueError:
                print('\n\nDebe contestar [si o no]  o salir para cancelar')

            else:
                while True:
                    if not raAdd:
                        print('\n\nDebe contestar [si o no]  o salir para cancelar')
                    if raAdd == 'si':
                        print('\n\nRedirigiendo a opcion 1- Añadir libro')
                        aLibro(biblioteca)
                        break
                    elif raAdd == 'no':
                        print(f'\n\t\t\t Saliendo opcion |mostrar libros de {aL} en biblioteca |--->>')
                        return None
                    else:
                        print('\t\t NON CAPITO NIENTE CATZZO!!! && COMPUTER SAYS NO!¿¡ BY THE WAY!!\n\tSaliendo opcion |mostrar biblioteca |--->>')
                        return None
                

        if len(aL)>=1:
            print(f'Aqui tiene los libros del autor {aut} incluidos en su biblioteca ')
            iA = 0
            for libro in biblioteca:
                print(f'libro-numero:{iA}')
                iA += 1
                for k,v in libro.items():
                    print(f'\n\n \t\t[{k}]|---:---|{v}\n')
                return None
if __name__=='__main__':
    mLibA()