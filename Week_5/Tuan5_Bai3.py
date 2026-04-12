class CanBo:
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
    def loai_can_bo(self):
        return "Cán bộ"
    def hien_thi(self):
        print(f" Họ tên : {self.ho_ten}")
        print(f" Năm sinh : {self.nam_sinh}")
        print(f" Giới tính : {self.gioi_tinh}")
        print(f" Địa chỉ : {self.dia_chi}")
    
    def __str__(self):
        return f"{self.loai_can_bo()} | Họ tên: {self.ho_ten} | Năm sinh: {self.nam_sinh} | Giới tính: {self.gioi_tinh} | Địa chỉ: {self.dia_chi}"
      
class CongNhan(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        if not (1 <= bac <= 10):
            raise ValueError("Bậc công nhân phải từ 1 đến 10.")
        self.bac = bac
    def loai_can_bo(self):
        return "Công nhân"
    def hien_thi(self):
        print(f"--Công nhân--")
        super().hien_thi()
        print(f" Bậc : {self.bac}")
    
    def __str__(self):
        return f"{super().__str__()} | Bậc: {self.bac}"

class KySu(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao
    def loai_can_bo(self):
        return "Kỹ sư"
    def hien_thi(self):
        print(f"--Kỹ sư--")
        super().hien_thi()
        print(f" Ngành đào tạo : {self.nganh_dao_tao}")
    
    def __str__(self):
        return f"{super().__str__()} | Ngành đào tạo: {self.nganh_dao_tao}"
    
class NhanVienSanXuat(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec
    def loai_can_bo(self):
        return "Nhân viên sản xuất"
    def hien_thi(self):
        print(f"--Nhân viên sản xuất--")
        super().hien_thi()
        print(f" Công việc : {self.cong_viec}")
    
    def __str__(self):
        return f"{super().__str__()} | Công việc: {self.cong_viec}"
    
class QuanLyCanBo:
    def __init__(self):
        self.danh_sach_can_bo = []
    def them_can_bo(self, can_bo):
        print("\n--Thêm cán bộ mới--" )
        print(" 1. Công nhân")
        print(" 2. Kỹ sư")
        print(" 3. Nhân viên sản xuất ")
        loai = input("Chọn loại (1/2.3):").strip()

ho_ten = input("Họ tên: ")
nam_sinh = int(input("Năm sinh: "))
gioi_tinh = input("Giới tính: ")
dia_chi = input("Địa chỉ: ")
 
if loai == "1":
    bac = int(input("Bậc công nhân (1-10): "))
    can_bo = CongNhan(ho_ten, nam_sinh, gioi_tinh, dia_chi, bac)
elif loai == "2":
    nganh_dao_tao = input("Ngành đào tạo: ")
    can_bo = KySu(ho_ten, nam_sinh, gioi_tinh, dia_chi, nganh_dao_tao)
elif loai == "3":
    cong_viec = input("Công việc: ")
    can_bo = NhanVienSanXuat(ho_ten, nam_sinh, gioi_tinh, dia_chi, cong_viec)
else:
    print("Lựa chọn không hợp lệ.") 

    exit(1)
      
self.danh_sach_can_bo.append(can_bo)
print("\n--Danh sách cán bộ sau khi thêm--")
def tim_kiem(self):
    tu_khoa - input("\n Nhập họ tên cần tìm: ").strip().lower()
    ket_qua = [cb for cb in self.danh_sach_can_bo if tu_khoa in cb.ho_ten.lower()]
    if tu_khoa in cb.ho_ten.lower():
        print("\n--Kết quả tìm kiếm--")
        for cb in ket_qua:
            print(cb)
            cb.hien_thi()

def hien_thi_danh_sach(self):
    if not self.danh_sach_can_bo:
        print("\nDanh sách cán bộ trống.")
        return
    print("\n--Danh sách cán bộ--")
    for cb in self.danh_sach_can_bo:
        print(cb)
        cb.hien_thi()
def chay(self):
    while True:
        print("\n===== QUẢN LÝ CÁN BỘ =====")
        print("1. Thêm cán bộ")
        print("2. Tìm kiếm cán bộ theo họ tên")
        print("3. Hiển thị danh sách cán bộ")
        print("4. Thoát")
        choice = input("Chọn chức năng (1-4): ").strip()
        if choice == "1":
            self.them_can_bo()
        elif choice == "2":
            self.tim_kiem()
        elif choice == "3":
            self.hien_thi_danh_sach()
        elif choice == "4":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
if __name__ == "__main__":
    qlcb = QuanLyCanBo()
    qlcb.chay()
    