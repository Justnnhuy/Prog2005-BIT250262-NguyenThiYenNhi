# Quản lý sản phẩm – Tệp văn bản
   # Viết chương trình nhập thông tin sản phẩm gồm:
     # Mã sản phẩm (Code): kiểu chuỗi (String)
     # Tên sản phẩm (Name): kiểu chuỗi (String)
     # Giá (Price): kiểu số (Number)
   # Mỗi sản phẩm sau khi nhập thành công sẽ được nối thêm (append) vào tệp theo định dạng:
     # ProductCode;ProductName;Price
   # Ví dụ dữ liệu trong tệp sau khi thêm:
     # sv1;Cocacolala;15.5
     # sp2;Bưởi 5 Roi;18.0
     # sp3;Bia 333;14.5
   # Chương trình cần thực hiện hai chức năng chính:
     # Hiển thị danh sách sản phẩm từ tệp.
     # Sắp xếp sản phẩm theo giá giảm dần và hiển thị kết quả.

def add_product(filename):
    code = input("Nhập mã sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{code};{name};{price}\n")
    print("Đã thêm sản phẩm thành công!\n")
def display_products(filename):
    print("Danh sách sản phẩm:")
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
def sort_products_by_price(filename):
    products = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) == 3:
                code, name, price = parts[0], parts[1], float(parts[2])
                products.append((code, name, price))
    products.sort(key=lambda x: x[2], reverse=True)
    print("\nDanh sách sản phẩm sắp xếp theo giá giảm dần:")
    for code, name, price in products:
        print(f"{code};{name};{price}")
filename = "products.txt"
while True:
    print("\n--- MENU ---")
    print("1. Thêm sản phẩm")
    print("2. Hiển thị danh sách sản phẩm")
    print("3. Sắp xếp sản phẩm theo giá giảm dần")
    print("4. Thoát")
    choice = input("Chọn chức năng (1-4): ")
    if choice == "1":
        add_product(filename)
    elif choice == "2":
        display_products(filename)
    elif choice == "3":
        sort_products_by_price(filename)
    elif choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")