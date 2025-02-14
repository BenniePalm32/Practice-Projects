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


tableData =  [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    columnWidth = [0] * len(table)
    lenOfList = len(table[0])

    for column in range(len(table)):
        

