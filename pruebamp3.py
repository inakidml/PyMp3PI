import pygame
from pygame.locals import *
import time
pygame.init()
#pygame.display.set_caption("")
screen = pygame.display.set_mode((800, 400), 0, 32)
pygame.mixer.init()
pygame.mixer.music.load("2.mp3")

def texts(texto):
   font=pygame.font.SysFont(None ,32)
   text=font.render(texto, True,(255,255,255))
   textrect = text.get_rect()
   textrect.centerx = screen.get_rect().centerx
   textrect.centery = screen.get_rect().centery
   screen.fill((0, 0, 0))
   screen.blit(text, textrect)
   pygame.display.flip()
texts("en marcha")
pygame.mixer.music.play()


while True: #pygame.mixer.music.get_busy() == True:
#    print "while"
#    texts("while")
    for event in pygame.event.get():
	print event	
	if event.type == KEYDOWN:
		if event.key == K_p:
	    	    texts("playing")
		    pygame.mixer.music.play()
		if event.key == K_s:
		    texts("stop")
		    pygame.mixer.music.stop()
    time.sleep(0.005)
