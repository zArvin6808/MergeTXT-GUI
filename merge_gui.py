import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]

def merge_txt_files(folder_path):
    try:
        txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        txt_files.sort(key=natural_sort_key)
        total = len(txt_files)

        progress['maximum'] = total
        progress['value'] = 0
        status_label.config(text="开始合并...")
        root.update_idletasks()

        output_file = os.path.join(folder_path, "merged.txt")

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for i, filename in enumerate(txt_files, start=1):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n\n')
                progress['value'] = i
                status_label.config(text=f"正在合并: {filename}")
                root.update_idletasks()

        status_label.config(text="合并完成！")
        messagebox.showinfo("完成", f"合并完成！文件已保存为：{output_file}")

    except Exception as e:
        messagebox.showerror("错误", str(e))

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        merge_txt_files(folder_path)

# 创建 GUI 窗口
root = tk.Tk()
root.title("TXT 文件合并器 - GUI 版")
root.geometry("400x250")
root.resizable(False, False)

# 进度条
progress = Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

# 状态标签
status_label = tk.Label(root, text="请选择包含 TXT 文件的文件夹", font=("微软雅黑", 10))
status_label.pack(pady=10)

# 按钮
button = tk.Button(root, text="选择文件夹", command=select_folder, width=20, height=2)
button.pack()

# 运行主循环
root.mainloop()