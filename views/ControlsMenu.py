import pygame_menu
import pygame


class ControlsMenu:
    """
    A class to represent the UI, that allows to choose the controls for different actions
    """

    def __init__(self, screen_width, screen_height, screen, controls):
        self.controls = controls
        self.screen = screen
        self.menu = pygame_menu.Menu(
            "Change controls",
            screen_width,
            screen_height,
            theme=pygame_menu.themes.THEME_BLUE,
        )

    def exit(self):
        """
        Saves changes and returns back
        :return:
        """
        self.controls.writeValues()
        self.menu.disable()

    def refresh(self):
        """
        Refreshes the UI
        :return:
        """
        self.menu.clear()
        self.init()

    def openMenu(self):
        """
        A function to launch the menu UI
        :return:
        """
        self.menu.enable()
        self.menu.clear()
        self.view()

    def change_control(self, bomberman, key, value):
        """
        Sets the given control to the given bomberman
        :param bomberman:
        :param key:
        :param value:
        :return:
        """
        self.controls.set_control(bomberman, key, value)

    def listen_for_key(self, bomberman, key):
        """
        Listens for key events
        :param bomberman:
        :param key:
        :return:
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.change_control(bomberman, key, event.key)
                    self.refresh()
                    return

    def init(self):
        """
        Puts menu items on the screen
        :return:
        """
        self.menu.add.label("Genrale")
        self.menu.add.button(
            "Pause: " + pygame.key.name(self.controls.get_control(0, "pause")),
            self.listen_for_key,
            0,
            "pause",
        )
        self.menu.add.label("Bomberman 1")
        self.menu.add.button(
            "Up: " + pygame.key.name(self.controls.get_control(1, "up")),
            self.listen_for_key,
            1,
            "up",
        )
        self.menu.add.button(
            "Down: " + pygame.key.name(self.controls.get_control(1, "down")),
            self.listen_for_key,
            1,
            "down",
        )
        self.menu.add.button(
            "Left: " + pygame.key.name(self.controls.get_control(1, "left")),
            self.listen_for_key,
            1,
            "left",
        )
        self.menu.add.button(
            "Right: " + pygame.key.name(self.controls.get_control(1, "right")),
            self.listen_for_key,
            1,
            "right",
        )
        self.menu.add.button(
            "Bomb: " + pygame.key.name(self.controls.get_control(1, "bomb")),
            self.listen_for_key,
            1,
            "bomb",
        )
        self.menu.add.button(
            "Obstacle: " + pygame.key.name(self.controls.get_control(1, "obstacle")),
            self.listen_for_key,
            1,
            "obstacle",
        )
        self.menu.add.button(
            "Detonator: " + pygame.key.name(self.controls.get_control(1, "detonator")),
            self.listen_for_key,
            1,
            "Detonator",
        )
        self.menu.add.label("Bomberman 2")
        self.menu.add.button(
            "Up: " + pygame.key.name(self.controls.get_control(2, "up")),
            self.listen_for_key,
            2,
            "up",
        )
        self.menu.add.button(
            "Down: " + pygame.key.name(self.controls.get_control(2, "down")),
            self.listen_for_key,
            2,
            "down",
        )
        self.menu.add.button(
            "Left: " + pygame.key.name(self.controls.get_control(2, "left")),
            self.listen_for_key,
            2,
            "left",
        )
        self.menu.add.button(
            "Right: " + pygame.key.name(self.controls.get_control(2, "right")),
            self.listen_for_key,
            2,
            "right",
        )
        self.menu.add.button(
            "Bomb: " + pygame.key.name(self.controls.get_control(2, "bomb")),
            self.listen_for_key,
            2,
            "bomb",
        )
        self.menu.add.button(
            "Obstacle: " + pygame.key.name(self.controls.get_control(2, "obstacle")),
            self.listen_for_key,
            2,
            "obstacle",
        )
        self.menu.add.button(
            "Detonator: " + pygame.key.name(self.controls.get_control(2, "detonator")),
            self.listen_for_key,
            2,
            "detonator",
        )
        self.menu.add.button("Back", self.exit)

    def view(self):
        """
        Views the menu
        :return:
        """
        self.init()
        self.menu.mainloop(self.screen)
