import curses

def main(stdscr):
    w = 80
    h = 24
    states = [[0 for x in range(w)] for y in range(h)]

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

            if states[y][x] == 0:
                stdscr.attron(curses.color_pair(2))
                stdscr.addch(y, x, " ")
                stdscr.attroff(curses.color_pair(2))

                states[y][x] = 1

            elif states[y][x] == 1:
                stdscr.attron(curses.color_pair(1))
                stdscr.addch(y, x, " ")
                stdscr.attroff(curses.color_pair(1))

                states[y][x] = 0

        elif key == 27:
            break

# curses.wrapper(main)

def step (in_state):
    out_state = [[0 for x in range(len(in_state))] for y in range(len(in_state[0]))]

    for y in range(len(in_state)):
        
        for x in range(len(in_state[y])):
            current_node = 0

            # print(f'x {x} y {y}')

            if y == 0:
                current_node += in_state[y + 1][x]
                if x == 0:
                    current_node += in_state[y + 1][x + 1]
                    current_node += in_state[y][x + 1]
                elif x == len(in_state) - 1:
                    current_node += in_state[y - 1][x - 1]
                    current_node += in_state[y][x - 1]
                else:
                    current_node += in_state[y + 1][x + 1]
                    current_node += in_state[y][x + 1]
                    current_node += in_state[y - 1][x - 1]
                    current_node += in_state[y][x - 1]
            elif y == len(in_state[y]) - 1:
                current_node += in_state[y - 1][x]
                if x == 0:
                    current_node += in_state[y - 1][x + 1]
                    current_node += in_state[y][x + 1]
                elif x == len(in_state) - 1:
                    current_node += in_state[y - 1][x - 1]
                    current_node += in_state[y][x - 1]
                else:
                    current_node += in_state[y - 1][x + 1]
                    current_node += in_state[y][x + 1]
                    current_node += in_state[y - 1][x - 1]
                    current_node += in_state[y][x - 1]
            elif x == 0:
                current_node += in_state[y - 1][x]
                current_node += in_state[y - 1][x + 1]
                current_node += in_state[y][x + 1]
                current_node += in_state[y + 1][x + 1]
                current_node += in_state[y + 1][x]
            elif x == len(in_state) - 1:
                current_node += in_state[y - 1][x]
                current_node += in_state[y - 1][x - 1]
                current_node += in_state[y][x - 1]
                current_node += in_state[y + 1][x - 1]
                current_node += in_state[y + 1][x]
            else:
                current_node += in_state[y][x + 1]
                current_node += in_state[y][x - 1]
                current_node += in_state[y + 1][x + 1]
                current_node += in_state[y + 1][x]
                current_node += in_state[y - 1][x + 1]
                current_node += in_state[y - 1][x]
                current_node += in_state[y + 1][x - 1]
                current_node += in_state[y - 1][x - 1]

            print(f'current state {in_state[y][x]} current_node {current_node}')

            if in_state[y][x] == 1 and (current_node == 2 or current_node == 3):
                out_state[y][x] = 1
            elif in_state[y][x] == 0 and current_node == 3:
                out_state[y][x] = 1

            # print(f'current_node {current_node}')

    print(in_state)

    return out_state

input = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

print(input)

print(step(input))