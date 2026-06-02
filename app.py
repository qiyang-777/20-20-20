import tkinter as tk
import time
import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image

def get_interval():
    minutes = float(input("请输入提醒间隔（分钟）："))
    return  minutes * 5

interval = get_interval()

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

def start_remainder():
    threading.Thread(
        target=timer_loop,
        daemon=True
    ).start()

def create_the_tray():
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
    icon.run()

def main():
    start_remainder()
    create_the_tray()

if __name__ == "__main__" :
    main()

