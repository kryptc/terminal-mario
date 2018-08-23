import config
from scene import minGroundHeight, matrix
import time
from board import *


def fillMatrix(objectType):
    row = objectType.returnRow()
    col = objectType.returnCol()
    matrix[row][col] = objectType.returnCode()


def shadowMatrix(row, col):
    matrix[row][col] = 0;


class Object():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.dead = 0

    def returnRow(self):
        return self.row

    def returnCol(self):
        return self.col

    def returnCode(self):
        return self.code

    def checkCollision(self, row, col):
        #lands on top of an enemy
        if matrix[row][col] == 12 or matrix[row][col] == 13:
            return 2
        #lands on top of Mario
        elif matrix[row][col] == 11:
            return 3
        #lands on top of a mystery brick
        elif matrix[row][col] == 7:
            return 4
        #lands on an object
        elif matrix[row][col] != 0:
            return 1
        #free space
        else:
            return 0

    def gravityEffect(self):
        #normal cases
        try:
            # if self.checkCollision(self.row + 1, self.col) is False:
                self.moveDown()

        #death by canyon
        except IndexError:
            if self.code == 11:
                self.dead = 1
            else:
                shadowMatrix(self.row, self.col)

    def moveDown(self):
        #kill enemies if mario drops on a shroom or an orc
        if self.checkCollision(self.row + 1, self.col) == 2 and self.code == 11:
            if killEnemies(self.row + 1, self.col) is True:
                self.kills += 1

        elif self.checkCollision(self.row + 1, self.col) == 0:
            # time.sleep(0.8)
            shadowMatrix(self.returnRow(), self.returnCol())
            self.row += 1
            fillMatrix(self)
        #death by canyon
        elif self.row > map_row_blocks - 1:
            self.dead = 1


    def death(self):
        return self.dead 



class Mario(Object):
    def __init__(self, row, col, lives):
        super().__init__(row, col)
        self.code = 11
        self.lives = lives
        self.inJump = False
        self.jumpTime = 0
        self.kills = 0

    def returnJumpStatus(self):
        return self.inJump

    def returnKills(self):
        return self.kills

    def returnLives(self):
        return self.lives

    def moveRight(self):
        # if self.col == int(config.columns):
        if self.col == map_col_blocks:
            pass
        elif self.checkCollision(self.row, self.col + 1) == 2:
            self.dead = 1
        elif self.checkCollision(self.row, self.col + 1) != 0:
            pass
        else:
            shadowMatrix(self.returnRow(), self.returnCol())
            self.col += 1
            fillMatrix(self)
        
    
    def moveLeft(self):
        if self.col == 0:
            pass
        elif self.checkCollision(self.row, self.col - 1) == 2:
            self.dead = 1
        elif self.checkCollision(self.row, self.col - 1) != 0:
            pass
        else:
            shadowMatrix(self.returnRow(), self.returnCol())
            self.col -= 1
            fillMatrix(self)
        

    def jump(self):
        #also checks if Mario lands on any enemies
        if self.checkCollision(self.row - 1, self.col) == 4:
            breakBricks(self.row - 1, self.col)
            self.inJump = False
            self.jumpTime = 0

        elif self.checkCollision(self.row - 1, self.col) != 0:
            self.inJump = False
            self.jumpTime = 0

        elif self.jumpTime == 3:
            self.inJump = False
            self.jumpTime = 0
        else:
            shadowMatrix(self.returnRow(), self.returnCol())
            self.inJump = True
            self.jumpTime += 1
            self.row -= 1
            fillMatrix(self)

    def oneLessLife(self):
        self.lives -= 1


class Enemies(Object):
    def __init__(self, row, col):
        super().__init__(row, col)

    #both directions
    
    def move(self, mario_xcoord):
        var = 0
        if mario_xcoord > self.row:
            #go right
            var = 1
        elif mario_xcoord < self.row:
            #go left
            var = -1

        if self.checkCollision(self.row, self.col + var) == 0:
            shadowMatrix(self.returnRow(), self.returnCol())
            self.col += var
            fillMatrix(self)

        elif self.checkCollision(self.row, self.col + var) == 3:
            print ("u die1")
            return 1
        return 0



class mushroomMinion(Enemies):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.code = 12


class highOrc(Enemies):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.code = 13
        self.inJump = False
        self.jumpTime = 0

    def jump(self):
        if self.checkCollision(self.row - 1, self.col) != 0:
            self.inJump = False
            self.jumpTime = 0

        elif self.jumpTime == 3:
            self.inJump = False
            self.jumpTime = 0
        else:
            shadowMatrix(self.returnRow(), self.returnCol())
            self.inJump = True
            self.jumpTime += 1
            self.row -= 1
            fillMatrix(self)


    def returnJumpStatus(self):
        return self.inJump

# class shadowMinion(Enemies):
#     def __init__(self, row, col):
#         super().__init__(row, col)
#         self.code = 22

# class shadowOrc(Enemies):
#     def __init__(self, row, col):
#         super().__init__(row, col)
#         self.code = 23


enemies = list()

class Coin(Object):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.code = 8
        self.appearsFor = 11

    def coinLife(self):
        self.appearsFor -= 1
        if self.appearsFor == 0:
            shadowMatrix(self.row, self.col)
            coins.remove(self)
            return 1
        return 0

coins = list()


def create_mario(x, y, lives):
    mario = Mario(x, y, lives)
    fillMatrix(mario)
    return mario


def create_enemies():
    for i, pos in enumerate(shroom_spawn_list):
        ht = shroom_row[i]
        enemy_object = mushroomMinion(minGroundHeight - ht, pos)
        enemies.append(enemy_object)

    for pos in orc_spawn_list:
        enemy_object = highOrc(minGroundHeight, pos)
        enemies.append(enemy_object)

    for i in range(len(enemies)):
        enemy_object = enemies[i]

        if (enemy_object.returnCode() == 12):
            fillMatrix(enemy_object)

        elif (enemy_object.returnCode() == 13):
            fillMatrix(enemy_object)     


def killEnemies(mrow, mcol):
    if matrix[mrow][mcol] == 12:
        print ("found minion")

        #kill shroom
        for enemy in enemies:
            if enemy.returnRow() == mrow and enemy.returnCol() == mcol:
                shadowMatrix(mrow, mcol)
                enemies.remove(enemy)
                return True

    elif matrix[mrow][mcol] == 13:
        print ("found orc")
        # shadowMatrix(mrow, mcol)
        enemy_object = mushroomMinion(mrow, mcol)
        fillMatrix(enemy_object)
        return True

    return False


def breakBricks(row, col):
    coin_object = Coin(row - 1, col)
    fillMatrix(coin_object)
    coins.append(coin_object)

    rand = randint(0,4)
    #brick disappears
    if rand == 0:
        matrix[row][col] = 0
    #brick becomes normal
    elif rand == 1 or rand == 3:
        matrix[row][col] = 3
    #more mysteries to be unlocked
    elif rand == 2:
        matrix[row][col] = 7
