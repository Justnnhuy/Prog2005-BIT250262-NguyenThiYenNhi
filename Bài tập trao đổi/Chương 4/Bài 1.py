# Viết hàm nhận vào một tuple các số nguyên và trả về:
  # Tổng
  # Giá trị lớn nhất
  # Giá trị nhỏ nhất
def thongtin_tuple(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)
    return tong, lon_nhat, nho_nhat
cacso = (3, 7, 2, 9, 5)
tong, lon, nho = thongtin_tuple(cacso)
print("Tổng:", tong)
print("Giá trị lớn nhất:", lon)
print("Giá trị nhỏ nhất:", nho)