import pygame

from controlMapper import ControlMapper


class Controls:
    """
    A clas to represent the logic of switching the game control keys
    """

    def __init__(self):
        self.controlMapper = ControlMapper()
        self.bomberman1 = {}
        self.bomberman2 = {}
        self.pause = 0

    def readValues(self):
        """
        Pulls the current values from the json file using controlMapper instance
        :return:
        """
        values = self.controlMapper.read_json()
        self.bomberman1 = values["bomberman1"]
        self.bomberman2 = values["bomberman2"]
        self.pause = values["pause"]

    def writeValues(self):
        """
        Pushes the current values to the json file using controlMapper instance
        :return:
        """
        values = {
            "bomberman1": self.bomberman1,
            "bomberman2": self.bomberman2,
            "pause": self.pause,
        }
        self.controlMapper.write_json(values)

    def set_control(self, bomberman, key, value):
        """
        Sets a control to the given bomberman's dictionary
        :param bomberman:
        :param key:
        :param value:
        :return:
        """
        if key == "pause":
            self.pause = value
        elif bomberman == 1:
            self.bomberman1[key] = value
        elif bomberman == 2:
            self.bomberman2[key] = value

    def get_control(self, bomberman, key):
        """
        Gets a control from the given bomberman's control dictionary
        :param bomberman:
        :param key:
        :return:
        """
        if key == "pause":
            return self.pause
        if bomberman == 1:
            return self.bomberman1[key]
        elif bomberman == 2:
            return self.bomberman2[key]
