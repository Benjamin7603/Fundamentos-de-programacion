# Función para calcular los descuentos y el líquido a pagar.
def calcular_liquido(sueldo_bruto):
    descuento_salud = sueldo_bruto * 0.07  # 7% de descuento para salud.
    descuento_afp = sueldo_bruto * 0.12    # 12% de descuento para AFP.
    liquido = sueldo_bruto - (descuento_salud + descuento_afp)
    return descuento_salud, descuento_afp, liquido

trabajadores=[]
#Registrar Usuarios.
def registrar_usuario():
    nombre = input("Ingrese el nombre del trabajador: ")
    apellido = input("Ingrese el apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador: ")
    sueldo = int(input("Ingrese sueldo: "))
    trabajador = {"nombre": nombre, "apellido": apellido, "cargo": cargo, "sueldo": sueldo}
    trabajadores.append(trabajador)
    crear_planilla_txt(nombre, apellido, cargo, sueldo) #Se crea el archivo .txt con las respectivas variables

#Hacer listado de trabajadores.
def mostrar_trabajadores():
    if len(trabajadores) == 0:
        print("No hay trabajadores registrados.")
    else:
        print("Listado de trabajadores:")
        for i, trabajador in enumerate(trabajadores, start=1): # Enumerate agrega un contador y start=1 inicia el contador en 1.
            nombre = trabajador["nombre"] # Accede al valor asociado con la clave "nombre"
            apellido = trabajador["apellido"] # Accede al valor asociado con la clave "apellido"
            cargo = trabajador["cargo"] # Accede al valor asociado con la clave "cargo"
            print(f"{i}.- {nombre} {apellido} - {cargo}")

# Imprimir en un archivo .txt los datos del trabajador y su sueldo.
def crear_planilla_txt(nombre, apellido, cargo, sueldo):
    descuento_salud, descuento_afp, liquido = calcular_liquido(sueldo)
    with open("registro_usuarios.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre} {apellido}\n")
        archivo.write(f"Cargo: {cargo}\n")
        archivo.write(f"Sueldo Bruto: {sueldo}\n")
        archivo.write(f"Descuento Salud: {descuento_salud}\n")
        archivo.write(f"Descuento AFP: {descuento_afp}\n")
        archivo.write(f"Liquido a Pagar: {liquido}\n")
        archivo.write("\n")