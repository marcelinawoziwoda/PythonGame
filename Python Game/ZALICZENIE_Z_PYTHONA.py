###### Marcelina Woziwoda, Anna Woś

import sys
import pygame
import time
pygame.init()

ekran = pygame.display.set_mode((1020, 574))

pygame.display.set_caption("DZIWNY PTASZEK")

idz_prawo = [pygame.image.load('RS1.png'), pygame.image.load('RG1.png'), pygame.image.load('RD3.png'), pygame.image.load('RD4.png'), pygame.image.load('RS1.png'),pygame.image.load('RG1.png'), pygame.image.load('RD3.png'),  pygame.image.load('RD4.png'), pygame.image.load('RS1.png')]
idz_lewo = [pygame.image.load('LG1.png'), pygame.image.load('LS2.png'), pygame.image.load('LD3.png'),pygame.image.load('LD4.png'), pygame.image.load('LG1.png'), pygame.image.load('LS2.png'), pygame.image.load('LD3.png'),pygame.image.load('LD4.png'), pygame.image.load('LG1.png')]
tlo = pygame.image.load('background.jpg')
przod = pygame.image.load('char1.png')
clock = pygame.time.Clock()


jumpSound = pygame.mixer.Sound('jump.wav')

music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1,0.0)

punkt = 0

