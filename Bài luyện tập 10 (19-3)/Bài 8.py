# Nhập 5 chuỗi bất kỳ từ bàn phím, sử dụng bubble sort để sắp xếp đồ dài các chuỗi theo thứ tự giảm dần.
   # In ra màn hình từng bước sắp xếp.
ds = [input(f"Nhập chuỗi {i+1}: ") for i in range(5)]
print("\nBan đầu:", ds)
for i in range(len(ds)):
    for j in range(len(ds) - 1):
        if len(ds[j]) < len(ds[j + 1]):
            ds[j], ds[j + 1] = ds[j + 1], ds[j]
            print("Đổi chỗ:", ds)
print("\nKết quả:", ds)