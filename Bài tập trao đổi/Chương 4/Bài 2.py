# Tạo lớp biển có các thuộc tính: Tên, Màu . Tạo một đối tượng và in thông tin Biển bằng hàm print() sử dụng đối tượng vừa tạo.
class Bien:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    def __str__(self):
        return f"Biển {self.ten}, màu {self.mau}"
bien= Bien("Biển Đông", "Xanh")
print(bien)