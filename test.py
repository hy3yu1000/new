import tkinter as tk
from tkinter import ttk

# 定義計算函數
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "錯誤：不能除以 0"
        else:
            result = "錯誤：無效的運算符號"

        result_label.config(text=f"結果：{num1} {operator} {num2} = {result}")
    except ValueError:
        result_label.config(text="錯誤：請輸入有效的數字！")

# 創建主視窗
window = tk.Tk()
window.title("簡單計算機")
window.geometry("300x200")  # 設定視窗大小

# 創建並放置元件
# 第一個數字輸入框
tk.Label(window, text="第一個數字：").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

# 第二個數字輸入框
tk.Label(window, text="第二個數字：").grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# 運算符號下拉菜單
tk.Label(window, text="運算符號：").grid(row=2, column=0, padx=5, pady=5)
operator_var = tk.StringVar()
operator_menu = ttk.Combobox(window, textvariable=operator_var, values=['+', '-', '*', '/'], state="readonly")
operator_menu.grid(row=2, column=1, padx=5, pady=5)
operator_menu.set('+')  # 預設選項

# 計算按鈕
calc_button = tk.Button(window, text="計算", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

# 結果顯示標籤
result_label = tk.Label(window, text="結果將顯示在這裡")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# 啟動主迴圈
window.mainloop()