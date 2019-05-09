class Settings:
    """存储游戏设置的类"""
    def __init__(self):
        self.screen_width = 1366
        self.screen_height = 768
        self.background_color = (230, 230, 230)
        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)