import random

def doc_ky_luc(filename="ky_luc.txt"):
    try:
        with open(filename, "r") as f:
            return int(f.read())
    except FileNotFoundError:
        with open(filename, "w") as f:
            f.write("")
        return None
    except ValueError:
        return None 

def luu_ky_luc(so_lan_doan, filename="ky_luc.txt", so_luot_choi=None):

    ky_luc_cu = doc_ky_luc(filename)
    if ky_luc_cu is None or so_lan_doan < ky_luc_cu:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(so_lan_doan))
            if so_luot_choi is not None:
                f.write(f"\nSố lượt chơi đã sử dụng: {so_luot_choi}")
        return True
    return False

def cung_cap_goi_y(so_can_tim, luot_hien_tai):
    # Tính năng gợi ý: Thông báo chẵn/lẻ ở lượt thứ 3.
    if luot_hien_tai == 3:
        loai = "Chẵn" if so_can_tim % 2 == 0 else "Lẻ"
        print(f"Gợi ý: Số cần tìm là một số {loai}.")

def main():
    so_can_tim = random.randint(1, 100)
    so_luot_toi_da = 7
    da_thang = False

    print("=== TRÒ CHƠI ĐOÁN SỐ (1 - 100) ===")
    print(f"Bạn có tối đa {so_luot_toi_da} lượt để tìm ra con số may mắn.")

    ky_luc_hien_tai = doc_ky_luc()
    if ky_luc_hien_tai:
        print(f"Kỷ lục hiện tại: {ky_luc_hien_tai} lần đoán.")

    for luot in range(1, so_luot_toi_da + 1):
        try:
            doan = int(input(f"\nLượt {luot}: Nhập số bạn đoán: "))

            if doan == so_can_tim:
                print(f"Chúc mừng! Bạn đã đoán đúng số {so_can_tim} ở lượt thứ {luot}!")
                da_thang = True
                if luu_ky_luc(luot):
                    print("Tuyệt vời! Bạn đã thiết lập kỷ lục mới!")
                break
            

            if doan < so_can_tim:
                print("Số cần tìm LỚN HƠN số bạn vừa đoán.")
            else:
                print("Số cần tìm NHỎ HƠN số bạn vừa đoán.")
            cung_cap_goi_y(so_can_tim, luot)

        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")


    if not da_thang:
        print(f"\nGame Over! Rất tiếc, số đúng là: {so_can_tim}. Chúc bạn may mắn lần sau!")

if __name__ == "__main__":
    main()