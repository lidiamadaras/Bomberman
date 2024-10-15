import pygame
from bomberman import Bomberman
from gameSprite import Transparency
from wall import Wall
from box import Box
from tile import Tile
from explosion import Explosion
from monster import Monster
from bomb import Bomb
import random

tile_size = 48
wall_img = pygame.image.load("img/wall.png")
box_img = pygame.image.load("img/box.png")
exp = pygame.image.load("img/explosion.png")
wall = pygame.image.load("img/wall.png")
wallImage = pygame.transform.scale(wall, (tile_size, tile_size))
player1_img = pygame.image.load("img/player1.png")
player2_img = pygame.image.load("img/player2.png")
exp = pygame.image.load("img/explosion.png")
explosionImage = pygame.transform.scale(exp, (0.75 * tile_size, 0.75 * tile_size))
transparentWall = pygame.image.load("img/transparentWall.png")
transparentWallImage = pygame.transform.scale(transparentWall, (tile_size, tile_size))
transparency = pygame.image.load("img/transparency.png")
transparencyImage = pygame.transform.scale(transparency, (tile_size, tile_size))

# -----
bombImage = pygame.image.load("img/bombPowerUp.png")
bombPowerUpImage = pygame.transform.scale(bombImage, (tile_size, tile_size))
skull = pygame.image.load("img/skull.png")
skullImage = pygame.transform.scale(skull, (tile_size, tile_size))
plant = pygame.image.load("img/plant.png")
plantImage = pygame.transform.scale(plant, (tile_size, tile_size))
ghost = pygame.image.load("img/ghost.png")
ghostImage = pygame.transform.scale(ghost, (tile_size, tile_size))
obstacle = pygame.image.load("img/obstacle.png")
obstacleImage = pygame.transform.scale(obstacle, (tile_size, tile_size))
rollerSkate = pygame.image.load("img/rollerSkate.png")
rollerSkateImage = pygame.transform.scale(rollerSkate, (tile_size, tile_size))
shield = pygame.image.load("img/shield.png")
shieldImage = pygame.transform.scale(shield, (tile_size, tile_size))
detonator = pygame.image.load("img/detonator.png")
detonatorImage = pygame.transform.scale(detonator, (tile_size, tile_size))


