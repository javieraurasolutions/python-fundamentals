class Lamp:
    _LAMPS = [
        """
             .
        .    |    .
         \   '   /
        `  .-. '
      --- (   ) ---
           \ /
          _|=|_
         |_____|
      """,
        """
           .-.
          (   )
           \ /
          _|=|_
         |_____|
      """,
    ]

    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


def run():
    menu = """
            ¿Which action would you like to do?
            
            [p]Turn on
            [a]Turn off
            [s]Salir
        """
    lamp = Lamp(is_turned_on=False)

    while True:
        command = str(input(menu))
        command = command.lower()

        if command == "p":
            lamp.turn_on()
        elif command == "a":
            lamp.turn_off()
        else:
            break


if __name__ == "__main__":
    run()
