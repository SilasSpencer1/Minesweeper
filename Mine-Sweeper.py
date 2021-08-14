import pygame
import random
import math

class MS:
    def __init__(this):
        this.width = 15
        this.height = 15
        this.mines = 10
        this.grid_list = []
        for i in range(this.width):
            row_list = []
            for j in range(this.height):
                row_list.append(int(0))
            this.grid_list.append(row_list)
        this.mine_list = []
        n = 0
        while n < this.mines:
            i = random.randint(0, this.width - 1)
            j = random.randint(0, this.height - 1)
            data = (i, j)
            while data in this.mine_list:
                i = random.randint(0, this.width - 1)
                j = random.randint(0, this.height - 1)
                data = (i, j)
            this.mine_list.append(data)
            this.grid_list[i][j] = 9
            n += 1
        this.calculate_surrounding()
        this.visible_list = []
        this.show_surrounding()
        this.colors = [
            [187, 255, 200],
            [106, 90, 205],
            [205, 92, 92],
            [139, 58, 58],
            [139, 58, 58],
            [139, 58, 58],
            [139, 58, 58],
            [139, 58, 58],
            [139, 58, 58],
        ]

    def calculate_surrounding(this):
        for i in range(this.width):
            for j in range(this.height):
                grid_list = this.grid_list
                if grid_list[i][j] == 9:
                    if i - 1 >= 0 and grid_list[i - 1][j] != 9:
                        grid_list[i - 1][j] = int(int(grid_list[i - 1][j]) + 1)
                    if i + 1 < this.width and grid_list[i + 1][j] != 9:
                        grid_list[i + 1][j] = int(int(grid_list[i + 1][j]) + 1)
                    if j - 1 >= 0 and grid_list[i][j - 1] != 9:
                        grid_list[i][j - 1] = int(int(grid_list[i][j - 1]) + 1)
                    if j + 1 < this.height and grid_list[i][j + 1] != 9:
                        grid_list[i][j + 1] = int(int(grid_list[i][j + 1]) + 1)
                    if i - 1 >= 0 and j - 1 >= 0 and grid_list[i - 1][j - 1] != 9:
                        grid_list[i - 1][j - 1] = int(int(grid_list[i - 1][j - 1]) + 1)
                    if i + 1 < this.width and j - 1 >= 0 and grid_list[i + 1][j - 1] != 9:
                        grid_list[i + 1][j - 1] = int(int(grid_list[i + 1][j - 1]) + 1)
                    if i - 1 >= 0 and j + 1 < this.width and grid_list[i - 1][j + 1] != 9:
                        grid_list[i - 1][j + 1] = int(int(grid_list[i - 1][j + 1]) + 1)
                    if i + 1 < this.height and j + 1 < this.width and grid_list[i + 1][j + 1] != 9:
                        grid_list[i + 1][j + 1] = int(int(grid_list[i + 1][j + 1]) + 1)
                    this.grid_list = grid_list

    def show_surrounding(this):
        for i in range(this.width):
            temp = []
            for j in range(this.height):
                temp.append(int(0))
            this.visible_list.append(temp)

    def after_click(this, i, j):
        if this.grid_list[i][j] == 9:
            this.visible_list[i][j] = 1
            return 0
        this.show_grid(i, j)
        this.visible_list[i][j] = 1
        return 1
    
    def show_grid(this, i, j):
        if this.grid_list[i][j] == 0:
            this.visible_list[i][j] = 1
            x = [-1, 0, 1, 0, -1, 1, -1, 1]
            y = [0, -1, 0, 1, -1, -1, 1, 1]
            for k in range(8):
                last_x = i + x[k]
                last_y = j + y[k]
                if 0 <= last_x < this.width and 0 <= last_y < this.height and visible_list[last_x][last_y] != 1:
                    this.visible_list[last_x][last_y] = 1
                    this.show_grid(last_x, last_y)

width = 450
height = 450
pygame.init()
pygame.display.set_caption('Mine-Sweeper')
screen = pygame.display.set_mode([width, height])
font = pygame.font.Font(None, 30)
timer = pygame.time.Clock()
flag = 0

ms = MS()

while True:
    if flag == -1:
        break
    timer.tick(30)
    screen.fill([200, 200, 200])
    visible_list = ms.visible_list
    grid_list = ms.grid_list
    mx, my = pygame.mouse.get_pos()
    for i in range(15):
        for j in range(15):
            x = i * 26 + 10
            y = j * 26 + 10
            last_i = math.floor(mx / 26)
            last_j = math.floor(my / 26)
            position = (x, y, 20, 20)
            if last_i == i and last_j == j:
                pygame.draw.rect(screen, [125, 125, 125], position, 5)
            else:
                if visible_list[i][j] == 1:
                    pygame.draw.rect(screen, [125, 125, 125], position, 2)
                else:
                    pygame.draw.rect(screen, [105, 105, 105], position, 0)
            if visible_list[i][j] == 1 and grid_list[i][j] != 0:
                text = font.render(str(grid_list[i][j]), True, ms.colors[grid_list[i][j]])
                screen.blit(text, (x + 2, y + 2))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if mx < 0 or mx > width or my < 0 or my > height:
                pass
            result = ms.after_click(last_i, last_j)
            if result == 0:
                flag = -1

    ms.visible_list = visible_list
    ms.grid_list = grid_list
    pygame.display.flip()