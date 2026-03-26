# Viết chương trình nhận vào một danh sách số nguyên từ người dùng. Sau đó, tìm và in ra số đầu tiên lớn hơn 10, nếu có. Nếu không có số nào lớn hơn 10, in ra thông báo phù hợp.
ds = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
so_lon_hon_10 = None
for so in ds:
    if so > 10:
        so_lon_hon_10 = so
        break
if so_lon_hon_10 is not None:
    print("Số đầu tiên lớn hơn 10 là:", so_lon_hon_10)
else:
    print("Không có số nào lớn hơn 10 trong danh sách.")