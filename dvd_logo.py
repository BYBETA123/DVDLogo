import pygame
# Define some variables
BLACK=(0,0,0)
WHITE=(255,255,255)
initial_x=684
initial_y=384
x_change=1
y_change=1
previous_x=1
previous_y=1
speed=0
# Setup
pygame.init()
screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window_width=screen.get_width()
window_height=screen.get_height()

originalimage=pygame.image.load('dvdlogo.jpg')
originalimagex=originalimage.get_width()
originalimagey=originalimage.get_height()
print("Original image size: ",originalimagex,"x",originalimagey)


secondimage=pygame.image.load('DVD_Logo.jpg')
secondimagex=secondimage.get_width()
secondimagey=secondimage.get_height()
print("Second image size: ",secondimagex,"x",secondimagey)

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Hide the mouse cursor
pygame.mouse.set_visible(0)
x=initial_x
y=initial_y
image=originalimage
screencolor=BLACK
imagechange=True
# -------- Main Program Loop -----------
while not done:
    up_coords=[x+112,y]
    left_coords=[x,y+52]
    right_coords=[x+224,y+52]
    bottom_coords=[x+112,y+104]
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done=True
    if right_coords[0]>=window_width:
        x_change=-1
    if bottom_coords[1]>=window_height:
        y_change=-1
    if left_coords[0]<=0:
        x_change=1
    if up_coords[1]<=0:
        y_change=1
    if speed==10:
        x+=x_change
        y+=y_change
        speed=0
    # if not(x_change==previous_x and y_change==previous_y):
    #     imagechange=not(imagechange)
    if (x_change!=previous_x and y_change!=previous_y):
        imagechange=not(imagechange)

    if imagechange==True:
        image=originalimage
        screencolor=BLACK
    else:
        image=secondimage
        screencolor=WHITE
    previous_x=x_change
    previous_y=y_change
    speed+=1
    coordinates=[x,y]
    screen.blit(image,coordinates)
    pygame.display.flip()
    screen.fill(screencolor)
# Close the window and quit.
pygame.quit()