from pystray import Icon, Menu, MenuItem
from PIL import Image


def quit_app(icon):
    icon.stop()


image = Image.new("RGB", (64, 64), "blue")

icon = Icon(
    "Reminder",
    image,
    menu=Menu(
        MenuItem("退出", quit_app)
    )
)

icon.run()