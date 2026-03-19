# Tạo một 2 class bất kỳ bao gồm
  # constructor
  # getter
  # setter
  # __str__
  # phương thức đối tượng
  # phương thức lớp
  # static method
  # có xác thực thuộc tính sử dụng ValueError bằng 2 cách
  # Nạp chồng toán tử `==`
  # 1 trong 2 class có kế thừa từ class kia
  # Chạy ví dụ in ra màn hình tất cả các thành phần của class ở trên
class MyPham:
    so_luong_kho = 0
    def __init__(self, ten, gia):
        self.ten = ten
        if gia < 0:
            raise ValueError("Giá mỹ phẩm không thể là số âm")
        self._gia = gia
        MyPham.so_luong_kho += 1
    @property
    def gia(self):
        return self._gia
    @gia.setter
    def gia(self, gia_moi):
        if gia_moi < 1000:
            raise ValueError("Giá cập nhật quá thấp, không hợp lệ")
        self._gia = gia_moi
    def thong_tin(self):
        return f"{self.ten} - Giá: {self._gia}đ"
    @classmethod
    def bao_cao_kho(cls):
        return f"Hiện có {cls.so_luong_kho} mặt hàng mỹ phẩm"
    @staticmethod
    def kiem_tra_han_dung(nam_hien_tai, nam_het_han):
        return nam_het_han > nam_hien_tai
    def __str__(self):
        return f"Sản phẩm: {self.ten}"
    def __eq__(self, other):
        if isinstance(other, MyPham):
            return self.ten == other.ten and self._gia == other._gia
        return False
class SonMoi(MyPham):
    def __init__(self, ten, gia, mau_sac):
        super().__init__(ten, gia)
        self.mau_sac = mau_sac
    @property
    def mau_sac(self):
        return self._mau_sac
    @mau_sac.setter
    def mau_sac(self, value):
        if not value:
            raise ValueError("Màu sắc không được để trống")
        self._mau_sac = value
    def thong_tin(self):
        return f"Son {self.ten} - Màu {self.mau_sac} - Giá: {self.gia}đ"
    def __str__(self):
        return f"Son môi: {self.ten} ({self.mau_sac})"
try:
    sp1 = MyPham("Kem chống nắng", 350000)
    sp2 = MyPham("Kem chống nắng", 350000)
    son1 = SonMoi("Rouge G", 850000, "Đỏ thuần")
    print(sp1)
    print(son1)
    print(son1.thong_tin())
    son1.gia = 900000
    print(f"Giá mới của son: {son1.gia}")
    print(MyPham.bao_cao_kho())
    print(f"Còn hạn dùng: {MyPham.kiem_tra_han_dung(2024, 2026)}")
    print(f"So sánh sp1 và sp2: {sp1 == sp2}")
    son1.mau_sac = ""
except ValueError as e:
    print(f"Lỗi: {e}")