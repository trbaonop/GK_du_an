def nhap_du_lieu():
    """Hàm xử lý việc nhập dữ liệu từ bàn phím vào danh sách."""
    danh_sach = []
    print("--- Nhập danh sách chi tiêu (Gõ 'q' để dừng) ---")
    while True:
        ten_mon = input("Nhập tên món hàng: ")
        if ten_mon.lower() == 'q':
            break
        try:
            gia_tien = float(input(f"Nhập giá tiền cho '{ten_mon}': "))
            danh_sach.append({"ten": ten_mon, "gia": gia_tien})
        except ValueError:
            print("Lỗi: Vui lòng nhập giá tiền là một con số.")
    return danh_sach


def xuat_file(tong, mon_dat_nhat, ds, filename="ket_qua_chi_tieu.txt"):
    """Xuất kết quả thu được ra một file .txt."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== BÁO CÁO CHI TIÊU ===\n")
        f.write(f"Tổng số tiền đã chi: {tong:,.0f} VNĐ\n")
        f.write("Các món hàng đã chi tiêu:\n")
        for item in ds:
            f.write(f"  - {item['ten']}: {item['gia']:,.0f} VNĐ\n")
        if mon_dat_nhat:
            f.write(f"Món hàng đắt nhất: {mon_dat_nhat['ten']} ({mon_dat_nhat['gia']:,.0f} VNĐ)\n")
    print(f"\nĐã xuất kết quả thành công ra file: {filename}")

def main():
    ds = nhap_du_lieu()
    if ds:
        tong = sum(item['gia'] for item in ds)
        dat_nhat = max(ds, key=lambda x: x['gia'])
        print(f"\nTổng chi tiêu: {tong:,.0f} VNĐ")
        print(f"các mon hàng đã chi tiêu:")
        for item in ds:
            print(f"  - {item['ten']}: {item['gia']:,.0f} VNĐ")
        print(f"Món hàng đắt nhất: {dat_nhat['ten']}")
        xuat_file(tong, dat_nhat, ds)
    else:
        print("Danh sách trống, không có dữ liệu để xử lý.")

if __name__ == "__main__":
    main()