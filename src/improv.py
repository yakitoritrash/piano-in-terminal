import termios, sys, tty
import pygame
def improv():
    pygame.mixer.init()
    key_map = {
            'a': pygame.mixer.Sound("assets/c1.wav"),
            's': pygame.mixer.Sound("assets/d1.wav"),
            'd': pygame.mixer.Sound("assets/e1.wav"),
            'f': pygame.mixer.Sound("assets/f1.wav"),
            'v': pygame.mixer.Sound("assets/g1.wav"),
            'b': pygame.mixer.Sound("assets/a1.wav"),

            'n': pygame.mixer.Sound("assets/c2.wav"),
            'j': pygame.mixer.Sound("assets/d1s.wav"),
            'k': pygame.mixer.Sound("assets/f1s.wav"),
            'l': pygame.mixer.Sound("assets/g1s.wav"),
            ';': pygame.mixer.Sound("assets/a1s.wav"),

            }
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno());
    try:
        while (True):
            key = sys.stdin.read(1)
            if key in key_map:
                key_map[key].play()
            elif key == "q":
                break;
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        print()

