# Tạo lớp Hoa có các thuộc tính: Tên, Màu . Tạo một đối tượng và in thông tin Hoa bằng hàm print() sử dụng đối tượng vừa tạo
# Định nghĩa lớp Hoa
class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    def __str__(self):
        return f"Hoa: {self.ten}, Màu: {self.mau}"
hoaa = Hoa("Hồng", "Đỏ")
print(hoaa)
