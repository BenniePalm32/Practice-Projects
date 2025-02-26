''' 
Zombie Dice Bots

1. Place all 13 dice in the cup. The player randomly draws three dice from the cup and then rolls them. Players always roll exactly three dice.

2. They set aside and count up any brains (humans whose brains were eaten) and shotguns (humans who fought back). 
   Accumulating three shotguns automatically ends a player’s turn with zero points (regardless of how many brains they had). 
   If they have between zero and two shotguns, they may continue rolling if they want. 
   They may also choose to end their turn and collect one point per brain.

3. If the player decides to keep rolling, they must reroll all dice with footsteps. Remember that the player must always roll three dice; 
   they must draw more dice out of the cup if they have fewer than three footsteps to roll. 
   A player may keep rolling dice until either they get three shotguns—losing everything—or all 13 dice have been rolled. 
   A player may not reroll only one or two dice, and may not stop mid-reroll.

4. When someone reaches 13 brains, the rest of the players finish out the round. 
   The person with the most brains wins. If there’s a tie, the tied players play one last tiebreaker round.


'''

import zombiedice
import random 

class MyZombie:
    
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class FiftyFiftyZombie: # A bot that, after the first roll, randomly decides if it will continue or stop
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll

        while diceRollResults is not None:

            choice = random.randint(0,1)

            if choice == 1:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class TwoShotgunsZombie: # A bot that stops rolling after it has rolled two Shotguns
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        shotguns = 0

        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            
            # keeps rolling until two shotguns are rolled
            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break 

class TwoBrainsZombie: # A bot that stops rolling after it has rolled two brains
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        brains = 0

        while diceRollResults is not None:
            brains += diceRollResults['brains']
            
            # keeps rolling until two brains are rolled
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break 

class OneToFourRollZombie: # A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns

    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        rolls = random.randint(1,4)
        turn = 1
        shotguns = 0

        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2 and turn < rolls:
                diceRollResults = zombiedice.roll() # roll again
                turn += 1
            else:
                break

class MoreShotgunsThanBrainsZombie: # A bot that stops rolling after it has rolled more shotguns than brains

    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll 

        while diceRollResults is not None:  
            shotguns = diceRollResults['shotgun']
            brains = diceRollResults['brains']
            
            if shotguns < brains:
                diceRollResults = zombiedice.roll() # roll again
            else: 
                break


#---------------------------------MAIN CODE---------------------------------#
        

zombies = (
    FiftyFiftyZombie(name = '50/50 Zombie'),
    TwoShotgunsZombie(name = '2 Shotty Zombie'),
    TwoBrainsZombie(name = '2 Brains Zombie'),
    OneToFourRollZombie(name = '1 to 4 Roll Zombie'),
    MyZombie(name='My Zombie Bot'),
    MoreShotgunsThanBrainsZombie(name = 'Shotguns > Brains Zombie')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)

