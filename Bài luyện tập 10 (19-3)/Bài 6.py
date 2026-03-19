# Viết chương trình đảo ngược một chuỗi nhập từ bàn phím bằng vòng lặp
chuoi = input("Nhập chuỗi: ")
dao_nguoc = ""
for ky_tu in chuoi:
    dao_nguoc= ky_tu + dao_nguoc

print("Chuỗi đảo ngược:", dao_nguoc)