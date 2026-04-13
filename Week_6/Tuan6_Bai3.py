class MauSoBangKhong(Exception):
    def __init__(self, message="Mẫu số không được bằng 0"):
        self.message = message
        super().__init__(self.message)

class PhanSo:
    def __init__(self, tu_so, mau_so):
        if mau_so == 0:
            raise MauSoBangKhong()
        self.tu_so = tu_so
        self.mau_so = mau_so

    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"
@property
def tu_so(self):
    return self._tu_so
@tu_so.setter
def tu_so(self, value):
    self._tu_so = value
@property
def mau_so(self):
    return self._mau_so
@mau_so.setter
def mau_so(self, value):
    if value == 0:
        raise MauSoBangKhong()
    self._mau_so = value
def toi_gian(self):
    g = gcd(abs(self.tu_so), abs(self.mau_so))
    tu_so = self.tu_so // g
    mau_so = self.mau_so // g
    if mau_so < 0:
        tu_so = -tu_so
        mau_so = -mau_so
    return PhanSo(tu_so, mau_so)
def is_toi_gian(self):
    return gcd(self.tu_so, abs(self.mau_so)) == 1
def __add__(self, other):
    """ps1 + ps2: a/b +c/d = (a*d + b*c) / (b*d)"""
    tu_so = self.tu_so * other.mau_so + self.mau_so * other.tu_so
    mau_so = self.mau_so * other.mau_so
    return PhanSo(tu_so, mau_so).toi_gian()
def __sub__(self, other):
    """ps1 - ps2: a/b - c/d = (a*d - b*c) / (b*d)"""
    tu_so = self.tu_so * other.mau_so - self.mau_so * other.tu_so
    mau_so = self.mau_so * other.mau_so
    return PhanSo(tu_so, mau_so).toi_gian()
def __mul__(self, other):
    """ps1 * ps2: a/b * c/d = (a*c) / (b*d)"""
    return PhanSo(
        self.tu_so * other.tu_so,
        self.mau_so * other.mau_so
    ).toi_gian()
def __truediv__(self, other):
    """ps1 / ps2: a/b / c/d = (a*d) / (b*c)"""
    if other.tu_so == 0:
        raise MauSoBangKhong("Không thể chia cho phân số có tử số bằng 0")
    return PhanSo(
        self.tu_so * other.mau_so,
        self.mau_so * other.tu_so
    ).toi_gian()
def __eq__(self, other):
    a = self.tu_so * other.mau_so
    b = self.mau_so * other.tu_so
    return a.tu_so == b.tu_so and a.mau_so == b.mau_so
def __lt__(self, other):
    return self.tu_so * other.mau_so < self.mau_so * other.tu_so
def __gt__(self, other):
    return self.tu_so * other.mau_so > self.mau_so * other.tu_so
def __hash__(self):
    r = self.toi_gian()
    return hash((r.tu_so, r.mau_so))
def __str__(self):
    if self.mau_so == 1:
        return str(self.tu_so)
    return f"{self.tu_so}/{self.mau_so}"
def __repr__(self):
    return f"PhanSo({self.tu_so}, {self.mau_so})"

ds = [PhanSo(1, 2), PhanSo(2, 4), PhanSo(3, 6), PhanSo(1, 3)]
print("Danh sách phân số:")
for ps in ds:
    tg = ps.toi_gian()
    print(f"{ps} -> {tg} | Tối giản: {'Có' if ps.is_toi_gian() else 'Không'}")
print("\nPhép toán:")
print("\n--Phép toán--")
ps_a = PhanSo(1, 2)
ps_b = PhanSo(1, 3)
print(f"{ps_a} + {ps_b} = {ps_a + ps_b}")
print(f"{ps_a} - {ps_b} = {ps_a - ps_b}")
print(f"{ps_a} * {ps_b} = {ps_a * ps_b}")
print(f"{ps_a} / {ps_b} = {ps_a / ps_b}")

print("\n--Sắp xếp tăng dần--")
for ps in sorted(ds):
    tg = ps.toi_gian()
    print(f"{tg} ={ps.tu_so}/{ps.mau_so:.4f}")
print("\n--So sánh--")
print(f" 2/4 == 1/2: {PhanSo(2, 4) == PhanSo(1, 2)}")
print(f" 1/3 < 1/2: {PhanSo(1, 3) < PhanSo(1, 2)}")
print(f" 1/3 > 1/2: {PhanSo(1, 3) > PhanSo(1, 2)}")
print("\n--Loại trùng (set)--")
ds2 = [PhanSo(1, 2), PhanSo(2, 4), PhanSo(3, 6), PhanSo(1, 3)]
unique = list(set(ds2))
print(f" Trước: {[str(p) for p in ds2]}")
print(f" Sau: {[str(p) for p in unique]}")
print("\n--Validation--")
try:
    ps_invalid = PhanSo(1, 0)
except MauSoBangKhong as e:
    print(f"Lỗi: {e}")
