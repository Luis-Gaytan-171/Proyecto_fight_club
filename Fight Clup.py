# Simulador de Combate en Python
# Este programa simula un combate por turnos entre dos personajes usando variables, condicionales y ciclos.
# Los personajes pueden atacar y usar habilidades, y se calcula el daño o el efecto en función de sus atributos.

import random

"""
================== Funciones principales del simulador de combate ====================
"""

def crear_personaje(nombre, fuerza, defensa, vida, habilidades):
    """
    Crea un personaje con los atributos especificados.
    recibe: 
        - nombre (cadena)
        - fuerza (entero)
        - defensa (entero)
        - vida (entero)
        - habilidades (matriz de enteros)
    devuelve: diccionario con los atributos del personaje.
    """
    return {
        "nombre": nombre,
        "fuerza": fuerza,
        "defensa": defensa,
        "vida": vida,
        "habilidades": habilidades
    }

def calcular_dano(fuerza_atacante, defensa_defensor):
    """
    Calcula el daño infligido por un personaje al otro.
    recibe: 
        - fuerza_atacante (entero)
        - defensa_defensor (entero)
    devuelve: daño total (entero)
    """
    return max(0, fuerza_atacante - defensa_defensor)  # El daño mínimo es 0

def atacar(atacante, defensor):
    """
    Realiza un ataque del atacante al defensor y reduce la vida del defensor.
    recibe:
        - atacante (diccionario del personaje atacante)
        - defensor (diccionario del personaje defensor)
    """
    dano = calcular_dano(atacante["fuerza"], defensor["defensa"])
    defensor["vida"] -= dano
    print(f"{atacante['nombre']} atacó a {defensor['nombre']} infligiendo {dano} puntos de daño.")
    print(f"Vida restante de {defensor['nombre']}: {defensor['vida']}")

def usar_habilidad(usuario, objetivo, indice_habilidad):
    """
    Usa una habilidad del usuario sobre un objetivo.
    recibe:
        - usuario (diccionario del personaje que usa la habilidad)
        - objetivo (diccionario del personaje objetivo)
        - indice_habilidad (entero, índice de la habilidad en la lista de habilidades)
    """
    tipo_habilidad, valor_habilidad = usuario["habilidades"][indice_habilidad]
    
    if tipo_habilidad == 0:  # Daño
        dano = max(0, valor_habilidad - objetivo["defensa"])
        objetivo["vida"] -= dano
        print(f"{usuario['nombre']} usó una habilidad de daño sobre {objetivo['nombre']} infligiendo {dano} puntos de daño.")
    elif tipo_habilidad == 1:  # Curación
        usuario["vida"] += valor_habilidad
        print(f"{usuario['nombre']} usó una habilidad de curación y restauró {valor_habilidad} puntos de vida.")
    elif tipo_habilidad == 2:  # Defensa
        usuario["defensa"] += valor_habilidad
        print(f"{usuario['nombre']} usó una habilidad de defensa, incrementando su defensa en {valor_habilidad} puntos.")

    print(f"Estado actual de {usuario['nombre']} - Vida: {usuario['vida']}, Defensa: {usuario['defensa']}")

"""
================== Función menú principal ====================
"""

def menu(jugador, enemigo):
    """
    Función que muestra las opciones de acción del jugador y permite elegir una.
    recibe:
        - jugador (diccionario del personaje jugador)
        - enemigo (diccionario del personaje enemigo)
    """
    print(f"\nTurno de {jugador['nombre']}. ¿Qué quieres hacer?")
    print("1. Atacar")
    print("2. Usar habilidad")

    opcion = input("Selecciona una opción (1 o 2): ")

    if opcion == "1":
        atacar(jugador, enemigo)
    elif opcion == "2":
        print("\nSelecciona la habilidad que deseas usar:")
        for i, habilidad in enumerate(jugador["habilidades"]):
            print(f"{i + 1}. Tipo: {['Daño', 'Curación', 'Defensa'][habilidad[0]]}, Valor: {habilidad[1]}")

        indice_habilidad = int(input("Ingresa el número de la habilidad que deseas usar: ")) - 1
        if 0 <= indice_habilidad < len(jugador["habilidades"]):
            usar_habilidad(jugador, enemigo, indice_habilidad)
        else:
            print("Selección de habilidad inválida. Turno perdido.")
    else:
        print("Selección de acción inválida. Turno perdido.")

