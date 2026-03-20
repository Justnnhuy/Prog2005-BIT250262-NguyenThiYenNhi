# Biểu đồ tròn (Pie Chart)
  # Thể hiện phần trăm doanh số của 5 sản phẩm: A: 30%, B: 25%, C: 15%, D: 20%, E: 10%
  # Vẽ biểu đồ tròn có kèm nhãn
import matplotlib.pyplot as plt
labels= ["A", "B", "C", "D", "E"]
sizes= [30, 25, 15, 20, 10]
colors= ["#ff69b4", "#ffb6c1", "#ffc0cb", "#ffe4e1", "#f8bbd0"]
explode= [0.1, 0, 0, 0, 0]
plt.figure(figsize=(7,7), facecolor="#fff0f5")
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
               autopct="%1.1f%%", startangle=90, shadow=True,
               textprops={"color":"#c71585", "fontsize":12})
plt.title("Tỷ lệ doanh số các sản phẩm", fontsize=14, color="#c71585")
plt.show()