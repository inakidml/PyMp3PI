
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
import time


def texts(texto):
   font=pygame.font.SysFont(None ,32)
   text=font.render(texto, True,(255,255,255))
   textrect = text.get_rect()
   textrect.centerx = screen.get_rect().centerx
   textrect.centery = screen.get_rect().centery
   screen.fill((0, 0, 0))
   screen.blit(text, textrect)
   pygame.display.flip()
#texts("en marcha")

def play():
    texts("playing sound")
    sound.play()
#    texts("playing music")
#    pygame.mixer.music.play()

def stop():
    texts("stop")
    sound.stop()
#    pygame.mixer.music.stop()
#    pygame.mixer.init()
#    pygame.mixer.music.load("2.mp3")
def mi_callback(pin):
    texts("Boton pulsado")
    play()
    time.sleep(2)
    GPIO.remove_event_detect(pin)
    GPIO.add_event_detect(18, GPIO.RISING, callback=mi_callback, bouncetime=200)
	
GPIO.setmode(GPIO.BOARD)# Ponemos la placa en modo BOARD -> identificacion de los pimes por numero de pin del conector(no puerto GPIO)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)# Configuramos el pin 18 (GPIO 24) como entrada y resistencia pull UP -> Pulsador entre pin y masa (Pull Down pulsador entre +3.3v y pin)
# Configuramos una interrupcion para cuando se aprete el boton
GPIO.add_event_detect(18, GPIO.RISING, callback=mi_callback, bouncetime=200)

pygame.init()
pygame.display.set_caption("PyMp3PI")
screen = pygame.display.set_mode((800, 800), 0, 32)
pygame.mixer.init()
#pygame.mixer.music.load("2.mp3")
#print "music loaded"
sound = pygame.mixer.Sound("1.wav")
#print "sound loaded"
#pygame.mixer.music.play()
#print "playing music"
loop = True

while loop: #pygame.mixer.music.get_busy() == True:
#    print "while"
#    texts("while")
    for event in pygame.event.get():
#       print event     
        if event.type == KEYDOWN:
                if event.key == K_p:
                    play()
                if event.key == K_s:
                    stop()
                if event.key == K_q:
                    loop = False
    time.sleep(0.005)


