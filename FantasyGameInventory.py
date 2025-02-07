'''
Create a fantasy game inventory for a player. The data structure to model the player's inventory is a dictionary where the keys are string values 
describing the item in the inventory and the value is an integer value detailing how many of that item the player has.
For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
means the player has 1 rope, 6 torches, 42 gold coins, and so on.

part 1.
Write a function named displayInventory() that would take any possible inventory and display it.

part 2.
Write a function named addToInventory() that takes a list of newly found items and adds them to your dictionary of current items.

'''
# This function prints out the current inventory of items and the grand total of items in the inventory
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

# This function will add any new items found and add those items to your inventory
def addToInventory(inventory, addedItems):

    for item in addedItems:
        
        inventory[item] = inventory.get(item, 0) + 1
    
    return inventory



#-----------------------------------------------MAIN CODE-------------------------------------------------#

currentInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} # dictionary of current inventory
foundLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] # newly found loot to add to the current inventory

print('Previous')
displayInventory(currentInventory) # calling the function to print out the original inventory 

addToInventory(currentInventory, foundLoot) # calls the function that adds the newly found items to the original inventory

print(f'Updated')
displayInventory(currentInventory) # prints out the newly updated inventory and the total number of items
