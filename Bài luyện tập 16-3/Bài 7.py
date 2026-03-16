# Tạo đối tượng Person có thuộc tính name và age, có class method tạo đối tượng Person từ chuỗi "name-age"
# (ví dụ: "Nam-20").
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, s):
        name, age = s.split('-')
        return cls(name, int(age))
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
p1 = Person("Nam", 20)
print(p1)
p2 = Person.from_string("Lan-25")
print(p2)