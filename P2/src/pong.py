import curses
from curses import wrapper
import random
import time

def pong(stdscr):

    stdscr.keypad(True)
    # Inicializamos una serie de colores, los mismos que el ejemplo del menú
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    #Mensajes que mostraremos por pantalla antes de comenzar
    welcome = "Bienvenido a Pong, puede pausar con la tecla P"
    str_jug1 = "El jugador de la izquierda(1) juega con W(arriba) y S(abajo)"
    str_jug2 = "El jugador de la derecha(2) con las flechas arriba y abajo del teclado"
    str_play = "Pulse cualquier tecla para comenzar"


    stdscr.nodelay(True)

    #Obtenemos los mayores valores que podrán obtener x e y
    max_y, max_x = stdscr.getmaxyx()

    # Las coordenadas x,y serán las de la pelotita, las inicializamos en el medio de la ventana
    x = max_x // 2
    y = max_y // 2

    # Inicializamos los puntos de cada jugador
    puntos_1 = 0
    puntos_2 = 0

    # Inicializamos los valores que podrá tomar la pelota
    # Se podría hacer que la pelota fuera más rápido pero entonces
    # sería capaz de traspasar la pala con el código actual
    # por ello se deja en unitario
    direction_x = 1
    direction_y = 1

    # La dirección será aleatoria
    # Izquierda o derecha
    direction_x = random.choice([-direction_x, direction_x])
    # Arriba o abajo
    direction_y = random.choice([-direction_y, direction_y])

    # Inicializamos las cosas necesarias por ncurses como en los ejemplos
    curses.initscr()
    curses.noecho()

    # Añadimos el recuadro
    stdscr.border()

    # El valor de la longitud de la barra, ahora mismo es una cuarta parte de la pantalla
    barra_len = max_y // 4

    curses.curs_set(False)

    # Para centrar los mensajes
    comienzo_y = int(max_y/2)-3
    comienzo_x = int(max_x/2)

    # Coordenadas de inicio de ambos jugadores
    barra1_y = 2
    barra1_x = 2

    barra2_y = 2
    barra2_x = max_x - 2
    #No se ha anotado ningún punto aún
    gol = False

    # Mostramos por pantalla los mensajes
    stdscr.addstr(comienzo_y,   comienzo_x - len(welcome) // 2, welcome, curses.color_pair(1))
    stdscr.addstr(comienzo_y+1, comienzo_x - len(str_jug1) // 2, str_jug1, curses.color_pair(1))
    stdscr.addstr(comienzo_y+2, comienzo_x - len(str_jug2) // 2, str_jug2, curses.color_pair(2))
    stdscr.addstr(comienzo_y+3, comienzo_x - len(str_play) // 2, str_play, curses.color_pair(1))
    stdscr.refresh()
    # Mientras no se pulse ninguna tecla no comienza la jugada
    while True:
        q = stdscr.getch()
        if q > -1:
            break
    # Inicializamos el marcador
    mensaje = "Jugador 1 = {} |||| Jugador 2= {}".format(puntos_1, puntos_2)
    
    # Mientras ninguno de ambos juagdores anote 5 puntos
    while puntos_1 < 5 and puntos_2 < 5:
        
        #El jugador 2 ha anotado un punto
        if x == 0:
            # Le sumamos el gol
            puntos_2 += 1
            # Devolvemos la pelota al centro
            x = max_x // 2
            y = max_y // 2
            # Dirección aleatoria
            direction_x = random.choice([-direction_x, direction_x])
            direction_y = random.choice([-direction_y, direction_y])
            # Ha habido un gol
            gol = True
            # Actualizamos el marcador
            mensaje = "Jugador 1 = {} |||| Jugador 2= {}".format(puntos_1, puntos_2)
            # Nos saltamos una iteración del bucle ya que no queremos que continúe queremos que vaya a la pausa post-anotar
            continue
        # Anota el jugador 1
        elif x == max_x-1:
            puntos_1 +=1
            x = max_x // 2
            y = max_y // 2
            direction_x = random.choice([-direction_x, direction_x])
            direction_y = random.choice([-direction_y, direction_y])
            gol = True
            mensaje = "Jugador 1 = {} |||| Jugador 2= {}".format(puntos_1, puntos_2)
            continue

        # Colisión arriba o abajo
        if y in (max_y - len("o"), 0): 
            direction_y = -direction_y # reverse
        
        # Esta línea no es que sea necesaria pero con algunos tamaños de ventana a veces crashea el juego al anotar el gol, por ello dejamos esta línea para asegurarnos
        if x in (max_x - len("o"), 0): 
            direction_x = -direction_x # reverse
        
        # Si la pelota colisiona con alguna de las palas de los jugadores por delante, su sentido en el eje x se invierte
        if x == barra1_x and direction_x == -1:
            if y in range(barra1_y, barra1_y+barra_len):
                direction_x = -direction_x

        elif x == barra2_x and direction_x == 1:
            if y in range(barra2_y, barra2_y+barra_len):
                direction_x = -direction_x

        # Obtenemos la tecla pulsada y dependiendo de ello:
        key = stdscr.getch()
        # Saldremos del juego
        if key == ord('q') or key == ord('Q'):
            break
        # Moveremos las palas arriba o abajo
        elif key == curses.KEY_DOWN and barra2_y < max_y - barra_len:
            barra2_y += 1
        elif key == curses.KEY_UP and barra2_y > 0:
            barra2_y -= 1
        elif (key == ord('s') or key == ord('S')) and barra1_y < max_y - barra_len:
            barra1_y += 1
        elif (key == ord('w') or key == ord('W')) and barra1_y > 0:
            barra1_y -= 1
        # Pausamos el juego
        elif (key == ord('p') or key == ord('P')):
            # Una vez pausado no nos detendremos hasta que no se pulse otra vez la tecla P
            while True:
                q = stdscr.getch()
                if (q == ord('p') or q == ord('P')):
                    q = None
                    break
                pausa = "PAUSA, PULSE P PARA CONTINUAR"
                stdscr.addstr(max_y // 2, max_x // 2 - len(pausa) // 2, pausa, curses.color_pair(1))
        
        # Actualizamos los valores de x e y
        x += direction_x
        y += direction_y  

        

        # Similar a usleep en los ejemplos de C
        time.sleep(0.1)

        # Limpiamos la pantalla
        stdscr.clear()     
        # Imprimos el recuadro
        stdscr.border() 
        # Mostramos la pelota
        stdscr.addch(y,x,"o")
        # La línea de medio
        for i in range(1,max_y-1):
            stdscr.addch(i, max_x // 2, '|')
        # Los jugadores
        for i in range(barra_len):
            stdscr.addch(barra2_y + i, barra2_x, '|', curses.color_pair(1))
            stdscr.addch(barra1_y + i, barra1_x, '|', curses.color_pair(2))
        # El marcador
        stdscr.addstr(1, max_x // 2 - len(mensaje) // 2, mensaje, curses.color_pair(3))
        # En caso de gol se detiene el juego
        if gol:
            while True:
                gol = False
                pausa = "PUNTO, PULSE P PARA HACER EL SAQUE"
                stdscr.addstr(max_y // 2, max_x // 2 - len(pausa) // 2, pausa, curses.color_pair(1))
                # Una vez pulsada la tecla P se reanuda el partido
                q = stdscr.getch()
                if (q == ord('p') or q == ord('P')):
                    q = None
                    break

        stdscr.refresh()

    #Se imprime el mensaje final para indicar el resultado y quién ha ganado o si han empatado
    if puntos_2 > puntos_1:
        mensaje_f = "JUGADOR 2 HAS GANADO {} - {}".format(puntos_1, puntos_2)
    elif puntos_1 > puntos_2:
        mensaje_f = "JUGADOR 1 HAS GANADO {} - {}".format(puntos_1, puntos_2)
    else:
        mensaje_f = "EMPATE {} - {}".format(puntos_1, puntos_2)
    # El mensaje se mantiene en pantalla hasta que no se pulse una tecla
    while True:
        stdscr.addstr(max_y // 2, max_x // 2 - len(mensaje_f) // 2, mensaje_f, curses.color_pair(1))
        q = stdscr.getch()
        if q > -1:
            break
    # Se finaliza el juego        
    curses.endwin()

def main():
    curses.wrapper(pong)

if __name__ == "__main__":
    main()