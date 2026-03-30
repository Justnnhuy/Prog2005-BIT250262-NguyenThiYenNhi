# Nhập một số và tính căn bậc hai số đó
# Nếu nhập số âm,in thông báo lỗi
import math
n = float(input('Nhập một số bất kì:'))
if n < 0:
    print('Không thể tính căn bậc hai của số âm')
else:
    print('Căn bậc hai của số đó là:',math.sqrt(n))