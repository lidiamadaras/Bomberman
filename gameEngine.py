import pygame
from pygame.locals import *

import level
from maps import MAP1, MAP2, MAP3, MAP4
import views.mainMenu as mainMenu
import views.pauseMenu as pauseMenu
from controls import Controls
from player import Player
from enum import Enum


class Mode(Enum):
    """
    Modes of the UI
    """

    Menu = 0
    Game = 1
    Pause = 2


pygame.init()

# define game variables
tile_size = 48


screen_height = level.tile_size * len(MAP4) + tile_size * 2
screen_width = level.tile_size * len(MAP4[0])

pygame.mixer.init()

pygame.mixer.music.load("ost.mp3")

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bomberman")


# Keys

clock = pygame.time.Clock()


class GameEngine:
    """
    A class to represent the launched game's logic with several rounds
    """

    def __init__(self):
        self.map = MAP4
        self.currentRound = 0
        self.roundsNumber = 1
        self.isRunning = True
        self.Mode = Mode.Menu
        self.control = Controls()
        self.player1 = Player(1, "Player 1")
        self.player2 = Player(2, "Player 2")
        self.level = level.Level(
            self.map, screen, self.control, self.player1, self.player2
        )

    def handleKeys(self, menu):
        """
        Handles the keys related to the menu
        :param menu:
        :return:
        """
        key = pygame.key.get_pressed()
        if key[self.control.get_control(0, "pause")]:
            menu.open_menu()
            self.Mode = Mode.Pause

    def play(self):
        """
        Lanches the game
        :return:
        """
        print("Playing")
        self.Mode = Mode.Game
        print(self.Mode)

    def quit(self):
        """
        Stops the game
        :return:
        """
        self.isRunning = False

    def restart(self):
        """
        Restarts the game
        :return:
        """
        self.level = level.Level(
            self.map, screen, self.control, self.player1, self.player2
        )

    def changeLevel(self, map):
        """
        Chooses the other map
        :param map:
        :return:
        """
        if map == 1:
            self.map = MAP4
        elif map == 2:
            self.map = MAP4
        elif map == 3:
            self.map = MAP4
        elif map == 4:
            self.map = MAP4
        self.level = level.Level(
            self.map, screen, self.control, self.player1, self.player2
        )

    def changeRoundsNumber(self, roundsNumber):
        """
        Chooses the number of rounds to play
        :param roundsNumber:
        :return:
        """
        self.roundsNumber = roundsNumber * 2 + 1
        self.level = level.Level(
            self.map, screen, self.control, self.player1, self.player2
        )

    def changePlayerName(self, id, name):
        """
        Changes the player's name
        :param id:
        :param name:
        :return:
        """
        if id == 1:
            self.player1.name = name
        if id == 2:
            self.player2.name = name

    def newRound(self):
        """
        Launches the new round
        :return:
        """
        self.currentRound += 1
        self.level = level.Level(
            self.map, screen, self.control, self.player1, self.player2
        )

    def main_menu(self):
        """
        Goes to main menu
        :return:
        """
        self.Mode = Mode.Menu
        self.restart()


game = GameEngine()
mainMenu_ = mainMenu.MainMenu(screen_width, screen_height, game, screen, game.control)
pauseMenu_ = pauseMenu.PauseMenu(screen_width, screen_height, game, screen, mainMenu_)
mainMenu_.view()
pauseMenu_.view()

pygame.mixer.music.play(-1, 0.0)

fps = 100
run = True

# Custom events
BOMB_EXPLOSION = pygame.USEREVENT + 1

#  Game loop
while run:
    if game.Mode == Mode.Menu:
        mainMenu_.loop()
    elif game.Mode == Mode.Pause:
        pauseMenu_.loop()
    elif game.Mode == Mode.Game:
        clock.tick(fps)
        screen.fill("#6FA428")
        game.level.draw()
        game.handleKeys(pauseMenu_)
        game.level.handleKeys()
        game.level.refresh()
        icon_side = tile_size // 2 + tile_size // 6
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        myfont = pygame.font.SysFont("monospace", 25)
        color = (6, 16, 89)

        name1 = myfont.render(
            f"{game.player1.name} won {game.player1.wins} times", 1, color
        )
        game.level.screen.blit(name1, (0, game.level.row_count * tile_size))

        name2 = myfont.render(
            f"{game.player2.name} won {game.player2.wins} times", 1, color
        )
        game.level.screen.blit(
            name2,
            (
                game.level.col_count * tile_size - name2.get_width(),
                game.level.row_count * tile_size,
            ),
        )

        rounds = myfont.render(
            f"Round {game.currentRound}/{game.roundsNumber}", 1, color
        )
        game.level.screen.blit(
            rounds,
            (
                (game.level.col_count // 2) * tile_size - 5 * (icon_side // 2),
                game.level.row_count * tile_size,
            ),
        )

    if not game.isRunning:
        run = False
    if game.currentRound == game.roundsNumber:
        game.Mode = Mode.Menu
        mainMenu_.open_menu()
    if game.level.isNextRound:
        game.newRound()

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == game.control.get_control(1, "bomb"):
                if (
                    game.level.bombermans[0].isAlive
                    and not game.level.bombermans[0].noBombs
                ):
                    game.level.bombermans[0].placeBomb()
            if event.key == game.control.get_control(2, "bomb"):
                if (
                    game.level.bombermans[1].isAlive
                    and not game.level.bombermans[1].noBombs
                ):
                    game.level.bombermans[1].placeBomb()
            # Obstacle
            if event.key == game.control.get_control(1, "obstacle"):
                if (
                    game.level.bombermans[0].isAlive
                    and game.level.bombermans[0].obstaclesNum > 0
                ):
                    game.level.bombermans[0].placeObstacle()
            if event.key == game.control.get_control(2, "obstacle"):
                if (
                    game.level.bombermans[1].isAlive
                    and game.level.bombermans[1].obstaclesNum > 0
                ):
                    game.level.bombermans[1].placeObstacle()
            # Detonator
            if event.key == game.control.get_control(1, "detonator"):
                if game.level.bombermans[0].isAlive:
                    for bomb in game.level.bombermans[0].bombs:
                        bomb.isDetonated = True
            if event.key == game.control.get_control(2, "detonator"):
                if game.level.bombermans[1].isAlive:
                    for bomb in game.level.bombermans[1].bombs:
                        bomb.isDetonated = True

    pygame.display.update()
pygame.quit()
