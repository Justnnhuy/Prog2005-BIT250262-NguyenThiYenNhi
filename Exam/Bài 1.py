#Yêu cầu nhập :a,b,c
#Tìm số lớn nhất và nhỏ nhất trong 3 số a,b,c
#Giải phương trình bậc hai a(x^2) + bx + c = 0
import math
a= float(input("Nhập a: "))
b= float(input("Nhập b: "))
c= float(input("Nhập c: "))
max_giatri= max(a, b, c)
min_giatri= min(a, b, c)
print("Số lớn nhất trong 3 số là: ", max_giatri)
print("Số nhỏ nhất trong 3 số là: ", min_giatri)
if a== 0:
        if b!= 0:
            x= -c / b
            print("Phương trình có nghiệm duy nhất:", x)
        else:
            if c== 0:
                print("Phương trình có vô số nghiệm")
            else:
                print("Phương trình vô nghiệm")
else:
        delta= b ** 2 - 4 * a * c
        if delta> 0:
            x1= (-b + math.sqrt(delta))/ (2 * a)
            x2= (-b - math.sqrt(delta))/ (2 * a)
            print("Phương trình có 2 nghiệm phân biệt:")
            print("x1 =",x1)
            print("x2 =",x2)
        elif delta== 0:
            x = -b/ (2 * a)
            print("Phương trình có nghiệm kép:", x)
        else:
            print("Phương trình có vô số nghiệm")



