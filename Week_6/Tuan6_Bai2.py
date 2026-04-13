from abc import ABC, abstractmethod

class TuoiKhongHopLe(Exception):
    def __init__(self, tuoi):
        self.tuoi = tuoi
        super().__init__(f"Tuổi {tuoi} không hợp lệ. (18-70)")

class BacKhongHopLe(Exception):
    def __init__(self, bac):
        self.bac = bac
        super().__init__(f"Bậc {bac} không hợp lệ. (1-10)")

class CanBo(ABC):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    @property
    def ho_ten(self):
        return self._ho_ten
    @property
    def gioi_tinh(self):
        return self._gioi_tinh
    @property
    def dia_chi(self):
        return self._dia_chi
    @property
    def tuoi(self):
        return self.nam_sinh
    @tuoi.setter
    def tuoi(self, value):
        if value < 18 or value > 70:
            raise TuoiKhongHopLe(value)
        self.nam_sinh = value

    @abstractmethod
    def mo_ta(self):
        pass
    def __str__(self):
        return (f"{self.ho_ten} / {self.nam_sinh} / {self.gioi_tinh} / {self.dia_chi}")
    def __repr__(self):
        return f"{self.__class__.__name__}({self.ho_ten}',{self.nam_sinh},'{self.gioi_tinh}','{self.dia_chi}')"
    def __eq__(self, other):
        if not isinstance(other, CanBo):
            return NotImplemented
        return self.ho_ten == other.ho_ten and self.nam_sinh == other.nam_sinh
    def __lt__(self, other):
        return self.ho_ten < other.ho_ten
    def __hash__(self):
        return hash((self.ho_ten, self.nam_sinh))
    
class CongNhan(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.bac = bac
    @property
    def bac(self):
        return self._bac
    @bac.setter
    def bac(self, value):
        if value < 1 or value > 10:
            raise BacKhongHopLe(value)
        self._bac = value
    def mo_ta(self):
        return f"Công nhân bậc {self.bac}"
    
class KySu(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao
    def mo_ta(self):
        return f"Kỹ sư ngành {self.nganh_dao_tao}"

class NhanVienSanXuat(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec
    def mo_ta(self):
        return f"Nhân viên sản xuất công việc {self.cong_viec}"
    
ds = [CongNhan("Nguyen Xuan A", 1990, "Nam", "Hanoi", 5),
      KySu("Tran Ngoc B", 1985, "Nu", "HCM", "CNTT"),
      NhanVienSanXuat("Pham Van C", 1995, "Nam", "Da Nang", "Lắp ráp")]

print("--Đa hình: 1 vòng lặp, 3 loại Cán bộ--")
for cb in ds:
    print(cb)
    print("\n-- Sắp xếp theo tên (A-Z) --")
    for cb in sorted(ds):
        print(f"{cb.ho_ten}")
    print("\n-- Validation --")
    try:
        CongNhan("X", 1990, "Nam", "Hanoi", 5)  # Tuổi không hợp lệ
        print(f"{e}")
    except TuoiKhongHopLe as e:
        print(f"{e}")
    try:
        CongNhan("Y", 1990, "Nam", "Hanoi", 15)  # Bậc không hợp lệ
        print(f"{e}")
    except BacKhongHopLe as e:
        print(f"{e}")
    print("\n-- Lưu file --")
    with open("can_bo.txt", "w") as f:
        for cb in ds:
            f.write(str(cb) + "\n")
    print(f"Đã lưu {len(ds)} cán bộ ")
