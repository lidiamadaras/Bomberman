import pygame_menu


class PauseMenu:
    """
    A class to represent the pause menu UI
    """

    def __init__(self, screen_width, screen_height, game, screen, main_menu):
        self.game = game
        self.main_menu = main_menu
        self.screen = screen
        self.menu = pygame_menu.Menu(
            "Pause", screen_width, screen_height, theme=pygame_menu.themes.THEME_BLUE
        )

    def open_main_menu(self):
        """
        Goes to the main menu
        :return:
        """
        self.menu.disable()
        self.main_menu.open_menu()
        self.game.main_menu()

    def back_to_game(self):
        """
        Returns back to the game
        :return:
        """
        self.game.play()
        self.menu.disable()

    def open_menu(self):
        """
        Launches the pause menu
        :return:
        """
        self.menu.enable()
        print("Menu Opened")

    def loop(self):
        """
        Pause menu loop
        :return:
        """
        self.menu.mainloop(self.screen)

    def quit(self):
        """
        Closes the pause menu
        :return:
        """
        self.game.quit()
        self.game.play()

    def view(self):
        """
        Puts and views the pause menu items
        :return:
        """
        self.menu.add.button("Back to game", self.back_to_game)
        self.menu.add.button("Main Menu", self.open_main_menu)
        self.menu.add.button("Quit", quit)
