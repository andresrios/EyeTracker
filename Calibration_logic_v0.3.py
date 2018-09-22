# -*- coding: cp1252 -*-
import pygame
import time
import random


## Some variables 
clock = pygame.time.Clock()
crashed = False
factor_text = 0.0000400
factor_radio = 0.0000180
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (240,240,60)
gray = (50,50,50)




#Set Window app position
x = 0
y = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


#Initialize pygame
pygame.init()


#Set full resolution
infoObject = pygame.display.Info()
display_width = (infoObject.current_w /1)
display_height = (infoObject.current_h /1)

print 'Screen resolution: x:%d, y:%d'%(display_width,display_height)


##display_width = 1366
##display_height = 768

##gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
##


#Set font size
def font_size(factor_text):
    area = display_width * display_height 
    font_size = int(factor_text * area)
    return font_size

##


#Set radio size
def radio_size():
    area = display_width * display_height
    radio_size = int(factor_radio * area)
    return radio_size

##


#Set window name
pygame.display.set_caption("Test xyz")
##


#Set up Text
def text_objects(text, font, text_color):
    textSurface = font.render(text, True, text_color)
    return textSurface, textSurface.get_rect()

def intro_text(text, text_color):
    largeText = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",font_size(factor_text))
    TextSurf, TextRect = text_objects(text, largeText, text_color)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

