# A bouncing ball animation combined with fizz-buzz logic to make this project awesome!

#importing library
import pygame
# initializing pygame gui
pygame.init()
# setting the screen
screen = pygame.display.set_mode((1000,500))
red = 22, 70, 70
screen.fill(red)
#some variable initializations
moveX = 1
moveY = 1
x = 100
y = 100
num = 1
# loop to keep GUI window open
while True:
    for event in pygame.event.get():
        # close window logic
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # animation on screen
    pygame.draw.circle(screen, (111, 200, 30), (x, y), 80)


    pygame.display.set_caption('Fizz-buzz motion')
    pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    # fizz-buzz logic
    if(num%3 and num%5==0):
        textsurface = myfont.render('FizzBuzz', False, (225,23,58))
        screen.blit(textsurface,(x-30,y-45))
    elif(num%3 or num%5==0):
        textsurface = myfont.render('Fizz', False, (245,194,41))
        screen.blit(textsurface,(x-45,y-45))
    else:
        textsurface = myfont.render('Buzz', False, (255,239,245))
        screen.blit(textsurface,(x-30,y-30))

    # moving ball and bounce back logic
    num+=1
    pygame.display.update()
    screen.fill(red)
    x += moveX
    y += moveY
    if x > 1000-50:
        moveX =- 1
    elif y > 500-50:
        moveY =- 1
    elif x < 50:
        moveX = 1
    elif y < 50:
        moveY = 1
