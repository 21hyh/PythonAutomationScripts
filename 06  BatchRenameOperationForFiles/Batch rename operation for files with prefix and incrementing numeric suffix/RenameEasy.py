import os
import shutil
import tkinter as tk
from tkinter import filedialog, Label, Entry, Button, messagebox, font

class App:
    def __init__(self, root):
        self.root = root
        root.title("Batch rename operation for files with prefix and incrementing numeric suffix")

        # 设置字体
        self.custom_font = font.Font(family="Times New Roman", size=12)

        # 默认设置，用于保存和加载
        self.settings = {
            "source_directory": "",
            "target_directory": "",
            "prefix": "train",
            "start_number": "1",
            "extension": "txt"
        }
        self.load_settings()

        # 设置界面元素
        self.create_widgets()

    def create_widgets(self):
        # 源文件夹选择按钮和显示
        self.source_label = Label(self.root, text="Source Folder:", font=self.custom_font)
        self.source_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.source_entry = Entry(self.root, width=50, font=self.custom_font)
        self.source_entry.grid(row=0, column=1, padx=10, pady=5)
        self.source_entry.insert(0, self.settings["source_directory"])
        self.source_button = Button(self.root, text="Browse", font=self.custom_font, command=self.select_source_directory)
        self.source_button.grid(row=0, column=2, padx=10, pady=5)

        # 目标文件夹选择按钮和显示
        self.target_label = Label(self.root, text="Target Folder:", font=self.custom_font)
        self.target_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.target_entry = Entry(self.root, width=50, font=self.custom_font)
        self.target_entry.grid(row=1, column=1, padx=10, pady=5)
        self.target_entry.insert(0, self.settings["target_directory"])
        self.target_button = Button(self.root, text="Browse", font=self.custom_font, command=self.select_target_directory)
        self.target_button.grid(row=1, column=2, padx=10, pady=5)

        # 前缀设置
        self.prefix_label = Label(self.root, text="Filename Prefix:", font=self.custom_font)
        self.prefix_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.prefix_entry = Entry(self.root, width=50, font=self.custom_font)
        self.prefix_entry.grid(row=2, column=1, padx=10, pady=5)
        self.prefix_entry.insert(0, self.settings["prefix"])

        # 起始编号设置
        self.number_label = Label(self.root, text="Start Number:", font=self.custom_font)
        self.number_label.grid(row=3, column=0, sticky='w', padx=10, pady=5)
        self.number_entry = Entry(self.root, width=50, font=self.custom_font)
        self.number_entry.grid(row=3, column=1, padx=10, pady=5)
        self.number_entry.insert(0, self.settings["start_number"])

        # 文件扩展名设置
        self.extension_label = Label(self.root, text="File Extension:", font=self.custom_font)
        self.extension_label.grid(row=4, column=0, sticky='w', padx=10, pady=5)
        self.extension_entry = Entry(self.root, width=50, font=self.custom_font)
        self.extension_entry.grid(row=4, column=1, padx=10, pady=5)
        self.extension_entry.insert(0, self.settings["extension"])

        # 执行按钮
        self.run_button = Button(self.root, text="Run", font=self.custom_font, command=self.run)
        self.run_button.grid(row=5, column=1, pady=10)

    def select_source_directory(self):
        folder = filedialog.askdirectory()
        if folder:
            self.source_entry.delete(0, tk.END)
            self.source_entry.insert(0, folder)

    def select_target_directory(self):
        folder = filedialog.askdirectory()
        if folder:
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, folder)

    def run(self):
        source_directory = self.source_entry.get()
        target_directory = self.target_entry.get()
        prefix = self.prefix_entry.get()
        start_number = int(self.number_entry.get())
        extension = self.extension_entry.get()

        # 保存设置
        self.settings = {
            "source_directory": source_directory,
            "target_directory": target_directory,
            "prefix": prefix,
            "start_number": self.number_entry.get(),
            "extension": extension
        }
        self.save_settings()

        # 文件操作
        self.copy_and_rename_files(source_directory, target_directory, prefix, start_number, extension)
        messagebox.showinfo("Completed", "Operation completed successfully!")

    def copy_and_rename_files(self, source_directory, target_directory, prefix, start_number, extension):
        files = sorted(os.listdir(source_directory))
        for i, filename in enumerate(files):
            new_name = f"{prefix}{start_number + i}.{extension}"
            old_file = os.path.join(source_directory, filename)
            new_file = os.path.join(target_directory, new_name)
            shutil.copy2(old_file, new_file)

    def save_settings(self):
        # 保存设置到文件
        with open("settings.txt", "w") as f:
            for key, value in self.settings.items():
                f.write(f"{key}={value}\n")

    def load_settings(self):
        # 从文件加载设置
        try:
            with open("settings.txt", "r") as f:
                for line in f:
                    key, value = line.strip().split('=')
                    self.settings[key] = value
        except FileNotFoundError:
            print("Settings file not found, using default values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
