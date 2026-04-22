import matplotlib.pyplot as plt

def main():
    du_lieu_ban_hang = {'Laptop': 10, 'Mouse': 50, 'Keyboard': 30}
    bang_gia = {
        'Laptop': 25000000, 
        'Mouse': 500000, 
        'Keyboard': 1200000
    }

    doanh_thu_tung_mon = {mon: du_lieu_ban_hang[mon] * bang_gia[mon] for mon in du_lieu_ban_hang}
    tong_doanh_thu = sum(doanh_thu_tung_mon.values())

    print("=== BÁO CÁO DOANH THU BÁN HÀNG ===")
    for mon, doanh_thu in doanh_thu_tung_mon.items():
        print(f"- {mon}: {doanh_thu:,.0f} VND")
    print(f"\n=> TỔNG DOANH THU: {tong_doanh_thu:,.0f} VND")
    print("-" * 35)

    ten_san_pham = list(du_lieu_ban_hang.keys())
    so_luong_ban = list(du_lieu_ban_hang.values())

    plt.figure(figsize=(8, 5))
    plt.bar(ten_san_pham, so_luong_ban, color=['skyblue', 'lightgreen', 'salmon'])
    plt.xlabel('Sản phẩm')
    plt.ylabel('Số lượng đã bán')
    plt.title('BIỂU ĐỒ SỐ LƯỢNG SẢN PHẨM ĐÃ BÁN')
    plt.show()

if __name__ == "__main__":
    main()