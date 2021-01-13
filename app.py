import curses

def main(stdscr):
    w = 80
    h = 24
    states = [[1 for x in range(w)] for y in range(h)]

    screen_state = 'welcome'

    curses.start_color()
    # curses.use_default_colors()
    curses.curs_set(0)
    curses.mousemask(1)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.addstr(1, 1, "welcome to conway's game of life")
    stdscr.addstr(3, 1, "click any location to toggle a cell's living state")
    stdscr.addstr(5, 1, "press enter to start the simulation")

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()

            # delete content 
            if (screen_state == 'welcome'):
                stdscr.clear()
                curses.endwin()
                screen_state = 'setup'

            # stdscr.addstr(0, 0, "({},{}))".format(y, x))

            if states[y][x] == 1:
                stdscr.attron(curses.color_pair(2))
                stdscr.addch(y, x, " ")
                stdscr.attroff(curses.color_pair(2))

                states[y][x] = 2

            elif states[y][x] == 2:
                stdscr.attron(curses.color_pair(1))
                stdscr.addch(y, x, " ")
                stdscr.attroff(curses.color_pair(1))

                states[y][x] = 1

        elif key == 27:
            break

curses.wrapper(main)