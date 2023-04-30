import arcade
import numpy as np
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCALE = 5

oceanColor  = [17,173,193]
sandColor   = [247,182,158]
grassColor  = [91,179,97]
forestColor = [30,136,117]
rockColor   = [96,108,129]
snowColor   = [255, 255, 255]

def generate_noise(width, height, scale):
    grid = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            grid[i][j] = random.random()

    def smooth(x, y):
        corners = (grid[x-1][y-1] + grid[x-1][y+1] + grid[x+1][y-1] + grid[x+1][y+1]) / 16
        sides = (grid[x-1][y] + grid[x][y-1] + grid[x+1][y] + grid[x][y+1]) / 8
        center = grid[x][y] / 4
        return corners + sides + center

    def interpolate(x, y):
        x_int = int(x)
        y_int = int(y)
        x_frac = x - x_int
        y_frac = y - y_int

        v1 = smooth(x_int, y_int)
        v2 = smooth(x_int + 1, y_int)
        v3 = smooth(x_int, y_int + 1)
        v4 = smooth(x_int + 1, y_int + 1)

        i1 = interpolate_linear(v1, v2, x_frac)
        i2 = interpolate_linear(v3, v4, x_frac)

        return interpolate_linear(i1, i2, y_frac)

    def interpolate_linear(a, b, x):
        return a * (1 - x) + b * x

    noise_array = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            x = i / scale
            y = j / scale
            noise_array[i][j] = interpolate(x, y)

    return noise_array

def combine_noise (width, height, SCALE):
    """
    n1 = generate_noise(width, height, SCALE)
    for i in range (2):
        n2 = generate_noise(width, height, SCALE)
        n1 = n1 + n2
    return np.divide(n1, 1)
    """
    return generate_noise(width, height, SCALE)

def path_generation ():
    pass

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.noise_array = combine_noise(width, height, SCALE)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.noise_array = combine_noise(SCREEN_WIDTH // SCALE, SCREEN_HEIGHT // SCALE, SCALE)
            print(self.noise_array)

    def on_draw(self):
        arcade.start_render()

        for i in range(SCREEN_WIDTH // SCALE):
            for j in range(SCREEN_HEIGHT // SCALE):
                x = i * SCALE
                y = j * SCALE
                #color = int(self.noise_array[i][j] * 255)
                #arcade.draw_rectangle_filled(x, y, SCALE, SCALE, (color, color, color))                
                if (self.noise_array[i][j] <.1):
                    arcade.draw_rectangle_filled(x, y, SCALE, SCALE, oceanColor)
                elif(self.noise_array[i][j] <.2):
                    arcade.draw_rectangle_filled(x, y, SCALE, SCALE, sandColor)
                elif(self.noise_array[i][j] <.4):
                    arcade.draw_rectangle_filled(x, y, SCALE, SCALE, grassColor)
                elif(self.noise_array[i][j] <.7):
                    arcade.draw_rectangle_filled(x, y, SCALE, SCALE, forestColor)
                elif(self.noise_array[i][j] <.92):
                    arcade.draw_rectangle_filled(x, y, SCALE, SCALE, rockColor)
                else:
                    arcade.draw_rectangle_filled(x, y, SCALE, SCALE, snowColor)
                

if __name__ == "__main__":
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "TTRPG Map Generator")
    arcade.run()


