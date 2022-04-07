import curses
from curses import wrapper
import time

def pelotita(stdscr):
    DELAY = 30000

    x = 10
    y = 10

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    welcome = "Bienvenido a Pong"
    str_jug1 = "El jugador de la izquierda juega con W(arriba) y S(abajo)"
    str_jug2 = "El jugador de la derecha con las flechas arriba y abajo del teclado"
    str_play = "Pulse cualquier tecla para comenzar"


    stdscr.nodelay(True)

    max_y, max_x = stdscr.getmaxyx()
    k = 0
    next_x = 0
    direction_x = 1
    direction_y = 1

    curses.initscr()
    curses.noecho()

    stdscr.border()

    curses.curs_set(False)

    comienzo_y = int(max_y/2)-2
    comienzo_x = int(max_x/2)


    stdscr.addstr(comienzo_y, comienzo_x, welcome, curses.color_pair(1))
    stdscr.addstr(comienzo_y+1, comienzo_x-20, str_jug1, curses.color_pair(1))
    stdscr.addstr(comienzo_y+2, comienzo_x-20, str_jug2, curses.color_pair(1))
    stdscr.addstr(comienzo_y+3, comienzo_x-10, str_play, curses.color_pair(1))
    stdscr.refresh()
    while True:
        q = stdscr.getch()
        if q > -1:
            break

    while k != ord('q'):

        x += direction_x
        y += direction_y  

        stdscr.clear()      

        time.sleep(0.1)

        if y in (max_y - len("o"), 0): 
            direction_y = -direction_y # reverse
        # left and right
        if x in (max_x - len("o"), 0): 
            direction_x = -direction_x # reverse

        stdscr.addstr(y,x,"o")
        stdscr.refresh()

        k = stdscr.getch()

    curses.endwin()

def main():
    curses.wrapper(pelotita)

if __name__ == "__main__":
    main()