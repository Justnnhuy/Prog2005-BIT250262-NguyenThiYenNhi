# Viết một hàm đệ quy để tính giai thừa của một số do người dùng nhập vào.
def giai_thua(n):
    if n== 0 or n== 1:
        return 1
    else:
        return n* giai_thua(n - 1)
n = int(input("Nhập số nguyên không âm: "))
if n < 0:
    print("Số âm không có giai thừa")
else:
    print(f"{n}! = {giai_thua(n)}")