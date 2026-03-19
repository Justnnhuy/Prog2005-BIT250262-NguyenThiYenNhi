# Yêu cầu người dùng nhập vào một chuỗi và một ký tự, sau đó đếm xem ký tự đó xuất hiện bao nhiêu lần trong chuỗi.
chuoi= input("Nhập vào một chuỗi: ")
ky_tu= input("Nhập vào một ký tự: ")
if len(ky_tu) != 1:
    print("Chỉ được nhập một ký tự")
else:
    so_lan = chuoi.count(ky_tu)
    print(f"Ký tự '{ky_tu}' xuất hiện {so_lan} lần trong chuỗi.")