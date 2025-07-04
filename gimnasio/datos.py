import os
from datetime import datetime

# Diccionarios globales para almacenar clientes y asistencias
clientes = {}
asistencias = []

# Nombres de los archivos que contienen los datos
ARCHIVO_CLIENTES = "clientes.txt"
ARCHIVO_ASISTENCIAS = "asistencias.txt"

# Carga los datos de los clientes y asistencias desde los archivos
def cargar_datos():
    global clientes, asistencias
    if os.path.exists(ARCHIVO_CLIENTES):
        with open(ARCHIVO_CLIENTES, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) >= 7:
                    nombre = partes[0].split(":")[1].strip()
                    cedula = partes[1].split(":")[1].strip()
                    contacto = partes[2].split(":")[1].strip()
                    tipo = partes[3].split(":")[1].strip()
                    inicio = datetime.strptime(partes[4].split(":")[1].strip(), "%Y-%m-%d")
                    renovacion = datetime.strptime(partes[5].split(":")[1].strip(), "%Y-%m-%d")
                    estado = partes[6].split(":")[1].strip()
                    clientes[cedula] = {
                        'nombre': nombre,
                        'contacto': contacto,
                        'tipo_membresia': tipo,
                        'fecha_inicio': inicio,
                        'fecha_renovacion': renovacion,
                        'pagos': [],
                        'activo': estado == "Activo"
                    }

     # Cargar asistencias
    if os.path.exists(ARCHIVO_ASISTENCIAS):
        with open(ARCHIVO_ASISTENCIAS, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) >= 3:
                    cedula = partes[0].split(":")[1].strip()
                    fecha_str = partes[2].split(":")[1].strip()
                    asistencias.append({"cedula": cedula, "fecha": datetime.strptime(fecha_str, "%Y-%m-%d")})

# Guarda los datos actuales de clientes y asistencias en archivos de texto
def guardar_datos():
    with open(ARCHIVO_CLIENTES, "w", encoding="utf-8") as f:
        for cedula, cliente in clientes.items():
            f.write(
                f"Nombre: {cliente['nombre']} | "
                f"Cédula: {cedula} | "
                f"Contacto: {cliente['contacto']} | "
                f"Membresía: {cliente['tipo_membresia']} | "
                f"Inicio: {cliente['fecha_inicio'].date()} | "
                f"Renovación: {cliente['fecha_renovacion'].date()} | "
                f"Estado: {'Activo' if cliente['activo'] else 'Inactivo'}\n"
            )
# Guardar asistencias
    with open(ARCHIVO_ASISTENCIAS, "w", encoding="utf-8") as f:
        for a in asistencias:
            nombre = clientes.get(a["cedula"], {}).get("nombre", "Desconocido")
            f.write(f"Cédula: {a['cedula']} | Nombre: {nombre} | Fecha: {a['fecha'].date()}\n")
