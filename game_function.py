import sys
import pygame


def check_events(fighter):
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 让最近绘制的屏幕可见
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, fighter)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, fighter)
        pygame.display.flip()


def check_keyup_event(event, fighter):
    """
    按键松开事件
    :param event:事件
    :param fighter:飞机类
    :return:
    """
    if event.key == pygame.K_RIGHT:
        fighter.moving_right = False  # 松开方向键右 停止移动
    if event.key == pygame.K_LEFT:
        fighter.moving_left = False
    if event.key == pygame.K_UP:
        fighter.moving_up = False
    if event.key == pygame.K_DOWN:
        fighter.moving_down = False

def check_keydown_event(event, fighter):
    """
    按键按下事件
    :param event:事件
    :param fighter:飞机类
    :return:
    """
    if event.key == pygame.K_RIGHT:
        fighter.moving_right = True  # 按住方向键右 向右移动战机
    if event.key == pygame.K_LEFT:
        fighter.moving_left = True
    if event.key == pygame.K_UP:
        fighter.moving_up = True
    if event.key == pygame.K_DOWN:
        fighter.moving_down = True

def update_screen(setting, screen, fighter):
    """更新屏幕显示内容"""
    screen.fill(setting.background_color)
    fighter.blitme()
    pygame.display.flip()   # 让最近绘制的屏幕可见
