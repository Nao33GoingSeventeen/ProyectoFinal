## Crear diccionario calendario (espera keys y values)
calendario = {}

##Función para mostrar el menu
def mostrarMenu():
    print("\n--------CALENDARIO DE ACTIVIDADES--------\n")
    print("1. AGREGAR ACTIVIDAD")
    print("2. VER ACTIVIDADES DE UNA FECHA")
    print("3. VER TODAS LAS ACTIVIDADES")
    print("4. ELIMINAR UNA ACTIVIDAD")
    print("5. SALIR")
    
##Función para pedir la fecha
def pedirFecha():
    fecha = input("\nIngrese la fecha (AAAA-MM-DD): \n--> ").strip()
    
    ##Verificar que la fecha no esté vacía
    if fecha == "":
        print("\nLa fecha no puede estar vacía ")
        return None
    return fecha

##Función para agregar una actividad
def agregarActividad():
    fecha = pedirFecha()
    
    ##Verificar la fecha
    ##Si está vacía
    if fecha is None:
        return
    ##Si no está vacía
    hora = input("\nDígite la hora (HH:MM): \n--> ").strip()
    ##Si la hora está vacía
    if hora == "" :
        print("\nLa hora no puede estar vacía")
        return
    
    titulo = input("\nTítulo de la actividad: \n--> ").strip()
    ##Si el título está vacío
    if titulo == "":
        print("\nEl título de la actividad no puede estar vacío")
        return
    
    ## Si aún no está la fecha
    if fecha not in calendario:
        ##Se crea una fecha y se deja vacía
        calendario[fecha] = []
        
    ##Crear actividad (keys: values)
    actividad = {"hora": hora, "titulo": titulo}
    
    ## Agregar actividad al calendario dependiendo de la fecha
    calendario[fecha].append(actividad)
    print("\n¡Actividad agregada correctamente!")
    
##Función para ver actividades por fecha
def verActividadesFecha():
    ##Pedir la fecha
    fecha = pedirFecha()
    
    ## Si la fecha está vacía
    if fecha is None:
        return
    
    ##Si la fecha no está en el calendario
    if fecha not in calendario or len(calendario[fecha]) == 0:
        print("\n No hay actividades registradas para esa fecha")
        return
    ##Si hay actividades en esa fecha
    print(f"\n----- ACTIVIDADES DEL {fecha} -----")
    ##Función enumerate:
    ## enumerar todo las actividades que tiene el calendario (teniendo en cuenta su fecha) e inicializar en 1
    for idx, actividad in enumerate(calendario[fecha], start = 1):
        print(f"{idx}. {actividad['hora']} -- {actividad['titulo']}")
        
##Función para ver todas las actividades
def verTodasActividades():
    ##Si el calendario está vacío
    if not calendario:
        print("\nNo hay actividades en el calendario ")     
        return
    
    ##Si hay actividades
    print("\n----- ACTIVIDADES -----\n")
    
    ##Ordenar por fecha con sorted
    for fecha in sorted(calendario.keys()):
        print(f"\n {fecha}: ")
        ##Si no hay actividades para esa fecha
        if len(calendario[fecha]) == 0:
            print("\nSin actividades")
        else:
            ## enumerar todo las actividades que tiene el calendario (teniendo en cuenta su fecha) e inicializar en 1
            for idx, actividad in enumerate(calendario[fecha], start = 1):
                print(f"{idx}. {actividad['hora']} -- {actividad['titulo']}")
            

## Función para eliminar actividades
def eliminarActividad():
    fecha = pedirFecha()
    
    ##Si la fecha está vacía
    if fecha is None:
        return
    ##Si la fecha no está en el calendario
    if fecha not in calendario or len(calendario[fecha]) == 0:
        print("\n No hay actividades para esa fecha")
        return
    
    ## Si está la fecha en el calendario
    print(f"\n----- ACTIVIDADES DEL {fecha} -----")
    for idx, actividad in enumerate(calendario[fecha], start = 1):
        print(f"{idx}. {actividad['hora']} -- {actividad['titulo']}")
        
    ##Pedir el número de la actividad a eliminar
    try:
        numero = int(input("\n Ingrese el número de la actividad a eliminar: \n--> "))
    except ValueError:
        print("\nPor favor dígite números ")
        return
    
    ##Verificar que no sea cero o menor y a la vez que no sea mayor al tamaño
    if numero >= 0 and numero <= len(calendario[fecha]):
        actividadEliminada = calendario[fecha].pop(numero - 1)
        print(f"\n Actividad {actividadEliminada['titulo']} eliminada")
        
        ##Si al eliminar esa actividad la fecha se queda sin actividades
        if len(calendario[fecha]) == 0:
            ##Eliminar fecha del calendario
            del calendario[fecha]
            
    else:
        print("\nNúmero de actividad inválido")
        
##Función para ejecutar programa
def ejecutarAplicacion():
    while True:
        mostrarMenu()
        
        opcion = input("\nDigite una opción: \n--> ")
        
        if opcion == "1":
            agregarActividad()
        elif opcion == "2":
            verActividadesFecha()
        elif opcion == "3":
            verTodasActividades()
        elif opcion == "4":
            eliminarActividad()
        elif opcion == "5":
            print("\nHasta la próxima.....")
            break
        else:
            print("\nOpción de menú inválida")
            print("Intente de nuevo")
            
## Ejecutar siempre la aplicación (ejecutador principal)
if __name__ == "__main__":
    ejecutarAplicacion()