class ptak(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.predkosc = 8
        self.skok = False
        self.left = False
        self.right = False
        self.lkrok = 0
        self.lskok = 10
        self.stoj = True
        self.uderz = (self.x, self.y, 45, 45)


    def rysuj(self, ekran):
        if self.lkrok + 1 >= 9:
            self.lkrok = 0

        if not (self.stoj):
            if self.left:
                ekran.blit(idz_lewo[self.lkrok], (self.x, self.y))
                self.lkrok += 1
            elif self.right:
                ekran.blit(idz_prawo[self.lkrok], (self.x, self.y))
                self.lkrok += 1
            else:
                ekran.blit(przod, (self.x, self.y))

        else:
            if self.right:
                ekran.blit(idz_prawo[0], (self.x, self.y))
            elif self.left:
                ekran.blit(idz_lewo[0], (self.x, self.y))
            else:
                ekran.blit(przod, (self.x, self.y))
        self.uderz = (self.x , self.y, 45, 45)


    def uderzenie(self):
        self.skok = False
        self.lskok = 10
        self.x = 300
        self.y = 200
        self.lkrok = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        ekran.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()



class jajo_zebr(object):
    idz_prawo = [pygame.image.load('egg1.png'), pygame.image.load('egg2.png'), pygame.image.load('egg3.png'),pygame.image.load('egg4.png'), pygame.image.load('egg1.png'), pygame.image.load('egg2.png'), pygame.image.load('egg3.png'), pygame.image.load('egg4.png'), pygame.image.load('egg1.png'), pygame.image.load('egg2.png'), pygame.image.load('egg3.png')]
    idz_lewo = [pygame.image.load('eggl1.png'), pygame.image.load('eggl2.png'), pygame.image.load('eggl3.png'),pygame.image.load('eggl4.png'), pygame.image.load('eggl1.png'), pygame.image.load('eggl2.png'), pygame.image.load('eggl3.png'), pygame.image.load('eggl4.png'), pygame.image.load('eggl1.png'), pygame.image.load('eggl2.png'), pygame.image.load('eggl3.png')]

    def __init__(self, x, y, width, height, koniec):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.koniec = koniec
        self.sciezka = [self.x, self.koniec]
        self.lkrok = 0
        self.predkosc = 2
        self.uderz = (self.x, self.y, 45, 45)
        self.zycie = 10
        self.widzialnosc = True

    def rysuj(self, ekran):
        self.ruch()
        if self.widzialnosc:
            if self.lkrok + 1 >= 33:
                self.lkrok = 0

            if self.predkosc > 0:
                ekran.blit(self.idz_prawo[self.lkrok // 3], (self.x, self.y))
                self.lkrok += 1
            else:
                ekran.blit(self.idz_lewo[self.lkrok // 3], (self.x, self.y))
                self.lkrok += 1

            self.uderz = (self.x, self.y, 45, 45)


    def ruch(self):
        if self.predkosc > 0:
            if self.x + self.predkosc < self.sciezka[1]:
                self.x += self.predkosc
            else:
                self.predkosc = self.predkosc * -1
                self.walkCount = 0
        else:
            if self.x - self.predkosc > self.sciezka[0]:
                self.x += self.predkosc
            else:
                self.predkosc = self.predkosc * -1
                self.lkrok = 0
    def uderzenie(self):
        if self.zycie > 0:
            self.zycie -= 1
        else:
            self.widzialnosc = False


class czarne_jajo(object):
    idz_prawo = [pygame.image.load('begg1.png'), pygame.image.load('begg2.png'), pygame.image.load('begg3.png'), pygame.image.load('begg4.png'), pygame.image.load('begg1.png'), pygame.image.load('begg2.png'), pygame.image.load('begg3.png'), pygame.image.load('begg4.png'),pygame.image.load('begg1.png'), pygame.image.load('begg2.png'), pygame.image.load('begg3.png')]
    idz_lewo = [pygame.image.load('beggl1.png'), pygame.image.load('beggl2.png'), pygame.image.load('beggl3.png'), pygame.image.load('beggl4.png'), pygame.image.load('beggl1.png'), pygame.image.load('beggl2.png'), pygame.image.load('beggl3.png'), pygame.image.load('beggl4.png'),pygame.image.load('beggl1.png'), pygame.image.load('beggl2.png'), pygame.image.load('beggl3.png')]
    def __init__(self, x, y, width, height, koniec):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.koniec = koniec
        self.sciezka = [self.x, self.koniec]
        self.lkrok = 0
        self.predkosc =6
        self.uderz = (self.x, self.y, 45, 45)
        self.zycie = 10
        self.widzialnosc = True

    def rysuj(self, ekran):
        self.ruch()
        if self.widzialnosc:
            if self.lkrok + 1 >= 33:
                self.lkrok = 0

            if self.predkosc > 0:
                ekran.blit(self.idz_prawo[self.lkrok // 3], (self.x, self.y))
                self.lkrok += 1
            else:
                ekran.blit(self.idz_lewo[self.lkrok // 3], (self.x, self.y))
                self.lkrok += 1


            self.uderz = (self.x, self.y, 45, 45)


    def ruch(self):
        if self.predkosc > 0:
            if self.x + self.predkosc < self.sciezka[1]:
                self.x += self.predkosc
                self.predkosc += 0.02
            else:
                self.predkosc = self.predkosc * -1
                self.lkrok = 0
        else:
            if self.x - self.predkosc > self.sciezka[0]:
                self.x += self.predkosc
            else:
                self.predkosc = self.predkosc * -1
                self.lkrok = 0
    def uderzenie(self):
        if self.zycie > 0:
            self.zycie -= 1
        else:
            self.widzialnosc = False


def redrawGameWindow():
    ekran.blit(tlo, (0, 0))
    text = font.render('Score: ' + str(punkt), 1, (0,0,0))
    ekran.blit(text, (880, 10))
    ptak.rysuj(ekran)
    jajo1.rysuj(ekran)
    jajo2.rysuj(ekran)
    koniec_gry = True
    for j in jaja:
        j.rysuj(ekran)
        if j.widzialnosc == True:
            koniec_gry = False
    if koniec_gry:

        font1 = pygame.font.SysFont('comicsans', 110)
        text = font1.render('YOU WIN!', 3, (255, 0, 0))
        text1 = font1.render('Score: ' + str(punkt), 3, (255, 0, 0))

        ekran.blit(text, (200, 100))
        ekran.blit(text1, (200, 200))
        pygame.display.update()

        time.sleep(3)
        sys.exit()


    pygame.display.update()


####################################################################################################
####################################################################################################
font = pygame.font.SysFont('comicsans', 30, True, True)
ptak = ptak(300, 200, 64, 890)
jajo1 = czarne_jajo(50, 150, 64, 64, 890)
jajo2 = czarne_jajo(500, 50, 64, 64, 890)
jaja = []
dobre_jajo2 = jajo_zebr(200, 100, 64, 64, 1000)
dobre_jajo3 = jajo_zebr(300, 60, 64, 64, 1000)
dobre_jajo4 = jajo_zebr(-400, 120, 64, 64, 1000)
dobre_jajo5 = jajo_zebr(500, 120, 64, 64, 1000)
dobre_jajo6 = jajo_zebr(600, 120, 64, 64, 1000)
dobre_jajo7 = jajo_zebr(400, 120, 64, 64, 1000)
jaja.append(jajo_zebr(100, 180, 64, 64, 1000))
jaja.append(dobre_jajo2)
jaja.append(dobre_jajo3)
jaja.append(dobre_jajo4)
jaja.append(dobre_jajo5)
jaja.append(dobre_jajo6)
jaja.append(dobre_jajo7)
run = True
while run:
    clock.tick(27)
    for j in jaja:
        if ptak.uderz[1] < j.uderz[1] + j.uderz[3] and ptak.uderz[1] + ptak.uderz[3] > j.uderz[1]:
            if ptak.uderz[0] + ptak.uderz[2] > j.uderz[0] and ptak.uderz[0] < j.uderz[0] + j.uderz[2]:
                j.widzialnosc = False
                punkt +=5


    if jajo1.widzialnosc == True:

        if ptak.uderz[1] < jajo1.uderz[1] + jajo1.uderz[3] and ptak.uderz[1] + ptak.uderz[3] > jajo1.uderz[1]:
            if ptak.uderz[0] + ptak.uderz[2] > jajo1.uderz[0] and ptak.uderz[0] < jajo1.uderz[0] + jajo1.uderz[2]:
                ptak.uderzenie()
                punkt -= 5

    if jajo2.widzialnosc == True:

        if ptak.uderz[1] < jajo2.uderz[1] + jajo2.uderz[3] and ptak.uderz[1] + ptak.uderz[3] > jajo2.uderz[1]:
            if ptak.uderz[0] + ptak.uderz[2] > jajo2.uderz[0] and ptak.uderz[0] < jajo2.uderz[0] + jajo2.uderz[2]:
                ptak.uderzenie()
                punkt -= 5






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)


    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and ptak.x > ptak.predkosc:
        ptak.x -= ptak.predkosc
        ptak.left = True
        ptak.right = False
        ptak.stoj = False
    elif keys[pygame.K_RIGHT] and ptak.x < 1020 - ptak.width - ptak.predkosc:
        ptak.x += ptak.predkosc
        ptak.right = True
        ptak.left = False
        ptak.stoj = False
    else:
        ptak.stoj = True
        ptak.lkrok = 0

    if not (ptak.skok):
        if keys[pygame.K_SPACE]:
            jumpSound.play()
            ptak.skok = True
            ptak.right = False
            ptak.left = False
            ptak.lkrok = 0
    else:
        if ptak.lskok >= -10:
            neg = 1
            if ptak.lskok < 0:
                neg = -1
            ptak.y -= (ptak.lskok ** 2) * 0.5 * neg
            ptak.lskok -= 1
        else:
            ptak.skok = False
            ptak.lskok = 10

    redrawGameWindow()

pygame.quit()
