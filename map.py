from pyray import *
from raylib import *

WIDTH = 1920
HEIGHT = 1080
FPS = 60
TITLE = "Map"

show_fps = False

set_config_flags(FLAG_WINDOW_RESIZABLE)
init_window(WIDTH, HEIGHT, TITLE)
set_target_fps(FPS)

camera = Camera2D(
    (get_screen_width() / 2, get_screen_height() / 2),
    (0, 0),
    0.0,
    1.0,
)
# hide_cursor()
show_cursor_lines = True


def panning():
    if is_mouse_button_down(MOUSE_BUTTON_MIDDLE):
        md = get_mouse_delta()
        camera.offset.x += md.x
        camera.offset.y += md.y

    if is_key_pressed(KEY_C):
        camera.offset = Vector2(get_screen_width() / 2, get_screen_height() / 2)


def cursor():
    global show_cursor_lines

    mouse_position = get_mouse_position()

    if get_key_pressed() == KeyboardKey.KEY_L:
        show_cursor_lines = not show_cursor_lines

    if show_cursor_lines:
        for i in range(int(get_screen_width() / 5)):
            draw_pixel(i * 5, int(mouse_position.y), fade(GREEN, 0.5))
            draw_pixel(int(mouse_position.x), i * 5, fade(GREEN, 0.5))


def tactical_map():
    draw_circle_lines(
        0,
        0,
        500,
        GREEN,
    )


def zoom():
    global camera

    wheel = get_mouse_wheel_move()

    if is_key_pressed(KEY_ONE):
        camera.zoom = 1.0

    if wheel:
        camera.zoom += wheel / 15


def display_fps():
    global show_fps

    if is_key_pressed(KEY_F):
        show_fps = not show_fps

    if show_fps:
        draw_fps(10, 10)


def handle_fullscreen():
    if is_key_pressed(KEY_F11):
        display = get_current_monitor()

        if is_window_fullscreen():
            set_window_size(WIDTH, HEIGHT)
        else:
            set_window_size(get_monitor_width(display), get_monitor_height(display))

        toggle_fullscreen()


if __name__ == "__main__":
    while not window_should_close():
        begin_drawing()
        clear_background(BLACK)
        begin_mode_2d(camera)
        panning()
        zoom()
        handle_fullscreen()
        tactical_map()
        # Center
        draw_circle(0, 0, 5, RED)
        end_mode_2d()
        cursor()
        display_fps()
        end_drawing()

    close_window()
