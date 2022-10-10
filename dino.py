import pygame, random, math, sys
from pygame.locals import *
SCREEN_RECT = Rect(0, 0,640, 480)
screen = pygame.display.set_mode(SCREEN_RECT.size)
def blit(a,b,c,d):
    font = pygame.font.SysFont("MS Gothic", a)
    text = font.render(b, True, (0,0,0))
    screen.blit(text, (c, d))
class Wa_i():
    def __init__(self):
        self.scene = 0
        self.score = 0
        self.jump = False
        self.x = -10
        self.wa_i = pygame.image.load("wa-i.png")
        self.bullet = []
    def action(self):
        if self.scene == 0:
            miniwa_i = pygame.transform.rotozoom(self.wa_i, 0, 0.5)
            screen.blit(miniwa_i,(190,0))
            blit(30,"start",280,300)
            blit(30,"how to play",230,350)
            rect1 = pygame.Rect(220,296,180,40)
            pygame.draw.rect(screen,(0,0,0),rect1,3)
            rect2 = pygame.Rect(220,346,180,40)
            pygame.draw.rect(screen,(0,0,0),rect2,3)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if rect1.collidepoint(event.pos):
                            self.scene = 1
                        elif rect2.collidepoint(event.pos):
                            self.scene = 2
        elif self.scene == 1:
            pressed_keys = pygame.key.get_pressed()
            self.score += 1
            pygame.draw.rect(screen, (0,0,0), (0,270,640,210), 0)
            blit(25,"score"+str(self.score),5,5)
            a = (self.x**2)-(15**2)
            miniwa_i = pygame.transform.rotozoom(self.wa_i, 0, 0.2)
            screen.blit(miniwa_i,(72,330+a))
            player_x1 = 76
            player_x2 = 88
            player_x3 = 119
            player_x4 = 150
            player_x5 = 162
            player_y1 = 369 + a
            player_y2 = 383 + a
            if pressed_keys[K_SPACE]:
                if self.jump == False:
                    self.x = -10
                    self.jump = True
            if self.jump == True:
                if self.x < 10:
                    self.x += 1
                else:
                    self.jump = False
            if self.score >= 100:
                num = random.randrange(0,30)
                if num == 0:
                    o = random.randrange(175,230)
                    self.bullet += [[640,o]]
            bullet_count = len(self.bullet)
            for z in range(bullet_count):
                bullet = self.bullet[bullet_count-1-z]
                bullet[0] -= 10
                pygame.draw.ellipse(screen, (0,0,0), (bullet[0],bullet[1],30,30))
                ellipse_x = bullet[0] + 15
                ellipse_y = bullet[1] + 15
                e = math.sqrt((ellipse_x - player_x1)**2 + ((player_y1 - ellipse_y)**2))
                g = math.sqrt((ellipse_x - player_x2)**2 + ((player_y2 - ellipse_y)**2))
                i = math.sqrt((ellipse_x - player_x3)**2 + ((player_y1 - ellipse_y)**2))
                j = math.sqrt((ellipse_x - player_x3)**2 + ((player_y2 - ellipse_y)**2))
                k = math.sqrt((ellipse_x - player_x4)**2 + ((player_y2 - ellipse_y)**2))
                l = math.sqrt((ellipse_x - player_x5)**2 + ((player_y1 - ellipse_y)**2))
                if (e <= 15) or (g <= 15) or (i <= 15) or (j <= 15) or (k <= 15) or (l <= 15):
                    pygame.quit()
                    sys.exit()
                if bullet[0] <= -10:
                    del bullet
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        elif self.scene == 2:
            blit(30,"このゲームについて",5,5)
            blit(20,"このゲームはChrome Dinoのようなやつが作りたかったので",5,35)
            blit(20,"作りました。",5,55)
            blit(30,"操作方法",5,75)
            blit(20,"スペースを押すとジャンプします",5,105)
            blit(30,"クリア条件",5,125)
            blit(20,"未定",5,155)
            blit(30,"弾の当たり判定",5,175)
            miniwa_i = pygame.transform.rotozoom(self.wa_i, 0, 0.2)
            screen.blit(miniwa_i,(50,200))
            pygame.draw.ellipse(screen, (255,0,0), (53,238,5,5))
            pygame.draw.ellipse(screen, (255,0,0), (138,238,5,5))
            pygame.draw.ellipse(screen, (255,0,0), (63,252,5,5))
            pygame.draw.ellipse(screen, (255,0,0), (128,252,5,5))
            pygame.draw.ellipse(screen, (255,0,0), (98,252,5,5))
            pygame.draw.ellipse(screen, (255,0,0), (98,238,5,5))
            blit(20,"赤い点に弾があたると死にます",5,300)
            blit(30,"back",560,440)
            rect3 = pygame.Rect(556,436,75,40)
            pygame.draw.rect(screen,(0,0,0),rect3,3)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if rect3.collidepoint(event.pos):
                            self.scene = 0
def main():
    pygame.init()
    pygame.display.set_caption("わぁーい")
    wa_i = Wa_i()
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        screen.fill((255,255,255))
        wa_i.action()
        pygame.display.update()
if __name__ == '__main__':
    main()