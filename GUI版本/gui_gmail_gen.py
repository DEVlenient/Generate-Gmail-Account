import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

def generate_gmail_account():
    try:
        num_credentials = int(num_credentials_entry.get())
        email_length = int(email_length_entry.get())
        password_length = int(password_length_entry.get())
        
        if num_credentials < 1 or num_credentials > 100:
            raise ValueError("帳號數量必須介於 1 和 100 之間")
        if email_length < 6 or email_length > 30:
            raise ValueError("帳號長度必須介於 6 和 30 個半形字元之間")
        if password_length < 8 or password_length > 100:
            raise ValueError("密碼長度必須介於 8 和 100 個半形字元之間")
    except ValueError as e:
        messagebox.showerror("錯誤", str(e))
        return

    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)

    # 設定放大後的字型大小
    output_text.tag_configure("big", font=("Courier", 12))

    for i in range(1, num_credentials + 1):
        random_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length)) + "@gmail.com"
        random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
        output_text.insert(tk.END, f"{i}. 帳號: {random_email}\n   密碼: {random_password}\n\n", "big")
    
    output_text.config(state=tk.DISABLED)

# 建立主視窗
root = tk.Tk()
root.title("Gmail 帳號生成器")
root.configure(bg="#f0f0f0")

# 設置全局字體樣式和顏色
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0", foreground="#333333")
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12, "bold"), background="#4CAF50", foreground="white")
style.map("TButton", background=[("active", "#45a049")])

# 設置窗體最小大小
root.minsize(800, 600)

# 創建主框架
main_frame = ttk.Frame(root, padding="20", style="Main.TFrame")
main_frame.grid(row=0, column=0, sticky="nsew")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# 創建標題
title_label = ttk.Label(main_frame, text="Gmail 帳號生成器", font=("Helvetica", 24, "bold"), background="#f0f0f0", foreground="#333333")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# 創建輸入框架
input_frame = ttk.Frame(main_frame, padding="20", relief="groove", borderwidth=2)
input_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
main_frame.grid_columnconfigure(0, weight=1)

# 輸入框和標籤
num_credentials_label = ttk.Label(input_frame, text="帳號數量:")
num_credentials_entry = ttk.Entry(input_frame, width=20)

email_length_label = ttk.Label(input_frame, text="帳號長度:")
email_length_entry = ttk.Entry(input_frame, width=20)

password_length_label = ttk.Label(input_frame, text="密碼長度:")
password_length_entry = ttk.Entry(input_frame, width=20)

# 生成按鈕
generate_button = ttk.Button(input_frame, text="生成帳號", command=generate_gmail_account, style="Accent.TButton")
style.configure("Accent.TButton", padding=10)

# 注意事項標籤
note_label = ttk.Label(input_frame, text="注意事項：\n帳號數量範圍：1 到 100 個之間\n帳號長度範圍：6 到 30 個字元\n密碼長度範圍：8 到 100 個字元", font=("Helvetica", 10), background="#f0f0f0", foreground="#555")
note_label.grid(row=10, column=0, columnspan=2, pady=(20, 0))

# 輸出框架
output_frame = ttk.Frame(main_frame, padding="20", relief="groove", borderwidth=2)
output_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))
main_frame.grid_columnconfigure(1, weight=2)
main_frame.grid_rowconfigure(1, weight=1)

# 輸出框
output_text = tk.Text(output_frame, wrap=tk.WORD, font=("Courier", 10), bg="#333333", fg="#ffffff")
output_scrollbar = ttk.Scrollbar(output_frame, orient="vertical", command=output_text.yview)
output_text.configure(yscrollcommand=output_scrollbar.set)

# 佈局
num_credentials_label.grid(row=0, column=0, padx=5, pady=10, sticky="e")
num_credentials_entry.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

email_length_label.grid(row=1, column=0, padx=5, pady=10, sticky="e")
email_length_entry.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

password_length_label.grid(row=2, column=0, padx=5, pady=10, sticky="e")
password_length_entry.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

generate_button.grid(row=3, column=0, columnspan=2, pady=20)

output_text.pack(side="left", fill="both", expand=True)
output_scrollbar.pack(side="right", fill="y")

input_frame.columnconfigure(1, weight=1)

# 啟動主視窗
root.mainloop()
