### Print 9 x 9 Multiplication Table
import math

def main ():
    c = input("How many columns?(1 to 9) ")
    col = int(c)
    
    number_of_row = math.ceil(9/col)
    print(number_of_row)

    def hline(col):
        for i in range (0,col):
            print("+------------",end='')
        print("+")

    i = 0
    row = 1
    while row <= number_of_row:
        hline(col)
        for j in range (1,10):
            buff = "|"
            col_print = 0
            for o in range (1,col+1):
                v = i + o
                if (v < 10):
                    k = (v)*j
                    if (k < 10):
                        eq = " =  ";
                    else :
                        eq = " = ";
                    buff = buff + " " + str(v) + " x " + str(j) + eq + str(k) + " |"
                    col_print += 1
            print(buff)
        i = i+col
        row += 1
    hline(col_print)
    print("")
    
redo = "y"
while (redo == "y"):
    main()
    redo = input("Re-do?(y/n) ")

