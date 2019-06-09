import sys
import pygame
import time
from bullet import Bullet

def check_events(setting, screen, fighter, bullets):
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 让最近绘制的屏幕可见
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, setting, screen, fighter, bullets)
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

def check_keydown_event(event, settings, screen, fighter, bullets):
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
    if event.key == pygame.K_SPACE:
        fire_bullet(event, settings, screen, fighter, bullets)
def update_screen(setting, screen, fighter, bullets):
    """更新屏幕显示内容"""
    screen.fill(setting.background_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    fighter.blitme()
    pygame.display.flip()   # 让最近绘制的屏幕可见
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

def fire_bullet(event, settings, screen, fighter, bullets):
    """如果还有子弹，发射"""
    if len(bullets) < settings.bullet_allowed:
        bullet = Bullet(settings, screen, fighter)
        bullets.add(bullet)
