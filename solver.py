import sys
# Sudoku Solver 
# Harsh
# Start - 10 May 2025
#    -----
#  /       \
# |  O   O  |
# |    ^    |
# |  \___/  |
#  \_______/

# 3*3 box checker for indexes
def box_checker( array_for_line , row_number , col_number , number ):
    quo_row = int(row_number/3)
    quo_col = int(col_number/3)
    for i in range(3*quo_row , 3*(quo_row+1) ):
        for j in range(3*quo_col , 3*(quo_col+1)):
            if number== array_for_line[i][j] : return False
    return True

# value finder for a particular index
def array_maker_for_values(array_for_line , row_number , col_number ):
    array_for_value_it_can_take =[]
    for i in range(1,10):
        if i not in array_for_line[row_number] and i not in array_col_wise[col_number] and box_checker(array_for_line, row_number, col_number , i) :
            array_for_value_it_can_take.append(i)
    return array_for_value_it_can_take

#  Recusrsive Function to solve 
def Suduko_solver(array_for_line , row_number , col_number):
    if array_for_line[row_number][col_number]!=0 :
        if col_number<8:
            return Suduko_solver(array_for_line ,row_number , col_number+1 )
        elif row_number<8:
            return Suduko_solver(array_for_line , row_number +1 , 0)
        else:
            return "Done"
    if array_for_line[row_number][col_number]==0 :
        values_it_can_take = array_maker_for_values(array_for_line,  row_number , col_number)
        if len(values_it_can_take)==0 :
            return None
        for k in values_it_can_take:
            array_for_line[row_number][col_number]=k
            array_col_wise[col_number][row_number]=k
            if col_number<8:
                S = Suduko_solver(array_for_line ,row_number , col_number+1 )
            elif row_number<8:
                S =  Suduko_solver(array_for_line , row_number +1 , 0)
            else:
                return "Done"
            if S=="Done":
                return S 
            array_for_line[row_number][col_number]=0
            array_col_wise[col_number][row_number]=0
        return None

#  Taking 0 at the place of blank space 
#  Taking Inputs 
print("\nEnter 9*9 Sudoku having 0 at blank spaces :-)")
array_for_line_of_sudoku =  [[],[],[],[],[],[],[],[],[]] 
for i in range(9):
    array_for_line_of_sudoku[i]=input().split()
    array_for_line_of_sudoku[i]=[float(k) for k in array_for_line_of_sudoku[i]]


# Checking if the values are valid or not
for i in range(9):
    for j in range(9):
        value = array_for_line_of_sudoku[i][j]
        if ( value < 0 or value >9 or 0<=value<=9 and int(value/1)!=value ):
            print(f"\nInvalid entry ",end="")
            if int(value/1)==value : print(int(value),end=" ")
            else :
                print(value,end=" ")
            print(f"at Position ( {i+1}, {j+1})\n")
            sys.exit(1)

for i in range(9):
    array_for_line_of_sudoku[i]=[int(k) for k in array_for_line_of_sudoku[i]]
    
print("\nGiven Sudoku :")
for i in range(9):
    if i ==3 or i== 6:
        print("---------------------")
    for j in range(9):
        if j==3 or j==6 :
            print("| ",end="")
        print(array_for_line_of_sudoku[i][j],end=" ")
    print()
print()

# Checking if dupliactes are given or not in rows
for i in range(9):
    for j in range(1,10):
        if array_for_line_of_sudoku[i].count(j)>1 :
            print(f"Invalid : There are repititive entries of {j} in row number {i+1}\n")
            sys.exit(1)
    
#  Creating column wise array from rows
array_col_wise = [[],[],[],[],[],[],[],[],[]] 
for i in range(9):
    for j in range(9):
        array_col_wise[i].append(array_for_line_of_sudoku[j][i])

# Checking if dupliactes are given or not in columns
for i in range(9):
    for j in range(1,10):
        if array_col_wise[i].count(j)>1 :
            print(f"Invalid : There are repititive entries of {j} in column number {i+1}\n")
            sys.exit(1)

# Duplicate checking in 3*3 grids
for row in range(3):
    for col in range(3):
        Dictionary_for_grid_checker = {}
        for i in range(3*row , 3*(row+1)):
            for j in range(3*(col) , 3*(col+1)):
                Dictionary_for_grid_checker[array_for_line_of_sudoku[i][j]] = Dictionary_for_grid_checker.get(array_for_line_of_sudoku[i][j],0)+1
        for value in Dictionary_for_grid_checker:
            if value!=0 and Dictionary_for_grid_checker[value]>1 :
                print(f"Invalid : Duplicates of {value} are present in 3x3 Block which has rows from ({3*row+1 , 3*(row+1)}) , column from ({3*(col)+1 , 3*(col+1)})\n")
                sys.exit(1)

# Calling function to solve
F = Suduko_solver(array_for_line_of_sudoku , 0, 0)

#  Final Priting 
if F=="Done":
    print("\n\n")
    print("Here is Your Solved Sudoku")
    for i in range(9):
        if i ==3 or i== 6:
            print("---------------------")
        for j in range(9):
            if j==3 or j==6 :
                print("| ",end="")
            print(array_for_line_of_sudoku[i][j],end=" ")
        print()
    print()
else : print("\n\nThe Given Sudoku can't be solved.\n")
