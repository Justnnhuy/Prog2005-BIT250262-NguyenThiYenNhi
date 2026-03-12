# Viết chương trình kiểm tra một key có tồn tại trong dictionary hay không.
def kiem_tra_key(sinh_vien: dict[str, float], key: str) -> bool:
    for ten, diem in sinh_vien.items():
        if ten == key:
            return True
    return False
# Ví dụ:
ds_sinh_vien = {"Nnhuy": 7.5,
                "Thuong": 8.0,
                "Chi": 6.5}
print("Có Nnhuy không?", kiem_tra_key(ds_sinh_vien, "Nnhuy"))
print("Có Lan không?", kiem_tra_key(ds_sinh_vien, "Lan"))