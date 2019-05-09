import pygame

class Fighter:
    def __init__(self, screen):
        """初始化战机"""
        self.screen = screen
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/Fighter.png')
        self.image = pygame.transform.scale(self.image, (160, 120))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # 移动速度
        self.speed = 3
    def blitme(self):
        """在指定位置绘制战机"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.rect.right < self.screen_rect.right:
            if self.moving_right:
                self.rect.centerx += self.speed
        if self.rect.left > 0:
            if self.moving_left:
                self.rect.centerx -= self.speed
        if self.rect.bottom > 160:
            if self.moving_up:
                self.rect.bottom -= self.speed
        if self.rect.bottom < self.screen_rect.bottom:
            if self.moving_down:
                self.rect.bottom += self.speed