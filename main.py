import gamelib
import csv
from random import randint

NPOKEMON_MINIMO = 1
NPOKEMON_MAXIMO = 151

def crear_diccionario_pokemon():
    """
    Crea un diccionario a partir del archivo
    'pokemons.csv' que contiene al número del
    pokémon como clave y sus estadísticas como
    valor.
    """

    with open("pokemons.csv") as pok:
        resultado = {}
        lector = csv.DictReader(pok, delimiter = ";")

        for fila in lector:
            resultado[int(fila["numero"])] = fila
            fila.pop("numero")
         
    return resultado

def crear_diccionario_pokemon_nombre_numero():
    """
    Crea un diccionario a partir del archivo
    'pokemons.csv' que contiene al nombre del
    pokémon como clave y su número como valor.
    """

    with open("pokemons.csv") as pok:
        resultado = {}
        lector = csv.DictReader(pok, delimiter = ";")

        for fila in lector:
            resultado[fila["nombre"]] = int(fila["numero"])
    
    return resultado

def crear_diccionario_pokemon_movimientos():
    """
    Crea un diccionario a partir del archivo
    'movimientos.csv' que contiene al nombre del
    pokémon como clave y una lista de sus movimientos
    como valor.
    """

    with open("movimientos.csv") as mov:
        resultado = {}
        lector = csv.DictReader(mov, delimiter = ";")

        for fila in lector:
            resultado[fila["pokemon"]] = fila["movimientos"].split(",")
    
    return resultado

def mostrar_pokemon(diccionario_pokemon, numero_pokemon):
    """
    Recibe un diccionario de pokemones y
    un número asociado a un pokémon, y
    muestra en pantalla toda su información.
    """

    gamelib.draw_image("screen.gif", 50, 50)
    gamelib.draw_image(diccionario_pokemon[numero_pokemon]["imagen"], 90, 200)
    
    nombre = diccionario_pokemon[numero_pokemon]["nombre"]
    tipo = ", ".join(diccionario_pokemon[numero_pokemon]["tipos"].split(","))
    hp = diccionario_pokemon[numero_pokemon]["hp"]
    atk = diccionario_pokemon[numero_pokemon]["atk"]
    defense = diccionario_pokemon[numero_pokemon]["def"]
    spa = diccionario_pokemon[numero_pokemon]["spa"]
    spd = diccionario_pokemon[numero_pokemon]["spd"]
    spe = diccionario_pokemon[numero_pokemon]["spe"]

    gamelib.draw_text(f"{nombre}", 500, 200, fill="black", anchor="nw", size=25, bold=True)
    gamelib.draw_text(f"Type: {tipo}", 500, 250, fill="black", anchor="nw", size=20, bold=True)
    gamelib.draw_text(f"HP: {hp}", 500, 350, fill="black", anchor="nw", size=20, bold=True)
    gamelib.draw_text(f"ATK: {atk}", 500, 400, fill="black", anchor="nw", size=20, bold=True)
    gamelib.draw_text(f"DEF: {defense}", 500, 450, fill="black", anchor="nw", size=20, bold=True)
    gamelib.draw_text(f"SPA: {spa}", 700, 350, fill="black", anchor="nw", size=20, bold=True)
    gamelib.draw_text(f"SPD: {spd}", 700, 400, fill="black", anchor="nw", size=20, bold=True)
    gamelib.draw_text(f"SPE: {spe}", 700, 450, fill="black", anchor="nw", size=20, bold=True)

def mostrar_equipos(diccionario_de_equipos, numero_equipo):
    """
    Recibe un diccionario de equipos y
    un número de equipo, y muestra en
    pantalla toda la información del equipo.
    """
    
    gamelib.draw_image("screen.gif", 50, 50)

    if not diccionario_de_equipos:
        gamelib.draw_text("No se encuentra ningún Equipo.\n\nCree un Equipo nuevo para\ncomenzar a crear su grupo\nde Pokemones.", 125, 225, fill="black", anchor="nw", size=32, bold=True)

    cantidad_pok = 0

    if diccionario_de_equipos:
        
        y = 0
        y_slot = 0

        equipo_actual = numero_equipo
        gamelib.draw_text(f"Equipo {equipo_actual + 1}", 150, 200, fill="black", anchor="nw", size=20, bold=True)

        for pokemon in diccionario_de_equipos[equipo_actual]:
            cantidad_pok += 1

        for clave, valor in diccionario_de_equipos[equipo_actual].items():
            gamelib.draw_text(f"{clave}", 150, 250 + y, fill="black", anchor="nw", size=20, bold=True)
            gamelib.draw_text(", ".join(valor), 350, 250 + y, fill="black", anchor="nw", size=15, bold=True)
            y += 50

        for n in range(6 - cantidad_pok):
            gamelib.draw_text("<añadir pokémon>", 150, 500 - y_slot, fill="black", anchor="nw", size=15, bold=True)
            y_slot += 50

