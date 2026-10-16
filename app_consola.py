cola_pendientes = []
pila_historial = []
siguiente_id = 1

def mostrar_estado():
    print("\n--- ESTADO ACTUAL ---")
    print("Pendientes:", cola_pendientes)
    print("Historial:", pila_historial)
    print("---------------------")

def registrar_solicitud(cliente, asunto):
    global siguiente_id
    if not cliente.strip() or not asunto.strip():
        return None
    
    solicitud = {
        "id": siguiente_id,
        "cliente": cliente.strip(),
        "asunto": asunto.strip(),
        "estado": "pendiente"
    }
    cola_pendientes.append(solicitud)
    siguiente_id += 1
    return solicitud

def atender_siguiente():
    if not cola_pendientes:
        return None
    
    solicitud = cola_pendientes.pop(0)
    solicitud["estado"] = "atendida"
    pila_historial.append(solicitud)
    return solicitud

def deshacer_ultima_atencion():
    if not pila_historial:
        return None
    
    solicitud = pila_historial.pop()
    solicitud["estado"] = "pendiente"
    cola_pendientes.insert(0, solicitud)
    return solicitud

def consultar_siguiente():
    if not cola_pendientes:
        print("No hay solicitudes pendientes en la cola.")
        return None
    siguiente = cola_pendientes[0]
    print(f"\nPróximo turno -> ID: {siguiente['id']} | Cliente: {siguiente['cliente']} | Asunto: {siguiente['asunto']}")
    return siguiente

def buscar_por_id():
    try:
        id_buscado = int(input("Ingrese el ID de la solicitud a buscar: "))
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return None
    
    for s in cola_pendientes:
        if s["id"] == id_buscado:
            print(f"Encontrada en [PENDIENTES]: ID {s['id']} - {s['cliente']} ({s['asunto']})")
            return s
            
    for s in pila_historial:
        if s["id"] == id_buscado:
            print(f"Encontrada en [HISTORIAL]: ID {s['id']} - {s['cliente']} ({s['asunto']})")
            return s
            
    print(f"No se encontró ninguna solicitud con el ID {id_buscado}.")
    return None

def cancelar_solicitud():
    try:
        id_cancelar = int(input("Ingrese el ID de la solicitud pendiente a cancelar: "))
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return None
        
    for i, s in enumerate(cola_pendientes):
        if s["id"] == id_cancelar:
            cancelada = cola_pendientes.pop(i)
            print(f"¡Solicitud ID {id_cancelar} de {cancelada['cliente']} cancelada y eliminada!")
            return cancelada
            
    print("No se encontró una solicitud pendiente con ese ID (solo se pueden cancelar las que están en cola).")
    return None

def deshacer_multiples():
    if not pila_historial:
        print("El historial está vacío. No hay nada que deshacer.")
        return
        
    try:
        cantidad = int(input(f"¿Cuántas solicitudes deseas deshacer? (Tienes {len(pila_historial)} en el historial): "))
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return

    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        return

    for _ in range(cantidad):
        if not pila_historial:
            print("Se han deshecho todas las acciones disponibles en el historial.")
            break
            
        solicitud = pila_historial.pop()
        solicitud["estado"] = "pendiente"
        cola_pendientes.insert(0, solicitud)
        print(f" -> Solicitud ID {solicitud['id']} ({solicitud['cliente']}) devuelta a pendientes.")

def mostrar_estadisticas():
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    print(f"• Solicitudes pendientes en cola: {len(cola_pendientes)}")
    print(f"• Solicitudes atendidas (historial): {len(pila_historial)}")
    print(f"• Total de solicitudes gestionadas: {len(cola_pendientes) + len(pila_historial)}")
    print("---------------------------------")

def ejecutar_menu():
    while True:
        print("\n--- MENÚ PRINCIPAL: SOPORTE TÉCNICO ---")
        print("1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Deshacer última atención")
        print("4. Mostrar estado")
        print("5. Ver siguiente turno")
        print("6. Buscar por ID")
        print("7. Cancelar solicitud")
        print("8. Deshacer múltiples")
        print("9. Ver estadísticas")
        print("10. Salir")
        
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cliente = input("Cliente: ")
            asunto = input("Asunto: ")
            resultado = registrar_solicitud(cliente, asunto)
            print("Registrada:", resultado if resultado else "Datos inválidos")
        elif opcion == "2":
            print("Atendida:", atender_siguiente())
        elif opcion == "3":
            print("Restaurada:", deshacer_ultima_atencion())
        elif opcion == "4":
            mostrar_estado()
        elif opcion == "5":
            consultar_siguiente()
        elif opcion == "6":
            buscar_por_id()
        elif opcion == "7":
            cancelar_solicitud()
        elif opcion == "8":
            deshacer_multiples()
        elif opcion == "9":
            mostrar_estadisticas()
        elif opcion == "10":
            print("¡Saliendo del sistema!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    ejecutar_menu()