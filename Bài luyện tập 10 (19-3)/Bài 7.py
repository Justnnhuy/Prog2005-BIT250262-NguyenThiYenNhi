# Viết chương trình sử dụng while để yêu cầu người dùng nhập mật khẩu cho đến khi đúng từ khóa "python123"
mat_khau_dung= "python123"
nhap = ""

while nhap != mat_khau_dung:
    nhap = input("Nhập mật khẩu: ")
    if nhap != mat_khau_dung:
        print("Mật khẩu không hợp lệ")
print("Đăng nhập thành công")