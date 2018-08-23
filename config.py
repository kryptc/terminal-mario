import os
import random
from kbhit import *
import tty, termios, sys
import time
from colorama import Fore, Back, Style

rows, columns = os.popen('stty size', 'r').read().split()

colours = []

restart = 0

 
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:   
        _ = os.system('clear')


def getchar():
   #Returns a single character from standard input
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch



timer = 150
lives = 3
score = 0 

def reset_controls():
  global timer
  global score
  timer = 150
  score = 0

cur_time = time.time()

def tick():
    global timer
    global cur_time
    if (timer > 0): 
        if time.time() - cur_time >= 1:
            timer -= 1
            cur_time = time.time()
    return timer

def scoreAlgo(kills, time, coins):
  global score
  score = int((kills * 100) + ((150 - time) * 0.5) + (coins * 25))
  return score

# Codes
# 0 - air
# 1 - ground
# 2 - clouds
# 3 - bricks
# 4 - cement stairs
# 5 - pipes
# 6 - pipe body
# 7 - mystery bricks
# 8 - coins
# 11 - Mario
# 12 - mushroom minion
# 13 - high orc

# 50,51,52,53,60,61 - metadata stuff
# 80,81,82 - flag specs
# 90,91,92 - castle specs

#testing

if __name__ == "__main__":
    print (rows)
    print (columns)
    print ("press any key")
    ch = getchar()
    print ('You pressed')
    print(ch)
    if(ch=='q'):
        exit(0)
