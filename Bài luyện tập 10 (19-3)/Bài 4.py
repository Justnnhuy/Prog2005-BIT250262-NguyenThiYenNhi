# Nhập một chuỗi và in ra độ dài của nó. Xử lý trường hợp người dùng nhập chuỗi rỗng bằng cách hiển thị thông báo lỗi.
chuoi = input("Nhập một chuỗi: ")
if chuoi == "":
    print("Chuỗi rỗng,vui lòng nhập chuỗi")
else:
    print("Độ dài của chuỗi là:",len(chuoi))