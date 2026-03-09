# In các số lẻ từ 17 đến 111 (theo thứ tự giảm dần)
# In ra các số nguyên tố trong khoảng từ 17 đến 111
# In các số lẻ từ 17 đến 111 theo thứ tự giảm dần
print ("Các số lẻ từ 17 đến 111(theo thứ tự giảm dần) bao gồm: ")
for i in range(111, 16, -1):
    if i % 2 == 1:
        print(i, end=" ")
print("/n")
def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True
print("Các số nguyên tố từ 17 đến 111:")
for i in range(17, 112):
    if is_prime(i):
        print(i,end=" ")
