from abc import ABC, abstractmethod
from datetime import datetime


class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, don_gia, so_luong):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.don_gia = don_gia
        self.so_luong = so_luong

    @property
    def don_gia(self):
        return self._don_gia

    @don_gia.setter
    def don_gia(self, value):
        if value < 0:
            raise ValueError("Đơn giá phải >= 0")
        self._don_gia = value

    @property
    def so_luong(self):
        return self._so_luong

    @so_luong.setter
    def so_luong(self, value):
        if value < 0:
            raise ValueError("Số lượng phải >= 0")
        self._so_luong = value

    def thanh_tien(self):
        return self.don_gia * self.so_luong

    def __lt__(self, other):
        return self.thanh_tien() < other.thanh_tien()

    @abstractmethod
    def danh_gia(self):
        pass

    def __str__(self):
        return f"{self.ma_hang} | {self.ten_hang} | {self.don_gia} | {self.so_luong} | {self.thanh_tien()}"


class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, don_gia, so_luong, bao_hanh, cong_suat):
        super().__init__(ma_hang, ten_hang, don_gia, so_luong)
        self.bao_hanh = bao_hanh
        self.cong_suat = cong_suat

    def danh_gia(self):
        return "Bán tốt" if self.so_luong < 3 else "Bình thường"

    def __str__(self):
        return super().__str__() + f" | Bảo hành: {self.bao_hanh} | Công suất: {self.cong_suat}"

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, don_gia, so_luong, nha_sx, ngay_nhap):
        super().__init__(ma_hang, ten_hang, don_gia, so_luong)
        self.nha_sx = nha_sx
        self.ngay_nhap = datetime.strptime(ngay_nhap, "%d/%m/%Y")

    def danh_gia(self):
        days = (datetime.now() - self.ngay_nhap).days
        return "Bán chậm" if self.so_luong > 50 and days > 10 else "Bình thường"

    def __str__(self):
        return super().__str__() + f" | NSX: {self.nha_sx} | Ngày nhập: {self.ngay_nhap.strftime('%d/%m/%Y')}"


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, don_gia, so_luong, ngay_sx, ngay_hh):
        super().__init__(ma_hang, ten_hang, don_gia, so_luong)
        self.ngay_sx = datetime.strptime(ngay_sx, "%d/%m/%Y")
        self.ngay_hh = datetime.strptime(ngay_hh, "%d/%m/%Y")

        if self.ngay_hh < self.ngay_sx:
            raise ValueError("Hạn sử dụng phải sau ngày sản xuất")

    def danh_gia(self):
        if datetime.now() > self.ngay_hh:
            return "Hết hạn"
        return "Còn hạn"

    def __str__(self):
        return super().__str__() + f" | NSX: {self.ngay_sx.strftime('%d/%m/%Y')} | HSD: {self.ngay_hh.strftime('%d/%m/%Y')}"


class QuanLyHangHoa:
    def __init__(self):
        self.ds = []

    def them(self, hang):
        self.ds.append(hang)

    def hien_thi(self):
        for h in self.ds:
            print(h, "| Đánh giá:", h.danh_gia())

    def tim_kiem(self, ten):
        kq = [h for h in self.ds if ten.lower() in h.ten_hang.lower()]
        return kq

    def sap_xep(self):
        self.ds.sort()  


if __name__ == "__main__":
    ql = QuanLyHangHoa()

    try:
        ql.them(HangDienMay("DM01", "Tivi", 5000, 2, 12, 100))
        ql.them(HangSanhSu("SS01", "Chén", 20, 60, "Bát Tràng", "01/03/2024"))
        ql.them(HangThucPham("TP01", "Sữa", 30, 10, "01/04/2024", "01/05/2024"))

        print("\n--- DANH SÁCH ---")
        ql.hien_thi()

        print("\n--- SẮP XẾP ---")
        ql.sap_xep()
        ql.hien_thi()

    except Exception as e:
        print("Lỗi:", e)