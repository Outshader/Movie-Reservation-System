import curses
from curses.textpad import Textbox


arrows = [259, 258]  # curses.KEY_UP, curses.KEY_DOWN
funcs = [49, 50]  # 1,2
actions = [113]  # q
enter = [10, 13]


def term_main(stdscr):
    stdscr.clear()
    main_paint(stdscr)

    try:
        while True:
            key = stdscr.getch()
            if key in arrows:
                cursor_move(stdscr, key)
            elif key in funcs:
                match key:
                    case 49:
                        login_main(stdscr)
                    case 50:
                        return
            elif key in actions:
                match key:
                    case 113:
                        return
    except KeyboardInterrupt:
        return


def login_main(stdscr):
    user_input = login_paint(stdscr).split()
    stdscr.addstr(0, 0, f"Input: {user_input!r}")


def login_paint(stdscr):
    stdscr.clear()
    win = curses.newwin(2, 40, 2, 2)

    textbox = Textbox(win)

    def login_validator(key):  # key is autopassed
        y, _ = win.getyx()
        if key in enter and y == 1:
            return 7
        return key

    win.addstr(0, 0, "Login: ")
    win.addstr(1, 0, "Password: ")

    textbox.edit(login_validator)

    return textbox.gather()


def cursor_move(stdscr, key):
    y, x = stdscr.getyx()
    if key == "KEY_DOWN":
        if y < 1:
            y = y + 1
            stdscr.move(y, x)
    else:
        if y > 0:
            y = y - 1
            stdscr.move(y, x)
    stdscr.refresh()


def main_paint(stdscr):
    stdscr.addstr(0, 0, "1) Login")
    stdscr.addstr(1, 0, "2) Exit")


def main():
    curses.wrapper(term_main)
