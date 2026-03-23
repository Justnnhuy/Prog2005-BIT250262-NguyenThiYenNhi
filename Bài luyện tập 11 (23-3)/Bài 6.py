# Nhập tên và tuổi từ bàn phím
# Lưu thông tin trên thông qua Dict với key là tên và value là tuổi.
# Tính tuổi trung bình
# Nhập tên và tuổi từ bàn phím
# Lưu thông tin vào dictionary với key = tên, value = tuổi
# Tính tuổi trung bình

people = {}

n = int(input("Nhập số người: "))

for i in range(n):
    name = input(f"Nhập tên người thứ {i+1}: ")
    age_str = input(f"Nhập tuổi của {name}: ")
    if age_str.strip() == "":
        print("❌ Lỗi: tuổi không được để trống!")
        exit()
    try:
        age = int(age_str)
    except:
        print("❌ Lỗi: tuổi phải là số nguyên!")
        exit()
    people[name] = age

print("\nDictionary lưu thông tin:", people)
if len(people) > 0:
    avg_age = sum(people.values()) / len(people)
    print("Tuổi trung bình là:", avg_age)
else:
    print("Không có dữ liệu để tính tuổi trung bình.")