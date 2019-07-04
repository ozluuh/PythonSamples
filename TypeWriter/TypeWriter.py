import sys
from time import sleep
try:
    import pygame
except ImportError:
    print('Unable to import pygame. Make sure you have pygame installed.')
    sys.exit()

pygame.mixer.init()
snd_keypress = pygame.mixer.Sound('key.wav')
snd_ding = pygame.mixer.Sound('ding.wav')
snd_quit = pygame.mixer.Sound('select.wav')

cont = 0
speed = 0.3
if len(sys.argv) > 1:
    sample = sys.argv[1]
else:
    sample = 'Hello, stranger.\nWelcome to my imaginary world!\n\
If you want to simulate the effect with a text of your choice,\n\
try passing an argument - using the quotation mark (")\n\
to identify the beginning and end of the text - after the script name.\n\nGood Luck!'

try:
    for char in sample:
        cont = cont + 1
        sys.stdout.write(char)
        if char != ' ' and char != '\n':
            sys.stdout.flush()
            snd_keypress.play()
        if cont == len(sample):
            raise KeyboardInterrupt
        if char == '\n':
            sleep(speed)
            snd_ding.play()
            sleep(speed + 0.6)
        else:
            sleep(speed)

except KeyboardInterrupt:
    sleep(speed)
    snd_quit.play()
    sleep(speed + 0.8)
    pygame.quit()
    sys.exit('\n\nBye\n\ne.g. python SampleTypeWriter.py "Not enough cash, stranger!"\n')