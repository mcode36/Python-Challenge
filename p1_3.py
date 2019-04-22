### Print 9 x 9 Multiplication Table
i = 0
for row in range (0,3):
    print("+------------+------------+------------+")
    for j in range (1,10):
        k = (i+1)*j
        if (k < 10):
            eq = " =  ";
        else :
            eq = " = ";
        buff = "| "+str(i+1)+ " x "+ str(j)+ eq+ str(k)+ " |"

        k = (i+2)*j
        if (k < 10):
            eq = " =  ";
        else :
            eq = " = ";
        buff = buff + " "+str(i+2)+ " x "+ str(j)+ eq+ str(k)+ " |"

        k = (i+3)*j
        if (k < 10):
            eq = " =  ";
        else :
            eq = " = ";
        buff = buff + " "+str(i+3)+ " x "+ str(j)+ eq+ str(k)+ " |" 
        print(buff)
    i = i+3
print("+------------+------------+------------+")