"""
================== Función principal ====================
"""

def main():
    """
    Función principal del simulador de combate.
    Crea personajes, controla el flujo del combate y determina al ganador.
    """
    # Creación de los personajes con sus atributos y habilidades iniciales
    habilidades_jugador = [
        [0, 25],  # Daño de 25 puntos
        [1, 20],  # Curación de 20 puntos
        [2, 10]   # Defensa incrementada en 10 puntos
    ]
    habilidades_enemigo = [
        [0, 30],  # Daño de 30 puntos
        [1, 15],  # Curación de 15 puntos
        [2, 5]    # Defensa incrementada en 5 puntos
    ]

    print("Bienvenido al Simulador de Combate.\n")
    nombre_jugador = input("Ingresa el nombre de tu personaje: ")
    jugador = crear_personaje(nombre_jugador, 35, 15, 100, habilidades_jugador)
    enemigo = crear_personaje("Enemigo", 30, 10, 100, habilidades_enemigo)

    # Mostrar información inicial de los personajes
    print("\n--- Información inicial de los personajes ---")
    print(f"Personaje Jugador: {jugador}")
    print(f"Personaje Enemigo: {enemigo}")

    # Variable para llevar el control del turno
    turno = 1

    # Ciclo principal del combate
    while jugador["vida"] > 0 and enemigo["vida"] > 0:
        print(f"\n--- Turno {turno} ---")

        # Turno del jugador
        menu(jugador, enemigo)

        # Verificar si el enemigo ha sido derrotado
        if enemigo["vida"] <= 0:
            print(f"{enemigo['nombre']} ha sido derrotado. ¡{jugador['nombre']} gana el combate!")
            break

        # Turno del enemigo (usa habilidades de manera aleatoria para simular IA básica)
        print(f"\nTurno de {enemigo['nombre']}.")
        accion_enemigo = random.choice([0, 1, 2])  # Selección aleatoria de ataque o habilidades
        if accion_enemigo == 0:
            atacar(enemigo, jugador)
        else:
            usar_habilidad(enemigo, jugador, accion_enemigo - 1)  # -1 porque los índices de habilidades inician en 0

        # Verificar si el jugador ha sido derrotado
        if jugador["vida"] <= 0:
            print(f"{jugador['nombre']} ha sido derrotado. ¡{enemigo['nombre']} gana el combate!")
            break

        turno += 1

    print("\n--- Fin del combate ---")

"""
================== Función de pruebas para el simulador ====================
"""

def pruebas_simulador():
    """
    Función de pruebas para el simulador de combate.
    Realiza pruebas en las funciones principales y auxiliares para asegurar su correcto funcionamiento.
    """

    print("\n==================== PRUEBAS DEL SIMULADOR ====================\n")

    # Crear personajes de prueba
    print("Probando creación de personajes...\n")
    habilidades_test_jugador = [
        [0, 20],  # Habilidad 1: Daño de 20 puntos
        [1, 15],  # Habilidad 2: Curación de 15 puntos
        [2, 5]    # Habilidad 3: Defensa de 5 puntos
    ]

    habilidades_test_enemigo = [
        [0, 25],  # Habilidad 1: Daño de 25 puntos
        [1, 10],  # Habilidad 2: Curación de 10 puntos
        [2, 7]    # Habilidad 3: Defensa de 7 puntos
    ]

    # Crear dos personajes de prueba
    jugador_test = crear_personaje("Jugador_Test", 30, 10, 100, habilidades_test_jugador)
    enemigo_test = crear_personaje("Enemigo_Test", 35, 15, 100, habilidades_test_enemigo)

    # Mostrar los personajes para ver que se crearon correctamente
    print("Personaje Jugador:", jugador_test)
    print("Personaje Enemigo:", enemigo_test, "\n")

    # Probar ataques
    print("Probando ataques...\n")
    dano_esperado = calcular_dano(jugador_test["fuerza"], enemigo_test["defensa"])
    print(f"Daño esperado del Jugador_Test al Enemigo_Test: {dano_esperado}")
    atacar(jugador_test, enemigo_test)
   
main()
