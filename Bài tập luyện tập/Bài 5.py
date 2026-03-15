# Xử lý danh sách đa chiều. Viết chương trình cho phép:
    # Khởi tạo và nhập một ma trận M x N với các phần tử ngẫu nhiên
    # Hiển thị bất kỳ hàng nào dựa trên đầu vào của người dùng (ví dụ: yêu cầu hiện thị hàng 3)
    # Hiển thị bất kỳ cột nào dựa trên đầu vào của người dùng (ví dụ: yêu cầu hiện thị cột 2)
    # Hiển thị giá trị lớn nhất trong ma trận
import random
M= int(input("Nhập số hàng M: "))
N= int(input("Nhập số cột N: "))
matrix =[[random.randint(1, 100) for _ in range(N)] for _ in range(M)]
print("Ma trận vừa tạo:")
for row in matrix:
    print(row)
row_index= int(input("Nhập số thứ tự hàng muốn hiển thị (1 đến M): ")) - 1
if 0 <= row_index< M:
    print(f"Hàng {row_index + 1}: {matrix[row_index]}")
else:
    print("Số hàng không hợp lệ.")
col_index= int(input("Nhập số thứ tự cột muốn hiển thị (1 đến N): ")) - 1
if 0 <= col_index < N:
    print(f"Cột {col_index + 1}: {[matrix[i][col_index] for i in range(M)]}")
else:
    print("Số cột không hợp lệ.")
max_value= max(max(row) for row in matrix)
print(f"Giá trị lớn nhất trong ma trận là: {max_value}")