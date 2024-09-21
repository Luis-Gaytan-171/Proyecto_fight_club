import random

"""
================== Funciones primarias y secundarias =========================
"""

def crear_personaje(nombre, fuerza, defensa, vida, habilidad):
    """
    (uso de diccionarios, asignación de atributos)
    recibe: nombre (cadena), fuerza (entero), defensa (entero), vida (entero), habilidad (cadena)
    crea un personaje con sus atributos correspondientes
    devuelve: diccionario con los atributos del personaje
    """
    personaje = {
        "nombre": nombre,
        "fuerza": fuerza,
        "defensa": defensa,
        "vida": vida,
        "habilidad": habilidad,
        "vida_inicial": vida  # Guarda la vida inicial para referencia
    }
    return personaje

def calcular_dano(fuerza_atacante, defensa_defensor):
    """
    (operadores aritméticos)
    recibe: fuerza_atacante (entero), defensa_defensor (entero)
    calcula el daño restando la defensa del defensor a la fuerza del atacante
    asegura que el daño no sea negativo (mínimo 0)
    devuelve: entero (daño infligido)
    """
    dano = fuerza_atacante - defensa_defensor
    if dano < 0:
        dano = 0
    return dano

def atacar(atacante, defensor):
    """
    (funciones, diccionarios)
    recibe: atacante (diccionario), defensor (diccionario)
    realiza el cálculo de daño y lo aplica al defensor reduciendo su vida
    muestra el resultado del ataque en pantalla
    """
    dano = calcular_dano(atacante["fuerza"], defensor["defensa"])
    defensor["vida"] -= dano
    print(f"{atacante['nombre']} ataca a {defensor['nombre']} y causa {dano} puntos de daño.")

def usar_habilidad(atacante, defensor):
    """
    (condicionales, operadores)
    recibe: atacante (diccionario), defensor (diccionario)
    ejecuta la habilidad especial del atacante (Curación o Ataque Fuerte)
    si es curación, el atacante recupera vida; si es ataque fuerte, inflige más daño
    """
    print(f"{atacante['nombre']} usa su habilidad especial: {atacante['habilidad']}!")
    if atacante["habilidad"] == "Curación":
        curacion = random.randint(10, 20)
        atacante["vida"] += curacion
        print(f"{atacante['nombre']} recupera {curacion} puntos de vida.")
    elif atacante["habilidad"] == "Ataque Fuerte":
        dano = calcular_dano(atacante["fuerza"] * 2, defensor["defensa"])
        defensor["vida"] -= dano
        print(f"{atacante['nombre']} realiza un ataque fuerte causando {dano} puntos de daño.")

def mostrar_estado(personaje):
    """
    (uso de diccionarios)
    recibe: personaje (diccionario)
    muestra el estado actual del personaje en términos de vida, fuerza y defensa
    """
    print(f"{personaje['nombre']} - Vida: {personaje['vida']} - Fuerza: {personaje['fuerza']} - Defensa: {personaje['defensa']}")

"""
================== Funciones del sistema de turnos ============================
"""

def menu(jugador, enemigo):
    """
    (condicionales, interacción con el usuario)
    recibe: jugador (diccionario), enemigo (diccionario)
    muestra las opciones disponibles para el jugador (atacar o usar habilidad)
    ejecuta la acción seleccionada
    """
    accion = input("Selecciona una acción: Atacar (a), Usar Habilidad (h): ").lower()
    if accion == 'a':
        atacar(jugador, enemigo)
    elif accion == 'h':
        usar_habilidad(jugador, enemigo)

def main():
    """
    (bucle principal, control de turnos)
    inicia y controla el flujo del combate por turnos entre el jugador y el enemigo
    muestra el estado de los personajes en cada turno y determina el ganador
    """
    # Creación de los personajes por parte del usuario
    nombre_jugador = input("Introduce el nombre de tu personaje: ")
    fuerza_jugador = int(input("Introduce la fuerza de tu personaje: "))
    defensa_jugador = int(input("Introduce la defensa de tu personaje: "))
    vida_jugador = int(input("Introduce los puntos de vida de tu personaje: "))
    habilidad_jugador = input("Introduce la habilidad especial de tu personaje (Curación o Ataque Fuerte): ")
    
    jugador = crear_personaje(nombre_jugador, fuerza_jugador, defensa_jugador, vida_jugador, habilidad_jugador)
    
    # Creación del enemigo con datos proporcionados
    nombre_enemigo = input("Introduce el nombre del enemigo: ")
    fuerza_enemigo = int(input("Introduce la fuerza del enemigo: "))
    defensa_enemigo = int(input("Introduce la defensa del enemigo: "))
    vida_enemigo = int(input("Introduce los puntos de vida del enemigo: "))
    habilidad_enemigo = input("Introduce la habilidad especial del enemigo (Curación o Ataque Fuerte): ")

    enemigo = crear_personaje(nombre_enemigo, fuerza_enemigo, defensa_enemigo, vida_enemigo, habilidad_enemigo)

    # Control del combate
    turno = 1
    while jugador["vida"] > 0 and enemigo["vida"] > 0:
        print(f"\n--- Turno {turno} ---")
        mostrar_estado(jugador)
        mostrar_estado(enemigo)

        # Turno del jugador
        print(f"\nTurno de {jugador['nombre']}.")
        menu(jugador, enemigo)

        # Verificar si el enemigo ha sido derrotado
        if enemigo["vida"] <= 0:
            print(f"{enemigo['nombre']} ha sido derrotado.")
            break

        # Turno del enemigo (selección aleatoria de acción)
        print(f"\nTurno de {enemigo['nombre']}.")
        if random.choice(['a', 'h']) == 'a':
            atacar(enemigo, jugador)
        else:
            usar_habilidad(enemigo, jugador)

        # Verificar si el jugador ha sido derrotado
        if jugador["vida"] <= 0:
            print(f"{jugador['nombre']} ha sido derrotado.")
            break

        turno += 1

    # Mostrar el resultado final
    print("\n--- Fin del combate ---")
    if jugador["vida"] > 0:
        print(f"¡{jugador['nombre']} ha ganado el combate!")
    else:
        print(f"¡{enemigo['nombre']} ha ganado el combate!")

    print(f"El combate duró {turno} turnos.")

"""
================== Parte principal del programa ===============================
"""

# Iniciar el simulador de combate llamando a la función principal
main()
