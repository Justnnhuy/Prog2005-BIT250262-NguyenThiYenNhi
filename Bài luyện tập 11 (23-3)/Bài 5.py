# Khởi tạo một dictionary đơn giản
to= {"ten": "Nnhuy",
     "tuoi": 19,
     "truong": "Đại học CMC"}
print("Dictionary ban đầu:",to)
key = input("Nhập key: ")
if key in to:
    print(f"Key '{key}' tồn tại trong dictionary mang giá trị:",to[key])
else:
    print(f"Không thấy '{key}'tồn tại trong dictionary.")