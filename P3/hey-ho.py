for i in range (1, 101):
    s = str(i)
    if (i%6 == 0) :
        s = "hey-ho"
    else:
        if (i%2 == 0) :
            s = "hey"
        if (i%3 == 0) :
            s = "ho"
    print(s)
