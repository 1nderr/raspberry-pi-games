import pygame
import time
import random
from sys import exit
import RPi.GPIO as GPIO

number = 1
score = 0

GPIO.setmode(GPIO.BCM)
IN = GPIO.IN
btnRed = 4
btnGreen = 17
btnBlue = 27
btnYellow = 22
GPIO.setup(btnRed, IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnGreen, IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnBlue, IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnYellow, IN, pull_up_down = GPIO.PUD_UP)

red = (255, 0, 0)
blue = (33, 110, 255)
yellow = (255, 255, 0)
green =  (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
width = 800
height = 400
size = (width, height)
screen = pygame.display.set_mode(size)
fontpath = "/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf"
myfont = pygame.font.SysFont(fontpath, 200)
myfont2 = pygame.font.SysFont(fontpath, 85)
myfont3 = pygame.font.SysFont(fontpath, 78)
myfont4 = pygame.font.SysFont(fontpath, 60)
text = myfont3.render("Press the                     to Start!", 1, white)
text2 = myfont3.render("            Red Button          ", 1, red)
text_rect = text.get_rect(center = (width/2, height/2))
text2_rect = text2.get_rect(center = (width/2, height/2))
screen.blit(text, text_rect)
screen.blit(text2, text2_rect)
pygame.display.flip()
GPIO.wait_for_edge(btnRed, GPIO.FALLING)
screen.fill(black)
pygame.display.flip()

def correct():
    text = myfont.render("Correct!", 1, green)
    text_rect = text.get_rect(center = (width/2, height/2))
    screen.fill(black)
    pygame.display.flip()
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(1)
    screen.fill(black)
    pygame.display.flip()

def wrong():
    text = myfont.render("Wrong!", 1, red)
    text_rect = text.get_rect(center = (width/2, height/2))
    screen.fill(black)
    pygame.display.flip()
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(1)
    screen.fill(black)
    pygame.display.flip()

def question(number):
    text = myfont2.render("What Was Color Number %r?" % number, 1, white)
    text_rect = text.get_rect(center = (width/2, height/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    number = number + 1
    return number

def word_display():
    rand = random.randint(1, 12)
    if rand == 1:
        color = red
        word = "Green"
    
    elif rand == 2:
        color = blue
        word = "Yellow"
    
    elif rand == 3:
        color = yellow
        word = "Blue"
    
    elif rand == 4:
        color = green
        word = "Red"
        
    elif rand == 5:
        color = red
        word = "Yellow"
    
    elif rand == 6:
        color = blue
        word = "Red"
    
    elif rand == 7:
        color = yellow
        word = "Red"
    
    elif rand == 8:
        color = green
        word = "Yellow"
        
    elif rand == 9:
        color = red
        word = "Blue"
    
    elif rand == 10:
        color = blue
        word = "Green"
    
    elif rand == 11:
        color = yellow
        word = "Green"
    
    elif rand == 12:
        color = green
        word = "Blue"

    text = myfont.render(word, 1, color)
    text_rect = text.get_rect(center = (width/2, height/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(.5)
    screen.fill(black)
    pygame.display.flip()
    return color

def button_answer(answer):
    while True:
        if not GPIO.input(btnRed) and answer == red:
            correct()
            score_up = 1
            return score_up
            break
    
        elif not GPIO.input(btnBlue) and answer == blue:
            correct()
            score_up = 1
            return score_up
            break
    
        elif not GPIO.input(btnGreen) and answer == green:
            correct()
            score_up = 1
            return score_up
            break
    
        elif not GPIO.input(btnYellow) and answer == yellow:
            correct()
            score_up = 1
            return score_up
            break

        elif not GPIO.input(btnRed) and answer != red:
            wrong()
            score_down = 0
            return score_down
            break

        elif not GPIO.input(btnYellow) and answer != yellow:
            wrong()
            score_down = 0
            return score_down
            break
    
        elif not GPIO.input(btnGreen) and answer != green:
            wrong()
            score_down = 0
            return score_down
            break
    
        elif not GPIO.input(btnBlue) and answer != blue:
            wrong()
            score_down = 0
            return score_down
            break
        
def levelone(number, score):
    text = myfont.render("Level 1", 1, white)
    text_rect = text.get_rect(center = (width/2, height/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(1)
    screen.fill(black)
    pygame.display.flip()
    time.sleep(.3)
    
    color1 = word_display()
    time.sleep(.5)
    color2 = word_display()
    time.sleep(.5)
    color3 = word_display()
    time.sleep(.5)
    color4 = word_display()
    time.sleep(.5)

    score_text(score)
    
    number = question(number)
    scorecheck = button_answer(color1)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
    elif scorecheck == 0:
        score = score - 1
        score_text(score)
    
    number = question(number)
    scorecheck = button_answer(color2)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
    elif scorecheck == 0:
        score = score - 1
        score_text(score)
        
    number = question(number)
    scorecheck = button_answer(color3)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
    elif scorecheck == 0:
        score = score - 1
        score_text(score)
        
    number = question(number)
    scorecheck = button_answer(color4)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
    elif scorecheck == 0:
        score = score - 1
        score_text(score)
    return score

def exit_screen():
    screen.fill(black)
    pygame.display.flip()
    text = myfont.render("Exiting...", 1, white)
    text_rect = text.get_rect(center = (width/2, height/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(1)
    GPIO.cleanup()
    pygame.quit()
    exit()

def level_two(number, score):
    screen.fill(black)
    pygame.display.flip()
    text = myfont.render("Level 2", 1, white)
    text_rect = text.get_rect(center = (width/2, height/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(1)
    screen.fill(black)
    pygame.display.flip()
    time.sleep(.3)
    
    color1 = word_display()
    time.sleep(.5)
    color2 = word_display()
    time.sleep(.5)
    color3 = word_display()
    time.sleep(.5)
    color4 = word_display()
    time.sleep(.5)
    color5 = word_display()
    time.sleep(.5)
    color6 = word_display()
    time.sleep(.5)
    color7 = word_display()
    time.sleep(.5)
    color8 = word_display()
    time.sleep(.5)

    score_text(score)
    
    number = question(number)
    scorecheck = button_answer(color1)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
    elif scorecheck == 0:
        score = score - 1
        score_text(score)
    
    number = question(number)
    scorecheck = button_answer(color2)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
    elif scorecheck == 0:
        score = score - 1
        score_text(score)
        
    number = question(number)
    scorecheck = button_answer(color3)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
    elif scorecheck == 0:
        score = score - 1
        score_text(score)
        
    number = question(number)
    scorecheck = button_answer(color4)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
    elif scorecheck == 0:
        score = score - 1
        score_text(score)
    
    number = question(number)
    scorecheck = button_answer(color5)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
    elif scorecheck == 0:
        score = score - 1
        score_text(score)
    
    number = question(number)
    scorecheck = button_answer(color6)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
    elif scorecheck == 0:
        score = score - 1
        score_text(score)
        
    number = question(number)
    scorecheck = button_answer(color7)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
        
    number = question(number)
    scorecheck = button_answer(color8)
    if scorecheck == 1:
        score = score + 1
        score_text(score)
    return score
    
def score_text(score):
    text = myfont4.render("Score: %r" % score, 1, white)
    screen.blit(text, (10,0))
    pygame.display.flip()

    
final_score = levelone(number, score)

if final_score >= 4:
    screen.fill(black)
    pygame.display.flip()
    text = myfont2.render("You Scored %r. Next Level!" % final_score, 1, white)
    text_rect = text.get_rect(center = (width/2, height/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(2)
    final_score = level_two(number, score)
    
    if final_score == 8:
        screen.fill(black)
        pygame.display.flip()
        text = myfont2.render("You Scored %r. You Win!!!" % final_score, 1, white)
        text_rect = text.get_rect(center = (width/2, height/2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(2)
        exit_screen()
        
    else:
        screen.fill(black)
        pygame.display.flip()
        text = myfont2.render("You Scored %r. You Lose!" % final_score, 1, white)
        text_rect = text.get_rect(center = (width/2, height/2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(2)
        exit_screen()

else:
    screen.fill(black)
    pygame.display.flip()
    text = myfont2.render("You Scored %r. You Lose!" % final_score, 1, white)
    text_rect = text.get_rect(center = (width/2, height/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(2)
    exit_screen()

