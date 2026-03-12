# Tạo dictionary lưu tên sinh viên làm key và điểm số làm value.
# Viết hàm tính điểm trung bình của các sinh viên (Ví dụ: Nếu có 3 sinh viên thì sẽ tính tổng số điển chia cho 3)
def diem_trung_binh(sinh_vien: dict[str, float]) -> float:
    tong_diem = 0
    so_luong = 0
    for ten, diem in sinh_vien.items():
        tong_diem += diem
        so_luong += 1
    trung_binh = tong_diem / so_luong
    return trung_binh
ds_sinh_vien = {"Nnhuy": 7.5,
                "Thuong": 8.0,
                "Chi": 6.5}
ket_qua = diem_trung_binh(ds_sinh_vien)
print("Điểm trung bình của các sinh viên là:", ket_qua)