def chuan_hoa_ten(ho_ten):
    cac_tu = ho_ten.strip().split()
    ten_chuan_hoa = " ".join(tu.capitalize() for tu in cac_tu)
    return ten_chuan_hoa

def main():
    ds_khach_hang = [
        " nguYen vaN a ", 
        "tRAn tHi b", 
        "  le hoang   NAM  ", 
        "pham  mInh   TuAn "
    ]

    ds_sach = [chuan_hoa_ten(ten) for ten in ds_khach_hang]
    print("Danh sách sau chuẩn hóa:", ds_sach)

    ds_sap_xep = sorted(ds_sach, key=lambda x: x.split()[-1])

    print("\nDanh sách sắp xếp theo Tên (thứ tự bảng chữ cái):")
    for i, ten in enumerate(ds_sap_xep, 1):
        print(f"{i}. {ten}")

if __name__ == "__main__":
    main()