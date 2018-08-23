# TERMINAL SUPER MARIO 

This is a terminal based game written in Python-3 without the help of any user interface libraries like Pygame, curses etc. The game is at present, single player with a sliding game window. The code is written in an Object Oriented fashion and demonstrates inheritance, encapsulation, abstraction and polymorphism.

## Objective
Without getting killed by the Mushroom Minions and High Orcs or falling down treacherous canyons, get to the end of the game having collected as many coins as you can.

## Prerequisites
- colorama v.0.3.9, used for colouring ASCII characters during gameplay.
- Audio files mentioned in the code

## Run the Game
- Install all the requirements specified in requirements.txt:
`pip install -r requirements.txt`
- Run the game with:
 `python3 main.py`
> Note: For better effect, it is recommended to run the game in a full-screen terminal window.

## Controls
Control Mario by using:
- `w` - Jump
- `a` - Move left
- `d` - Move right
You can quit the game at any moment by pressing `q`.
> Note: All keys are case-sensitive.

## Functionality
- Mario possesses basic movement to the left and right as per user directions.
- Mario's jump has a gravity-like effect. Gravity affects every animate object on screen, including enemies.
- Bricks, cement blocks, mystery bricks, pipes and canyons form the landscape map. Randomly generated clouds dot the sky.
- Towards the end of the game, a flag that rises to the top and a castle form the scenery.
- Enemies are of 2 kinds: 
    1. Mushroom Minions are your standard, run-of-the-mill enemies that move towards Mario in a non-random way.
    2. High Orcs, or the Boss enemies, move faster than Minions and can also jump. Killing a boss enemy gives you double the points.
- Coins can be collected from mystery bricks which gives you an added score.
- Score, time left and lives left are all displayed on the top portion of the screen.
- Mario has 3 lives, after which the game gets over. After each life is lost, he goes back to the start and score and time are reset. However, coins collected doesn't reset.

### Additionally
- Every object in the game has a particular colour and design assigned to it.
- Sound effects from the original game have been used for getting coins, killing enemies, dying, winning etc.
- All enemies are smart and exhibit non-random behaviour.
- A flag goes up as soon as the level is completed.

