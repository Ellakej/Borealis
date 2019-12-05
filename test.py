import curses
#import serial

#Inicio del puerto serial
#arduino.serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = 3.0)


def main(stdscr):

    while 1:
        key = stdscr.getch()

		# clear existing texts
        stdscr.clear()
        if key == curses.KEY_UP:
            #arduino.write('w')
            stdscr.addstr(0,0, "Letra W")
        elif key == curses.KEY_LEFT:
            #arduino.write('a')
            stdscr.addstr(0,0, "Letra A")
        elif key == curses.KEY_DOWN:
            #arduino.write('s')
            stdscr.addstr(0,0, "Letra S")
        elif key == curses.KEY_RIGHT:
            #arduino.write('d')
		    stdscr.addstr(0,0, "Letra D")
        else:
            break

		# update screen
        stdscr.refresh()


curses.wrapper(main)
