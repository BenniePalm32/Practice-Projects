# Create a fantasy game inventory for a player. The data structure to model the player's inventory is a dictionary where the keys are string values 
# describing the item in the inventory and the value is an integer value detailing how many of that item the player has.
# For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
# means the player has 1 rope, 6 torches, 42 gold coins, and so on.

# Write a function named displayInventory() that would take any possible inventory and display it.

def displayInventory(inventory):
    
    print('Inventory:\n') 
    
    # Setting the total item count to 0
    itemTotal = 0  

    # iterate through the items and their totals
    for item, total in inventory.items():
        
        # display the total amount of an individual item
        print(f"{total} {item}('s)\n")

        # updates the total item iventory
        itemTotal += total 

    # prints out the overall total number of items
    print(f'Total number of items: {itemTotal}')

#-----------------------------------------------MAIN CODE-------------------------------------------------#

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} # random dictionary of items to test the function
displayInventory(stuff) # calls the function 