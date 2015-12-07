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
gray   = (128 , 128 , 128)

#   CAPTION   #
img = pygame.image.load('calendar.png')
img.set_colorkey(white)
pygame.display.set_icon(img)
pygame.display.set_caption("Calendar")
pygame.mouse.set_visible(1)

#   VARIABLES   #
dateNow = str(datetime.now().date())
year = dateNow[0:4]
month = dateNow[5:7]
day = dateNow[9:11]
dateNow = [year,month,day]
month = int(month)
if month == 12:
    prefix = 'DEC'
elif month == 11:
    prefix = 'NOV'
elif month == 10:
    prefix = 'OCT'
elif month == 9:
    prefix = 'SEP'
elif month == 8:
    prefix = 'AUG'
elif month == 7:
    prefix = 'JUL'
elif month == 6:
    prefix = 'JUN'
elif month == 5:
    prefix = 'MAY'
elif month == 4:
    prefix = 'APR'
elif month == 3:
    prefix = 'MAR'
elif month == 2:
    prefix = 'FEB'
elif month == 1:
    prefix = 'JAN'
text = prefix + ' ' + year
del year, month, day, prefix

'''                      SUN  MON   TUE  WED  THU  FRI  SAT              '''
appointments = [     [   [],[],[],[],[],[],[]   ],#WEEK 1
                     [   [],[],[],[],[],[],[]   ],#WEEK 2
                     [   [],[],[],[],[],[],[]   ],#WEEK 3
                     [   [],[],[],[],[],[],[]   ],#WEEK 4
                     [   [],[],[],[],[],[],[]   ] #WEEK 5
]

# FUNCTIONS   #
def typetext(font, size, text, x, y, alias, color, upside):
    defined_font = pygame.font.Font(font, size)
    stamp = defined_font.render(text, alias, color)
    if upside:
        stamp = pygame.transform.flip(stamp, False, True)
    screen.blit(stamp, [x,y])
def padZero(num):
    if int(num) < 10:
        return '0' + str(num)
    return num

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
days = strDays
del strDays

# -------- Main Program Loop -----------
while not done:
    screen.fill(white)
    mouse = pygame.mouse.get_pos()
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            for y in range(len(days)):
                index = [y,None]
                y = (y) * 75 + 125
                for x in range(7):
                    index[1] = x
                    x = (x) * 100 + 50
                    if (mouse[0] > x and mouse[0] < x + 100) and (mouse[1] > y and mouse[1] < y + 75):
                        if pygame.mouse.get_pressed()[0]:
                            print(index)
                            inputWrite = input("Appointment Name: ")
                            if inputWrite:
                                appointments[index[0]][index[1]].append(inputWrite)
                            else:
                                print("You cannot set an appointment with no name.")
                            del inputWrite
                        else:
                            print("Appointments / Events:")
                            if appointments[index[0]][index[1]]:
                                for appointment in appointments[index[0]][index[1]]:
                                    print(appointment)
                            else:
                                print("No Appointments / Events set on this date.")
            del index

    pygame.draw.rect(screen,(0,200,0),[50,25,700,50])
    for y in range(len(days)):
        y = (y) * 75 + 125
        for x in range(7):
            x = (x) * 100 + 50
            pygame.draw.rect(screen,black,[x,y,100,75],1)
    for y in range(len(days)):
        pos = [(y) * 75 + 125,'']
        for x in range(7):
            pos[1] = (x) * 100 + 50
            #print(pos)
            if appointments[y][x]:
                pygame.draw.circle(screen,red,[pos[1]+10,pos[0]+60],3)
#pygame.draw.rect(screen,black,[x,y,100,75],1)
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
    for weekNum in range(len(days)):
        for dayNum in range(len(days[week])):
            if days[weekNum][dayNum][5:7] != dateNow[1]:
                typetext('font.TTF', 50, days[weekNum][dayNum][8:12], dayNum * 100 + 75, weekNum * 75 + 135, True, (128,128,128), False)
            elif str(days[weekNum][dayNum][8:12]) == padZero(dateNow[2]):
                typetext('font.TTF', 50, days[weekNum][dayNum][8:12], dayNum * 100 + 75, weekNum * 75 + 135, True, red, False)
            else:
                typetext('font.TTF', 50, days[weekNum][dayNum][8:12], dayNum * 100 + 75, weekNum * 75 + 135, True, black, False)
    typetext('font.TTF', 50, text, 315, 25, True, black, False)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(100)
