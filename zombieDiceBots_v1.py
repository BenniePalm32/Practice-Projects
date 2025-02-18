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

class MyZombie:
    
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() #first roll
        

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

zombiedice.runTournament(zombies=zombies, numGames=1000)

