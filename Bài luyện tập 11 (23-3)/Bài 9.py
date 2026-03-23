# Viết chương trình cộng hai ma trận cùng kích thước, giá trị của ma trận nhập từ bàn phím
# Báo lỗi nếu nhập vào giá trị trống
def nhapmatrix(hang, cot):
    matrix= []
    for i in range(hang):
        dong= []
        for j in range(cot):
            val= input(f"Nhập phần tử [{i}][{j}]: ")
            if val.strip()== "":
                print("Nhập lại")
                return None
            try:
                dong.append(int(val))
            except:
                print("Phải là số nguyên!")
                return None
        matrix.append(dong)
    return matrix
hang= int(input("Nhập số hàng: "))
cot= int(input("Nhập số cột: "))
print("Nhập ma trận A: ")
A = nhapmatrix(hang, cot)
if A is None:
    exit()
print(" Nhập ma trận B:")
B = nhapmatrix(hang,cot)
if B is None:
    exit()
C = []
for i in range(hang):
    dong = []
    for j in range(cot):
        dong.append(A[i][j] + B[i][j])
    C.append(dong)
print(" Ma trận kết quả (A + B) có dạng:")
for dong in C:
    print(dong)