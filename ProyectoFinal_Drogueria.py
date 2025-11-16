'''
El proyecto final se tratará de un droguería cuya key será el nombre de los medicamentos
Podrá realizar acciones como:
 print("\n------ DROGUERÍA ------\n")
    print("1. AGREGAR MEDICAMENTO")
    print("2. ELIMINAR MEDICAMENTO")
    print("3. VER MEDICAMENTOS POR EL NOMBRE")
    print("4. VER TODA LA LISTA DE MEDICAMENTOS")
    print("5. SALIR")

'''

## Crear un diccionaro llamado drogueria
drogueria = {
    "PARACETAMOL": [
        {"presentacion": "tabletas", "precio": 2500, "unidades": 30, "Fecha De Vencimiento": "2025-05-10"},
        {"presentacion": "jarabe", "precio": 3500, "unidades": 10, "Fecha De Vencimiento": "2024-12-20"},
        {"presentacion": "inyección", "precio": 4800, "unidades": 5, "Fecha De Vencimiento": "2026-01-15"},
        {"presentacion": "suspensión", "precio": 4000, "unidades": 15, "Fecha De Vencimiento": "2025-11-08"},
        {"presentacion": "gota pediátrica", "precio": 3000, "unidades": 8, "Fecha De Vencimiento": "2025-02-14"}
    ],

    "IBUPROFENO": [
        {"presentacion": "tabletas", "precio": 2700, "unidades": 25, "Fecha De Vencimiento": "2025-03-10"},
        {"presentacion": "jarabe", "precio": 3300, "unidades": 12, "Fecha De Vencimiento": "2024-11-30"},
        {"presentacion": "capsulas", "precio": 2900, "unidades": 18, "Fecha De Vencimiento": "2026-04-18"},
        {"presentacion": "inyección", "precio": 5000, "unidades": 7, "Fecha De Vencimiento": "2025-10-05"},
        {"presentacion": "gel tópico", "precio": 4200, "unidades": 20, "Fecha De Vencimiento": "2026-02-22"}
    ],

    "AMOXICILINA": [
        {"presentacion": "capsulas", "precio": 3400, "unidades": 30, "Fecha De Vencimiento": "2025-06-11"},
        {"presentacion": "suspensión", "precio": 4600, "unidades": 12, "Fecha De Vencimiento": "2024-09-19"},
        {"presentacion": "polvo para reconstituir", "precio": 3800, "unidades": 9, "Fecha De Vencimiento": "2025-12-31"},
        {"presentacion": "masticables", "precio": 3200, "unidades": 20, "Fecha De Vencimiento": "2026-03-27"},
        {"presentacion": "tabletas", "precio": 3100, "unidades": 25, "Fecha De Vencimiento": "2025-01-09"}
    ]
}

##Función para mostrar el menú
def mostrarMenu():
    print("\n------ DROGUERÍA ------\n")
    print("1. AGREGAR MEDICAMENTO")
    print("2. ELIMINAR MEDICAMENTO")
    print("3. VER MEDICAMENTOS POR EL NOMBRE")
    print("4. VER TODA LA LISTA DE MEDICAMENTOS")
    print("5. SALIR")
    
##Función para pedir el nombre del medicamento
def pedirNombreMedicamento():
    nombre = input("\nIngrese el nombre del medicamento: \n--> ").strip().upper()
    ##Verificar que el nombre no esté vacío
    if nombre == "":
        print("\nEl nombre del medicamento no puede estar vacío ")
        return None
    ##Si hay nombre, retonar
    return nombre

