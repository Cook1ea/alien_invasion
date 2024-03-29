import pygame


class Ship():

    # 宇宙飞船的类
    def __init__(self, game_settings, screen):
        # 初始化飞船类
        self.screen = screen
        self.game_settings = game_settings

        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将新飞船放到屏幕底部正中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性中存储小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.game_settings.ship_speed_factor

        self.rect.centerx = self.center


    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)


        
