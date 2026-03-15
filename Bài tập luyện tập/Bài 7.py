# Tạo lớp `Student` có `tên` và `điểm`. Khởi tạo 2 đối tượng sinh viên khác nhau.
class Student:
    def __init__(self, name, score):
        self.name= name
        self.score= score
    def display_info(self):
        print(f"Tên: {self.name}, Điểm: {self.score}")
student1= Student("Nnhuy",8.5)
student2= Student("Thuong",9.2)
student1.display_info()
student2.display_info()