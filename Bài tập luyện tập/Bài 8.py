# Xác thực điểm sinh viên nằm trong khoảng `0–10`.
class Student:
    def __init__(self, name, score):
        self.name= name
        if 0 <= score<= 10:
            self.score= score
        else:
            raise ValueError("Số điểm nằm trong khoảng 0-10")
    def display_info(self):
        print(f"Tên: {self.name}, Điểm: {self.score}")
try:
    hs1= Student("Nnhuy", 8.5)
    hs2= Student("Thuong", 9.2)
    hs1.display_info()
    hs2.display_info()
    hs3= Student("Chi", 12)
except ValueError as e:
    print("Lỗi:", e)