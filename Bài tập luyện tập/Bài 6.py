# Tách và xử lý chuỗi.Cho một chuỗi như "`5; 7; 8; -2; 8; 11; 13; 9; 10`" (có thể nhập từ bàn phím):
   # In từng số trên một dòng riêng
   # In ra có bao nhiêu số chẵn
   # In ra có bao nhiêu số âm
   # In ra có bao nhiêu số nguyên tố
   # Tính và in giá trị trung bình
import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
s= input("Nhập chuỗi số, cách nhau bằng dấu ';': ")
numbers= [int(x.strip()) for x in s.split(";")]
print("Các số trong chuỗi:")
for num in numbers:
    print(num)
even_count= sum(1 for num in numbers if num % 2 == 0)
negative_count= sum(1 for num in numbers if num < 0)
prime_count= sum(1 for num in numbers if is_prime(num))
average_value= sum(numbers) / len(numbers)
print(f"Số lượng số chẵn: {even_count}")
print(f"Số lượng số âm: {negative_count}")
print(f"Số lượng số nguyên tố: {prime_count}")
print(f"Giá trị trung bình: {average_value}")

