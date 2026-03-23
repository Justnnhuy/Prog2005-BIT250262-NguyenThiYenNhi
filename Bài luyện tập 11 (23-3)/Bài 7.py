# Nhập thông tin nhân viên: tên, tuổi, id
name = input("Nhập tên nhân viên: ")
age = input("Nhập tuổi nhân viên: ")
emp_id = input("Nhập ID nhân viên: ")

# Lưu thông tin vào file text
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"Tên: {name}\n")
    f.write(f"Tuổi: {age}\n")
    f.write(f"ID: {emp_id}\n")

print("Đã lưu thông tin vào file nhanvien.txt")

# Lưu thông tin vào file csv
import csv
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])
    writer.writerow([name, age, emp_id])

print("Đã lưu thông tin vào file nhanvien.csv")