def cal_result_text(text, x, y, text_color):
    largeText = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",font_size(factor_text/3))
    TextSurf, TextRect = text_objects(text, largeText, text_color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
##


#Intro Text
intro_text("Sigue los círculos...", white)
pygame.display.update()
time.sleep(2)
gameDisplay.fill(black)

##for x in range(5,0,-1):
##    message_display(str(x))
##    pygame.display.update()
##    time.sleep(1)
##    gameDisplay.fill(black)
##


#Draw random circles

radio = radio_size()
number_of_points = 8 ##get from main

center_x0 = random.randint(radio,display_width/2)
center_y0 = random.randint(radio,display_height/2)

center_x1 = random.randint(display_width/2,display_width - radio)
center_y1 = random.randint(radio,display_height/2)

center_x2 = random.randint(radio,display_width/2)
center_y2 = random.randint(display_height/2, display_height - radio)

center_x3 = random.randint(display_width/2, display_width - radio)
center_y3 = random.randint(display_height/2, display_height - radio)


def draw_cal_circles(x, y):
    for r in range(radio,radio/3,-1):
        gameDisplay.fill(black)
        pygame.draw.circle(gameDisplay, white, (x, y), r)
        pygame.draw.circle(gameDisplay, red, (x, y), int(radio/3))
        pygame.display.update()
        time.sleep(0.050)
    
    for r in range(radio/3,radio,1):
        gameDisplay.fill(black)
        pygame.draw.circle(gameDisplay, white, (x, y), r)
        pygame.draw.circle(gameDisplay, red, (x, y), int(radio/3))
        pygame.display.update()
        time.sleep(0.050)
    time.sleep(1)
    gameDisplay.fill(black)


def show_cal_circles():

    count_p = 1
##    scr_per_x= 0.0
##    scr_per_y= 0.0

    for n in range(0,number_of_points/4):

        scr_per_x= (center_x0/float(display_width))*100
        scr_per_y= (center_y0/float(display_height))*100
        print 'Coordinates for point %d: x:%d, y:%d ||Screen Percentage: x:%.2f, y:%.2f' %(count_p,center_x0,center_y0,scr_per_x,scr_per_y)
        draw_cal_circles(center_x0, center_y0)
        count_p = count_p+1

        scr_per_x= (center_x1/float(display_width))*100
        scr_per_y= (center_y1/float(display_height))*100
        print 'Coordinates for point %d: x:%d, y:%d ||Screen Percentage: x:%.2f, y:%.2f' %(count_p,center_x1,center_y1,scr_per_x,scr_per_y)
        draw_cal_circles(center_x1, center_y1)
        count_p = count_p+1

        scr_per_x= (center_x2/float(display_width))*100
        scr_per_y= (center_y2/float(display_height))*100
        print 'Coordinates for point %d: x:%d, y:%d ||Screen Percentage: x:%.2f, y:%.2f' %(count_p,center_x2,center_y2,scr_per_x,scr_per_y)
        draw_cal_circles(center_x2, center_y2)
        count_p = count_p+1

        scr_per_x= (center_x3/float(display_width))*100
        scr_per_y= (center_y3/float(display_height))*100
        print 'Coordinates for point %d: x:%d, y:%d ||Screen Percentage: x:%.2f, y:%.2f' %(count_p,center_x3,center_y3,scr_per_x,scr_per_y)
        draw_cal_circles(center_x3, center_y3)
        count_p = count_p+1


show_cal_circles()

##



#Draw final points
circle0_x = 2*radio
circle0_y = display_height/9

circle1_x = display_width/2
circle1_y = display_height/9

circle2_x = display_width - (2*radio)
circle2_y = display_height/9

circle3_x = 2*radio
circle3_y = display_height/2

circle4_x = display_width/2
circle4_y = display_height/2

circle5_x = display_width - (2*radio)
circle5_y = display_height/2

circle6_x = 2*radio
circle6_y = display_height -(display_height/9)

circle8_x = display_width - (2*radio)
circle8_y = display_height -(display_height/9)

def draw_final_points():
    pygame.draw.circle(gameDisplay, white, (circle0_x , circle0_y), radio)
    pygame.draw.circle(gameDisplay, black, (circle0_x, circle0_y), int(radio/3))

    pygame.draw.circle(gameDisplay, white, (circle1_x , circle1_y), radio)
    pygame.draw.circle(gameDisplay, black, (circle1_x, circle1_y), int(radio/3))

    pygame.draw.circle(gameDisplay, white, (circle2_x , circle2_y), radio)
    pygame.draw.circle(gameDisplay, black, (circle2_x, circle2_y), int(radio/3))

    pygame.draw.circle(gameDisplay, white, (circle3_x , circle3_y), radio)
    pygame.draw.circle(gameDisplay, black, (circle3_x, circle3_y), int(radio/3))

    pygame.draw.circle(gameDisplay, white, (circle4_x , circle4_y), radio)
    pygame.draw.circle(gameDisplay, black, (circle4_x, circle4_y), int(radio/3))

    pygame.draw.circle(gameDisplay, white, (circle5_x , circle5_y), radio)
    pygame.draw.circle(gameDisplay, black, (circle5_x, circle5_y), int(radio/3))

    pygame.draw.circle(gameDisplay, white, (circle6_x , circle6_y), radio)
    pygame.draw.circle(gameDisplay, black, (circle6_x, circle6_y), int(radio/3))

    pygame.draw.circle(gameDisplay, white, (circle8_x , circle8_y), radio)
    pygame.draw.circle(gameDisplay, black, (circle8_x, circle8_y), int(radio/3))


draw_final_points()

def get_calibration_result():
    cal_result = random.randint(0, 5)
    return cal_result


#Show calibration results

recal_text_x = display_width - (display_width*0.584375)
recal_text_y = (2*display_height/3) + (display_height/6)
quit_text_x = display_width - (display_width*0.4152)
quit_text_y = (2*display_height/3) + (display_height/6)

def show_cal_results():
    #Draw rate points
    for m in range(1,6):
        rate_circle_x = (display_width/3) + m*((((2*display_width/3) - (display_width/3))/12))
        rate_circle_y = (2*display_height/3) + (display_height/30)
        pygame.draw.circle(gameDisplay, gray, (rate_circle_x , rate_circle_y), radio/2)
        ref_x_cal_result_text = rate_circle_x + (2*display_width/3)/6
    cal_result_text("Resultado de la calibración:", ref_x_cal_result_text, rate_circle_y, white)
    #End Draw rate points

    cal_result = get_calibration_result()

    cal_result_text("RECALIBRAR", recal_text_x, recal_text_y, white)
    cal_result_text("ACEPTAR", quit_text_x, quit_text_y, white)

    if cal_result == 0:
        cal_result_text("SIN CALIBRAR", ref_x_cal_result_text, (rate_circle_y + (display_height/30)), white)

    if cal_result == 1:
        for m in range(1,2):
            rate_circle_x = (display_width/3) + m*((((2*display_width/3) - (display_width/3))/12))
            rate_circle_y = (2*display_height/3) + (display_height/30)
            pygame.draw.circle(gameDisplay, yellow, (rate_circle_x , rate_circle_y), radio/2)
        cal_result_text("RECALIBRAR", ref_x_cal_result_text, (rate_circle_y + (display_height/30)), white)

    if cal_result == 2:
        for m in range(1,3):
            rate_circle_x = (display_width/3) + m*((((2*display_width/3) - (display_width/3))/12))
            rate_circle_y = (2*display_height/3) + (display_height/30)
            pygame.draw.circle(gameDisplay, yellow, (rate_circle_x , rate_circle_y), radio/2)
        cal_result_text("POBRE", ref_x_cal_result_text, (rate_circle_y + (display_height/30)), white)

    if cal_result == 3:
        for m in range(1,4):
            rate_circle_x = (display_width/3) + m*((((2*display_width/3) - (display_width/3))/12))
            rate_circle_y = (2*display_height/3) + (display_height/30)
            pygame.draw.circle(gameDisplay, yellow, (rate_circle_x , rate_circle_y), radio/2)
        cal_result_text("MODERADO", ref_x_cal_result_text, (rate_circle_y + (display_height/30)), white)

    if cal_result == 4:
        for m in range(1,5):
            rate_circle_x = (display_width/3) + m*((((2*display_width/3) - (display_width/3))/12))
            rate_circle_y = (2*display_height/3) + (display_height/30)
            pygame.draw.circle(gameDisplay, yellow, (rate_circle_x , rate_circle_y), radio/2)
        cal_result_text("BUENO", ref_x_cal_result_text, (rate_circle_y + (display_height/30)), white)

    if cal_result == 5:
        for m in range(1,6):
            rate_circle_x = (display_width/3) + m*((((2*display_width/3) - (display_width/3))/12))
            rate_circle_y = (2*display_height/3) + (display_height/30)
            pygame.draw.circle(gameDisplay, yellow, (rate_circle_x , rate_circle_y), radio/2)
        cal_result_text("PERFECTO", ref_x_cal_result_text, (rate_circle_y + (display_height/30)), white)


    print "done"
##

show_cal_results()


#While running
while not crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            pygame.quit()
            quit()


    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
##    print(event)

    cal_result = 4

    if recal_text_x+(display_width*0.1153/2) > mouse[0] > recal_text_x-(display_width*0.1153/2) and recal_text_y+(display_height*0.0186/2) > mouse[1] > recal_text_y-(display_height*0.0186/2):
        cal_result_text("RECALIBRAR", recal_text_x, recal_text_y, yellow)
        pygame.display.update()
        if click[0] == 1:
            show_cal_circles()
            draw_final_points()
            show_cal_results()
    else:
        cal_result_text("RECALIBRAR", recal_text_x, recal_text_y, white)
        pygame.display.update()

    if quit_text_x+(display_width*0.10/2) > mouse[0] > quit_text_x-(display_width*0.10/2) and quit_text_y+(display_height*0.0186/2) > mouse[1] > quit_text_y-(display_height*0.0186/2):
        cal_result_text("ACEPTAR", quit_text_x, quit_text_y, yellow)
        pygame.display.update()
        if click[0] == 1:
            pygame.quit()
            quit() 
    else:
        cal_result_text("ACEPTAR", quit_text_x, quit_text_y, white)
        pygame.display.update()

    clock.tick(60)

        
##    print "Alive..."
##    time.sleep(5)
    
