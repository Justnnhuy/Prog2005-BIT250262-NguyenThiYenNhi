# Bài 1: Biểu đồ cột về số lượng học sinh theo môn học yêu thích
  # Một lớp có số học sinh yêu thích các môn học như sau: Toán: 8, Lý: 5, Hóa: 7, Sinh: 4, Văn: 6
  # Vẽ biểu đồ cột thể hiện dữ liệu trên
  # Thêm tiêu đề và nhãn cho các trục
import matplotlib.pyplot as plt
cacmonhoc = ['Toán','Lý','Hóa','Sinh','Văn']
soluong = [8,5,7,4,6]
fig,ax = plt.subplots()
plt.bar(cacmonhoc,soluong,color = '#ee74b7')
plt.xlabel('Số lượng học sinh yêu thích môn học ')
plt.ylabel('Các môn học')
plt.title('Số lượng học sính theo môn học yêu thích')
ax.set_facecolor('#ffe6f0')
fig.patch.set_facecolor('pink')
plt.show()
