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
    if ( 0<=row_number<=2 and 0<=col_number<=2 ):
        for i in range(3):
            for j in range(3):
                if number== array_for_line[i][j] :
                    return False
        return True  
    if ( 3<=row_number<=5 and 0<=col_number<=2 ):
        for i in range(3,6):
            for j in range(3):
                if number== array_for_line[i][j] :
                    return False
        return True  
    if ( 6<=row_number<=8 and 0<=col_number<=2 ):
        for i in range(6,9):
            for j in range(3):
                if number== array_for_line[i][j] :
                    return False
        return True  
    if ( 0<=row_number<=2 and 3<=col_number<=5 ):
        for i in range(3):
            for j in range(3,6):
                if number== array_for_line[i][j] :
                    return False
        return True  
    if ( 3<=row_number<=5 and 3<=col_number<=5 ):
        for i in range(3,6):
            for j in range(3,6):
                if number== array_for_line[i][j] :
                    return False
        return True  
    if ( 6<=row_number<=8 and 3<=col_number<=5 ):
        for i in range(6,9):
            for j in range(3,6):
                if number== array_for_line[i][j] :
                    return False
        return True  
    if ( 0<=row_number<=2 and 6<=col_number<=8 ):
        for i in range(3):
            for j in range(6,9):
                if number== array_for_line[i][j] :
                    return False
        return True  
    if ( 3<=row_number<=5 and 6<=col_number<=8 ):
        for i in range(3,6):
            for j in range(6,9):
                if number== array_for_line[i][j] :
                    return False
        return True  
    if ( 6<=row_number<=8 and 6<=col_number<=8 ):
        for i in range(6,9):
            for j in range(6,9):
                if number== array_for_line[i][j] :
                    return False
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
    # print("Here for -",row_number,col_number)
    if array_for_line[row_number][col_number]==0 :
        values_it_can_take = array_maker_for_values(array_for_line,  row_number , col_number)
        # print(values_it_can_take)
        if len(values_it_can_take)==0 :
            return None
        for k in values_it_can_take:
            # print(f"taking {k} for {row_number} , {col_number}")
            array_for_line[row_number][col_number]=k
            array_col_wise[col_number][row_number]=k
            # print()
            # for i in range(9):
            #     for j in range(9):
            #         print(array_for_line_of_sudoku[i][j],end=" ")
            #     print()
            # print()
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
array_for_line_of_sudoku =  [[],[],[],[],[],[],[],[],[]] 
for i in range(9):
    array_for_line_of_sudoku[i]=input().split()
    array_for_line_of_sudoku[i]=[int(k) for k in array_for_line_of_sudoku[i]]
array_col_wise = [[],[],[],[],[],[],[],[],[]] 
#  Creating column wise array from rows
for i in range(9):
    for j in range(9):
        array_col_wise[i].append(array_for_line_of_sudoku[j][i])


# Calling function to solve
F = Suduko_solver(array_for_line_of_sudoku , 0, 0)


#  Final Priting 
if F=="Done":
    print("\n\n")
    print("Here is Your Solved Sudoku")
    for i in range(9):
        for j in range(9):
            print(array_for_line_of_sudoku[i][j],end=" ")
        print()
else :
    print("\n\nThe Given Sudoku can't be solved.")
