import pyautogui as auto

class Control(object):
    def __init__(self):
        pass

    def move_left(self):
        auto.press("left")

    def move_right(self):
        auto.press("right")

    def rotate_up(self):
        auto.press("up")

    def soft_drop(self):
        auto.press("down")

    def hard_drop(self):
        auto.press("space")

    def hold(self):
        auto.press("c")