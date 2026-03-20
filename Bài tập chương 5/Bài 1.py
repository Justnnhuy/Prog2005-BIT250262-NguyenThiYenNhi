# Yêu cầu: Biểu đồ cột
  # Một lớp có kết quả học tập như sau: Xuất sắc: 6, Giỏi: 10, Trung bình: 12, Yếu: 4, Kém: 1
  # Vẽ biểu đồ cột thể hiện dữ liệu trên
  # Thêm tiêu đề và nhãn cho các trục
import matplotlib.pyplot as plt
categories = ["Xuất sắc", "Giỏi", "Trung bình", "Yếu", "Kém"]
values = [6, 10, 12, 4, 1]
plt.figure(figsize=(8,5))
colors = ["#ffb6c1", "#ff69b4", "#ff85c1", "#ff9ecb", "#ffc0cb"]
bars = plt.bar(categories, values, color=colors)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, str(height),
             ha='center', va='bottom')

plt.title("Biểu đồ kết quả học tập của lớp", fontsize=14)
plt.xlabel("Mức độ")
plt.ylabel("Số lượng học sinh")
plt.grid(axis='y', linestyle='--', alpha=0.5)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.show()