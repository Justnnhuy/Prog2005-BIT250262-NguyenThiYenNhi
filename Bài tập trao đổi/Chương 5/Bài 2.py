# Bài 2: Biểu đồ cột
  # Một lớp khảo sát số học sinh tham gia các hoạt động ngoại khóa: Thể thao: 7, Âm nhạc: 5, Mỹ thuật: 6, Khoa học: 4, Văn học: 3
  # Vẽ biểu đồ cột thể hiện dữ liệu trên
  # Thêm tiêu đề và nhãn cho các trục
import matplotlib.pyplot as plt
fig,ax = plt.subplots()
ax.set_facecolor('#fcd5df')
fig.patch.set_facecolor('#fba8bd')
hdong = ['Thể thao','Âm nhạc','Mỹ thuật','Khoa học','Văn học']
sluong = [7,5,6,4,3]
plt.bar(hdong,sluong,color='#e84770')
plt.title('Khảo sát số học sinh tham gia hoạt động ngoại khóa')
plt.xlabel('Các hoạt động ngoại khóa')
plt.ylabel('Số lượng học sinh')
plt.show()