def crear_equipo(diccionario_de_equipos, numero_equipo):
    """
    Recibe un diccionario de equipos y el número del
    equipo, y crea un equipo en el diccionario de equipos
    que tendrá como clave el número del equipo y como valor
    un diccionario vacio.
    """
    
    gamelib.say("Se ha creado un nuevo Equipo.")

    diccionario_de_equipos[numero_equipo] = {}
    return diccionario_de_equipos[numero_equipo]

def borrar_equipo(diccionario_de_equipos, numero_equipo):
    """
    Recibe un diccionario de equipos y el número del
    equipo, y devuelve un nuevo diccionario de equipos
    en el cuál se acomodarán los equipos de forma que
    no haya números de equipos no consecutivos.
    """

    resp = gamelib.input("¿Está seguro de que quiere eliminar el Equipo actual?")

    if resp == "y" or resp == "Y":

        if numero_equipo == None:
            return diccionario_de_equipos

        del diccionario_de_equipos[numero_equipo]

        diccionario_de_equipos_nuevo = {}
        numeros_equipos_nuevos = -1

        for clave in diccionario_de_equipos:
            numeros_equipos_nuevos += 1
            diccionario_de_equipos_nuevo[numeros_equipos_nuevos] = diccionario_de_equipos[clave]

        gamelib.say(f"Se ha eliminado el Equipo {numero_equipo + 1}.")
        
        return diccionario_de_equipos_nuevo
    return diccionario_de_equipos

def añadir_pokemon(diccionario, movimientos, nombre_numero, equipo):
    """
    Recibe un equipo y, según el dato ingresado por
    el usuario, se utilizará el diccionario de pokemones,
    diccionario de pokemones por nombre-número y el diccionario
    de movimientos para añadir al equipo el nombre de un pokemón
    como clave y una lista de los movimientos elegidos como valor.
    """

    if len(equipo) == 6: return

    movimientos_elegidos = []

    dato = gamelib.input("Ingrese el número del Pokémon o su nombre:")

    if not dato: return

    if dato.isdigit() and NPOKEMON_MINIMO <= int(dato) <= NPOKEMON_MAXIMO:
        nombre_pokemon = diccionario[int(dato)]["nombre"]
        mov_pok = movimientos[nombre_pokemon]
    elif nombre_numero.get(dato, ""):
        nombre_pokemon = dato
        mov_pok = movimientos[dato]
    else:
        return
    
    for movimiento in mov_pok:
        
        if len(movimientos_elegidos) == 4: break
        
        resp = gamelib.input(f"¿Añadir {movimiento}?")

        if resp == "y" or resp == "Y":
            movimientos_elegidos.append(movimiento)
        if resp == None:
            break

    if movimientos_elegidos == []:
        gamelib.say("Para agregar un Pokémon debe elegir al menos un movimiento.")
        return
    
    equipo[nombre_pokemon] = movimientos_elegidos

def eliminar_pokemon(diccionario, equipo):
    """
    Recibe un equipo y, según el dato ingresado
    por el usuario, se utilizará el diccionario de
    pokemones para eliminar el pokemón del equipo.
    """

    if equipo == {}:
        gamelib.say("El Equipo no tiene Pokemones para eliminar.")
        return

    dato = gamelib.input("Ingrese el número del Pokémon o su nombre:")

    if not dato: return

    else:

        if dato.isdigit() and NPOKEMON_MINIMO <= int(dato) <= NPOKEMON_MAXIMO:
            dato = diccionario[int(dato)]["nombre"]

        if not dato in equipo:
            gamelib.say("No se encuentra el Pokémon en el equipo.")
            return
        
        del equipo[dato]

