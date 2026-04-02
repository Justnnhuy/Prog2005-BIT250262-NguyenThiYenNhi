# Hình 1:
rong=4
dai=4
for i in range(rong):
    for j in range(dai):
        print(1,end=" ")
    print()
print()
# Hình 2:
rong=4
dai=4
for i in range(rong):
    for j in range(1,dai+1):
        print(j,end=" ")
    print()
# Hình 3:
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()
# Hình 4:
n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()
# Hình 5:
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        if i ==n or j==1 or j==i:
            print(j,end=" ")
        else:
            print(" ",end="")
    print()
print()
# Hình 6:
n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        if i ==n or j==1 or j==i:
            print(j,end=" ")
        else:
            print(" ",end="")
    print()
print()
# Hình 7:
for i in range(1,n+1):
    for j in range(1,n+1):
        print(" "*(n-i),end="")
        for _ in range (i):
            print(j,end=" ")
        print()
