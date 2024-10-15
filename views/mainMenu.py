import pygame_menu

from .ControlsMenu import ControlsMenu


class MainMenu:
    """
    A class to represent the main menu's UI
    """

    def __init__(self, screen_width, screen_height, game, screen, controls):
        self.game = game
        self.controlMenu = ControlsMenu(screen_width, screen_height, screen, controls)
        self.screen = screen
        self.menu = pygame_menu.Menu(
            "Welcome", screen_width, screen_height, theme=pygame_menu.themes.THEME_BLUE
        )
        controls.readValues()

    def set_map(self, value, *args):
        """
        Changes the game's map to the selected one
        :param value:
        :param args:
        :return:
        """
        print("Map selected:", value[0])
        self.game.changeLevel(value[1])
        pass

    def set_rounds_number(self, value, *args):
        """
        Sets the number of rounds to the selected amount
        :param value:
        :param args:
        :return:
        """
        self.game.changeRoundsNumber(value[1])
        pass

    def start_the_game(self):
        """
        Starts the game
        :return:
        """
        self.game.play()
        self.menu.disable()
        print("Playing")

    def set_first_name(self, value, *args):
        """
        Sets the name of the first player
        :param value:
        :param args:
        :return:
        """
        self.game.changePlayerName(1, value)

    def set_second_name(self, value, *args):
        """
        Sets the name of the second player
        :param value:
        :param args:
        :return:
        """
        self.game.changePlayerName(2, value)

    def open_menu(self):
        """
        Opens the menu
        :return:
        """
        self.menu.enable()
        print("Menu Opened")

    def loop(self):
        """
        Menu loop
        :return:
        """
        self.menu.mainloop(self.screen)

    def quit(self):
        """
        Quits the main menu
        :return:
        """
        self.game.quit()
        self.game.play()

    def view(self):
        """
        Puts and views the menu items on the screen
        :return:
        """
        self.menu.add.text_input(
            "Player 1: ", default="Player 1", onchange=self.set_first_name
        )
        self.menu.add.text_input(
            "Player 2: ", default="Player 2", onchange=self.set_second_name
        )
        self.menu.add.selector(
            "Map: ",
            [("One", 1), ("Two", 2), ("Three", 3), ("Four", 4)],
            onchange=self.set_map,
        )
        self.menu.add.selector(
            "Number of rounds: ",
            [("1", 1), ("3", 3), ("5", 5)],
            onchange=self.set_rounds_number,
        )
        self.menu.add.button("Controls", self.controlMenu.openMenu)
        self.menu.add.button("Play", self.start_the_game)
        self.menu.add.button("Quit", quit)
