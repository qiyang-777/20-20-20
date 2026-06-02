import tkinter as tk
import time
import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(BASE_DIR, "config.json")
icon_path = os.path.join(BASE_DIR, "logo.ico")

def load_interval():
    if not os.path.exists(config_path):
        return 20

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    return config.get("interval", 20)

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
    os._exit(0)

def start_remainder():
    threading.Thread(
        target=timer_loop,
        daemon=True
    ).start()

def create_the_tray():
    image = Image.open(
        icon_path
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

