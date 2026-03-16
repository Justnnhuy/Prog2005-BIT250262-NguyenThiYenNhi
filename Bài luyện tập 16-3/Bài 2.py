# Yêu cầu người dùng nhập vào một số và tính tổng các chữ số của số đó.

number = input('Nhâp một chữ số: ')
sum =sum(int(n) for n in number)
print('Tổng các chữ số đó là:',sum)