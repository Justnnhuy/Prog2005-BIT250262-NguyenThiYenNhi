# Tạo lớp Product với thuộc tính _price và getter/setter kiểm tra giá > 0. Viết hàm __str__ để in thông tin price của product.
class Product:
    def __init__(self, price):
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Giá sản phầm không thể là âm một số âm")
    def __str__(self):
        return f"Product(price={self._price})"
try:
    pricee = Product(36)
    print(f"Giá sản phẩm: {pricee.price}")
    print(pricee)
    pricee.price =-10
except ValueError as e:
    print(e)