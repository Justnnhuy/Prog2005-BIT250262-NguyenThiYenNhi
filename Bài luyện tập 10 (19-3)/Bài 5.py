# Subplots
  # Tạo một Figure gồm 1 hàng, 2 cột
  # Subplot bên trái: vẽ đồ thị y=x^2
  # Subplot bên phải: vẽ đồ thị y=sqrt(x)
  # Thêm tiêu đề và nhãn cho từng subplot
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(x, x**2, color='hotpink', linewidth=2)
axs[0].set_title("Đồ thị y = x^2", fontsize=12)
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[1].plot(x, np.sqrt(x), color='deeppink', linewidth=2)
axs[1].set_title("Đồ thị y = sqrt(x)", fontsize=12)
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")
axs[1].grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()