def guardar_equipos(equipos):
    """
    Escribe en el archivo 'equipos.csv', según
    la información de los equipos del diccionario
    de equipos, líneas con el formato:
    
    'equipo;pokemones;movimientos'

    donde cada línea es separada por equipos.
    """
    
    lista = []
    
    with open("D:\prog\Tp_3\equipos.csv", "w") as eq:
        eq.write("equipo;pokemones;movimientos\n")

        for equipo, valor in equipos.items():
            eq.write(f"{equipo};")
            
            for pokemon in valor:
                lista.append(pokemon)
            eq.write(",".join(lista))
            lista = []

            eq.write(";")
            
            for movimientos in valor.values():
                mov = "-".join(movimientos)
                lista.append(mov)
            
            eq.write(",".join(lista))
            eq.write("\n")
            
            lista = []

def cargar_equipos():
    """
    Lee toda la información del archivo
    'equipos.csv' y devuelve un diccionario
    de equipos.
    Si el archivo no existe, lo crea y devuelve
    un diccionario vacío.
    """

    resultado = {}
    pokemons = {}
    index = 0

    try:
        with open("D:\prog\Tp_3\equipos.csv") as entrada:
            entrada.readline()
            
            for linea in entrada:
                equipo, pokemones, movimientos = linea.rstrip().split(";")
                lista_de_movimientos = movimientos.split(",")
                lista_de_pokemones = pokemones.split(",")

                for movs in lista_de_movimientos:

                    if lista_de_pokemones[index] == "":
                        resultado[int(equipo)] = {}
                        continue

                    pokemons[lista_de_pokemones[index]] = movs.split("-")
                    resultado[int(equipo)] = pokemons
                    index += 1
                    if index == len(lista_de_movimientos):
                        index = 0
                
                pokemons = {}

        return resultado
    
    except FileNotFoundError:
        with open("equipos.csv", "w") as f:
            return {}
       
