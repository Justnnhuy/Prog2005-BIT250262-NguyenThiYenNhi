# Viết chương trình nhập hai số, tính các giá trị: lũy thừa, căn bậc 2, chia lấy phần nguyên, chia lấy phần dư, làm tròn số.
import math
a= float(input("Nhập số thứ nhất: "))
b= float(input("Nhập số thứ hai: "))
# Lũy thừa
print(f"{a}^{b}= {a**b}")

# Căn bậc 2 của từng số
print(f"Căn bậc 2 của {a}= {math.sqrt(a)}")
print(f"Căn bậc 2 của {b}= {math.sqrt(b)}")

# Chia lấy phần nguyên (a//b)
print(f"{a}//{b}= {a//b}")

# Chia lấy phần dư
print(f"{a}%{b}= {a%b}")


# Làm tròn số
print(f"Làm tròn {a}= {round(a)}")
print(f"Làm tròn {b}= {round(b)}")