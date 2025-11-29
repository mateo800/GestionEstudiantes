# ============================================================
# SISTEMA DE GESTIÓN DE ESTUDIANTES - CLUB DE CIENCIA ESCOLAR
# ============================================================

# CLASE ESTUDIANTE
class Estudiante:
    def __init__(self, nombre, edad, grado, puntajes):
        """Constructor de la clase Estudiante"""
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.puntajes = puntajes  # Lista con 3 puntajes
        self.promedio = 0.0
        self.calcular_promedio()
    
    def calcular_promedio(self):
        """Calcula el promedio de los puntajes del estudiante"""
        suma = 0
        for puntaje in self.puntajes:
            suma += puntaje
        self.promedio = suma / len(self.puntajes)
    
    def obtener_nombre(self):
        """Retorna el nombre del estudiante"""
        return self.nombre
    
    def obtener_edad(self):
        """Retorna la edad del estudiante"""
        return self.edad
    
    def obtener_grado(self):
        """Retorna el grado del estudiante"""
        return self.grado
    
    def obtener_puntajes(self):
        """Retorna la lista de puntajes"""
        return self.puntajes
    
    def obtener_promedio(self):
        """Retorna el promedio del estudiante"""
        return self.promedio
    
    def actualizar_puntaje(self, indice, nuevo_puntaje):
        """Actualiza un puntaje específico y recalcula el promedio"""
        if 0 <= indice < len(self.puntajes):
            self.puntajes[indice] = nuevo_puntaje
            self.calcular_promedio()
            return True
        return False


# FUNCIONES 

def limpiar_pantalla():
    """pone líneas en blanco"""
    print("\n" * 2)


def mostrar_titulo(titulo):
    """Muestra un título decorado"""
    linea = "=" * 60
    print(linea)
    print(titulo.center(60))
    print(linea)


def mostrar_subtitulo(subtitulo):
    """Muestra un subtítulo decorado"""
    print("\n" + "-" * 60)
    print(subtitulo)
    print("-" * 60)


def pausar():
    """Pausa la ejecución hasta que el usaurio presione Enter"""
    input("\nPresione Enter para continuar...")


def validar_numero_entero(mensaje, minimo, maximo):
    """Valida que el usuario ingrese un número entero en un rango"""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Error: Ingrese un valor entre {minimo} y {maximo}")
        except ValueError:
            print("Error: Debe ingresar un número entero válido")


