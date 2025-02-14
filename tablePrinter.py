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
    
    columnWidth = [0] * len(table)
    lengthOfList = len(table[0])
    
    for tableLen in range(len(table)):
        sortedTable = sorted(table[tableLen], key = len)
        columnWidth[tableLen] = len(sortedTable[-1])
        
    for row in range(lengthOfList):
        print()
        for column in range(len(table)):
            string = table[column][row]
            print(string.rjust(columnWidth[column]), end = ' ')


tableData =  [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
   
printTable(tableData)
        
            
        
        

