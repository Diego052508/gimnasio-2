from datetime import datetime
from datos import clientes, asistencias, guardar_datos

# Registra la asistencia de un cliente si está activo
def registrar_asistencia():
    cedula = input("Cédula del cliente: ")
    if cedula not in clientes: #Busca al cliente con la cedula introducida
        print("Cliente no encontrado.")
        return

    cliente = clientes[cedula]
    if not cliente['activo']:
        print("Cliente con membresía vencida o inactiva.") # si el cliente no esta activo no puede marcar asistencia
        return

    asistencias.append({'cedula': cedula, 'fecha': datetime.now()})
    guardar_datos() #se guarda la asitencia
    print(f"\nAsistencia registrada para {cliente['nombre']}.\n")
