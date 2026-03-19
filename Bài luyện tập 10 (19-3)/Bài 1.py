# Trích xuất tên bài hát từ đường dẫn. Cho một chuỗi biểu thị đường dẫn đến tệp nhạc, ví dụ: `d:\\music\\muabui.mp3`, viết hai hàm:
   # Hàm để trích xuất "muabui.mp3"
   # Hàm để trích xuất "muabui"
#  Đường dẫn có thể là bất kỳ đường dẫn bài hát nào, nên hàm phải trả về kết quả chính xác cho mọi đầu vào.
import os
def lay_ten_file(path):
    return os.path.basename(path)
def lay_ten_bai_hat(path):
    ten_file = os.path.basename(path)
    ten, _ = os.path.splitext(ten_file)
    return ten
path = input("Nhap duong dan bai hat: ")  # d:\music\Taylor Swift - Lover.mp3
print("Ten file:", lay_ten_file(path))
print("Ten bai hat:", lay_ten_bai_hat(path))