# Xây dựng chương trình console cho phép người dùng chọn chương trình chạy
# -Bài 1
# -Bài 2
# -Bài 3
# -Bài 4
# -Thoát
def bai1():
    print("Chạy Bài 1")
    # Người dùng có thể viết code xử lí bài 1 ở đây
def bai2():
    print("Chạy Bài 2")
    # Người dùng có thể viết code xử lí bài 2 ở đây
def bai3():
    print("Chạy Bài 3")
    # Người dùng có thể viết code xử lí bài 3 ở đây
def bai4():
    print("Chạy Bài 4")
    # Người dùng có thể viết code xử lí bài 4 ở đây
while True:
    print("\n===== MENU =====")
    print("1.Bài 1")
    print("2.Bài 2")
    print("3.Bài 3")
    print("4.Bài 4")
    print("5.Thoát")

    choice= input("Vui lòng chọn lại chương trình từ 1-5: ")
    if choice== "1":
        bai1()
    elif choice== "2":
        bai2()
    elif choice== "3":
        bai3()
    elif choice== "4":
        bai4()
    elif choice== "5":
        print("Người dùng đã thoát chương trình.")
        break
    else:
        print("Lựa chọn của bạn không hợp lệ,vui lòng nhập lạii")