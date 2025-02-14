'''

Table Printer: Takes a list of lists of strings and displays it in 
a well-organized table with each column right-justified. 
Assume that all the inner lists will contain the same number of strings.

For example:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

the printTable() funcion would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose

'''

def printTable(table):
    
    columnWidth = [0] * len(table) # Holds the maximum width of each column
    lengthOfList = len(table[0]) # The number of rows (all sublists have the same length)
    
    # Finds the max width of each column
    for column in range(len(table)): 
        sortedColumn = sorted(table[column], key=len)
        columnWidth[column] = len(sortedColumn[-1]) # sets the max string length in each sublist

    # Print the table with each column right justified   
    for row in range(lengthOfList):
        print()
        for column in range(len(table)):
            string = table[column][row] 
            print(string.rjust(columnWidth[column]), end =' ')

# Test list of lists variable
tableData =  [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
   
printTable(tableData) # Calling the function 
        
            
        
        

