# Viết chương trình nhập từ bàn phím lựa chọn để chạy 1 trong các bài tập trên sử dụng vòng lặp While
while True:
    print("\n===== MENU =====")
    print("1. Dem ky tu trong chuoi")
    print("2. Dao nguoc chuoi")
    print("3. Tinh giai thua")
    print("4. Do dai chuoi")
    print("0. Thoat")
    chon = input("Chon bai: ")
    if chon == "1":
        s = input("Nhap chuoi: ")
        c = input("Nhap ky tu: ")
        if len(c) != 1:
            print("Chi nhap 1 ky tu")
        else:
            print("So lan xuat hien:", s.count(c))
    elif chon == "2":
        s = input("Nhap chuoi: ")
        dao = ""
        for i in range(len(s)-1, -1, -1):
            dao += s[i]
        print("Chuoi dao nguoc:", dao)
    elif chon == "3":
        n = int(input("Nhap n: "))
        if n < 0:
            print("Khong hop le")
        else:
            gt = 1
            i = 1
            while i <= n:
                gt *= i
                i += 1
            print("Giai thua:", gt)
    elif chon == "4":
        s = input("Nhap chuoi: ")
        if s.strip() == "":
            print("Chuoi rong")
        else:
            print("Do dai:", len(s))
    elif chon == "0":
        print("Bye")
        break
    else:
        print("Lua chon khong hop le")