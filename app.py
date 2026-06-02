import tkinter as tk
import time
import threading

minutes = float(input("请输入提醒间隔（分钟）："))
interval = minutes * 5

def show_reminder():
    root = tk.Tk()

    root.title("提醒")
    root.geometry("300x100")

    label = tk.Label(
        root,
        text="该休息一下眼睛了！",
        font=("宋体", 14)
    )
    label.pack(expand=True)

    root.mainloop()


def timer_loop():
    while True:
        time.sleep(interval)
        show_reminder()


threading.Thread(target=timer_loop, daemon=True).start()

input("程序运行中，按回车退出...\n")