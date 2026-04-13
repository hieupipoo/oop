import math

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def hien_thi(self):
        print(f"Điểm ({self.x}, {self.y})")

    def doi_xung_qua_O(self):
        # Điểm đối xứng qua gốc O: (-x, -y)
        return Point(-self.x, -self.y)

    def khoang_cach_den_O(self):
        return math.sqrt(self.x**2 + self.y**2)

    def khoang_cach_den(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

A = Point(3, 4)
print("Điểm A:"); A.hien_thi()

xb = int(input("Nhập x của B: "))
yb = int(input("Nhập y của B: "))
B = Point(xb, yb)
print("Điểm B:"); B.hien_thi()

C = B.doi_xung_qua_O()
print("Điểm C (đối xứng B qua O):"); C.hien_thi()

print(f"Khoảng cách B đến O: {B.khoang_cach_den_O():.2f}")

print(f"Khoảng cách A đến B: {A.khoang_cach_den(B):.2f}")


class SieuNhan:
    def __init__(self, ten: str, vu_khi: str, mau_sac: str):
        self.ten     = ten
        self.vu_khi  = vu_khi
        self.mau_sac = mau_sac

    def __str__(self):
        return (f"Siêu nhân {self.ten} | "
                f"Vũ khí: {self.vu_khi} | "
                f"Màu sắc: {self.mau_sac}")


sieu_nhan_A = SieuNhan("A", "kiếm", "đỏ")
sieu_nhan_B = SieuNhan("B", "khiên", "xanh")

print(sieu_nhan_A)
print(sieu_nhan_B)


class SieuNhan:
    def __init__(self, ten="", vu_khi="", mau_sac="", suc_manh=0):
        self.ten      = ten
        self.vu_khi   = vu_khi
        self.mau_sac  = mau_sac
        self.suc_manh = suc_manh

    def __str__(self):
        return (f"  ✦ {self.ten:10} | Vũ khí: {self.vu_khi:8} | "
                f"Màu: {self.mau_sac:8} | Sức mạnh: {self.suc_manh}")


danh_sach = []
print("=== NHẬP DANH SÁCH SIÊU NHÂN ===")
print("(Nhấn Enter để kết thúc)\n")

while True:
    ten = input("Tên siêu nhân: ")
    if ten == "":
        break
    vu_khi  = input("Vũ khí: ")
    mau_sac = input("Màu sắc: ")
    suc_manh = int(input("Sức mạnh (1-100): "))
    danh_sach.append(SieuNhan(ten, vu_khi, mau_sac, suc_manh))
    print(f"  → Đã thêm {ten}!\n")

print(f"\n=== DANH SÁCH {len(danh_sach)} SIÊU NHÂN ===")
for i, sn in enumerate(danh_sach, 1):
    print(f"{i}.", sn)