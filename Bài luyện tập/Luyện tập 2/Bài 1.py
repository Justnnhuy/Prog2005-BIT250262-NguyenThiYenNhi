# Tạo một danh sách chứa tên của 5 người nhập từ bàn phím.
# Xóa tên người ở vị trí thứ hai trong danh sách
# In danh sách sau mỗi thao tác
names = []
for i in range(5):
    name = input(f"Nhập tên người thứ {i+1}: ")
    names.append(name)

print("Danh sách ban đầu:", names)

del names[1]

print("Danh sách sau khi xóa tên thứ hai:", names)