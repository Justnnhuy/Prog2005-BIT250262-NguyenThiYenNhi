# Khởi tạo một danh sách các số nguyên
# Thêm phần tử vào danh sách
# Nhập giá trị k và kiểm tra số lần xuất hiện của nó trong danh sách
# Tính tổng tất cả các số nguyên tố trong danh sách
# Sắp xếp danh sách
# Xóa danh sách
so= [1, 2, 3, 4, 5]
print("Ta có danh sách:",so)
x= int(input("Nhập số bạn muốn thêm: "))
so.append(x)
print("Ta có một danh sách mới sau khi thêm:",so)
k= int(input("Nhập giá trị k:"))
demk= so.count(k)
print(f"Số lần xuất hiện của {k} trong danh sách là:",demk)
def laprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
tongprime= 0
for num in so:
    if laprime(num):
        tongprime+= num
print("Tổng các số nguyên tố trong danh sách:",tongprime)
so.sort()
print("Danh sách sau khi sắp xếp:",so)
so.clear()
print("Danh sách sau khi xóa:",so)