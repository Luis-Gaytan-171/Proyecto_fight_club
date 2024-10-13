# ====================== Funciones principales =========================

def calcular_dano(atacante_fuerza, defensor_defensa):
    """
    Calcula el daño infligido en función de la fuerza del atacante y la defensa del defensor.
    Daño mínimo es 1.
    """
    dano = atacante_fuerza - defensor_defensa
    if dano < 1:
        dano = 1  # Daño mínimo de 1
    return dano

def aplicar_dano(vida_actual, dano_recibido):
    """
    Resta el daño recibido a los puntos de vida del personaje.
    """
    vida_actual -= dano_recibido
    if vida_actual < 0:
        vida_actual = 0  # La vida no puede ser negativa
    return vida_actual

def mostrar_estado(personaje, vida, fuerza, defensa):
    """
    Muestra el estado actual del personaje: nombre, vida, fuerza, defensa.
    """
    print(f"{personaje}: Vida = {vida}, Fuerza = {fuerza}, Defensa = {defensa}")

def turno_combate(personaje_atacante, personaje_defensor, fuerza_atacante, defensa_defensor, vida_defensor):
    """
    Ejecuta un turno de combate en el que el atacante inflige daño al defensor.
    """
    print(f"\nTurno de {personaje_atacante} atacando a {personaje_defensor}")
    dano = calcular_dano(fuerza_atacante, defensa_defensor)
    vida_defensor = aplicar_dano(vida_defensor, dano)
    print(f"{personaje_defensor} recibe {dano} puntos de daño.")
    return vida_defensor

def guardar_estado_personajes(estado_combate):
    """
    Guarda el estado final de los personajes en un archivo de texto llamado 'estado_personajes.txt'.
    """
    with open("estado_personajes.txt", "a") as archivo:
        archivo.write(estado_combate + "\n")

# ========================== Función Main ===========================

def main():
    """
    Función principal del simulador de peleas. Los usuarios ingresan los atributos de los personajes,
    y el combate se realiza por turnos hasta que uno de los personajes se quede sin vida.
    """

    # Recibir nombres y atributos de los personajes
    personaje_1 = input("Introduce el nombre del primer personaje: ")
    personaje_1_vida = int(input(f"Introduce la vida de {personaje_1}: "))
    personaje_1_fuerza = int(input(f"Introduce la fuerza de {personaje_1}: "))
    personaje_1_defensa = int(input(f"Introduce la defensa de {personaje_1}: "))

    personaje_2 = input("Introduce el nombre del segundo personaje: ")
    personaje_2_vida = int(input(f"Introduce la vida de {personaje_2}: "))
    personaje_2_fuerza = int(input(f"Introduce la fuerza de {personaje_2}: "))
    personaje_2_defensa = int(input(f"Introduce la defensa de {personaje_2}: "))

    turno_actual = 1

    # Bucle del combate
    while personaje_1_vida > 0 and personaje_2_vida > 0:
        print(f"\n----- Turno {turno_actual} -----")

        # Mostrar estado actual
        mostrar_estado(personaje_1, personaje_1_vida, personaje_1_fuerza, personaje_1_defensa)
        mostrar_estado(personaje_2, personaje_2_vida, personaje_2_fuerza, personaje_2_defensa)

        # Turno de personaje 1
        personaje_2_vida = turno_combate(personaje_1, personaje_2, personaje_1_fuerza, personaje_2_defensa, personaje_2_vida)

        # Si el personaje 2 sigue vivo, turno del personaje 2
        if personaje_2_vida > 0:
            personaje_1_vida = turno_combate(personaje_2, personaje_1, personaje_2_fuerza, personaje_1_defensa, personaje_1_vida)

        turno_actual += 1

    # Determinar ganador
    if personaje_1_vida > 0:
        print(f"\n{personaje_1} ha ganado el combate en {turno_actual - 1} turnos.")
    else:
        print(f"\n{personaje_2} ha ganado el combate en {turno_actual - 1} turnos.")

    # Guardar el estado final del combate en un archivo de texto
    estado_combate = f"Combate entre {personaje_1} y {personaje_2}:\n"
    estado_combate += f"{personaje_1} - Vida: {personaje_1_vida}, Fuerza: {personaje_1_fuerza}, Defensa: {personaje_1_defensa}\n"
    estado_combate += f"{personaje_2} - Vida: {personaje_2_vida}, Fuerza: {personaje_2_fuerza}, Defensa: {personaje_2_defensa}\n"
    estado_combate += f"Ganador: {personaje_1 if personaje_1_vida > 0 else personaje_2}\n"
    estado_combate += f"Turnos jugados: {turno_actual - 1}"

    guardar_estado_personajes(estado_combate)
    print("\nEl estado del combate ha sido guardado en 'estado_personajes.txt'.")

# ======================== Función de Pruebas =========================

def pruebas():
    """
    Realiza pruebas de las funciones principales para asegurar que se comportan de manera esperada.
    """

    # Prueba de cálculo de daño
    print("Prueba 1: Calcular daño")
    dano_esperado = calcular_dano(10, 5)
    print(f"Daño esperado (10 de fuerza vs 5 de defensa): {dano_esperado} (esperado: 5)")

    # Prueba de aplicar daño
    print("Prueba 2: Aplicar daño")
    vida_restante = aplicar_dano(20, 5)
    print(f"Vida restante (después de recibir 5 puntos de daño en 20 puntos de vida): {vida_restante} (esperado: 15)")

    # Prueba de mostrar estado
    print("Prueba 3: Mostrar estado del personaje")
    mostrar_estado("Heroe", 30, 10, 8)

    # Prueba de combate simple
    print("Prueba 4: Simulación de un turno de combate")
    vida_defensor = turno_combate("Heroe", "Villano", 15, 10, 20)
    print(f"Vida restante del defensor Villano después del ataque: {vida_defensor} (esperado: 15)")

# Ejecutar las pruebas
pruebas()

# Ejecutar el programa principal
main()
