def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                print("*",end="")
            else:
                print(j,end="")
        print()
n=4
pattern(n)