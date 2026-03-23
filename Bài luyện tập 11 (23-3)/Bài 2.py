# Từ các chuỗi ký tự đã được sắp xếp từ bài 9. Viết chương trình tìm kiếm sử dụng Binary search,
# Tìm kiếm 1 chuỗi bất kỳ (Nhập từ bàn phím) trong 5 chuỗi ở trên, trả về vị trí và in ra màn hình.
chuoi= []
for i in range(5):
    s= input(f"Nhập chuỗi thứ {i+1}: ")
    chuoi.append(s)
print("Ta có:",chuoi)
def i_s(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j= i - 1
        while j>= 0 and len(arr[j]) < len(key):
            arr[j + 1]= arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Bước {i}: {arr}")
i_s(chuoi)
print("Xét theo độ dài,ta được:",chuoi)
chuoingan = sorted(chuoi)
print("Sắp xếp xong ta có:",chuoingan)
def dinhvi(arr,target):
    left= 0
    right= len(arr) - 1
    while left <= right:
        mid = (left + right)// 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+ 1
        else:
            right = mid- 1
    return -1
timchuoi = input("Nhập chuỗi cần tìm: ")
timthay = dinhvi(chuoingan,timchuoi)
if timthay != -1:
    print(f"Tìm thấy '{timchuoi}' tại {timthay}")
else:
    print(f"'{timchuoi}'không có trong danh sách")