# Nhập 5 chuỗi bất kỳ từ bàn phím, sử dụng insertion sort để sắp xếp đồ dài các chuỗi theo thứ tự giảm dần.
# In ra màn hình từng bước sắp xếp.
strings= []
for i in range(5):
    s= input(f"Nhập chuỗi thứ {i+1}: ")
    strings.append(s)
print("\n Danh sách ban đầu:", strings)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j =i - 1
        while j>= 0 and len(arr[j]) < len(key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Bước {i}:{arr}")
insertion_sort(strings)
print("Kết quả cuối cùng:",strings)