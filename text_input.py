from pyray import *


class TextInput:
    def __init__(self, rect, title: str, message: str, buttons: str, max_length: int):
        self.rect = rect
        self.title = title
        self.message = message
        self.buttons = buttons
        self.max_length = max_length
        self.show = True
        self.buffer = ffi.new("char[64]")

    def render(self):
        if self.show:
            res = gui_text_input_box(
                self.rect,
                self.title,
                self.message,
                self.buttons,
                self.buffer,
                self.max_length,
                ffi.new("bool *", True),
            )

            if res == 0:
                self.show = False

    def display(self):
        self.show = True

    def hide(self):
        self.show = False
