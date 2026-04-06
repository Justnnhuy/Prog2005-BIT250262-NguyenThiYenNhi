# Xử lý mảng. Viết chương trình nhập một mảng các số tự nhiên. Hiển thị các thông tin sau:
# Dòng 1: Các số lẻ và tổng số lượng số lẻ
# Dòng 2: Các số nguyên tố (Chỉ chia hết cho 1 và chính nó)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input("Nhập các số tự nhiên, cách nhau bởi dấu cách: ").split()))

odd_numbers = [x for x in numbers if x % 2 != 0]
print("Các số lẻ:", odd_numbers, " | Tổng số lượng:", len(odd_numbers))

prime_numbers = [x for x in numbers if is_prime(x)]
print("Các số nguyên tố:", prime_numbers)