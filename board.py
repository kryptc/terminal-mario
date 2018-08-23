import config
from scene import *
from objects import *


mario_start_col = 2
mario_start_row = minGroundHeight

canyon_list = [25,26,47,52,53,54,71,72,73,86,87,120]

cementblocks_row_list = [0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4,
                        4, 3, 2, 1, 0, 3, 2, 1, 0, 2, 1, 0, 1, 0, 0, 
                        0, 1, 0, 1, 2, 4, 3, 2, 1, 0, 3, 2, 1, 0, 2, 
                        1, 0, 1, 0, 0]
cementblocks_col_list =  [90,91,91,92,92,92,93,93,93,93,94,94,94,94,94,
                        116,116,116,116,116,117,117,117,117,118,118,118,
                        119,119,136,137,137,138,138,138,151,151,151,151,
                        151,152,152,152,152,153,153,153,154,154,155]

bricks_row_list = [1,1,3,3,3,1,1,1,1,1,1,1,1,1,3,3,
                  2,2,2,1,2,3,4,4,4,4,4,4,4,1,2,1,2,
                  1,1,1,1,2,2,2,2,2,2,2,1,1,1,3,3,
                  2,2,4,2]
bricks_col_list = [7,8,9,10,11,12,13,14,23,24,25,26,27,28,25,26,
                  44,45,46,50,51,52,54,55,56,57,58,59,60,69,70,71,72,
                  77,78,85,84,96,97,98,99,101,102,104,121,122,123,123,124,
                  142,145,145,148]

mystery_row_list = [1,3,1,3,2,4,2,1,1,2,2,3,2]
mystery_col_list = [8,10,24,25,51,56,70,75,76,98,102,123,142]

pipe_list = [32,36,40,64,131,158]
pipe_heights = [0,1,2,1,1,2]

shroom_spawn_list = [15,37,43,52,59,69,70,100,97,133,142,146,148]
shroom_row = [0,0,0,4,5,0,0,0,3,0,0,5,0]

orc_spawn_list = [160]

castle_col_coord = [179,180,181,182,183]
castle_row_coord = [0,1,2]

def draw_scenery():
    try:
        #draw mountains
        pass
    except IndexError:
        pass

def fillMetadata(range_beg, range_end):
    matrix[0][range_end - 4] = 0
    matrix[0][range_end - 2] = 53
    matrix[0][range_end - 3] = 52
    matrix[0][range_beg + 1] = 51
    matrix[0][range_beg] = 50

    matrix[0][range_beg + 2] = 60
    matrix[0][range_end - 1] = 61
    


def generate_map():
    create_ground(row_blocks_per, map_col_blocks)
    draw_scenery()
    create_clouds(row_blocks_per, map_col_blocks)
    create_canyons(canyon_list) 
    create_cement(cementblocks_row_list, cementblocks_col_list)
    create_bricks(bricks_row_list, bricks_col_list)
    create_mysteryBricks(mystery_row_list, mystery_col_list)
    create_pipes(pipe_list, pipe_heights)
    build_castle(castle_row_coord, castle_col_coord)


