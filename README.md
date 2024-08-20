Luis Gaytan Garcia A01771191

Simulador de peleas

Descripcion:

El simulador implementa un sistema de juego basado en turnos, en el cual el personaje del usuario se enfrentara a un personaje generado a partir de las estadisticas insertadas por el usuario.
El daño infligido se calcula en función de variables como la fuerza y la defensa de los personajes
Los usuarios tienen la libertad de personalizar a sus personajes, ajustando sus atributos iniciales para crear estrategias únicas y adaptadas a su estilo de juego.

Algoritmo: Simulador de Peleas

Entradas:

Nombre de los personajes
Atributos de los personajes

Procesos:

Crear los Personajes con los datos proporcionados por el usuario.
Inicializar una variable para llevar el control del turno.
Bucle principal del combate:

Mientras ambos personajes tengan puntos de vida:
Determinar qué personaje tiene el turno.
Mostrar información sobre el estado actual de ambos personajes (nombre, atributos)
Pedir al jugador que seleccione una acción (atacar, usar habilidad, usar objeto, etc.).
Ejecutar la acción seleccionada:
Atacar: Calcular el daño basado en la fuerza del atacante y la defensa del defensor. Restar el daño a los puntos de vida del defensor.
Usar habilidad: Aplicar el efecto de la habilidad especial seleccionada.
Usar objeto: Aplicar el efecto del objeto equipado.
Cambiar al siguiente turno.
Finalización del combate:

Determinar el ganador (el personaje con más puntos de vida al final del combate).
Mostrar un mensaje indicando el ganador y un resumen del combate (número de turnos, daño total infligido, etc.).

Salidas:

Información durante el combate
Resultado final
Resumen estadístico del combate.