class Level:
    """
    A class representing the current round of the game
    """

    def __init__(self, data, screen, controls, player1, player2):
        self.screen = screen
        self.tiles = []
        self.bombermans = []
        self.monsters = []
        self.walls = []
        self.boxes = []
        self.bonuses = []
        self.bombs = []
        self.explosions = []
        self.isOver = False
        self.roundOverTime = pygame.time.get_ticks()
        self.isNextRound = False

        self.obstacles = []
        self.startTime = pygame.time.get_ticks()
        self.battleRoyaleCounter = 1
        self.battleRoyaleCounter2 = 0
        self.isWallAdded = False

        self.player1 = player1
        self.player2 = player2

        # load images
        wall_img = pygame.image.load("img/wall.png")
        box_img = pygame.image.load("img/box.png")
        player1_img = pygame.image.load("img/player1.png")
        player2_img = pygame.image.load("img/player2.png")
        monster_img = pygame.image.load("img/monster.png")

        self.controls = controls

        self.row_count = 0
        for row in data:
            col_count = 0
            tileRow = []
            for num in row:
                tile = Tile(self.row_count, col_count)
                if num == 1:
                    image = pygame.image.load("img/wall.png")
                    image = pygame.transform.scale(image, (tile_size, tile_size))
                    wall1 = Wall(
                        self,
                        self.row_count,
                        col_count,
                        col_count * tile_size,
                        self.row_count * tile_size,
                        image,
                    )
                    self.walls.append(wall1)
                    tile.sprites.append(wall1)
                elif num == 3:
                    bomberman1 = Bomberman(
                        0,
                        self,
                        self.row_count,
                        col_count,
                        col_count * tile_size,
                        self.row_count * tile_size,
                        image=pygame.image.load("img/player1.png"),
                    )
                    self.bombermans.append(bomberman1)
                    tile.sprites.append(bomberman1)
                elif num == 4:
                    bomberman2 = Bomberman(
                        1,
                        self,
                        self.row_count,
                        col_count,
                        col_count * tile_size,
                        self.row_count * tile_size,
                        image=pygame.image.load("img/player2.png"),
                    )
                    self.bombermans.append(bomberman2)
                    tile.sprites.append(bomberman2)
                elif num == 5:
                    image = pygame.image.load("img/box.png")
                    image = pygame.transform.scale(image, (tile_size, tile_size))
                    rand = random.randint(0, 2)
                    if rand == 0:
                        box = Box(
                            self,
                            self.row_count,
                            col_count,
                            col_count * tile_size,
                            self.row_count * tile_size,
                            False,
                            image,
                        )
                    else:
                        box = Box(
                            self,
                            self.row_count,
                            col_count,
                            col_count * tile_size,
                            self.row_count * tile_size,
                            True,
                            image,
                        )
                    self.boxes.append(box)
                    tile.sprites.append(box)
                elif num == 6:
                    image = pygame.transform.scale(monster_img, (tile_size, tile_size))
                    monster = Monster(
                        self,
                        self.row_count,
                        col_count,
                        col_count * tile_size,
                        self.row_count * tile_size,
                        image,
                    )
                    self.monsters.append(monster)
                    tile.sprites.append(monster)
                tileRow.append(tile)
                col_count += 1
            self.row_count += 1
            self.col_count = col_count
            self.tiles.append(tileRow)

    def draw(self):
        """
        draws each sprite of each tile on the screen
        :return:
        """
        for tileRow in self.tiles:
            for tile in tileRow:
                for sprite in tile.sprites:
                    self.screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))

    def redraw(self):
        """
        redraws each sprite of each tile on the screen
        :return:
        """
        for bomb in self.bombs:
            self.screen.blit(bomb.image, (bomb.rect.x, bomb.rect.y))
        for exp in self.explosions:
            self.screen.blit(exp.image, (exp.rect.x, exp.rect.y))
        for bomberman in self.bombermans:
            if bomberman.isAlive:
                self.screen.blit(bomberman.image, (bomberman.rect.x, bomberman.rect.y))

    def refresh(self):
        """
        updates every sprite of the entire map, altering level's lists of objects
        :return:
        """
        now = pygame.time.get_ticks()
        self.isLevelOver(now)
        self.footer(now)
        keys = pygame.key.get_pressed()
        for i in range(2):
            bm = self.bombermans[i]
            self.checkMoves(bm)
            bonusesToDelete = []
            for key in bm.bonuses.keys():
                if now - bm.bonuses[key][2] > bm.bonuses[key][1]:
                    bm.bonuses[key][0].cancelBonus(bm)
                    bonusesToDelete.append(key)

            for key in bonusesToDelete:
                bm.bonuses.pop(key)
            if bm.immediateBombs:
                bm.placeBomb()

            if bm.isAlive:

                if (
                    bm.overflowLeft
                    and not keys[self.controls.get_control(i + 1, "left")]
                    and not keys[self.controls.get_control(i + 1, "right")]
                ):
                    bm.moveLeft()
                elif (
                    bm.overflowRight
                    and not keys[self.controls.get_control(i + 1, "right")]
                    and not keys[self.controls.get_control(i + 1, "left")]
                ):
                    bm.moveRight()
                elif (
                    bm.overflowUp
                    and not keys[self.controls.get_control(i + 1, "up")]
                    and not keys[self.controls.get_control(i + 1, "down")]
                ):
                    bm.moveUp()
                elif (
                    bm.overflowDown
                    and not keys[self.controls.get_control(i + 1, "down")]
                    and not keys[self.controls.get_control(i + 1, "up")]
                ):
                    bm.moveDown()
                if self.tiles[bm.i][bm.j].containsBonus():
                    bonus = self.tiles[bm.i][bm.j].getBonus()
                    bonus.applyBonus(bm)
                    self.remBonus(bonus)

        self.bombsRefresh(now)
        self.explosionsRefresh(now)
        self.monstersRefresh(now)
        self.battleRoyale(now)

    def bombsRefresh(self, now):
        """
        refreshes the state of each bomb
        :param now: current time
        :return:
        """
        for bomb in self.bombs:
            if not self.bombermans[bomb.id].detonator:
                if bomb.imageCounter1 > 0:
                    bomb.imageCounter1 -= 1
                else:
                    if bomb.image == bomb.image1:
                        bomb.image = bomb.image2
                    elif bomb.image == bomb.image2:
                        bomb.image = bomb.image1
                    bomb.imageCounter2 -= 1
                    bomb.imageCounter1 = bomb.imageCounter2 * 4
                if now - bomb.initTime > 5000:
                    bomb.isExploding = True
                if now - bomb.initTime > 5720:
                    bomb.isExploding = False
                    self.remBomb(bomb)
            elif self.bombermans[bomb.id].detonator:
                bomb.imageCounter1 += 1
                if bomb.imageCounter1 % 120 < 60:
                    bomb.image = bomb.image1
                if bomb.imageCounter1 % 120 > 60:
                    bomb.image = bomb.image2
                if bomb.isDetonated:
                    bomb.isExploding = True
            if bomb.isExploding:
                bomb.explode()
                for i in range(bomb.blastRange):
                    if now - bomb.deathTime > i * 720 / bomb.blastRange:
                        if bomb.expNum == i:
                            self.explosion(bomb, i)
                    else:
                        continue
                if not bomb.isExploding:
                    self.remBomb(bomb)

    def explosionsRefresh(self, now):
        """
        refreshes the state of each explosion, and checks which sprites are affected by any of them
        :param now: current time
        :return:
        """
        for exp in self.explosions:
            if now - exp.initTime > 540:
                self.remExplosion(exp)
            for bomberman in self.bombermans:
                if pygame.sprite.collide_rect(bomberman, exp):
                    bomberman.absorbExplosion()
            for bomb in self.bombs:
                if pygame.sprite.collide_rect(bomb, exp):
                    bomb.absorbExplosion()
            for monster in self.monsters:
                if pygame.sprite.collide_rect(monster, exp):
                    monster.die(exp.id)
            for sprite in self.tiles[exp.i][exp.j].sprites:
                if pygame.sprite.collide_rect(sprite, exp):
                    sprite.absorbExplosion()

    def monstersRefresh(self, now):
        """
        refreshes the state of each monster and checks if any of them "catches" any of the bombermen
        :param now: current time
        :return:
        """
        for monster in self.monsters:
            monster.move()
            for bomberman in self.bombermans:
                if (
                    abs(bomberman.rect.centerx - monster.rect.centerx)
                    < 0.75 * tile_size
                    and abs(bomberman.rect.centery - monster.rect.centery)
                    < 0.75 * tile_size
                ):
                    bomberman.die()
            if not monster.isAlive and now - monster.deathTime > 500:
                self.remMonster(monster)

    def battleRoyale(self, now):
        """
        implements the battle royale warning effects and performs the wall placement itself
        :param now: current time
        :return:
        """
        # ----------------------------------------------------------------------------------
        # battle royale feature
        if self.battleRoyaleCounter < min(self.row_count, self.col_count) // 2:
            # flickering animation
            if now - self.startTime > 13000 + 20000 * self.battleRoyaleCounter:
                ind = self.battleRoyaleCounter
                for i in range(len(self.tiles)):
                    for j in range(len(self.tiles[0])):
                        if (
                            i == ind
                            or i == len(self.tiles) - 1 - ind
                            or j == ind
                            or j == len(self.tiles[0]) - 1 - ind
                        ):
                            tile = self.tiles[i][j]
                            if (
                                self.battleRoyaleCounter2 == 0
                                and not tile.containsTransparency()
                            ):
                                tile.sprites.append(
                                    Transparency(
                                        tile.j * tile_size,
                                        tile.i * tile_size,
                                        tile.i,
                                        tile.j,
                                        transparencyImage,
                                    )
                                )
                            elif self.battleRoyaleCounter2 % 50 == 24:
                                tile.getTransparency().image = transparentWallImage
                            elif self.battleRoyaleCounter2 % 50 == 49:
                                tile.getTransparency().image = transparencyImage
                self.battleRoyaleCounter2 += 1
            # placing walls
            if now - self.startTime > 20000 * (self.battleRoyaleCounter + 1):
                self.battleRoyaleCounter2 = 0
                ind = self.battleRoyaleCounter
                for i in range(len(self.tiles)):
                    for j in range(len(self.tiles[0])):
                        if (
                            i == ind
                            or i == len(self.tiles) - 1 - ind
                            or j == ind
                            or j == len(self.tiles[0]) - 1 - ind
                        ):
                            tile = self.tiles[i][j]
                            for sprite in tile.sprites:
                                if isinstance(sprite, Bomberman):
                                    sprite.die()
                                if isinstance(sprite, Monster):
                                    sprite.die()
                                    self.monsters.remove(sprite)
                                if isinstance(sprite, Explosion):
                                    self.explosions.remove(sprite)
                                if isinstance(sprite, Bomb):
                                    self.bombs.remove(sprite)
                                    self.explodeBomb(sprite)
                            tile.sprites.clear()
                            wall = Wall(
                                self,
                                tile.i,
                                tile.j,
                                tile.j * tile_size,
                                tile.i * tile_size,
                                wallImage,
                            )
                            tile.sprites.append(wall)
                            self.walls.append(wall)

                self.battleRoyaleCounter += 1

    def checkMoves(self, bomberman):
        """
        determines which directions are available for the bomberman
        :param bomberman: bomberman to check
        :return:
        """
        if self.tiles[bomberman.i + 1][bomberman.j].isFreeForBomberman(bomberman):
            bomberman.down = True
        else:
            bomberman.down = False
        if self.tiles[bomberman.i - 1][bomberman.j].isFreeForBomberman(bomberman):
            bomberman.up = True
        else:
            bomberman.up = False
        if self.tiles[bomberman.i][bomberman.j + 1].isFreeForBomberman(bomberman):
            bomberman.right = True
        else:
            bomberman.right = False
        if self.tiles[bomberman.i][bomberman.j - 1].isFreeForBomberman(bomberman):
            bomberman.left = True
        else:
            bomberman.left = False
        if bomberman.ghost:
            bomberman.left = bomberman.right = bomberman.up = bomberman.down = True

    def handleKeys(self):
        """
        calls the appropriate movement functions for both bombermen
        :return:
        """
        key = pygame.key.get_pressed()
        list1 = []
        list2 = []
        list3 = [list1, list2]
        for i in range(2):
            bm = self.bombermans[i]
            self.checkMoves(bm)
            if key[self.controls.get_control(i + 1, "down")]:
                list3[i].append(0)
            if key[self.controls.get_control(i + 1, "up")]:
                list3[i].append(1)
            if key[self.controls.get_control(i + 1, "right")]:
                list3[i].append(2)
            if key[self.controls.get_control(i + 1, "left")]:
                list3[i].append(3)

            if len(list3[i]) == 1 and bm.isAlive:
                if (
                    key[self.controls.get_control(i + 1, "down")]
                    and bm.down
                    and not key[self.controls.get_control(i + 1, "up")]
                ):  # down key
                    if 23 < bm.rect.x % tile_size < tile_size:
                        bm.moveRight()
                    if 0 < bm.rect.x % tile_size < 24:
                        bm.moveLeft()
                    bm.moveDown()
                # --------------------------------
                elif (
                    key[self.controls.get_control(i + 1, "up")]
                    and bm.up
                    and not key[self.controls.get_control(i + 1, "down")]
                ):  # up key
                    if 23 < bm.rect.x % tile_size < tile_size:
                        bm.moveRight()
                    if 0 < bm.rect.x % tile_size < 24:
                        bm.moveLeft()
                    bm.moveUp()
                # --------------------------------
                elif (
                    key[self.controls.get_control(i + 1, "right")]
                    and bm.right
                    and not key[self.controls.get_control(i + 1, "left")]
                ):  # right key
                    if 23 < bm.rect.y % tile_size < tile_size:
                        bm.moveDown()
                    if 0 < bm.rect.y % tile_size < 24:
                        bm.moveUp()
                    bm.moveRight()
                # --------------------------------
                elif (
                    key[self.controls.get_control(i + 1, "left")]
                    and bm.left
                    and not key[self.controls.get_control(i + 1, "right")]
                ):  # left key
                    if 23 < bm.rect.y % tile_size < tile_size:
                        bm.moveDown()
                    if 0 < bm.rect.y % tile_size < 24:
                        bm.moveUp()
                    bm.moveLeft()

    def addBomb(self, bomb):
        """
        places the bomb on the map
        :param bomb:
        :return:
        """
        self.bombs.append(bomb)
        self.tiles[bomb.i][bomb.j].sprites.insert(0, bomb)

    # for obstaclePowerup:
    def addObstacle(self, obstacle):
        """
        places the obstacle on the map
        :param obstacle:
        :return:
        """
        self.boxes.append(obstacle)
        self.tiles[obstacle.i][obstacle.j].sprites.insert(0, obstacle)

    def remBomb(self, bomb):
        """
        removes the bomb from the map
        :param bomb:
        :return:
        """
        self.bombs.remove(bomb)
        self.tiles[bomb.i][bomb.j].sprites.remove(bomb)

    def explodeBomb(self, bomb):
        """
        marks the bomb which is about to explode and increases the bomb number of the bomberman
        :param bomb:
        :return:
        """
        if not bomb.isReturned:
            bomb.deathTime = pygame.time.get_ticks()
            if bomb.id == 0:
                self.bombermans[0].bombsNum += 1
            elif bomb.id == 1:
                self.bombermans[1].bombsNum += 1
            bomb.isReturned = True

    def explodeObstacle(self, obstacle):
        """
        marks the bomb which is about to explode and increases the bomb number of the bomberman
        :param obstacle:
        :return:
        """
        # self.bombs.remove(bomb)
        if not obstacle.isReturned:
            if obstacle.id == 0:
                self.bombermans[0].obstaclesNum += 1
            elif obstacle.id == 1:
                self.bombermans[1].bombsNum += 1
            obstacle.isReturned = True

    def explosion(self, bomb, r):
        """
        creates explosions from r tiles far from the exploding bomb
        :param bomb:
        :param r: radius
        :return:
        """
        upIdx = bomb.i - r
        downIdx = bomb.i + r
        leftIdx = bomb.j - r
        rightIdx = bomb.j + r
        if upIdx >= 0:
            if self.tiles[upIdx][bomb.j].containsWall():
                bomb.upExplosion = False
            elif bomb.upExplosion:
                up = Explosion(
                    bomb.id,
                    bomb.rect.x + 3,
                    bomb.rect.y + 3 - tile_size * r,
                    upIdx,
                    bomb.j,
                    explosionImage,
                )
                self.explosions.append(up)
                self.tiles[upIdx][bomb.j].sprites.append(up)
            if self.tiles[upIdx][bomb.j].containsBox():
                bomb.upExplosion = False
        if downIdx < self.row_count:
            if self.tiles[downIdx][bomb.j].containsWall():
                bomb.downExplosion = False
            elif bomb.downExplosion:
                down = Explosion(
                    bomb.id,
                    bomb.rect.x + 3,
                    bomb.rect.y + 3 + tile_size * r,
                    downIdx,
                    bomb.j,
                    explosionImage,
                )
                self.explosions.append(down)
                self.tiles[downIdx][bomb.j].sprites.append(down)
            if self.tiles[downIdx][bomb.j].containsBox():
                bomb.downExplosion = False
        if leftIdx >= 0:
            if self.tiles[bomb.i][leftIdx].containsWall():
                bomb.leftExplosion = False
            elif bomb.leftExplosion:
                left = Explosion(
                    bomb.id,
                    bomb.rect.x + 3 - tile_size * r,
                    bomb.rect.y + 3,
                    bomb.i,
                    leftIdx,
                    explosionImage,
                )
                self.explosions.append(left)
                self.tiles[bomb.i][leftIdx].sprites.append(left)
            if self.tiles[bomb.i][leftIdx].containsBox():
                bomb.leftExplosion = False
        if rightIdx < self.col_count:
            if self.tiles[bomb.i][rightIdx].containsWall():
                bomb.rightExplosion = False
            elif bomb.rightExplosion:
                right = Explosion(
                    bomb.id,
                    bomb.rect.x + 3 + tile_size * r,
                    bomb.rect.y + 3,
                    bomb.i,
                    rightIdx,
                    explosionImage,
                )
                self.explosions.append(right)
                self.tiles[bomb.i][rightIdx].sprites.append(right)
            if self.tiles[bomb.i][rightIdx].containsBox():
                bomb.rightExplosion = False

        bomb.expNum += 1
        if r == bomb.blastRange - 1:
            bomb.isExploding = False

    def remExplosion(self, exp):
        """
        removes the explosion from the map
        :param exp:
        :return:
        """
        self.explosions.remove(exp)
        self.tiles[exp.i][exp.j].sprites.remove(exp)

    def blowUpBox(self, box):
        """
        blows up the box and puts the bonus if there is
        :param box:
        :return:
        """
        bomberman1 = self.bombermans[0]
        bomberman2 = self.bombermans[1]
        if box in self.boxes:
            if box.hasBonus:
                self.bonuses.append(box.bonus)
                self.tiles[box.i][box.j].sprites.append(box.bonus)
            self.remBox(box)
        if box in bomberman1.obstacles:
            bomberman1.obstacles.remove(box)
            bomberman1.obstaclesNum += 1
        elif box in bomberman2.obstacles:
            bomberman2.obstacles.remove(box)
            bomberman2.obstaclesNum += 1

    def remBox(self, box):
        """
        removes the box from the map
        :param box:
        :return:
        """
        self.boxes.remove(box)
        self.tiles[box.i][box.j].sprites.remove(box)

    def remBonus(self, bonus):
        """
        removes the bonus from the map
        :param bonus:
        :return:
        """
        self.bonuses.remove(bonus)
        self.tiles[bonus.i][bonus.j].sprites.remove(bonus)

    def remMonster(self, monster):
        """
        removes the monster from the map
        :param monster:
        :return:
        """
        self.monsters.remove(monster)
        self.tiles[monster.i][monster.j].sprites.remove(monster)

    # def isOver(self):
    #     if (
    #             not self.bombermans[0].isAlive
    #             and not self.bombermans[1].isAlive
    #             and len(self.bombs) == 0
    #             and len(self.explosions) == 0
    #     ):
    #         return True
    #     # if not self.bombermans[0].isAlive and not self.bombermans[1].isAlive:
    #     #     return True
    #     return False

    def isLevelOver(self, now):
        """
        checks if the current round is over and puts the winner on the footer
        :param now: current time
        :return:
        """
        icon_side = tile_size // 2 + tile_size // 6
        myfont = pygame.font.SysFont("monospace", 25)
        color = (6, 16, 89)
        if len(self.bombs) == 0 and len(self.explosions) == 0 and not self.isOver:
            if not self.bombermans[0].isAlive and self.bombermans[1].isAlive:
                self.player2.wins += 1
                self.roundOverTime = pygame.time.get_ticks()
                self.isOver = True
            elif self.bombermans[0].isAlive and not self.bombermans[1].isAlive:
                self.player1.wins += 1
                self.roundOverTime = pygame.time.get_ticks()
                self.isOver = True
            elif not self.bombermans[0].isAlive and not self.bombermans[1].isAlive:
                self.roundOverTime = pygame.time.get_ticks()
                self.isOver = True
        if self.isOver and now > self.roundOverTime + 5000:
            self.isNextRound = True
        elif self.isOver and now < self.roundOverTime + 5000:
            if not self.bombermans[0].isAlive and self.bombermans[1].isAlive:
                winner = myfont.render(f"{self.player2.name} wins!", 1, color)
                self.screen.blit(
                    winner,
                    (
                        (self.col_count // 2) * tile_size - winner.get_width() // 2,
                        self.row_count * tile_size + icon_side,
                    ),
                )
            elif self.bombermans[0].isAlive and not self.bombermans[1].isAlive:
                winner = myfont.render(f"{self.player1.name} wins!", 1, color)
                self.screen.blit(
                    winner,
                    (
                        (self.col_count // 2) * tile_size - winner.get_width() // 2,
                        self.row_count * tile_size + icon_side,
                    ),
                )
            elif not self.bombermans[0].isAlive and not self.bombermans[1].isAlive:
                winner = myfont.render("It's a draw!", 1, color)
                self.screen.blit(
                    winner,
                    (
                        (self.col_count // 2) * tile_size - winner.get_width() // 2,
                        self.row_count * tile_size + icon_side,
                    ),
                )

    def collides(self):
        pass

    def footer(self, now):
        """
        displays the current round's data: the time remained, players' power ups
        :param now:
        :return:
        """
        icon_side = tile_size // 2 + tile_size // 6
        myfont = pygame.font.SysFont("monospace", 25)
        color = (6, 16, 89)

        timeRemained = (182000 - now + self.startTime) // 1000
        seconds = timeRemained % 60
        minutes = timeRemained // 60

        if seconds < 10:
            timer = myfont.render(f"0{minutes}:0{seconds}", 1, color)
        else:
            timer = myfont.render(f"0{minutes}:{seconds}", 1, color)
        self.screen.blit(
            timer,
            (
                (self.col_count // 2) * tile_size - tile_size,
                (self.row_count + 2) * tile_size - icon_side,
            ),
        )

        for i in range(len(self.bombermans)):
            if i == 0:
                sign = 1
                offset = 0
            else:
                sign = -1
                offset = (self.col_count) * tile_size - icon_side

            if self.bombermans[i].isAlive:
                bomb = pygame.transform.scale(bombImage, (icon_side, icon_side))
                self.screen.blit(bomb, (offset, self.row_count * tile_size + icon_side))
                bombNum = myfont.render(f"x{self.bombermans[i].bombsNum}", 1, color)
                self.screen.blit(
                    bombNum, (offset, (self.row_count + 2) * tile_size - icon_side)
                )

                plant = pygame.transform.scale(plantImage, (icon_side, icon_side))
                self.screen.blit(
                    plant,
                    (
                        offset + sign * icon_side * 2,
                        self.row_count * tile_size + icon_side,
                    ),
                )
                blastRange = myfont.render(
                    f"x{self.bombermans[i].blastRange - 1}", 1, color
                )
                self.screen.blit(
                    blastRange,
                    (
                        offset + sign * icon_side * 2,
                        (self.row_count + 2) * tile_size - icon_side,
                    ),
                )

                obstacle = pygame.transform.scale(obstacleImage, (icon_side, icon_side))
                self.screen.blit(
                    obstacle,
                    (
                        offset + sign * icon_side * 4,
                        self.row_count * tile_size + icon_side,
                    ),
                )
                obstacleNum = myfont.render(
                    f"x{self.bombermans[i].obstaclesNum}", 1, color
                )
                self.screen.blit(
                    obstacleNum,
                    (
                        offset + sign * icon_side * 4,
                        (self.row_count + 2) * tile_size - icon_side,
                    ),
                )

                if self.bombermans[i].detonator:
                    detonator = pygame.transform.scale(
                        detonatorImage, (icon_side, icon_side)
                    )
                    self.screen.blit(
                        detonator,
                        (
                            offset + sign * icon_side * 6,
                            self.row_count * tile_size + icon_side,
                        ),
                    )
                    detonatorStatus = myfont.render(f"On", 1, color)
                    self.screen.blit(
                        detonatorStatus,
                        (
                            offset + sign * icon_side * 6,
                            (self.row_count + 2) * tile_size - icon_side,
                        ),
                    )
                else:
                    detonator = pygame.transform.scale(
                        detonatorImage, (icon_side, icon_side)
                    )
                    self.screen.blit(
                        detonator,
                        (
                            offset + sign * icon_side * 6,
                            self.row_count * tile_size + icon_side,
                        ),
                    )
                    detonatorStatus = myfont.render(f"Off", 1, color)
                    self.screen.blit(
                        detonatorStatus,
                        (
                            offset + sign * icon_side * 6,
                            (self.row_count + 2) * tile_size - icon_side,
                        ),
                    )

                if len(self.bombermans[i].bonuses) > 0:
                    j = 8
                    for key in self.bombermans[i].bonuses.keys():
                        img = pygame.transform.scale(
                            self.bombermans[i].bonuses[key][0].image,
                            (icon_side, icon_side),
                        )
                        self.screen.blit(
                            img,
                            (
                                offset + sign * icon_side * j,
                                self.row_count * tile_size + icon_side,
                            ),
                        )
                        time = myfont.render(
                            f"{(self.bombermans[i].bonuses[key][2] - now + self.bombermans[i].bonuses[key][1]) // 1000 + 1}s",
                            1,
                            color,
                        )
                        self.screen.blit(
                            time,
                            (
                                offset + sign * icon_side * j,
                                (self.row_count + 2) * tile_size - icon_side,
                            ),
                        )

                        j += 2
