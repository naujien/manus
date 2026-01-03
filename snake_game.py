import pygame
import random
import time

# 初始化 Pygame
pygame.init()

# 遊戲參數
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SNAKE_SPEED = 10  # 蛇的初始速度 (幀率)

# 顏色定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 設置屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python 貪吃蛇遊戲 - Manus AI")

# 字體設置
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def draw_score(score):
    """在屏幕上顯示分數"""
    value = score_font.render("分數: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

def draw_snake(snake_list):
    """繪製蛇身"""
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], GRID_SIZE, GRID_SIZE])

def generate_food(snake_list):
    """生成食物，確保不在蛇身上"""
    while True:
        food_x = round(random.randrange(0, SCREEN_WIDTH - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
        food_y = round(random.randrange(0, SCREEN_HEIGHT - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
        if [food_x, food_y] not in snake_list:
            return food_x, food_y

def message(msg, color):
    """顯示消息"""
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

def game_loop():
    """遊戲主循環"""
    game_over = False
    game_close = False

    # 蛇的初始位置和身體
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1

    # 食物初始位置
    food_x, food_y = generate_food(snake_list)

    # 遊戲時鐘
    clock = pygame.time.Clock()
    current_speed = SNAKE_SPEED

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("遊戲結束! 按 C 重新開始或 Q 退出", RED)
            draw_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop() # 重新開始遊戲

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -GRID_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = GRID_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -GRID_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = GRID_SIZE
                    x1_change = 0

        # 檢查是否撞牆
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True

        # 更新蛇頭位置
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)

        # 繪製食物
        pygame.draw.rect(screen, RED, [food_x, food_y, GRID_SIZE, GRID_SIZE])

        # 更新蛇身
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # 檢查是否撞到自己
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_list)
        draw_score(length_of_snake - 1)

        pygame.display.update()

        # 檢查是否吃到食物
        if x1 == food_x and y1 == food_y:
            food_x, food_y = generate_food(snake_list)
            length_of_snake += 1
            # 吃到食物後加速
            current_speed = SNAKE_SPEED + (length_of_snake - 1) * 0.5
            if current_speed > 30: # 設置最大速度
                current_speed = 30

        clock.tick(current_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
