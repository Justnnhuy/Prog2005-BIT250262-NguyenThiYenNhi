# Viết chương trình nhận vào một danh sách số từ người dùng và in ra tất cả các số chẵn, đồng thời tính tổng của các số chẵn đó.
so= input("Nhập các số, cách nhau bởi dấu cách: ")
so= so.split()
so= [int(x) for x in so]
print("Danh sách nhập:",so)
sochan= []
tong= 0
for n in so:
    if n % 2== 0:
        sochan.append(n)
        tong += n
print("Các số chẵn:",sochan)
print("Tổng các số chẵn:",tong)