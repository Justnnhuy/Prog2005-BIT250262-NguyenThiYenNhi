# Hình 1:
cao =4
rong=4
for i in range (cao):
    print("*"* rong)
# Hình 2:
n=4
for i in range(1,n+1):
    print("*"* i)
# Hình 3:
n=4
for i in range(n,0,-1):
    print("*"* i)
# Hình 4:
n=4
for i in range(1,n+1):
    print(" " * (n-i) + "*"* i)
# Hình 5:
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == n or j ==1 or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# Hình 6:
n=4
for i in range(n,0,-1):
    for j in range (i,0,-1):
        if i == n or j == 1 or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# Hình 7:
n=4
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i == n or j == 1 or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# Hình 8:
n=4
for i in range (n):
    print(" "*(n-i-1)+ "*"*(2*i+1))
# Hình 9:
n=4
for i in range (n):
    print(" "*(n-i-1),end="")
    for j in range(2*i+1):
        if j == 0 or j == 2*i or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# Hình 10:
n=4
for i in range (n,0,-1):
    print(" "*(n-i),end = "")
    for j in range(1,2*i):
        if i ==n or i ==1 or j==1 or j ==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()