def main():
    """
    Función principal. 
    Ejecuta un simulador de Pokedex.
    Muestra en pantalla una interfaz que le permite al usuario interactuar y jugar.
    """

    diccionario = crear_diccionario_pokemon()
    nombre_numero = crear_diccionario_pokemon_nombre_numero()
    movimientos = crear_diccionario_pokemon_movimientos()
    diccionario_de_equipos = cargar_equipos()

    gamelib.title("POKEDEX")
    gamelib.resize(950, 700)
    numero_pokemon = 1
    numero_equipo = 0

    while gamelib.is_alive():

        gamelib.draw_begin()
        mostrar_pokemon(diccionario, numero_pokemon)
        gamelib.draw_end()

        ev = gamelib.wait()

        if not ev:
            guardar_equipos(diccionario_de_equipos)
            break

        if ev.type == gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y
        else:
            x, y = -1, -1

        if ev.type == gamelib.EventType.KeyPress and ev.key == "Escape" or (770 <= x <= 870 and 70 <= y <= 120):
            resp = gamelib.input("¿Está seguro de que quiere salir?")
            
            if resp == "y" or resp == "Y":
                guardar_equipos(diccionario_de_equipos)
                break

        if ev.type == gamelib.EventType.KeyPress and ev.key == "Right" or (490 <= x <= 590 and 580 <= y <= 630):
            numero_pokemon += 1
            if numero_pokemon == NPOKEMON_MAXIMO + 1:
                numero_pokemon = 1

        if ev.type == gamelib.EventType.KeyPress and ev.key == "Left" or (350 <= x <= 450 and 580 <= y <= 630):
            numero_pokemon += -1
            if numero_pokemon == NPOKEMON_MINIMO - 1:
                numero_pokemon = NPOKEMON_MAXIMO
        
        if ev.type == gamelib.EventType.KeyPress and (ev.key == "s" or ev.key == "S") or (150 <= x <= 250 and 110 <= y <= 140):
            dato = gamelib.input("Ingrese un número o un nombre:")

            if not dato: continue

            if dato.isdigit() and NPOKEMON_MINIMO <= int(dato) <= NPOKEMON_MAXIMO:
                numero_pokemon = int(dato)

            if nombre_numero.get(dato, ""):
                numero_pokemon = nombre_numero[dato]

        if ev.type == gamelib.EventType.KeyPress and (ev.key == "h" or ev.key == "H") or (80 <= x <= 130 and 70 <= y <= 120):
            gamelib.say("ATAJOS DEL TECLADO:\n-E (Ver Equipos)\n-S (Buscar)\n-C (Crear Equipo)\n-D (Borrar Equipo)\n-B (Borrar Pokémon)\n-A (Añadir Pokémon)\n\nUTILIDAD:\n-Left/Right (Mover)\n-Y (Responder afirmación)\n-H (Ayuda)\n-Esc (Salir)")

        if ev.type == gamelib.EventType.KeyPress and (ev.key == "e" or ev.key == "E") or (660 <= x <= 760 and 70 <= y <= 120):

            while gamelib.is_alive():
                gamelib.draw_begin()
                mostrar_equipos(diccionario_de_equipos, numero_equipo)
                gamelib.draw_end()
                
                ev = gamelib.wait()

                if not ev:
                    guardar_equipos(diccionario_de_equipos)
                    break

                if ev.type == gamelib.EventType.ButtonPress:
                    x, y = ev.x, ev.y
                else:
                    x, y = -1, -1

                if ev.type == gamelib.EventType.KeyPress and (ev.key == "c" or ev.key == "C") or (80 <= x <= 180 and 580 <= y <= 630):
                    numero_equipo_creado = len(diccionario_de_equipos)
                    crear_equipo(diccionario_de_equipos, numero_equipo_creado)
                    numero_equipo = numero_equipo_creado 

                if ev.type == gamelib.EventType.KeyPress and (ev.key == "a" or ev.key == "A") or (770 <= x <= 870 and 580 <= y <= 630):
                    try:
                        añadir_pokemon(diccionario, movimientos, nombre_numero, diccionario_de_equipos[numero_equipo])
                    except KeyError:
                        gamelib.say("Cree un Equipo para poder añadir Pokemones.")
                
                if ev.type == gamelib.EventType.KeyPress and (ev.key == "b" or ev.key == "B") or (660 <= x <= 760 and 580 <= y <= 630):

                    try:
                        eliminar_pokemon(diccionario, diccionario_de_equipos[numero_equipo])
                    except KeyError:
                        gamelib.say("Cree un Equipo para poder eliminar Pokemones.")
                
                if ev.type == gamelib.EventType.KeyPress and (ev.key == "e" or ev.key == "E") or (660 <= x <= 760 and 70 <= y <= 120):
                    break

                if ev.type == gamelib.EventType.KeyPress and (ev.key == "d" or ev.key == "D") or (190 <= x <= 290 and 580 <= y <= 630):
                    
                    if not diccionario_de_equipos:
                        continue

                    diccionario_de_equipos = borrar_equipo(diccionario_de_equipos, numero_equipo)
                    numero_equipo = 0

                if ev.type == gamelib.EventType.KeyPress and (ev.key == "s" or ev.key == "S") or (150 <= x <= 250 and 110 <= y <= 140):

                    dato = gamelib.input("Ingrese el número del Equipo:")

                    if not dato: continue

                    if dato.isdigit():
                        dato = int(dato) - 1
                        if dato in diccionario_de_equipos:
                            numero_equipo = dato
                        else:
                            gamelib.say("El Equipo no existe.")
                    
                    else:
                        gamelib.say("No ingresó un número válido.")

                if ev.type == gamelib.EventType.KeyPress and (ev.key == "h" or ev.key == "H") or (80 <= x <= 130 and 70 <= y <= 120):
                    gamelib.say("ATAJOS DEL TECLADO:\n-E (Ver Equipos)\n-S (Buscar)\n-C (Crear Equipo)\n-D (Borrar Equipo)\n-B (Borrar Pokémon)\n-A (Añadir Pokémon)\n\nUTILIDAD:\n-Left/Right (Mover)\n-Y (Responder afirmación)\n-H (Ayuda)\n-Esc (Salir)")
                
                if ev.type == gamelib.EventType.KeyPress and ev.key == "Escape" or (770 <= x <= 870 and 70 <= y <= 120):
                    break
                
                if ev.type == gamelib.EventType.KeyPress and ev.key == "Right" or (490 <= x <= 590 and 580 <= y <= 630):
                    numero_equipo += 1
                    if numero_equipo > len(diccionario_de_equipos) - 1:
                        numero_equipo = 0

                if ev.type == gamelib.EventType.KeyPress and ev.key == "Left" or (350 <= x <= 450 and 580 <= y <= 630):
                    numero_equipo += -1
                    if numero_equipo < 0:
                        numero_equipo = len(diccionario_de_equipos) - 1

        if not ev:
            guardar_equipos(diccionario_de_equipos)
            break

gamelib.init(main)