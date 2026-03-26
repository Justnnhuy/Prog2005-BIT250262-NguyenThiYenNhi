# Viết chương trình tìm và in ra tất cả các số nguyên tố từ 1 đến 100. Một số nguyên tố là số lớn hơn 1 và chỉ chia hết cho 1 và chính nó.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")
