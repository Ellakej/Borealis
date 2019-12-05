import curses
import pyfiglet
import os
import time

class MenuDisplay:

    def __init__(self, menu, meta, ascii):
        # set menu parameter as class property
        self.menu = menu
        self.meta = meta
        self.ascii = ascii
        # run curses application
        curses.wrapper(self.mainloop)

    def mainloop(self, stdscr):
        # turn off cursor blinking
        curses.curs_set(0)

        # color scheme for selected row
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

        # set screen object as class property
        self.stdscr = stdscr

        # get screen height and width
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()

        # specify the current selected row
        current_row = 0



        # print the menu
        self.print_menu(current_row)

        #Imprime el titulo
        self.print_titulo()

        # imprime los metadatos
        self.print_meta()

        #Ciclo selector
        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # if user selected last row (Exit), confirm before exit the program
                if current_row == len(self.menu) - 1:
                    if self.confirm("Estas seguro de que deseas salir?"):
                        break
                if current_row == 0:
                    self.inicio()


            self.print_menu(current_row)
            self.print_titulo()
            self.print_meta()

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()
        for idx, row in enumerate(self.menu):
            x = self.screen_width // 2 - len(row) // 2
            y = self.screen_height // 2 - len(menu) // 2 + idx + 2
            if idx == selected_row_idx:
                self.color_print(y, x, row, 1)
            else:
                self.stdscr.addstr(y, x, row)
        self.stdscr.refresh()

    def color_print(self, y, x, text, pair_num):
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))

    def color_title(self, y, x, text, pair_num):
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))

    def print_confirm(self, selected="si"):
        # clear yes/no line
        curses.setsyx(self.screen_height // 2 + 1, 0)
        self.stdscr.clrtoeol()

        y = self.screen_height // 2 + 1
        options_width = 10

        # print yes
        option = "si"
        x = self.screen_width // 2 - options_width // 2 + len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        # print no
        option = "no"
        x = self.screen_width // 2 + options_width // 2 - len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        self.stdscr.refresh()

    #Pantalla de confirmacion de salida
    def confirm(self, confirmation_text):
        self.print_center(confirmation_text)

        current_option = "si"
        self.print_confirm(current_option)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_RIGHT and current_option == "si":
                current_option = "no"
            elif key == curses.KEY_LEFT and current_option == "no":
                current_option = "si"
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return True if current_option == "si" else False

            self.print_confirm(current_option)
    #Pantalla de inicio
    def inicio(self):
        password = "raspberry"
        self.print_center("Iniciando la raspberry pi...")
        while 1:
            self.stdscr.clear()
            self.stdscr.addstr(10, 10, str(os.system('python client.py')))

        self.stdscr.refresh()


    def print_center(self, text):
        self.stdscr.clear()
        x = self.screen_width // 2 - len(text) // 2
        y = self.screen_height // 2
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()

    def print_meta(self):
        for idx, row in enumerate(self.meta):
            x = 2
            y = self.screen_height - len(meta) // 2 - idx - 2
            self.stdscr.addstr(y, x, row)
        self.stdscr.refresh()

    def print_titulo(self):
        x = 0
        y = 4
        self.color_title(y, x, self.ascii, 2)
        self.stdscr.refresh()



if __name__ == "__main__":
    menu = ['Inicio', 'Informacion', 'Salir']
    meta = ['ESCOM - IPN MX', 'Ver 1.0 - Manual']
    ascii_banner = pyfiglet.figlet_format("          Rover-Finder")
    MenuDisplay(menu, meta, ascii_banner)
