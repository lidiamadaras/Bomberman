import pygame
import json

values = {
    "pause": pygame.K_ESCAPE,
    "bomberman1": {
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "bomb": pygame.K_RETURN,
        "obstacle": pygame.K_RSHIFT,
        "detonator": pygame.K_BACKSPACE,
    },
    "bomberman2": {
        "up": pygame.K_w,
        "down": pygame.K_s,
        "left": pygame.K_a,
        "right": pygame.K_d,
        "bomb": pygame.K_SPACE,
        "obstacle": pygame.K_LSHIFT,
        "detonator": pygame.K_TAB,
    },
}


class ControlMapper:
    """
    A class to deal with controls.json file
    """

    def __init__(self):
        self.intial = values

    def write_json(self, data):
        """
        Pushes the current values dictionary to the controls.json
        :param data:
        :return:
        """
        with open("controls.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    def intialize(self):
        self.write_json(self.intial)

    def read_json(self):
        """
        Reads the values from the controls.json file
        :return:
        """
        with open("controls.json", "r") as json_file:
            return json.load(json_file)
