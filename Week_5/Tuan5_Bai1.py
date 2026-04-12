class HangHoa:
    def __init__(self, ma_hang, ten_hang, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.gia = gia

    def xuat_thong_tin(self):
        return f"Mã: {self.ma_hang} | Tên: {self.ten_hang} | Giá: {self.gia:,} VNĐ"


class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, gia)
        self.bao_hanh = bao_hanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def xuat_thong_tin(self):
        return (
            f"[Điện máy] {super().xuat_thong_tin()} | "
            f"BH: {self.bao_hanh} tháng | {self.dien_ap}V | {self.cong_suat}W"
        )


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, loai_nguyen_lieu, xuat_xu):
        super().__init__(ma_hang, ten_hang, gia)
        self.loai_nguyen_lieu = loai_nguyen_lieu
        self.xuat_xu = xuat_xu

    def xuat_thong_tin(self):
        return (
            f"[Sành sứ] {super().xuat_thong_tin()} | "
            f"Nguyên liệu: {self.loai_nguyen_lieu} | Xuất xứ: {self.xuat_xu}"
        )


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, ngay_sx, ngay_hh, nhiet_do_bao_quan):
        super().__init__(ma_hang, ten_hang, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hh = ngay_hh
        self.nhiet_do_bao_quan = nhiet_do_bao_quan

    def xuat_thong_tin(self):
        return (
            f"[Thực phẩm] {super().xuat_thong_tin()} | "
            f"NSX: {self.ngay_sx} | HSD: {self.ngay_hh} | "
            f"Bảo quản: {self.nhiet_do_bao_quan}°C"
        )


class QuanLyKho:
    def __init__(self):
        self.danh_sach = []

    def them_hang(self, hang):
        self.danh_sach.append(hang)

    def hien_thi_tat_ca(self):
        print("\n===== DANH SÁCH HÀNG HÓA =====")
        for i, hang in enumerate(self.danh_sach, 1):
            print(f"{i}. {hang.xuat_thong_tin()}")


if __name__ == "__main__":
    kho = QuanLyKho()

    kho.them_hang(HangDienMay("DM01", "Máy giặt", 8500000, 24, 220, 1800))
    kho.them_hang(HangSanhSu("SS01", "Lọ hoa", 450000, "Gốm sứ Bát Tràng", "Hà Nội"))
    kho.them_hang(HangThucPham("TP01", "Sữa chua", 30000, "10/04/2026", "20/04/2026", 5))

    kho.hien_thi_tat_ca()


kho.hien_thi_tat_ca()