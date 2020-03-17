tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)

    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j]) > colWidths[i]: #compare the value of the current len to that of the current index of colWidths
                colWidths[i] = len(table[i][j]) #change it is greater

    for i in range(len(table[0])): #the table has a len of 4, the loop is for how many columns which 4
        row = ""
        for j in range(len(table)): # this one for the rows (3 rows)
            row = row + table[j][i].rjust(colWidths[j]) + " " #I added some space at the end for the invisible line
        print(row) # print every column

printTable(tableData)