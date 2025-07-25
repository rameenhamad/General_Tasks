def Fb_sequence(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        F1 = 0
        F2 = 1
        for i in range(2, n):
            #adding last two terms
            Fn = F2 + F1
            #values updated
            F1 = F2         #Now 1 has been stored in place of 0
            F2 = Fn         #Sum of both terms stored in 1st term
        # Returning value to the main funtion
        return Fn

Fn = eval(input("enter nth term for Fn: "))

print(Fb_sequence(Fn))