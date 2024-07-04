import os, time

lista_nifs = []

def menu():
    print(' Selecciones una opcion')
    print('1)Grabar')
    print('2)Buscar')
    print('3)Imprimir certificados')
    print('4)Salir')


def grabar():
    os.system('cls')
    time.sleep(1)
    
    while True:
        
        NIF_numerico = int(input('ingrese su NIF numerico: \n'))
        if NIF_numerico >11111111 and NIF_numerico <199999999:
            break
        
    while True:
        
        NIF_letras = input('ingrese su NIF letras: \n').upper()
        if NIF_letras is not "" or " ":
            break    
    
    while True: 
        nombre = input('ingrese su nombre : \n')
        if nombre is not "" or " ":
            break
    
    while True:
        try:
            edad = int(input('ingrese su edad: \n'))
            if edad > 15 :
                break
        except ValueError:
            print('Error: ingrese una edad valida')
            
    while True:
        estado_civil = input('ingrese su estado conyugal: \n')
        if estado_civil is not  "" or " ":
            break
    
    while True:
        try:
            dia_nacimiento = int(input('ingrese dia de nacimiento: \n'))
            if dia_nacimiento >0 and dia_nacimiento <100:
                mes_nacimiento = int(input('ingrese mes de nacimento: \n'))
                if mes_nacimiento >0 and mes_nacimiento <13:
                    anio_nacimiento= int(input('ingrese año de nacimiento: \n'))
                    if anio_nacimiento <2011 and anio_nacimiento >1940:
                        break
        except ValueError:
            print('valor invalido')
            
    fecha_nacimiento = dia_nacimiento, '/', mes_nacimiento,'/',anio_nacimiento
    nifTotal = NIF_numerico, '-', NIF_letras    

    dic_nifs = {'nif': nifTotal, 'nombre': nombre, 'edad':edad,'estado conyugal': estado_civil, 'fecha de nacimiento':fecha_nacimiento}
    lista_nifs.append(dic_nifs)  
    print('Persona ingresada con exito')          
            

def buscar():
    os.system('cls')
    time.sleep(1)
    
    print('buscar persona por NIF')
    persona_buscada = input('ingrese NIF de la persona (ejemplo: XXXXXXXX-XXX): \n').upper()
    for dic_nifs in lista_nifs:
        if dic_nifs['nif'] == persona_buscada:
            print(lista_nifs)
            
        else:
            print('Error: NIF no encontrado')
            
def imprimir_certificados():
    os.system('cls')
    time.sleep(1)
    
    print('1) Nacimiento $1500')
    print('2) Estado Conyugal $3500')
    print('3) Pertenencia a la union europea $5000')
    
    try:
        opcion_imprimir = int(input('ingrese la opcion'))
        
        if opcion_imprimir == 1:
            imprimir_fechanacimiento = input('ingrese NIF ')
            for dic_nifs in lista_nifs:
                if dic_nifs['nif'] == imprimir_fechanacimiento:
                    print('Certificado de fecha de nacimiento')
                    print(dic_nifs)
                return
        else:
            print('Error: NIF no encontrado')
            
        if opcion_imprimir == 2:
            imprimir_estadoconyugal = input('ingrese NIF ')
            for dic_nifs in lista_nifs:
                if dic_nifs['estado conyugal'] == imprimir_estadoconyugal:
                    print(dic_nifs)
                return
        else:
            print('Error: NIF no encontrado')   

        if opcion_imprimir == 3:
            imprimir_pertenenciaUE = input('ingrese NIF')
            for dic_nifs in lista_nifs:
                if dic_nifs['nif'] == imprimir_pertenenciaUE:
                    print('Certificado pertenencia a la Unión europea')
                    print(dic_nifs)
                return
        else:
            print('Error: NIF no encontrado')
    except ValueError:
        print('Error: ingrese una opcion valida')
        








while True:
    os.system('cls')
    time.sleep(1)
    
    menu()
    try:
        opcion = int(input('ingrese una opción: \n'))
        
        if opcion == 1:
            print('Grabar Datos')
            grabar()
        elif opcion == 2:
            print('Buscar')
            buscar()
        elif opcion == 3:
            print('Imprir certificados')
            imprimir_certificados()
        elif opcion == 4:
            print('Saliendo...')
            break
    except ValueError:
        print('Error: opcion invalida')    

