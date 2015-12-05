import pygame
from datetime import datetime
import calendar

pygame.init()

#   SCREEN SET   #
screen_size=[800,550]
screen = pygame.display.set_mode(screen_size)

#   COLORS   #
white  = (255 , 255 , 255)
black  = (000 , 000 , 000)
red    = (255 , 000 , 000)
green  = (000 , 255 , 000)
blue   = (000 , 000 , 255)
yellow = (255 , 255 , 000)
purple = (255 , 000 , 255)

#   CAPTION   #
'''pygame.display.set_icon(pygame.image.load(None))'''
pygame.display.set_caption("Calendar")
pygame.mouse.set_visible(1)

#   VARIABLES   #
dateNow = str(datetime.now().date())
year = dateNow[0:4]
month = dateNow[5:7]
day = dateNow[9:11]
dateNow = [year,month,day]
del year, month, day

# FUNCTIONS   #
def typetext(font, size, text, x, y, alias, color, upside):
    defined_font = pygame.font.Font(font, size)
    stamp = defined_font.render(text, alias, color)
    if upside:
        stamp = pygame.transform.flip(stamp, False, True)
    screen.blit(stamp, [x,y])

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
strDays = []
clock = pygame.time.Clock()
startWeek = calendar.Calendar(calendar.SUNDAY)
days = startWeek.monthdatescalendar(int(dateNow[0]),int(dateNow[1]))
for week in range(len(days)):
    strDays.append([])
    for day in range(7):
        strDays[week].append(str(days[week][day]))
days =  strDays
del strDays

# -------- Main Program Loop -----------
while not done:
    screen.fill(white)
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    pygame.draw.rect(screen,(0,200,0),[50,25,700,50])
    for y in range(len(days)):
        y = (y) * 75 + 125
        for x in range(7):
            x = (x) * 100 + 50
            pygame.draw.rect(screen,black,[x,y,100,75],1)
    for x in range(7):
        x = x * 100 + 50
        pygame.draw.rect(screen,black,[x,75,100,50],1)
    typetext('font.TTF', 50, "SUN", 60 , 75, True, black, False)
    typetext('font.TTF', 50, "MON", 160 , 75, True, black, False)
    typetext('font.TTF', 50, "TUE", 260 , 75, True, black, False)
    typetext('font.TTF', 50, "WED", 360 , 75, True, black, False)
    typetext('font.TTF', 50, "THU", 460 , 75, True, black, False)
    typetext('font.TTF', 50, "FRI", 570 , 75, True, black, False)
    typetext('font.TTF', 50, "SAT", 660 , 75, True, black, False)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(100)