def print_matrix(col_range_beg, col_range_end, score, lives, timer):
    strings = list()

    for ls in matrix:
        templist1 = list()
        templist2 = list()
        templist3 = list()
        for num in ls:
            if num==0:
                templist1.append("    ")
                templist2.append("    ")
                templist3.append("    ")

            elif num==1:
                templist1.append(Fore.GREEN + "XXXX")
                templist2.append(Fore.BLUE + "====")
                templist3.append(Fore.WHITE + "mmmm")
            elif num==2:
                templist1.append(Fore.CYAN + "  3 ")
                templist2.append(Fore.CYAN + " 333")
                templist3.append(Fore.CYAN + "3333")
            elif num==3:
                templist1.append(Fore.RED + "/##\\")
                templist2.append(Fore.RED + "|##|")
                templist3.append(Fore.RED + "\##/")
            elif num==4:
                templist1.append(Fore.WHITE + "^^^^")
                templist2.append(Fore.WHITE + "|  |")
                templist3.append(Fore.WHITE + "|__|")
            elif num==5:
                templist1.append(Fore.GREEN + "====")
                templist2.append(Fore.WHITE + "|  |")
                templist3.append(Fore.WHITE + "|  |")
            elif num==6:
                templist1.append(Fore.WHITE + "|  |")
                templist2.append(Fore.WHITE + "|  |")
                templist3.append(Fore.WHITE + "|  |")
            elif num==7:
                templist1.append(Fore.WHITE + "/??\\")
                templist2.append(Fore.WHITE + "|ss|")
                templist3.append(Fore.WHITE + "\??/")
            elif num == 8:
                templist1.append(Fore.YELLOW + " ,o,")
                templist2.append(Fore.YELLOW + " oOo")
                templist3.append(Fore.YELLOW + " 'o'")
            elif num==11:
                templist1.append(Fore.YELLOW + " \o/")
                templist2.append(Fore.RED + "  O ")
                templist3.append(Fore.YELLOW + " / \\")
            elif num==12:
                templist1.append("    ")
                templist2.append(Fore.RED + "oooo")
                templist3.append(Fore.MAGENTA + "||||")
            elif num==13:
                templist1.append(Fore.YELLOW + " oo ")
                templist2.append(Fore.BLUE + "[][]")
                templist3.append(Fore.BLUE + " || ")
            elif num==22:
                templist1.append("    ")
                templist2.append(Fore.RED + "oooo")
                templist3.append("    ")
            elif num==23:
                templist1.append(Fore.BLUE + "[  ]")
                templist2.append(Fore.YELLOW + " oo ")    
                templist3.append(Fore.BLUE + "[__]")
            elif num==50:
                templist1.append("    ")
                templist2.append(Fore.WHITE + "SCOR")
                templist3.append(Fore.WHITE + "LIVE")
            elif num==51:
                templist1.append("    ")
                templist2.append(Fore.WHITE + "E : ")
                templist3.append(Fore.WHITE + "S : ")
            elif num==52:
                templist1.append("    ")
                templist2.append("    ")
                templist3.append(Fore.WHITE + "TIME")
            elif num==53:
                templist1.append("    ")
                templist2.append("    ")
                templist3.append(Fore.WHITE + "R : ")
            elif num==60:
                templist1.append("    ")
                if score > 999:
                    templist2.append(Fore.WHITE + str(score))
                elif score > 99:
                    templist2.append(Fore.WHITE + "0" + str(score))
                elif score > 9:
                    templist2.append(Fore.WHITE + "00" + str(score))
                else:
                    templist2.append(Fore.WHITE + "000" + str(score))

                templist3.append(Fore.WHITE + "000" + str(lives))
            elif num==61:
                templist1.append("    ")
                templist2.append("    ")
                templist3.append(Fore.WHITE + "0" + str(timer))

            elif num==80:
                templist1.append(Fore.WHITE + " || ")
                templist2.append(Fore.WHITE + " || ")    
                templist3.append(Fore.BLUE + "/==\\")
            elif num==81:
                templist1.append(Fore.YELLOW + "====")
                templist2.append(Fore.GREEN + "++++")    
                templist3.append(Fore.YELLOW + "====")
            elif num==82:
                templist1.append(Fore.WHITE + " || ")
                templist2.append(Fore.WHITE + " || ")    
                templist3.append(Fore.WHITE + " || ")
            elif num==90:
                templist1.append(Fore.MAGENTA + "\\\\\\\\")
                templist2.append(Fore.WHITE + "////")
                templist3.append(Fore.MAGENTA + "\\\\\\\\")
            elif num==91:
                templist1.append(Fore.WHITE + "#  #")
                templist2.append(Fore.MAGENTA + "\\\\\\\\")
                templist3.append(Fore.WHITE + "////")
            elif num==92:
                templist1.append("    ")
                templist2.append(Fore.WHITE + "  //")    
                templist3.append(Fore.MAGENTA + " \\\\")


        strings.append(templist1)
        strings.append(templist2)
        strings.append(templist3)

    for string in strings:
        # print("".join(string))
        for i in range(col_range_beg, col_range_end):
            sys.stdout.write(string[i])
        sys.stdout.write("\n")



