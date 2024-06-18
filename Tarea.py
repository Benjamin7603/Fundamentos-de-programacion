import funcionesTarea as funcion
import time
import os #  Funciones del sistema operativo para manejar archivos, directorios y variables de entorno.

flag1=True;
flag2=True;

while flag1:
    usuarios_registrados= { # Diccionario para usuarios almacenados.
        "cristobal_gv": "1234",
        "benja_g": "4321",
        "francis_vr": "1111"
    }
    #Login de los usuarios.
    usuario = input("Ingrese un nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    if usuario in usuarios_registrados and contraseña == usuarios_registrados[usuario]:
        print(f"Inicio de sesion exitosa. ¡Bienvenido, @{usuario}!")
        print()
        while flag2:
            print("\n:::: MENÚ DE OPCIONES ::::\n")
            print("1.- Registrar trabajador.")
            print("2.- Listar todos los trabajadores.")
            print("3.- Imprimir planilla de sueldos.")
            print("4.- Salir del programa.")
            try: # Try para asegurarnos que las opciones ingresadas sean un valor númerico entre 1 a 4.
                opcion=int(input("\nIngrese una opcion: "))
            except:
                print("Por favor ingrese una opción valida. Vuelva a intentarlo")
            else:
                if opcion == 1:
                    print("::: Registrar Trabajadores :::\n")
                    funcion.registrar_usuario()
                elif opcion == 2:
                    print("::: Listado de Trabajadores :::")
                    funcion.mostrar_trabajadores()
                elif opcion == 3:
                    print("::: Imprimir planilla de Sueldo :::")
                    # El usuario debe ir al archivo .txt para visualizar los datos de los trabajadores.
                    print("Datos guardados en archivo .txt DIRÍJASE A ESE DOCUMENTO PARA VISUALIZARLO")
                elif opcion == 4:
                    print("Saliendo del programa...")
                    time.sleep(1.2)
                # Eliminar el archivo "registro_usuarios.txt".
                    try:
                        os.remove("registro_usuarios.txt")
                        print("El archivo 'registro_usuarios.txt' ha sido eliminado.")
                    except FileNotFoundError:
                        print("El archivo 'registro_usuarios.txt' no fue encontrado")
                    flag1=False
                    flag2=False
                    break # Cerrar el programa.
                else:
                    print("Por favor ingrese una opción válida.") #El usuario necesita ingresar una opción válida.
    else:
        print("\nCredenciales invalidas. Por favor, vuelva a intentarlo.\n") #Usuario y contraseña deben ser correctos, de lo contrario no dara acceso al menú.