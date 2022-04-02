import pygame as pg
import  ctypes
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
pg.init()

screen = pg.display.set_mode((1000,720))
screen.fill((255,255,255))
icon_url = resource_path('assets/tictactoe.ico')
pg.display.set_caption("TIC-TAC-TOE")
icon = pg.image.load(icon_url)
pg.display.set_icon(icon)

Font = pg.font.SysFont(None,40)
font_url = resource_path('assets/Rashkey.ttf')
FONT = pg.font.Font(font_url,150)
X = FONT.render('X',True,(255,255,255))
O=FONT.render('O',True,(255,255,255))
list =[[0,0,0],[0,0,0],[0,0,0]]

x=(750, 180)
y=(750, 240)

t=100
def draw_check(list1):
    for row in list1:
        for box in row:
            if box==0:
                return False
            else:
                continue
    return True
def win_check(num,list1):
        for row in list1:
            for box in row:
                if box == num:
                    continue
                else:
                    break
            else:
                return True

        for c in range(3):
            for r in list1:
                if r[c] == num:
                    continue
                else:
                    break
            else:
                return True

        for t in range(3):
            if list1[t][t] == num:
                continue
            else:
                break
        else:
            return True

        for k in range(3):
            if list1[k][2 - k] == num:
                continue
            else:
                break
        else:
            return True

won = False
text = Font.render('RESET:',True,(0,0,0))
screen.blit(text, (700, 120))
turn = 'first'
box1 = 'unoccupied'
box2 = 'unoccupied'
box3 = 'unoccupied'
box4 = 'unoccupied'
box5 = 'unoccupied'
box6 = 'unoccupied'
box7 = 'unoccupied'
box8 = 'unoccupied'
box9 = 'unoccupied'

x_url = resource_path('assets/ximg.jpg')
xImg = pg.image.load(x_url)
xImg = pg.transform.scale(xImg,(200,200))

y_url = resource_path('assets/yimg.jpg')
yImg = pg.image.load(y_url)
yImg = pg.transform.scale(yImg,(200,200))

list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

I = pg.draw.rect(screen, (0, 0, 0), (30, 30, 200, 200))
II = pg.draw.rect(screen, (0, 0, 0), (260, 30, 200, 200))
III = pg.draw.rect(screen, (0, 0, 0), (490, 30, 200, 200))

IV = pg.draw.rect(screen, (0, 0, 0), (30, 260, 200, 200))
V = pg.draw.rect(screen, (0, 0, 0), (260, 260, 200, 200))
VI = pg.draw.rect(screen, (0, 0, 0), (490, 260, 200, 200))

VII = pg.draw.rect(screen, (0, 0, 0), (30, 490, 200, 200))
VIII = pg.draw.rect(screen, (0, 0, 0), (260, 490, 200, 200))
IX = pg.draw.rect(screen, (0, 0, 0), (490, 490, 200, 200))

reset = pg.draw.rect(screen, (0, 0, 0), (800, 120, 25, 25))

#b1 = pg.draw.rect(screen,(0,0,255),(720,180,25,25))
#b2 = pg.draw.rect(screen,(255,0,0),(720,240,25,25))

screen.blit(pg.transform.scale(xImg,(25,25)), (720,180))
screen.blit(pg.transform.scale(yImg,(25,25)), (720,240))

p1=[0]
p2=[0]


def show_score(a,b):
    blay1 = pg.draw.rect(screen,(255,255,255),(750,180,180,30))
    p11 = Font.render('PLAYER X: '+str(sum(p1)), True, (0, 0, 0))

    blay2 = pg.draw.rect(screen, (255,255,255), (750, 240, 180, 30))
    p22 = Font.render('PLAYER O: '+str(sum(p2)), True, (0, 0, 0))

    screen.blit(p11,a)
    screen.blit(p22,b)



running = True


