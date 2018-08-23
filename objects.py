from random import *
from config import * 

#map creation

map_height = rows
map_length = 190 * 4

map_col_blocks = 190
map_row_blocks = int(int(map_height)/3) 

row_blocks_per = int(int(rows)/3)
col_blocks_per = int(int(columns)/4)

minGroundHeight = int(3*(row_blocks_per/4));
minCloudHeight = int(row_blocks_per/4)


matrix = list()


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
                return self.moveDown()

        #death by canyon
        except IndexError:
            if self.code == 11:
                self.dead = 1
            else:
                shadowMatrix(self.row, self.col)
        return 0

    def jump(self):
        pass

    def death(self):
        return self.dead 


class Cloud(Object):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.code = 2

class Ground(Object):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.code = 1

class Flag(Object):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.code = 81
        self.hoist = False

    def raise_flag(self):
        if self.checkCollision(self.row, self.col - 1) == 3 or self.hoist is True:
            shadowMatrix(self.row, self.col)
            matrix[self.row][self.col] = 82
            self.row -= 1
            fillMatrix(self)
            self.hoist = True


class FlagPole(Object):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.code = 82
 


clouds = list()
ground = list()


def create_ground(row_blocks, col_blocks):
    for i in range(row_blocks):
        templist = list()
        for j in range(col_blocks):
            # if(i > 11):
            if(i > minGroundHeight):
                templist.append(1)
                classobject = Ground(i,j)
                ground.append(classobject)
            else:
                templist.append(0)
        matrix.append(templist)
        


def create_clouds(row_blocks, col_blocks):
    for i in range(row_blocks):
        for j in range(col_blocks):
            if(i in range(1, minCloudHeight)):
                matrix[i][j] = 0
                random_number = random.random()
                if(random_number > 0.9):
                    matrix[i][j] = 2
                    classobject = Cloud(i,j)
                    clouds.append(classobject)

def create_canyons(canyon_list):
    for i in canyon_list:
        matrix[minGroundHeight+1][i] = 0
        try:
            matrix[minGroundHeight+2][i] = 0
            matrix[minGroundHeight+3][i] = 0
        except IndexError:
            pass

def create_cement(row_list, col_list):
    for i, row in enumerate(row_list):
        col = col_list[i]
        matrix[minGroundHeight - row][col] = 4

def create_bricks(row_list, col_list):
    for i, row in enumerate(row_list):
        col = col_list[i]
        matrix[minGroundHeight - row][col] = 3


def create_mysteryBricks(row_list, col_list):
    for i, row in enumerate(row_list):
        col = col_list[i]
        matrix[minGroundHeight - row][col] = 7


def create_pipes(positions, heights):
    for i, pos in enumerate(positions):
        ht = heights[i]
        for j in range(ht):
            matrix[minGroundHeight - j][pos] = 6
        matrix[minGroundHeight - ht][pos] = 5

def create_flag():
    matrix[minGroundHeight][174] = 80
    bandiera = Flag(minGroundHeight - 1, 174)
    fillMatrix(bandiera)
    for i in range(3):
        poleObject = FlagPole(minGroundHeight -2 - i, 174)
        fillMatrix(poleObject)
    return bandiera


def build_castle(castle_row_coord, castle_col_coord):
    for i in castle_row_coord:
        for j in castle_col_coord:
            if i == 0:
                matrix[minGroundHeight - i][j] = 90
            elif i == 1:
                matrix[minGroundHeight - i][j] = 91

    matrix[minGroundHeight - 2][181] = 91
    matrix[minGroundHeight - 2][180] = 92
    matrix[minGroundHeight - 2][182] = 92
    #build doorway
    matrix[minGroundHeight][181] = 0



