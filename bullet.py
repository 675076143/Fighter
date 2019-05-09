import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    子弹类
    """
    def __init__(self,setting,screen,fighter):
        super(Bullet,self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, setting.bullet_width,
                                setting.bullet_height)
        self.rect.centerx = fighter.rect.centerx
        self.rect.top = fighter.rect.top

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor

    def update(self):
        """
        更新表示子弹位置的小数值
        :return:
        """
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """
        在屏幕上绘制子弹
        :return:
        """
        pygame.draw.rect(self.screen, self.color, self.rect)