def validar_numero_decimal(mensaje, minimo, maximo):
    """Valida que el usuario ingrese un número decimal en un rango"""
    while True:
        try:
            valor = float(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Error: Ingrese un valor entre {minimo} y {maximo}")
        except ValueError:
            print("Error: Debe ingresar un número válido")


#FUNCIÓN DE CLASIFICACIÓN

def clasificar_estudiante(promedio):
    """Clasifica al estudiante según su promedio"""
    if promedio >= 4.5:
        categoria = "Excelente"
        mensaje = "Felicitaciones Rendimiento sobresaliente"
    elif promedio >= 3.5:
        categoria = "Bueno"
        mensaje = "Buen trabajo, sigue así"
    else:
        categoria = "Requiere apoyo"
        mensaje = "Necesitas refuerzo en las actividades"
    return categoria, mensaje


#FUNCIÓN DE REGISTRO

def registrar_estudiantes():
    """Registra los estudiantes del club"""
    mostrar_titulo("REGISTRO DE ESTUDIANTES")
    
    # Solicitar número de estudiantes
    numero_estudiantes = validar_numero_entero(
        "\n¿Cuántos estudiantes desea registrar? (1-100): ", 1, 100
    )
    
    lista_estudiantes = []
    
    # Ingresar información de cada estudiante
    for i in range(numero_estudiantes):
        print(f"\n{'='*60}")
        print(f"ESTUDIANTE {i + 1} de {numero_estudiantes}".center(60))
        print("="*60)
        
        # Solicitar datos básicos
        nombre = input("Nombre completo: ").strip()
        while not nombre:
            print("El nombre no puede estar vacío")
            nombre = input("Nombre completo: ").strip()
        
        edad = validar_numero_entero("Edad (5-18): ", 5, 18)
        grado = validar_numero_entero("Grado (1-11): ", 1, 11)
        
        # Solicitar puntajes de los 3 retos
        print("\nIngrese los puntajes de los 3 retos científicos (0.0 - 5.0):")
        puntajes = []
        for j in range(3):
            puntaje = validar_numero_decimal(
                f"  Reto {j + 1}: ", 0.0, 5.0
            )
            puntajes.append(puntaje)
        
        # Crear objeto estudiante y agregarlo a la lista
        estudiante = Estudiante(nombre, edad, grado, puntajes)
        lista_estudiantes.append(estudiante)
        
        print(f"Estudiante '{nombre}' registrado con promedio: {estudiante.obtener_promedio():.2f}")
    
    print(f"\nSe registraron {numero_estudiantes} estudiantes exitosamente")
    pausar()
    return lista_estudiantes


#FUNCIONES DE VISUALIZACIÓN

def mostrar_todos_estudiantes(lista_estudiantes):
    """Muestra todos los estudiantes registrados con sus datos"""
    if not lista_estudiantes:
        print("\nNo hay estudiantes registrados")
        pausar()
        return
    
    mostrar_titulo("LISTADO COMPLETO DE ESTUDIANTES")
    
    print(f"\nTotal de estudiantes: {len(lista_estudiantes)}\n")
    
    for i in range(len(lista_estudiantes)):
        estudiante = lista_estudiantes[i]
        categoria, mensaje= clasificar_estudiante(estudiante.obtener_promedio())
        
        print(f"{'─'*60}")
        print(f"[{i + 1}] {estudiante.obtener_nombre()}")
        print(f"{'─'*60}")
        print(f"  Edad: {estudiante.obtener_edad()} años | Grado: {estudiante.obtener_grado()}°")
        print(f"  Puntajes: {estudiante.obtener_puntajes()}")
        print(f"  Promedio: {estudiante.obtener_promedio():.2f}")
        print(f"  Clasificación:{categoria}")
        print(f"  {mensaje}")
        print()
    
    pausar()


def mostrar_estadisticas(lista_estudiantes):
    """Muestra estadísticas generales del grupo"""
    if not lista_estudiantes:
        print("\nNo hay estudiantes registrados")
        pausar()
        return
    
    mostrar_titulo("ESTADÍSTICAS DEL GRUPO")
    
    # Calcular promedio general usando acumualdor
    suma_promedios = 0
    for estudiante in lista_estudiantes:
        suma_promedios += estudiante.obtener_promedio()
    
    promedio_general = suma_promedios / len(lista_estudiantes)
    
    # Contar estudiantes por categoría usando acumuladores
    contador_excelente = 0
    contador_bueno = 0
    contador_apoyo = 0
    
    for estudiante in lista_estudiantes:
        promedio = estudiante.obtener_promedio()
        if promedio >= 4.5:
            contador_excelente += 1
        elif promedio >= 3.5:
            contador_bueno += 1
        else:
            contador_apoyo += 1
    
    # Mostrar estadísticas
    print(f"\nRESUMEN GENERAL")
    print(f"{'─'*60}")
    print(f"  Total de estudiantes: {len(lista_estudiantes)}")
    print(f"  Promedio general del grupo: {promedio_general:.2f}")
    print()
    print(f"DISTRIBUCIÓN POR DESEMPEÑO")
    print(f"{'─'*60}")
    print(f"  Excelente (≥ 4.5):        {contador_excelente} estudiantes")
    print(f"  Bueno (3.5 - 4.4):        {contador_bueno} estudiantes")
    print(f"  Requiere apoyo (< 3.5):   {contador_apoyo} estudiantes")
    
    pausar()


#FUNCIONES DE BÚSQUEDA Y ORDENAMENTO 

def buscar_estudiante_por_nombre(lista_estudiantes):
    """Busca y muestra un estudiante por su nombre"""
    if not lista_estudiantes:
        print("\nNo hay estudiantes registrados")
        pausar()
        return
    
    mostrar_subtitulo("BUSCAR ESTUDIANTE POR NOMBRE")
    
    # Crear arreglo con nombres
    nombres = []
    for estudiante in lista_estudiantes:
        nombres.append(estudiante.obtener_nombre())
    
    nombre_buscar = input("\nIngrese el nombre a buscar: ").strip().lower()
    
    encontrado = False
    for i in range(len(nombres)):
        if nombre_buscar in nombres[i].lower():
            estudiante = lista_estudiantes[i]
            categoria, mensaje = clasificar_estudiante(estudiante.obtener_promedio())
            
            print(f"\nESTUDIANTE ENCONTRADO")
            print(f"{'─'*60}")
            print(f"  Nombre: {estudiante.obtener_nombre()}")
            print(f"  Edad: {estudiante.obtener_edad()} años")
            print(f"  Grado: {estudiante.obtener_grado()}°")
            print(f"  Puntajes: {estudiante.obtener_puntajes()}")
            print(f"  Promedio: {estudiante.obtener_promedio():.2f}")
            print(f"  Clasificación: {categoria}")
            print(f"  {mensaje}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"\nNo se encontró ningún estudiante con el nombre '{nombre_buscar}'")
    
    pausar()


def ordenar_por_promedio(lista_estudiantes):
    """Ordena los estudiantes por promedio usando método burbuja"""
    if not lista_estudiantes:
        print("\nNo hay estudiantes registrados")
        pausar()
        return
    
    mostrar_subtitulo("ORDENAR ESTUDIANTES POR PROMEDIO")
    
    # Método de ordenamiento burbuja (de mayor a menor)
    n = len(lista_estudiantes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_estudiantes[j].obtener_promedio() < lista_estudiantes[j + 1].obtener_promedio():
                # Intercambiar estudiantes
                temporal = lista_estudiantes[j]
                lista_estudiantes[j] = lista_estudiantes[j + 1]
                lista_estudiantes[j + 1] = temporal
    
    print("\nEstudiantes ordenados por promedio (de mayor a menor)\n")
    
    # Mostrar lista ordenada
    print(f"{'POSICIÓN':<10} {'NOMBRE':<30} {'PROMEDIO':<10}")
    print("─" * 60)
    
    for i in range(len(lista_estudiantes)):
        estudiante = lista_estudiantes[i]
        print(f"{i + 1:<10} {estudiante.obtener_nombre():<30} {estudiante.obtener_promedio():<10.2f}")
    
    pausar()


#FUNCIONES DE MATRIZ 

def crear_matriz_puntajes(lista_estudiantes):
    """Crea una matriz bidimensional con los puntajes de todos los estudiantes"""
    if not lista_estudiantes:
        print("\nNo hay estudiantes registrados")
        pausar()
        return
    
    mostrar_titulo("ANÁLISIS MATRICIAL DE PUNTAJES")
    
    # Crear matriz
    matriz = []
    for estudiante in lista_estudiantes:
        matriz.append(estudiante.obtener_puntajes())
    
    # Mostrar matriz de puntajes
    print("\nMATRIZ DE PUNTAJES POR ESTUDIANTE Y RETO\n")
    print(f"{'ESTUDIANTE':<30} {'RETO 1':<10} {'RETO 2':<10} {'RETO 3':<10} {'TOTAL':<10}")
    print("─" * 70)
    
    for i in range(len(matriz)):
        nombre = lista_estudiantes[i].obtener_nombre()
        if len(nombre) > 28:
            nombre = nombre[:28] + ".."
        
        total = 0
        for puntaje in matriz[i]:
            total += puntaje
        
        print(f"{nombre:<30} {matriz[i][0]:<10.2f} {matriz[i][1]:<10.2f} {matriz[i][2]:<10.2f} {total:<10.2f}")
    
    # Calcular promedios por reto
    print("\n" + "─" * 70)
    print("\nPROMEDIOS POR RETO\n")
    
    for reto in range(3):
        suma_reto = 0
        for i in range(len(matriz)):
            suma_reto += matriz[i][reto]
        promedio_reto = suma_reto / len(matriz)
        print(f"  Reto {reto + 1}: {promedio_reto:.2f}")
    
    # Encontrar estudiante con mayor puntaje total
    print("\n" + "─" * 70)
    print("\nESTUDIANTE CON MAYOR PUNTAJE TOTAL\n")
    
    mayor_total = 0
    indice_mayor = 0
    
    for i in range(len(matriz)):
        total = 0
        for puntaje in matriz[i]:
            total += puntaje
        
        if total > mayor_total:
            mayor_total = total
            indice_mayor = i
    
    mejor_estudiante = lista_estudiantes[indice_mayor]
    print(f"  Estudiante: {mejor_estudiante.obtener_nombre()}")
    print(f"  Puntaje total: {mayor_total:.2f}")
    print(f"  Promedio: {mejor_estudiante.obtener_promedio():.2f}")
    
    pausar()


# ===== MENÚ PRINCIPAL =====

def mostrar_menu():
    """Muestra el menú principal del sistema"""
    mostrar_titulo("CLUB DE CIENCIA ESCOLAR - MENÚ PRINCIPAL")
    print("\n1. Registrar estudiantes")
    print("2. Ver todos los estudiantes")
    print("3. Ver estadísticas del grupo")
    print("4. Buscar estudiante por nombre")
    print("5. Ordenar por promedio")
    print("6. Análisis matricial de puntajes")
    print("7. Salir")
    print("\n" + "─" * 60)


def ejecutar_sistema():
    """Función principal que ejecuta el sistema"""
    lista_estudiantes = []
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        opcion = validar_numero_entero("Seleccione una opción (1-7): ", 1, 7)
        
        limpiar_pantalla()
        
        if opcion == 1:
            lista_estudiantes = registrar_estudiantes()
        
        elif opcion == 2:
            mostrar_todos_estudiantes(lista_estudiantes)
        
        elif opcion == 3:
            mostrar_estadisticas(lista_estudiantes)
        
        elif opcion == 4:
            buscar_estudiante_por_nombre(lista_estudiantes)
        
        elif opcion == 5:
            ordenar_por_promedio(lista_estudiantes)
        
        elif opcion == 6:
            crear_matriz_puntajes(lista_estudiantes)
        
        elif opcion == 7:
            mostrar_titulo("¡GRACIAS POR USAR EL SISTEMA!")
            print("\nHasta pronto\n")
            break


ejecutar_sistema()