##Función para agregar un medicamento
def agregarMedicamento():
    ##Pedir el nombre
    nombre = pedirNombreMedicamento()
    ## Si nombre está vacío
    if nombre is None:
        return
    ## Si nombre no está vacío
    ##Pedir el tipo de presentación en la que viene el medicamento
    presentacion = input("\nIngrese el tipo de presentación en la que viene el medicamento: \n--> ").strip()
    ## Si la presentación está vacía
    if presentacion == "":
        print("\nEl campo tipo presentación, no puede estar vacío: \n--> ")
        return
    ##Pedir el precio del medicamento
    precio = input("\nIngrese el precio del medicamento: \n--> ").strip()
    if precio == "":
        print("\n El valor del medicamento no puede ir vacío ")
        return
    
    ##Verificar que sea un valor numérico
    try:
        precioMedicamento = float(precio)
    except ValueError:
        print("\n Dígite solo valores numéricos ")
        return
    ## Si el precio del medicamento es negativo
    if precioMedicamento < 0:
        print("\nNo se aceptan valores negativos")
        return
    
    ##Pedir cuántas unidades hay para el medicamento
    ##Verificar que no esté vacío
    unidades = input("\nIngrese la cantidad de unidades existentes para el medicamento: \n--> ").strip()
    if unidades == "":
        print("\nLas unidades no pueden estar vacías")
        return
    ##Verificar que sea un dato numérico    
    try:
        unidadesMedicamento = int(unidades)
    except ValueError:
        print("\n Dígite solo valores numéricos ")
        return
    ## Si las unidades del medicamento son negativas
    if unidadesMedicamento < 0:
        print("\nNo se aceptan valores negativos")
        return
    ## Si hay cero unidades
    if unidadesMedicamento == 0:
        print("\nDebe haber al menos 1 unidad del medicamento")
        return     
        
    ## Pedir la fecha de Vencimiento del medicamento
    fechaVencimiento = input("\nIngrese la fecha de vencimiento de los medicamentos (AAAA-MM-DD): \n--> ").strip()
    ## Verificar que la fecha de vencimiento no esté vacía
    if fechaVencimiento == "":
        print("\nLa fecha de vencimiento no puede ir vacía")
        return
    
    ##Si el nombre aún no existe
    if nombre not in drogueria:
        ##Se crea una lista con el nombre y se deja vacía
        drogueria[nombre] = []
        
    ##Crear el medicamento
    medicamento = {"presentacion": presentacion, "precio": precioMedicamento, "unidades": unidadesMedicamento, "Fecha De Vencimiento": fechaVencimiento}   
    
    ##Agregar Medicamento a la drogueria
    drogueria[nombre].append(medicamento)
    print("\n¡Medicamento agregado con éxito!")
    
##Ver medicamentos por el nombre
def verMedicamentosNombre():
    nombre = pedirNombreMedicamento()
    ## Si el nombre del medicamento está vacío
    if nombre is None:
        return
    
    ## Si el nombre del medicamento no está en la drogueria
    if nombre not in drogueria or len(drogueria[nombre]) == 0:
        print("\nNo hay medicamentos registrados con ese nombre")
        return
    
    ## Si hay medicamentos con ese nombre
    ## Variable para calcular el total que se ha invertido en todos los medicamentos
    suma = 0
    print(f"\n ------ MEDICAMENTOS {nombre} ------")
    print("num --- Presentación --- Precio --- Unidades --- Fecha de Vencimiento \n")
    ## enumerar todos los medicamentos con ese nombre inicializando en 1
    for idm, medicamento in enumerate(drogueria[nombre], start = 1):
        print(f"{idm}. {medicamento['presentacion']} --- {medicamento['precio']} --- {medicamento['unidades']} --- {medicamento['Fecha De Vencimiento']}")
        suma += medicamento['precio'] * medicamento['unidades']
    
    print("------------------------------")
    print(f"EL TOTAL DE DINERO INVERTIDO EN LOS MEDICAMENTOS ES DE ${suma:,.2f}")
    
