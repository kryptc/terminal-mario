from scene import *
from objects import *
from board import *
import sys, signal, copy, termios, tty, time


def delete_all(mario):
    for enemy in enemies:
        enemies.remove(enemy)
    for coin in coins:
        coins.remove(coin)
    del mario
    matrix.clear()

def main():
    keep_playing = 1
    lives = 3
    coin_num = 0
    restart = 0

    while (keep_playing != 0):

        # global restart
        if restart == 1:
            if mario.lives == 0:
                print ("Game over!")
                keep_playing = 0
                exit()
            lives = mario.returnLives()
            restart = 0
            delete_all(mario)
            reset_controls()

            # clear()
            time.sleep(0.5)


        if restart == 0:
            clear()
            generate_map()
            create_enemies()

            mario = create_mario(mario_start_row, mario_start_col, lives)
            keypress = KBHit()
            var = 1;
            col_range_beg = 0
            col_range_end = col_blocks_per

            while True:
                timer = tick()
                score = scoreAlgo(mario.returnKills(), timer, coin_num)
                lives = mario.returnLives()

                #shifts screen according to position of mario
                if mario.returnCol() > ((col_range_end + col_range_beg) / 2) and col_range_end < map_col_blocks:
                    col_range_beg += 1
                    col_range_end += 1

                #updates score, lives and time
                fillMetadata(col_range_beg, col_range_end)

                #helps enemies move and enables gravity for them
                var += 1
                for enemy in enemies:
                    if enemy.returnCol() in range(col_range_beg, col_range_end):
                        #oh damn, them orcs can jump whaaaa ?!
                        if enemy.returnCode() == 13 and enemy.returnJumpStatus() is False: 
                            rand = randint(0,12)
                            if rand == 1:
                                enemy.jump()

                        if enemy.returnCode() == 13 and enemy.returnJumpStatus() is True:
                            enemy.jump()
                        else:
                            enemy.gravityEffect()

                        #move enemy according to its type
                        if enemy.returnCode() == 12:
                            if var % 8 == 0:
                                restart = (enemy.move(mario.returnCol()) | restart )
                        elif enemy.returnCode() == 13:
                            if var % 6 == 0:
                                restart = (enemy.move(mario.returnCol()) | restart )


                #enables gravity for mario and jumps
                if mario.returnJumpStatus() is True:
                    mario.jump()
                else:
                    mario.gravityEffect()

                #coin functions
                for coin in coins:
                    coin_num += coin.coinLife()

                #prints everything updated and filled till now on screen
                print_matrix(col_range_beg, col_range_end, score, lives, timer)

                if keypress.kbhit():

                    ch = keypress.getch()

                    if (ch == 'q'):
                        keep_playing = 0
                        exit()
                    elif (ch == 'w'):
                        if mario.returnJumpStatus() is True: 
                            pass
                        else:
                            mario.jump()
                    elif (ch == 'a'):
                        mario.moveLeft()
                    elif (ch == 'd'):
                        mario.moveRight()


                else:
                    #no key detected go down
                    restart = (mario.death() | restart)
                    time.sleep(0.09)


                #mario has been hit. he loses a life and respawns at the start
                if restart == 1:
                    mario.oneLessLife()
                    break

            # ch = config.getchar()
            # if (ch == 'q'):
            #     keep_playing = 0

            print(Style.RESET_ALL)


if __name__ == "__main__":
    main()

