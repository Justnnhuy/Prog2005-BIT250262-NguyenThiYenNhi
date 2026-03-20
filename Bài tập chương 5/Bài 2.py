# Nhiều đồ thị trên cùng một biểu đồ
  # Vẽ 2 hàm số: 𝑦=𝑥2 (màu xanh), 𝑦=𝑥3 (màu đỏ)
  # Hiển thị cả hai trên cùng một biểu đồ
  # Thêm chú thích (legend) để phân biệt từng đường
import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(-10, 10, 200)
y1= x**2
y2= x**3
plt.figure(figsize=(8,6), facecolor="#fff0f5")
plt.plot(x, y1, color="blue", linewidth=2.5, label="y = x^2")
plt.plot(x, y2, color="red", linewidth=2.5, linestyle="--", label="y = x^3")
plt.title("Đồ thị biểu thị hàm số", fontsize=14, color="#c71585")
plt.xlabel("x", fontsize=12, color="#c71585")
plt.ylabel("y", fontsize=12, color="#c71585")
plt.legend(loc="upper left", fontsize=12, frameon=True, facecolor="#ffe4e1", edgecolor="#ff69b4")
plt.grid(True, linestyle=":", color="#ffc0cb")
plt.show()