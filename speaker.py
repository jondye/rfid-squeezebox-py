from machine import Pin, Timer
import time


NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392
NOTE_A4 = 440
NOTE_B4 = 494
NOTE_C5 = 523


def ack_sound(pwm):
    pwm.duty(512)
    pwm.freq(int(NOTE_C4))
    time.sleep(0.1)
    pwm.duty(0)


def success_sound(pwm):
    pwm.duty(512)
    pwm.freq(int(NOTE_C4))
    time.sleep(0.1)
    pwm.freq(int(NOTE_F4))
    time.sleep(0.1)
    pwm.freq(int(NOTE_C5))
    time.sleep(0.1)
    pwm.duty(0)


def fail_sound(pwm):
    pwm.duty(512)
    pwm.freq(int(NOTE_C4))
    time.sleep(0.4)
    pwm.duty(0)


def mario(p):
    tune = [2637, 2637, 0, 2637, 0, 2093, 2637, 0, 3136, 0, 0, 0, 1568, 0, 0,
            0, 2093, 0, 0, 1568, 0, 0, 1319, 0, 0, 1760, 0, 1976, 0, 1865,
            1760, 0, 1568, 2637, 0, 3136, 3520, 0, 2794, 3136, 0, 2637, 0,
            2093, 2349, 1976, 0, 0, 2093, 0, 0, 1568, 0, 0, 1319, 0, 0, 1760,
            0, 1976, 0, 1865, 1760, 0, 1568, 2637, 0, 3136, 3520, 0, 2794,
            3136, 0, 2637, 0, 2093, 2349, 1976, 0, 0]
    for note in tune:
        if note == 0:
            p.duty(0)
        else:
            p.duty(512)
            p.freq(int(note/10))
        time.sleep(0.15)