## Ver todos los medicamentos de la droguería
def verMedicamentos():
    print("\n ------ MEDICAMENTOS ------")
    if not drogueria:
        print("\nNo hay medicamentos en la droguería")
        return
    ##Hay medicamentos
    ##Total de gastos de tosoa los medicamentos de la droguería
    sumaTotal = 0
    for nombre in drogueria:
        print(f"\n{nombre}:")
        print("num --- Presentación --- Precio --- Unidades --- Fecha de Vencimiento \n")
        
        ## Si no hay medicamentos con ese nombre
        if len(drogueria[nombre]) == 0:
            print("\nSin medicamentos con ese nombre")
        else:
            ## Ordenar los medicamentos por fecha de vencimiento
            medicamentosPorFechaVencimiento = sorted(
                                                    drogueria[nombre], 
                                                     key=lambda medicamento: medicamento["Fecha De Vencimiento"])
            
            ## Variable para calcular el total que se ha invertido en todos los medicamentos
            suma = 0
            for idm, medicamento in enumerate(medicamentosPorFechaVencimiento, start = 1):
                print(f"{idm}. {medicamento['presentacion']} --- {medicamento['precio']} --- {medicamento['unidades']} --- {medicamento['Fecha De Vencimiento']}")
                suma += medicamento['precio'] * medicamento['unidades']
            print("------------------------------")
            print(f"EL TOTAL DE DINERO INVERTIDO EN {nombre} ES DE ${suma:,.2f}")
        ##Total
        sumaTotal += suma
    print("\n------------------------------")
    print(f"EL TOTAL DE DINERO INVERTIDO EN TODOS LOS MEDICAMENTOS ES DE ${sumaTotal:,.2f}")
                      
## Función para eliminar el medicamento
def eliminarMedicamento():
    ##Mostrar la lista de medicamentos que hay con ese nombre
    nombre = pedirNombreMedicamento()
    ## Si el nombre del medicamento está vacío
    if nombre is None:
        return    
    ## Si el nombre del medicamento no está en la drogueria
    if nombre not in drogueria or len(drogueria[nombre]) == 0:
        print("\nNo hay medicamentos registrados con ese nombre")
        return
    
    ## Si hay medicamentos con ese nombre
    print(f"\n------ {nombre} MEDICAMENTOS ------")
    ## enumerar todos los medicamentos con ese nombre inicializando en 1
    for idm, medicamento in enumerate(drogueria[nombre], start = 1):
        print(f"{idm}. {medicamento['presentacion']} --- {medicamento['precio']} --- {medicamento['unidades']} --- {medicamento['Fecha De Vencimiento']}")    
    
    ##Número del medicamento a eliminar
    numero = input("\nIngrese el número del medicamento a eliminar: \n-->").strip()
    ##Verificar que el número no esté vacío
    if numero == "":
        print("\nEl número del medicamento no puede estar vacío ")
        return
    ## Verificar que el valor sea numérico
    try:
        numeroMedicamento = int(numero)
    except ValueError:
        print("\nDígite únicamente números")
        return    
    ## Verificar que el numero sea mayor a cero y menor o igual a los medicamentos
    if 0 < numeroMedicamento <= len(drogueria[nombre]):
        ##Eliminar medicamento
        medicamentoEliminado = drogueria[nombre].pop(numeroMedicamento - 1)
        print(f"\n¡Presentación {medicamentoEliminado['presentacion']} del medicamento {nombre} eliminada!")
        
        ## Si al eliminar ese medicamento no hay más con el mismo nombre
        if len(drogueria[nombre]) == 0:
            ## Eliminar nombre del medicamento de la droguería
            del drogueria[nombre]
    
    else:
        print("\nNúmero no válido")
        
## Función para ejecutar la aplicacion
def ejecutarAplicacion():
    while True:
        mostrarMenu()
        opcion = input("\nDigite una opcion: \n--> ").strip()
        
        ##Condicional dependiendo de la opcion
        if opcion == "1":
            agregarMedicamento()
        elif opcion == "2":
            eliminarMedicamento()
        elif opcion == "3":
            verMedicamentosNombre()
        elif opcion == "4":
            verMedicamentos()
        elif opcion == "5":
            print("\nHasta la próxima ......") 
            break
        else:
            print("\nOpción inválida")
            print("Intente de nuevo...")

## Ejecutar la aplicación
if __name__ == "__main__":
    ejecutarAplicacion()
    
        
        
    