import random
from pyray import *

init_window(1000, 1000, b"Overwhelm")
set_target_fps(60)

RADIUS = 15
SPEED = 120
FOOD_SPAWN_INTERVAL = 0.01
FOOD_SPAWN_TIME = 0


class Drawable:
    def __init__(self, pos: Vector2, radius: int, opacity: float):
        self.pos: Vector2 = pos
        self.radius = radius
        self.collected = 0
        self.opacity = opacity

    def draw(self):
        draw_circle(
            int(self.pos.x),
            int(self.pos.y),
            self.radius,
            fade(self.color, self.opacity),
        )

    def move(self):
        self.pos = get_mouse_position()

    def collide(self):
        for f in foods:
            if check_collision_circles(self.pos, RADIUS, f.pos, RADIUS):
                self.collected += 1
                foods.remove(f)
            else:
                self.color = GREEN


class Prey(Drawable):
    def __init__(self, pos: Vector2, radius: int):
        self.color = GREEN
        self.radius = radius
        super().__init__(pos, opacity=1.0, radius=self.radius)


class Food(Drawable):
    def __init__(self, pos: Vector2):
        self.color = WHITE
        super().__init__(pos, opacity=0.0)

    def draw(self):
        super().draw()
        if self.opacity < 1:
            self.opacity += get_frame_time()


preys = [Prey(Vector2(10, 10))]
foods = []

if __name__ == "__main__":
    while not window_should_close():
        FOOD_SPAWN_TIME += get_frame_time()
        begin_drawing()
        clear_background(BLACK)

        draw_text(
            b"Collected: %d, On screen: %d" % (preys[0].collected, len(foods)),
            10,
            10,
            20,
            WHITE,
        )

        if FOOD_SPAWN_TIME > FOOD_SPAWN_INTERVAL:
            foods.append(
                Food(Vector2(random.randint(10, 990), random.randint(10, 990)), 15)
            )
            FOOD_SPAWN_TIME = 0

        for f in foods:
            f.draw()

        for p in preys:
            p.draw()
            p.collide()
            p.move()

        end_drawing()
