import curses
from curses import wrapper
import random
import time

def pong(stdscr):
    DELAY = 30000

    

    stdscr.keypad(True)

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    welcome = "Bienvenido a Pong, puede pausar con la tecla P"
    str_jug1 = "El jugador de la izquierda(1) juega con W(arriba) y S(abajo)"
    str_jug2 = "El jugador de la derecha(2) con las flechas arriba y abajo del teclado"
    str_play = "Pulse cualquier tecla para comenzar"


    stdscr.nodelay(True)

    max_y, max_x = stdscr.getmaxyx()

    x = max_x // 2
    y = max_y // 2

    puntos_1 = 0
    puntos_2 = 0

    k = 0
    next_x = 0
    direction_x = 1
    direction_y = 1

    direction_x = random.choice([-direction_x, direction_x])
    direction_y = random.choice([-direction_y, direction_y])

    curses.initscr()
    curses.noecho()

    stdscr.border()

    barra_len = max_y // 3

    curses.curs_set(False)

    comienzo_y = int(max_y/2)-3
    comienzo_x = int(max_x/2)

    barra1_y = 2
    barra1_x = 2

    barra2_y = 2
    barra2_x = max_x - 2
    gol = False

    stdscr.addstr(comienzo_y,   comienzo_x - len(welcome) // 2, welcome, curses.color_pair(1))
    stdscr.addstr(comienzo_y+1, comienzo_x - len(str_jug1) // 2, str_jug1, curses.color_pair(1))
    stdscr.addstr(comienzo_y+2, comienzo_x - len(str_jug2) // 2, str_jug2, curses.color_pair(1))
    stdscr.addstr(comienzo_y+3, comienzo_x - len(str_play) // 2, str_play, curses.color_pair(1))
    stdscr.refresh()
    while True:
        q = stdscr.getch()
        if q > -1:
            break
    mensaje = "Jugador 1 = {} |||| Jugador 2= {}".format(puntos_1, puntos_2)
    
    while puntos_1 < 5 and puntos_2 < 5:
        
        if x == 0:
            puntos_2 += 1
            x = max_x // 2
            y = max_y // 2
            direction_x = random.choice([-direction_x, direction_x])
            direction_y = random.choice([-direction_y, direction_y])
            gol = True
            mensaje = "Jugador 1 = {} |||| Jugador 2= {}".format(puntos_1, puntos_2)
            continue
        elif x == max_x-1:
            puntos_1 +=1
            x = max_x // 2
            y = max_y // 2
            direction_x = random.choice([-direction_x, direction_x])
            direction_y = random.choice([-direction_y, direction_y])
            gol = True
            mensaje = "Jugador 1 = {} |||| Jugador 2= {}".format(puntos_1, puntos_2)
            continue


        if y in (max_y - len("o"), 0): 
            direction_y = -direction_y # reverse
        # left and right
        if x in (max_x - len("o"), 0): #or ( (x == barra2_x) and (y in (barra2_y+barra_len, barra2_y)) or ((x-1 == barra2_x) and ( y in (barra1_y+barra_len,barra1_y)))): 
            direction_x = -direction_x # reverse
        
        if x == barra1_x and direction_x == -1:
            if y in range(barra1_y, barra1_y+barra_len):
                direction_x = -direction_x

            
        elif x == barra2_x and direction_x == 1:
            if y in range(barra2_y, barra2_y+barra_len):
                direction_x = -direction_x


        key = stdscr.getch()
        if key == ord('q') or key == ord('Q'):
            break
        elif key == curses.KEY_DOWN and barra2_y < max_y - barra_len:
            barra2_y += 1
        elif key == curses.KEY_UP and barra2_y > 0:
            barra2_y -= 1
        elif (key == ord('s') or key == ord('S')) and barra1_y < max_y - barra_len:
            barra1_y += 1
        elif (key == ord('w') or key == ord('W')) and barra1_y > 0:
            barra1_y -= 1
        elif (key == ord('p') or key == ord('P')):
            while True:
                q = stdscr.getch()
                if (q == ord('p') or q == ord('P')):
                    q = None
                    break
                pausa = "PAUSA, PULSE P PARA CONTINUAR"
                stdscr.addstr(max_y // 2, max_x // 2 - len(pausa) // 2, pausa, curses.color_pair(1))
        
        x += direction_x
        y += direction_y  

        


        time.sleep(0.1)

        
        stdscr.clear()     
        stdscr.border() 
        stdscr.addch(y,x,"o")
        for i in range(1,max_y-1):
            stdscr.addch(i, max_x // 2, '|')
        for i in range(barra_len):
            stdscr.addch(barra2_y + i, barra2_x, '|', curses.color_pair(1))
            stdscr.addch(barra1_y + i, barra1_x, '|', curses.color_pair(2))
        stdscr.addstr(1, max_x // 2 - len(mensaje) // 2, mensaje, curses.color_pair(3))
        if gol:
            while True:
                gol = False
                pausa = "PUNTO, PULSE P PARA HACER EL SAQUE"
                stdscr.addstr(max_y // 2, max_x // 2 - len(pausa) // 2, pausa, curses.color_pair(1))
                q = stdscr.getch()
                if (q == ord('p') or q == ord('P')):
                    q = None
                    break

        stdscr.refresh()

        
    if puntos_2 > puntos_1:
        mensaje_f = "JUGADOR 2 HAS GANADO {} - {}".format(puntos_1, puntos_2)
    elif puntos_1 > puntos_2:
        mensaje_f = "JUGADOR 1 HAS GANADO {} - {}".format(puntos_1, puntos_2)
    else:
        mensaje_f = "EMPATE {} - {}".format(puntos_1, puntos_2)
    while True:
        stdscr.addstr(max_y // 2, max_x // 2 - len(mensaje_f) // 2, mensaje_f, curses.color_pair(1))
        q = stdscr.getch()
        if q > -1:
            break
            
    curses.endwin()

def main():
    curses.wrapper(pong)

if __name__ == "__main__":
    main()