# Với n nhập từ bàn phím,in ra các hình tam giác
n= int(input("Nhập n: "))
print("\nNhập n từ bàn phím,sau khi nhập sẽ in ra hình tam giác vuông: ")
for i in range(1,n+1):
    print("*"* i)

print("\nNhập n từ bàn phím,sau khi nhập sẽ in ra hình tam giác cân: ")
for i in range(1,n+1):
    print(" " * (n-i) + "*" * (2*i-1))



