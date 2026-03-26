# Tạo một danh sách chứa 5 số nguyên. In ra số lượng số nguyên trong danh sách và dùng vòng lặp để in từng số trên một dòng mới. Cuối cùng, tính và in ra tổng các số trong danh sách.
ds = [3, 7, 2, 9, 5]
print("Số lượng số nguyên trong danh sách:", len(ds))
print("Các số trong danh sách:")
for so in ds:
    print(so)
tong = sum(ds)
print("Tổng các số trong danh sách:", tong)