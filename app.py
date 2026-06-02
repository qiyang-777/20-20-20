import tkinter as tk
import time
import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image

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

def quit_app(icon):
    icon.stop()


# 创建托盘图标
image = Image.new(
    "RGB",
    (64, 64),
    "blue"
)

icon = Icon(
    "Reminder",
    image,
    menu=Menu(
        MenuItem("退出", quit_app)
    )
)

# 启动提醒线程
threading.Thread(
    target=timer_loop,
    daemon=True
).start()

# 启动托盘
icon.run()