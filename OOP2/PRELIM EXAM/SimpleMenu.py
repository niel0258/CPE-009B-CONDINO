from Reader import clear_screen
import sys

try:
    from pynput.keyboard import Key, Listener
except ImportError:
    print("Dependency missing!,\nplease install the pynput module")
    raise Exception("Import Error")

class SimpleMenu:
    def __init__(self,menu_choices,menu_title = "Base Menu"):
        self._current_choice = 0
        self._menu_choices = menu_choices
        self._menu_title = menu_title

    def _print_menu(self):
        clear_screen()

        print("-------------------------------------------------------")
        print(self._menu_title.center(55,' '))
        print("-------------------------------------------------------")

        for i in range(len(self._menu_choices)):
            if i == self._current_choice:
                print("> ",self._menu_choices[i])
            else:
                print("  ",self._menu_choices[i])
        
        print("\nUse UP/DOWN arrows to navigate. Press ENTER to select.\n\n");

    def navigate_menu(self):
        # Render initial menu
        self._print_menu()

        def select_on_menu(key):
            # Up arrow: move selection up (wraps around using modulo)
            if key == Key.up:
                self._current_choice = (self._current_choice- 1) % len(self._menu_choices)
            # Down arrow: move selection down (wraps around using modulo)
            elif key == Key.down:
                self._current_choice = (self._current_choice + 1) % len(self._menu_choices)
            # Enter key: confirm choice and stop listening for keypresses
            elif key == Key.enter:
                return False
            
            self._print_menu()

        # Start keyboard listener thread; blocks execution until Listener stops (returns False on Enter)
        with Listener(on_press=select_on_menu) as listener:
            listener.join()

        # Discard any leftover newline
        try:
            import termios
            termios.tcflush(sys.stdin, termios.TCIFLUSH)
        except ImportError:
            # Windows fallback
            import msvcrt
            while msvcrt.kbhit():
                msvcrt.getch()

        current_choice = self._current_choice
        self._current_choice = 0
        
        clear_screen()

        return current_choice