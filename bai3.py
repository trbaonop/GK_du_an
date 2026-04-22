
def chuyen_doi_nhiet_do():
    print("\n--- Chuyển đổi Nhiệt độ ---")
    print("1. Độ C sang độ F")
    print("2. Độ F sang độ C")
    
    try:
        chon = input("Chọn loại chuyển đổi (1/2): ")
        gia_tri = float(input("Nhập giá trị cần chuyển đổi: "))
        
        if chon == '1':
            ket_qua = (gia_tri * 9/5) + 32
            print(f"{gia_tri}°C = {ket_qua:.2f}°F")
        elif chon == '2':
            ket_qua = (gia_tri - 32) * 5/9
            print(f"{gia_tri}°F = {ket_qua:.2f}°C")
        else:
            print("Lựa chọn không hợp lệ.")
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập các chữ số cho giá trị nhiệt độ.")

def chuyen_doi_tien_te():
    print("\n--- Chuyển đổi USD sang VND ---")
    try:
        usd = float(input("Nhập số tiền USD: "))
        ty_gia = float(input("Nhập tỷ giá hiện tại (VND/USD): "))
        
        vnd = usd * ty_gia
        print(f"{usd:,.2f} USD tương đương với {vnd:,.0f} VND")
    except ValueError:
        print("Lỗi: Tỷ giá và số tiền phải là định dạng số.")

def main():
    while True:
        print("\n===== CÔNG CỤ CHUYỂN ĐỔI =====")
        print("1. Chuyển đổi Nhiệt độ (C <-> F)")
        print("2. Chuyển đổi Tiền tệ (USD -> VND)")
        print("q. Thoát chương trình")
        
        lua_chon = input("Nhập lựa chọn của bạn: ").lower()
        
        if lua_chon == '1':
            chuyen_doi_nhiet_do()
        elif lua_chon == '2':
            chuyen_doi_tien_te()
        elif lua_chon == 'q':
            print("Cảm ơn bạn đã sử dụng ứng dụng!")
            break
        else:
            print("Lựa chọn không có trong danh sách.")

if __name__ == "__main__":
    main()