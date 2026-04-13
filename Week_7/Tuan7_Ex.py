import json

class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, loai):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.loai = loai

    def to_dict(self):
        return {
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "gioi_tinh": self.gioi_tinh,
            "dia_chi": self.dia_chi,
            "loai": self.loai
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            ho_ten=data["ho_ten"],
            tuoi=data["tuoi"],
            gioi_tinh=data["gioi_tinh"],
            dia_chi=data["dia_chi"],
            loai=data["loai"],
        )

    def __str__(self):
        return f"{self.ho_ten}, {self.tuoi} tuổi, {self.gioi_tinh}, sống tại {self.dia_chi}, loại: {self.loai}"


danh_sach = [
    CanBo("Nguyen Van A", 30, "Nam", "Hanoi", "CongNhan"),
    CanBo("Tran Thi B", 25, "Nu", "HCM", "KySu"),
    CanBo("Le Van C", 40, "Nam", "Danang", "NhanVien"),
]

data = [can_bo.to_dict() for can_bo in danh_sach]
with open("can_bo.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with open("can_bo.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

danh_sach_loaded = [CanBo.from_dict(item) for item in raw]

for can_bo in danh_sach_loaded:
    print(can_bo)
     
    