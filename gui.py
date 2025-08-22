from pyray import *
from text_input import TextInput

init_window(500, 500, b"Test")
set_target_fps(60)

gui_load_style("genesis.rgs")

ti = TextInput(
    Rectangle(110, 220, 280, 120), b"Titolo", b"Messaggio", "Send;Cancel", 20
)
ti.hide()

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    if gui_button(Rectangle(0, 0, 180, 90), b"Ciao"):
        print("ciao")

    if gui_button(Rectangle(0, 91, 180, 90), "Open input"):
        ti.display()

    ti.render()

    end_drawing()
