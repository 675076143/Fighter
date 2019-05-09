import sys
import pygame
from settings import Settings
from fighter import Fighter
import game_function as gf
from pygame.sprite import Group

def run_game():
    """执行游戏的方法"""
    setting = Settings()    # 实例化设置
    bullet = Group()
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    fighter = Fighter(screen)  # s实例化战机
    pygame.display.set_caption("Alien Invasion")
    # 开始游戏的主循环
    while True:
        screen.fill(setting.background_color)
        fighter.blitme()
        fighter.update()
        gf.check_events(fighter)
        gf.update_screen(setting, screen, fighter)



run_game()