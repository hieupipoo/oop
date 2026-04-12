class NhanVien:
    def __init__(self, ma_nv, ten_nv, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh 
        self.dia_chi = dia_chi
        self.he_so_luong = he_so_luong
        self.luong_toi_da = luong_toi_da
    def tinh_luong(self):
        return self.he_so_luong * self.luong_toi_da
    def xuat_thong_tin(self):
        return f"{self.ma_nv} | {self.ten_nv} | {self.nam_sinh} | {self.gioi_tinh} | {self.dia_chi} | HSL: {self.he_so_luong} | Lương tối đa: {self.luong_toi_da:,} VNĐ | Lương thực tế: {self.tinh_luong():,} VNĐ"
    
class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ten_nv, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, so_gio_cong_tac):
        super().__init__(ma_nv, ten_nv, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.thoi_han_hop_dong = self.thoi_han_hop_dong
        self.phu_cap = self.phu_cap

    def tinh_luong(self):
        return super().tinh_luong() + self.phu_cap
    def xuat_thong_tin(self):
        return f"[CTV] {super().xuat_thong_tin()} // HĐ : {self.thoi_han_hop_dong} tháng | Phụ cấp: {self.phu_cap:,} VNĐ"

class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ten_nv, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, ngay_vao_lam):
        super().__init__(ma_nv, ten_nv, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.vi_tri_cong_viec = self.vi_tri_cong_viec
    
    def tinh_luong(self):
        return self.he_so_luong * self.luong_toi_da
    def xuat_thong_tin(self):
        return f"[NV chính thức] {super().xuat_thong_tin()} // Vị trí công việc: {self.vi_tri_cong_viec}"
    
class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ten_nv, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, phong_ban):
        super().__init__(ma_nv, ten_nv, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.phong_ban = phong_ban
        self.__ngay_bat_dau_ql = self.__ngay_bat_dau_ql
        self.__phu_cap = self.__phu_cap
    def tinh_luong(self):
        return super().tinh_luong() + self.__phu_cap
    def xuat_thong_tin(self):
        return f"[Trưởng phòng] {super().xuat_thong_tin()} // Phòng ban: {self.phong_ban} | Ngày bắt đầu quản lý: {self.__ngay_bat_dau_ql} | Phụ cấp: {self.__phu_cap:,} VNĐ"
    

class PhongBan:
    def __init__(self, ten_phong):
        self.ten_phong = ten_phong
        self.ds_nhan_vien = []

    def them_nhan_vien(self, nv):
        self.ds_nhan_vien.append(nv)

    def hien_thi_danh_sach(self):
        print(f"\n===== PHÒNG BAN: {self.ten_phong.upper()} =====")
        for stt, nv in enumerate(self.ds_nhan_vien, 1):
            print(f"{stt}. {nv.xuat_thong_tin()}")


if __name__ == "__main__":
    phong_it = PhongBan("Công nghệ thông tin")

    phong_it.them_nhan_vien(CongTacVien("CTV01", "Nguyễn Văn A", 1990, "Nam", "65 Van Bao, Ba Dinh, Ha Noi", 1.5, 5000000, 6, 1000000))
    phong_it.them_nhan_vien(NhanVienChinhThuc("NV01", "Trần Thị B", 1985, "Nữ", "123 Nguyen Trai, Thanh Xuan, Ha Noi", 2.0, 7000000, "Lập trình viên"))
    phong_it.them_nhan_vien(TruongPhong("TP01", "Lê Văn C", 1980, "Nam", "456 Le Loi, District 5, Ho Chi Minh City", 2.5, 12000000, "Phòng Kinh Doanh"))

    phong_it.hien_thi_danh_sach()