# Viết chương trình chuẩn hóa tên người dùng: Loại bỏ khoảng trắng thừa ở hai đầu, giữa các từ chỉ để lại một

name = input('Enter name: ')
words = name.strip().split()
chuanhoaten =' '.join(word.capitalize()for word in words)
print(chuanhoaten)