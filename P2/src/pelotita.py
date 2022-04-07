import curses
from curses import wrapper
import time

def pelotita(stdscr):
    DELAY = 30000

    x = 10
    y = 10

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