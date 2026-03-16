# Tạo lớp `User`, có thuộc tính id. Sử dụng `property` để chỉ cho phép đọc (read-only) thuộc tính id.

class User:
    def __init__(self, id):
        self._id = id
    @property
    def id(self):
        return self._id
u = User(101)
print(u.id)
