# Yêu cầu người dùng nhập một số nguyên, sau đó kiểm tra và in ra số đó là số chẵn hay số lẻ
num = int(input("Nhập một số nguyên: "))
if num % 2 == 0:
    print(num, "Này là số chẵn")
else:
    print(num, "Này là số lẻ")