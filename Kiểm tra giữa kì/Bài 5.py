# Tạo class Flower có thuộc tính name và color
# Viết phương thức __str__
# Khởi tạo đối tượng và in thông tin
class Flower:
    def init(self,name,color):
        self.name = name
        self.color = color
    def str(self):
        return f'Tên hoa:{self.name},Màu sắc:{self.color}'
f1 = Flower('Hoa hồng','Đỏ')
print(f1)
