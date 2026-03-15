# Thêm phương thức `display()` vào lớp `Student` để in thông tin theo format: "Sinh viên A có điểm là 10"
class Student:
    def __init__(self, name, score):
        if 0<= score<= 10:
            self.name= name
            self.score= score
        else:
            raise ValueError("Điểm phải nằm trong khoảng từ 0 đến 10.")
    def display(self):
        print(f"Sinh viên {self.name} có điểm là {self.score}")
hs= Student("Nnhuy", 10)
hs.display()