import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def archive_files():
    source_folder = source_var.get()
    archive_folder = archive_var.get()
    
    if not source_folder or not archive_folder:
        messagebox.showerror("錯誤", "請選擇來源和目標資料夾！")
        return
    
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)
    
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            first_letter = filename[0].upper()
            target_folder = os.path.join(archive_folder, first_letter)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            shutil.move(file_path, os.path.join(target_folder, filename))
    
    messagebox.showinfo("完成", "檔案歸檔成功！")

def select_source():
    folder = filedialog.askdirectory()
    source_var.set(folder)

def select_archive():
    folder = filedialog.askdirectory()
    archive_var.set(folder)

# 建立 GUI
root = tk.Tk()
root.title("檔案歸檔工具")
root.geometry("320x220")

source_var = tk.StringVar()
archive_var = tk.StringVar()

tk.Label(root, text="來源資料夾：").pack(pady=5)
tk.Entry(root, textvariable=source_var, width=40).pack()
tk.Button(root, text="選擇", command=select_source).pack()

tk.Label(root, text="目標資料夾：").pack(pady=5)
tk.Entry(root, textvariable=archive_var, width=40).pack()
tk.Button(root, text="選擇", command=select_archive).pack()

tk.Button(root, text="開始歸檔", command=archive_files).pack(pady=20)

root.mainloop()