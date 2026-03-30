# In ra các số chẵn từ 1 đến 20( dùng for)
# Tính tổng các số chẵn đó
sum = 0
for i in range(1,21):
    if i % 2 == 0:
        print(i,end=' ')
        sum +=1
print('\nTổng các số chẵn là:',sum)