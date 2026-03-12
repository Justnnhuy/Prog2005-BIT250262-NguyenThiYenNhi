#Viết hàm nhận vào một tuple các số nguyên và trả về:
   #Tổng
   #Giá trị lớn nhất
   #Giá trị nhỏ nhất
def xu_ly_tuple(numbers: tuple[int]) -> tuple[int, int, int]:
    tong = 0
    lon_nhat = numbers[0]
    nho_nhat = numbers[0]
    for num in numbers:
        tong += num
        if num > lon_nhat:
            lon_nhat = num
        if num < nho_nhat:
            nho_nhat = num
    return tong, lon_nhat, nho_nhat
# Ví dụ:
data = (3, 7, -2, 10, 5)
ket_qua = xu_ly_tuple(data)
print("Tổng:", ket_qua[0])
print("Giá trị lớn nhất:",ket_qua[1])
print("Giá trị nhỏ nhất:",ket_qua[2])