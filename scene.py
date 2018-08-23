import os
from random import *
from config import *

row_blocks_per = int(int(rows)/3)
col_blocks_per = int(int(columns)/4)

minGroundHeight = int(3*(row_blocks_per/4));
minCloudHeight = int(row_blocks_per/4)


matrix = list()

class Cloud():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.code = 2

class Ground():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.code = 1


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