while running:

            pg.time.delay(100)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    if reset.collidepoint(pos):
                        won = False
                        screen.blit(text, (700, 120))
                        turn = 'first'
                        box1 = 'unoccupied'
                        box2 = 'unoccupied'
                        box3 = 'unoccupied'
                        box4 = 'unoccupied'
                        box5 = 'unoccupied'
                        box6 = 'unoccupied'
                        box7 = 'unoccupied'
                        box8 = 'unoccupied'
                        box9 = 'unoccupied'

                        list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

                        I = pg.draw.rect(screen, (0, 0, 0), (30, 30, 200, 200))
                        II = pg.draw.rect(screen, (0, 0, 0), (260, 30, 200, 200))
                        III = pg.draw.rect(screen, (0, 0, 0), (490, 30, 200, 200))

                        IV = pg.draw.rect(screen, (0, 0, 0), (30, 260, 200, 200))
                        V = pg.draw.rect(screen, (0, 0, 0), (260, 260, 200, 200))
                        VI = pg.draw.rect(screen, (0, 0, 0), (490, 260, 200, 200))

                        VII = pg.draw.rect(screen, (0, 0, 0), (30, 490, 200, 200))
                        VIII = pg.draw.rect(screen, (0, 0, 0), (260, 490, 200, 200))
                        IX = pg.draw.rect(screen, (0, 0, 0), (490, 490, 200, 200))

                        reset = pg.draw.rect(screen, (0, 0, 0), (800, 120, 25, 25))
                    if draw_check(list):
                        list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        won = True
                        # sleep(1)
                        MessageBox = ctypes.windll.user32.MessageBoxW
                        MessageBox(None, 'DRAW !', 'GAME OVER', 0)

                        won = False
                        screen.blit(text, (700, 120))
                        turn = 'first'
                        box1 = 'unoccupied'
                        box2 = 'unoccupied'
                        box3 = 'unoccupied'
                        box4 = 'unoccupied'
                        box5 = 'unoccupied'
                        box6 = 'unoccupied'
                        box7 = 'unoccupied'
                        box8 = 'unoccupied'
                        box9 = 'unoccupied'

                        list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

                        I = pg.draw.rect(screen, (0, 0, 0), (30, 30, 200, 200))
                        II = pg.draw.rect(screen, (0, 0, 0), (260, 30, 200, 200))
                        III = pg.draw.rect(screen, (0, 0, 0), (490, 30, 200, 200))

                        IV = pg.draw.rect(screen, (0, 0, 0), (30, 260, 200, 200))
                        V = pg.draw.rect(screen, (0, 0, 0), (260, 260, 200, 200))
                        VI = pg.draw.rect(screen, (0, 0, 0), (490, 260, 200, 200))

                        VII = pg.draw.rect(screen, (0, 0, 0), (30, 490, 200, 200))
                        VIII = pg.draw.rect(screen, (0, 0, 0), (260, 490, 200, 200))
                        IX = pg.draw.rect(screen, (0, 0, 0), (490, 490, 200, 200))

                        reset = pg.draw.rect(screen, (0, 0, 0), (800, 120, 25, 25))

                    if win_check(1, list):
                        list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        p1.append(1)
                        won = True
                        # sleep(1)
                        MessageBox = ctypes.windll.user32.MessageBoxW
                        MessageBox(None, 'PLAYER X WINS', 'GAME OVER', 0)

                        won = False
                        screen.blit(text, (700, 120))
                        turn = 'first'
                        box1 = 'unoccupied'
                        box2 = 'unoccupied'
                        box3 = 'unoccupied'
                        box4 = 'unoccupied'
                        box5 = 'unoccupied'
                        box6 = 'unoccupied'
                        box7 = 'unoccupied'
                        box8 = 'unoccupied'
                        box9 = 'unoccupied'

                        list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

                        I = pg.draw.rect(screen, (0, 0, 0), (30, 30, 200, 200))
                        II = pg.draw.rect(screen, (0, 0, 0), (260, 30, 200, 200))
                        III = pg.draw.rect(screen, (0, 0, 0), (490, 30, 200, 200))

                        IV = pg.draw.rect(screen, (0, 0, 0), (30, 260, 200, 200))
                        V = pg.draw.rect(screen, (0, 0, 0), (260, 260, 200, 200))
                        VI = pg.draw.rect(screen, (0, 0, 0), (490, 260, 200, 200))

                        VII = pg.draw.rect(screen, (0, 0, 0), (30, 490, 200, 200))
                        VIII = pg.draw.rect(screen, (0, 0, 0), (260, 490, 200, 200))
                        IX = pg.draw.rect(screen, (0, 0, 0), (490, 490, 200, 200))

                        reset = pg.draw.rect(screen, (0, 0, 0), (800, 120, 25, 25))

                    if win_check(2, list):
                        won = True
                        list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        p2.append(1)
                        # pg.time.delay(10000)
                        MessageBox = ctypes.windll.user32.MessageBoxW
                        MessageBox(None, 'PLAYER O WINS', 'GAME OVER', 0)

                        won = False
                        screen.blit(text, (700, 120))
                        turn = 'first'
                        box1 = 'unoccupied'
                        box2 = 'unoccupied'
                        box3 = 'unoccupied'
                        box4 = 'unoccupied'
                        box5 = 'unoccupied'
                        box6 = 'unoccupied'
                        box7 = 'unoccupied'
                        box8 = 'unoccupied'
                        box9 = 'unoccupied'

                        list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

                        I = pg.draw.rect(screen, (0, 0, 0), (30, 30, 200, 200))
                        II = pg.draw.rect(screen, (0, 0, 0), (260, 30, 200, 200))
                        III = pg.draw.rect(screen, (0, 0, 0), (490, 30, 200, 200))

                        IV = pg.draw.rect(screen, (0, 0, 0), (30, 260, 200, 200))
                        V = pg.draw.rect(screen, (0, 0, 0), (260, 260, 200, 200))
                        VI = pg.draw.rect(screen, (0, 0, 0), (490, 260, 200, 200))

                        VII = pg.draw.rect(screen, (0, 0, 0), (30, 490, 200, 200))
                        VIII = pg.draw.rect(screen, (0, 0, 0), (260, 490, 200, 200))
                        IX = pg.draw.rect(screen, (0, 0, 0), (490, 490, 200, 200))

                        reset = pg.draw.rect(screen, (0, 0, 0), (800, 120, 25, 25))

                    if won!=True:
                        if I.collidepoint(pos):
                                if box1=='unoccupied' and turn =='first':
                                    screen.blit(xImg, (30, 30))
                                    pg.time.delay(t)

                                    box1='o'
                                    turn='second'
                                    list[0][0] = 1
                                elif box1=='unoccupied' and turn == 'second':
                                    screen.blit(yImg, (30, 30))
                                    pg.time.delay(t)

                                    box1 = 'o'
                                    turn = 'first'
                                    list[0][0] = 2

                        if II.collidepoint(pos):
                                if box2 == 'unoccupied' and turn == 'first':
                                    screen.blit(xImg, (260, 30))
                                    pg.time.delay(t)

                                    box2 = 'o'
                                    turn = 'second'
                                    list[0][1]=1
                                elif box2 == 'unoccupied' and turn == 'second':
                                    screen.blit(yImg, (260, 30))
                                    pg.time.delay(t)

                                    box2 = 'o'
                                    turn = 'first'
                                    list[0][1] = 2
                        if III.collidepoint(pos):
                                if box3 == 'unoccupied' and turn == 'first':
                                    screen.blit(xImg, (490, 30))
                                    pg.time.delay(t)

                                    box3 = 'o'
                                    turn = 'second'
                                    list[0][2] = 1
                                elif box3=='unoccupied' and turn == 'second':
                                    screen.blit(yImg, (490, 30))
                                    pg.time.delay(t)

                                    box3 = 'o'
                                    turn = 'first'
                                    list[0][2] = 2

                        if IV.collidepoint(pos):
                                if box4 == 'unoccupied' and turn == 'first':
                                    screen.blit(xImg, (30, 260))
                                    pg.time.delay(t)

                                    box4 = 'o'
                                    turn = 'second'
                                    list[1][0] = 1
                                elif box4=='unoccupied' and turn == 'second':
                                    screen.blit(yImg, (30, 260))
                                    pg.time.delay(t)

                                    box4 = 'o'
                                    turn = 'first'
                                    list[1][0] = 2
                        if V.collidepoint(pos):
                                if box5 == 'unoccupied' and turn == 'first':
                                    screen.blit(xImg, (260, 260))
                                    pg.time.delay(t)

                                    box5 = 'o'
                                    turn = 'second'
                                    list[1][1] = 1
                                elif box5=='unoccupied' and turn == 'second':
                                    screen.blit(yImg, (260, 260))
                                    pg.time.delay(t)

                                    box5 = 'o'
                                    turn = 'first'
                                    list[1][1] = 2
                        if VI.collidepoint(pos):
                                if box6 == 'unoccupied' and turn == 'first':
                                    screen.blit(xImg, (490, 260))
                                    pg.time.delay(t)

                                    box6 = 'o'
                                    turn = 'second'
                                    list[1][2] = 1
                                elif box6=='unoccupied' and turn == 'second':
                                    screen.blit(yImg, (490, 260))
                                    pg.time.delay(t)

                                    box6 = 'o'
                                    turn = 'first'
                                    list[1][2] = 2
                        if VII.collidepoint(pos):
                                if box7 == 'unoccupied' and turn == 'first':
                                    screen.blit(xImg, (30, 490))
                                    pg.time.delay(t)

                                    box7 = 'o'
                                    turn = 'second'
                                    list[2][0] = 1
                                elif box7=='unoccupied' and turn == 'second':
                                    screen.blit(yImg, (30, 490))
                                    pg.time.delay(t)

                                    box7 = 'o'
                                    turn = 'first'
                                    list[2][0]=2
                        if VIII.collidepoint(pos):
                                if box8 == 'unoccupied' and turn == 'first':
                                    screen.blit(xImg, (260, 490))
                                    pg.time.delay(t)

                                    box8 = 'o'
                                    turn = 'second'
                                    list[2][1] = 1
                                elif box8=='unoccupied' and turn == 'second':
                                    screen.blit(yImg, (260, 490))
                                    pg.time.delay(t)

                                    box8 = 'o'
                                    turn = 'first'
                                    list[2][1] = 2
                        if IX.collidepoint(pos):
                                if box9 == 'unoccupied' and turn == 'first':
                                    screen.blit(xImg, (490, 490))
                                    pg.time.delay(t)

                                    box9 = 'o'
                                    turn = 'second'
                                    list[2][2] = 1
                                elif box9=='unoccupied' and turn == 'second':
                                    screen.blit(yImg, (490, 490))
                                    pg.time.delay(t)

                                    box9 = 'o'
                                    turn = 'first'
                                    list[2][2] = 2
                show_score(x,y)
            pg.display.update()
pg.quit()