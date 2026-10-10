# def main():
#     print("Hello from schedule-tasks!")


# if __name__ == "__main__":
#     main()





import schedule
import time

def cong_viec_can_lam():
    print("Đang chạy tác vụ tự động...")




# # Lên lịch chạy vào 10:30 sáng mỗi ngày
# schedule.every().day.at("10:30").do(cong_viec_can_lam)



# Lên lịch chạy 3 giây 1 lần
schedule.every(3).seconds.do(cong_viec_can_lam)

# Vòng lặp giữ cho script luôn chạy để kiểm tra lịch
while True:
    schedule.run_pending()
    time.sleep(1)