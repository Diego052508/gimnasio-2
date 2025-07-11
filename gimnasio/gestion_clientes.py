from datetime import datetime
from datos import clientes, guardar_datos
from validar import validar_entrada

# Registra un nuevo cliente en el sistema y lo guarda como inactivo inicialmente
def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    cedula = input("Cédula del cliente: ")
    contacto = input("Teléfono o contacto: ")
    tipo_membresia = input("Tipo de membresía (mensual o diaria): ")
    
    valido, mensaje = validar_entrada(nombre, cedula, contacto, tipo_membresia)
    if not valido:
        print(mensaje)
        return

    fecha_inicio = datetime.now()
    clientes[cedula] = {
        'nombre': nombre,
        'contacto': contacto,
        'tipo_membresia': tipo_membresia,
        'fecha_inicio': fecha_inicio,
        'fecha_renovacion': fecha_inicio,
        'pagos': [],
        'activo': False # Se activa al registrar el primer pago
    }
    guardar_datos()
    print(f"\n Cliente {nombre} registrado como INACTIVO el {fecha_inicio.date()}.\n")
    
# Permite modificar los datos de un cliente ya registrado
def modificar_cliente():
    cedula = input("Ingrese la cédula del cliente a modificar: ") #Busca al cliente segun su cedula 
    if cedula not in clientes:
        print("Cliente no encontrado.")
        return

    cliente = clientes[cedula]
    print(f"Datos actuales: Nombre: {cliente['nombre']}, Contacto: {cliente['contacto']}, Membresía: {cliente['tipo_membresia']}") #muestra cuales son los datos actuales del cliente

    # Ingresa los datos nuevos del cliente
    nuevo_nombre = input("Nuevo nombre (dejar vacío para no modificar): ")
    nuevo_contacto = input("Nuevo contacto (dejar vacío para no modificar): ")
    nuevo_tipo = input("Nuevo tipo de membresía (mensual o diaria, dejar vacío para no modificar): ")

    if nuevo_nombre:
        cliente['nombre'] = nuevo_nombre
    if nuevo_contacto:
        cliente['contacto'] = nuevo_contacto
    if nuevo_tipo.lower() in ["mensual", "diaria"]:
        cliente['tipo_membresia'] = nuevo_tipo

    guardar_datos() #se guardan los datos actualizados del cliente
    print("Datos actualizados correctamente.")

# Busca al cliente y muestra todos ssus datos
def buscar_cliente():
    cedula = input("Ingrese la cédula del cliente a buscar: ")
    if cedula in clientes:
        c = clientes[cedula]
        print(f"Nombre: {c['nombre']}\nContacto: {c['contacto']}\nMembresía: {c['tipo_membresia']}\nEstado: {'Activo' if c['activo'] else 'Inactivo'}\nInicio: {c['fecha_inicio'].date()}\nRenovación: {c['fecha_renovacion'].date()}")
    else:
        print("Cliente no encontrado.")

# Elimina al cliente con todos su datos
def eliminar_cliente():
    cedula = input("Cédula del cliente a eliminar: ")
    from datos import asistencias  # evitar import circular
    if cedula in clientes:
        del clientes[cedula]
        asistencias[:] = [a for a in asistencias if a['cedula'] != cedula]
        guardar_datos()
        print("Cliente y asistencias eliminados exitosamente.")
    else:
        print("Cliente no encontrado.")
