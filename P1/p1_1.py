### Print 9 x 9 Multiplication Table

for i in range (1,10):
    for j in range (1,10):
        k = i*j
        if (k < 10):
            eq = " =  ";
        else :
            eq = " = ";
            
        print(i, " x ", j, eq, k)

