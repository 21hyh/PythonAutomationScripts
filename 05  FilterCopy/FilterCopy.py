import os
import shutil
from tkinter import Tk, filedialog, messagebox

def choose_directory(title="选择文件夹"):
    """ 弹出窗口让用户选择一个文件夹，并返回该文件夹的路径。"""
    root = Tk()
    root.withdraw()
    messagebox.showinfo("操作提示", title)  # 显示提示信息
    directory_path = filedialog.askdirectory(title=title)
    root.destroy()
    return directory_path

def choose_file(title="选择文件"):
    """ 弹出窗口让用户选择一个文件，并返回该文件的路径。"""
    root = Tk()
    root.withdraw()
    messagebox.showinfo("操作提示", title)  # 显示提示信息
    file_path = filedialog.askopenfilename(title=title, filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    root.destroy()
    return file_path

def read_substrings(file_path):
    """ 从文本文件中读取每一行作为一个筛选条件。"""
    with open(file_path, 'r', encoding='utf-8') as file:
        substrings = [line.strip() for line in file if line.strip()]
    return substrings

def copy_files_and_folders(source_dir, target_dir, substrings):
    """ 复制含有特定子字符串的文件和文件夹从源文件夹到目标文件夹。"""
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        target_path = os.path.join(target_dir, item)
        if any(sub in item for sub in substrings):
            if os.path.isdir(source_path):
                if not os.path.exists(target_path):
                    shutil.copytree(source_path, target_path)
                else:
                    print(f"目标文件夹 {target_path} 已存在。")
            else:
                shutil.copy(source_path, target_path)
            print(f"已复制：{item}")

def main():
    # 提示选择源文件夹
    source_dir = choose_directory("您正在选择源路径，请选择...")
    if not source_dir:
        messagebox.showinfo("信息", "未选择源文件夹")
        return

    # 提示选择目标文件夹
    target_dir = choose_directory("您正在选择目标路径，请选择...")
    if not target_dir:
        messagebox.showinfo("信息", "未选择目标文件夹")
        return

    # 提示选择包含筛选字符串的文本文件
    file_path = choose_file("请选择包含筛选条件的文本文件...")
    if not file_path:
        messagebox.showinfo("信息", "未选择文本文件")
        return

    # 从文本文件中读取筛选条件
    substrings = read_substrings(file_path)

    # 复制文件和文件夹
    copy_files_and_folders(source_dir, target_dir, substrings)
    messagebox.showinfo("完成", "文件和文件夹复制完成")

if __name__ == "__main__":
    main()
