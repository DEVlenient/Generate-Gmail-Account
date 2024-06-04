import random
import string
import tkinter as tk
from tkinter import ttk

def generate_gmail_account():
    num_credentials = int(num_credentials_entry.get())
    email_length = int(email_length_entry.get())
    password_length = int(password_length_entry.get())

    output_text.delete(1.0, tk.END)

    for i in range(1, num_credentials + 1):
        random_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length)) + "@gmail.com"
        random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
        output_text.insert(tk.END, f"{i}. 帳號: {random_email}, 密碼: {random_password}\n")

# 建立主視窗
root = tk.Tk()
root.title("Gmail 帳號生成器")

# 輸入框和標籤
num_credentials_label = ttk.Label(root, text="帳號數量:")
num_credentials_entry = ttk.Entry(root)

email_length_label = ttk.Label(root, text="帳號長度:")
email_length_entry = ttk.Entry(root)

password_length_label = ttk.Label(root, text="密碼長度:")
password_length_entry = ttk.Entry(root)

# 生成按鈕
generate_button = ttk.Button(root, text="生成", command=generate_gmail_account)

# 輸出框
output_text = tk.Text(root, height=10, width=50)

# 佈局
num_credentials_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
num_credentials_entry.grid(row=0, column=1, padx=5, pady=5)

email_length_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
email_length_entry.grid(row=1, column=1, padx=5, pady=5)

password_length_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
password_length_entry.grid(row=2, column=1, padx=5, pady=5)

generate_button.grid(row=3, column=0, columnspan=2, pady=10)

output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# 啟動主視窗
root.mainloop()
