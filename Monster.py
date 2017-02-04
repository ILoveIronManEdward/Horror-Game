import pygame
import Tkinter
import time
import random
import sys

pygame.init()

bg = pygame.image.load("background/testing/monsterBG/bg.png")
rpsInstW = [pygame.image.load("monsters/rps/rock.jpg"),pygame.image.load("monsters/rps/paper.jpg"),pygame.image.load("monsters/rps/scissors.jpg")]
rpsInstB = [pygame.image.load("monsters/rps/rock2.jpg"),pygame.image.load("monsters/rps/paper2.jpg"),pygame.image.load("monsters/rps/scissors2.jpg")]
font = pygame.font.SysFont("Ariel", 50)
sleeptime = 1.5

LoseScare = [pygame.image.load("scares/a.jpg"), pygame.image.load("scares/b.jpg"), pygame.image.load("scares/c.jpg"), pygame.image.load("scares/d.jpg"), pygame.image.load("scares/e.jpg"), pygame.image.load("scares/f.jpg"), pygame.image.load("scares/g.jpg")]

def dialog(display, Self, Oppo, result, scrX, scrY):
    label = font.render("You Chose " + Self, 1, (255, 255, 255))
    label2 = font.render("Opponent Chose " + Oppo, 1, (255, 255, 255))
    label3 = font.render(result, 1, (255, 255, 255))

    pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY))
    display.blit(label, (50, scrY - 190))
    pygame.display.update()
    time.sleep(sleeptime)

    pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY))
    display.blit(label2, (50, scrY - 190))
    pygame.display.update()
    time.sleep(sleeptime)

    pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY))
    display.blit(label3, (50, scrY - 190))
    pygame.display.update()
    time.sleep(sleeptime)

    if result == "You Lose" or result == "Tie":
        scare = random.randint(0, 3)
        display.blit(LoseScare[scare], (0, 0))
        pygame.display.update()
        time.sleep(0.5)

def WinOrLose(char, oppo):
    if char == oppo:
        result = "Tie"          #Tie
    elif char + 1 == oppo or char - 2 == oppo:
        result = "You Lose"          #Lose
    elif oppo + 1 == char or oppo - 2 == char:
        result = "You Win"          #Win
    return result
    

def MonsterMeet(name, Mstats, Minst, Chealth, Cbd, Cinv, CitemStats, scrX, scrY, display):
    Chp = Chealth
    Mhealth = Mstats[0]
    over = 0
    result2 = 2
    rpsCoor = [[12, scrY - 200],[294, scrY - 200],[576, scrY - 200]]
    for i in range(4):
        pygame.draw.rect(display, (0, 0, 0), (0, 0, scrX, scrY))
        pygame.display.update()
        time.sleep(0.1)
        pygame.draw.rect(display, (255, 255, 255), (0, 0, scrX, scrY))
        pygame.display.update()
        time.sleep(0.1)
    label = font.render("Met " + name + "!", 1, (255, 255, 255))
    display.blit(bg, (0, 0))
    display.blit(Minst, (400, 300))
    pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY))
    display.blit(label, (50, scrY - 190))
    pygame.display.update()
    time.sleep(sleeptime)
    rpsWBlit = [1, 0, 0]

    while over != 1:
        Cchoice = 0
        while Cchoice == 0:
            time.sleep(0.1)
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                nextW = rpsWBlit.index(1) + 1
                rpsWBlit[nextW - 1] = 0 
                if nextW == 3:
                    nextW = 0
                rpsWBlit[nextW] = 1

            elif keys[pygame.K_LEFT]:
                nextW = rpsWBlit.index(1) - 1
                rpsWBlit[nextW + 1] = 0
                if nextW == -1:
                    nextW = 2
                rpsWBlit[nextW] = 1

            elif keys[pygame.K_e]:
                CchoiceN = rpsWBlit.index(1)
                if CchoiceN == 0:
                    Cchoice = "Rock"
                elif CchoiceN == 1:
                    Cchoice = "Paper"
                elif CchoiceN == 2:
                    Cchoice = "Scissors"
            pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY))
            for index, a in enumerate(rpsWBlit):
                if rpsWBlit[index] == 1:
                    display.blit(rpsInstW[index], rpsCoor[index])
                else:
                    display.blit(rpsInstB[index], rpsCoor[index])
            pygame.display.update()
        MchoiceN = random.randint(0, 2)
        if MchoiceN == 0:
            Mchoice = "Rock"
        elif MchoiceN == 1:
            Mchoice = "Paper"
        elif MchoiceN == 2:
            Mchoice = "Scissors"
        result = WinOrLose(CchoiceN, MchoiceN)
        dialog(display, Cchoice, Mchoice, result, scrX, scrY)
        biggest = 0
        if result == "You Win":
            if len(CitemStats) != 0:
                Mhealth -= Cbd + int(CitemStats[-1])          #Character's weapons
            else:
                Mhealth -= Cbd
        elif result == "You Lose":
            Chp -= Mstats[1]
        elif result == "Tie":
            Chp -= 20
            Mhealth -= 20
        display.blit(bg, (0, 0))
        display.blit(Minst, (400, 300))
        if result == "Win":
            pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY))
            label3 = font.render("You attack with " + Cinv[biggest], 1, (255, 255, 255))
            display.blit(label3, (50, scrY - 190))
            pygame.display.update()
        time.sleep(sleeptime)
        pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY))
        label4 = font.render("Your HP changed to " + str(Chp) + ", " + name + "'s HP changed to " + str(Mhealth), 1, (255, 255, 255))
        display.blit(label4, (50, scrY - 190))
        pygame.display.update()
        time.sleep(sleeptime)
        if Mhealth <= 0:
            pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY))
            label5 = font.render(name + " was defeated.", 1, (255, 255, 255))
            display.blit(label5, (50, scrY - 190))
            pygame.display.update()
            time.sleep(sleeptime)
            over = 1
            result2 = 1
        elif Chp <= 0:
            pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY))
            label6 = font.render("You were killed by " + name + ".", 1, (255, 255, 255))
            display.blit(label6, (50, scrY - 190))
            pygame.display.update()
            time.sleep(sleeptime)
            over = 1
            result2 = 0
    return result2    
