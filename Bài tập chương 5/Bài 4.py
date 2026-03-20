# Yêu cầu: Biểu đồ Cột Ngang – Xếp hạng Diện tích Thành phố Viết chương trình hiển thị Top 10 thành phố lớn nhất theo diện tích ở California bằng biểu đồ cột ngang
  # Gợi ý:
   # Sử dụng cột area_total_km2
   # Sắp xếp dữ liệu theo diện tích giảm dần
   # Dùng plt.barh()
import matplotlib.pyplot as plt
cities= ["Los Angeles", "San Diego", "San Jose", "Bakersfield", "Fresno",
          "Sacramento", "Long Beach", "Oakland", "Riverside", "Stockton"]
areas= [1302, 964, 469, 381, 298, 259, 170, 145, 134, 162]
sorted_data= sorted(zip(areas, cities), reverse=True)
areas_sorted, cities_sorted= zip(*sorted_data)
plt.figure(figsize=(10,6), facecolor="#fff0f5")
bars= plt.barh(cities_sorted, areas_sorted, color="#ff69b4")
for bar, area in zip(bars, areas_sorted):
    plt.text(area + 10, bar.get_y() + bar.get_height()/2,
             f"{area} km²", va="center", fontsize=11, color="#c71585")
plt.xlabel("Diện tích (km²)", fontsize=12, color="#c71585")
plt.title("Top 10 thành phố lớn nhất theo diện tích tại California", fontsize=14, color="#c71585")
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle=":", color="#ffc0cb")
plt.show()