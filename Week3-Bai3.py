class NhanVien:
    LUONG_MAX = 50_000_000  # Class variable (static)

    def __init__(self, ten_nhan_vien: str,
                 luong_co_ban: float, he_so_luong: float):
        self.__tenNhanVien  = ten_nhan_vien
        self.__luongCoBan   = luong_co_ban
        self.__heSoLuong    = he_so_luong

    # ── Getter / Setter ─────────────────────────────────
    @property
    def tenNhanVien(self): return self.__tenNhanVien

    @tenNhanVien.setter
    def tenNhanVien(self, value):
        if not value.strip():
            raise ValueError("Tên không được rỗng!")
        self.__tenNhanVien = value

    @property
    def luongCoBan(self): return self.__luongCoBan

    @luongCoBan.setter
    def luongCoBan(self, value):
        if value < 0:
            raise ValueError("Lương không được âm!")
        self.__luongCoBan = value

    @property
    def heSoLuong(self): return self.__heSoLuong

    @heSoLuong.setter
    def heSoLuong(self, value):
        if value <= 0:
            raise ValueError("Hệ số lương phải > 0!")
        self.__heSoLuong = value

    # ── Phương thức nghiệp vụ ────────────────────────────
    def tinhLuong(self) -> float:
        return self.__luongCoBan * self.__heSoLuong

    def inTTin(self):
        luong = self.tinhLuong()
        print(f"""
╔══════════════════════════════════════╗
║        THÔNG TIN NHÂN VIÊN           ║
╠══════════════════════════════════════╣
║ Tên       : {self.__tenNhanVien:<25}║
║ Lương CB  : {self.__luongCoBan:>20,.0f} VNĐ ║
║ Hệ số     : {self.__heSoLuong:>25.1f} ║
║ Lương TT  : {luong:>20,.0f} VNĐ ║
╚══════════════════════════════════════╝""")

    def tangLuong(self, delta: float) -> bool:
        luong_moi = (self.__luongCoBan + delta) * self.__heSoLuong
        if luong_moi > NhanVien.LUONG_MAX:
            print(f"⚠️  Lương mới ({luong_moi:,.0f}) vượt LUONG_MAX. Không tăng!")
            return False
        self.__luongCoBan += delta
        print(f"✅ Đã tăng lương! Lương mới: {self.tinhLuong():,.0f} VNĐ")
        return True


nv = NhanVien("Tran Van A", 10_000_000, 3.0)
nv.inTTin()
nv.tangLuong(5_000_000)   # → 45M < 50M: OK
nv.tangLuong(10_000_000)  # → 75M > 50M: Cảnh báo
