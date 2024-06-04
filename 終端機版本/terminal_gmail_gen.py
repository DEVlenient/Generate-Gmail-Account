import random
import string

def generate_gmail_account():
    # 檢查帳號數量
    while True:
        try:
            num_credentials = int(input("請輸入要生成的帳號數量 (1-100): "))
            if 1 <= num_credentials <= 100:
                break
            else:
                print("請輸入1到100之間的數字。")
        except ValueError:
            print("請輸入整數。")

    # 檢查帳號長度
    while True:
        try:
            email_length = int(input("請輸入每個帳號的長度: "))
            if email_length > 0:
                break
            else:
                print("帳號長度應該是正整數。")
        except ValueError:
            print("請輸入整數。")

    # 檢查密碼長度
    while True:
        try:
            password_length = int(input("請輸入每個密碼的長度: "))
            if password_length > 0:
                break
            else:
                print("密碼長度應該是正整數。")
        except ValueError:
            print("請輸入整數。")

    # 生成帳號和密碼
    for i in range(1, num_credentials + 1):
        random_email = ''
        for _ in range(email_length):
            random_email += random.choice(string.ascii_lowercase + string.digits)
        random_email += "@gmail.com"

        random_password = ''
        for _ in range(password_length):
            random_password += random.choice(string.ascii_letters + string.digits)

        print(f"{i}. 帳號: {random_email}, 密碼: {random_password}")

# 呼叫生成器函數
generate_gmail_account()