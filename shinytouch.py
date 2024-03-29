import pygame
from pygame.locals import *
import sys
from PIL import Image, ImageColor, ImageDraw
import itertools
import os

fps = 120.0
width = 640
height = 480
input_type = "opencv"
camnum = 0

########END USEFUL CONFIGURATIOn########

mode = "image"
calibrate = False
box = 10
buildrange = False
imsrc = "cam"



canvas = Image.new("RGB", (width, height),(100,100,100))
canvaspix = canvas.load()
draw2 = ImageDraw.Draw(canvas)
touchconf = False

if input_type == "opencv":
  import opencv #this is important for capturing/displaying images
  from opencv import highgui 
  camera = highgui.cvCreateCameraCapture(camnum)
elif input_type == "videocapture":
  import VideoCapture
  camera = VideoCapture.Device(devnum=camnum)
  camera.setResolution(width,height)
else:
  print "No Camera Input type selected!"
  
w = 0
ytr = 0
ybr = 0


execfile("color.py")
execfile("tracking.py")
execfile("misc.py")



pygame.init()
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("ShinyTouch")
screen = pygame.display.get_surface()
clicks = 0
subavg = 0


while True:
    dolog = False
    getpix = False
    events = pygame.event.get()
    for event in events:
      if event.type == QUIT:
          sys.exit(0)
      if event.type == KEYDOWN:
        if event.unicode == "g":
          touchconf = True
          print "Move your finger around the visible area, click to stop"
        else:
          touchconf = False  
        if event.unicode == "d":
          mode = "draw"
        elif event.unicode == "i":
          mode = "image"
        elif event.unicode == "a":
          global autocal
          autocal = 1
        elif event.unicode == "q":
          sys.exit(0)
        elif event.unicode == "o":
          set_defaults()
          saveconfig()
        elif event.unicode == "b":
          if buildrange == True:
            buildrange = False
            print "Disabled Color Range Building"
          else:
            buildrange = True
            print "Enabled Color Range Building"
        elif event.unicode == "f":
          #pygame.display.set_mode((width,height),pygame.FULLSCREEN)
          pass
        elif event.unicode == "t":
          if mode == "transform":
            mode = ""
            print "Disabled Auto Transform"
          else:
            mode = "transform"
            print "Enabled Auto Transform"
        elif event.unicode == "s":
          import datetime
          canvas.save("imgs/purty"+str(datetime.datetime.now().isoformat()).replace(":","-")+".png","PNG")
          print "Saved Image"
        elif event.unicode == "c":
          calibrate = True
          print "Click Top Left Corner"
      if event.type == MOUSEBUTTONDOWN:
          touchconf = False
          if event.button == 3:
            dolog = True
          elif event.button == 2:
            canvas = Image.new("RGB", (width,height),(100,100,100))
            canvaspix = canvas.load()
            draw2 = ImageDraw.Draw(canvas)
            print "Reset Canvas"
            execfile("tracking.py")
            print "Loaded finger tracker core"
            execfile("color.py")
            print "Loaded Reflection Detection Algorithm"
            execfile("autoconf.py")
            print "Loaded Automatic Generated Configuration"
          elif event.button == 1 and calibrate == False and buildrange == True:
            #yes, i did something very stupid and ugly just to not edit the calibration code
            getpix = event.pos
            #buildrange = False
          elif event.button == 1 and calibrate == True:
            clicks += 1
            if clicks == 1:
              tl = event.pos[1]
              subavg = event.pos[0]
              xs = subavg
              print "Click Bottom Left Corner"
            elif clicks == 2:
              bl = event.pos[1]
              xs = (subavg + event.pos[0])/2
              print "Click Bottom Right Corner"
            elif clicks == 3:
              br = event.pos[1]
              subavg = event.pos[0]
              xe = subavg
              print "Click Top Right Corner"
            elif clicks == 4:
              tr = event.pos[1]
              xe = (subavg + event.pos[0])/2
              print "Done. To recalibrate, press c and then click Top Left corner again."
              calibrate = False
              saveconfig()
              clicks = 0
    im = get_image(dolog, getpix)
    pg_img = pygame.image.frombuffer(im.tostring(), im.size, im.mode)
    screen.blit(pg_img, (0,0))
    pygame.display.flip()
    #pygame.time.delay(int(1000 * 1.0/fps))

