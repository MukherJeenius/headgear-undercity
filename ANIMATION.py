from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI, PWM

# Constants
SPI_SPEED = 10000000
DC_PIN = Pin(6)
CS_PIN = Pin(17)
RST_PIN = Pin(7)
BACK_COLOR = color565(0, 0, 0)
RECT_COLOR = color565(255, 0, 0)
POLY_COLOR = color565(0, 64, 255)
CIRC_COLOR = color565(0, 255, 0)
ELLP_COLOR = color565(255, 0, 0)
TEXT_COLOR = color565(255, 255, 255)

DISPLAY_WIDTH = 240
DISPLAY_HEIGHT = 320

# Initialize SPI and Display
spi = SPI(1, baudrate=SPI_SPEED, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=DC_PIN, cs=CS_PIN, rst=RST_PIN)

# Setup PWM for backlight brightness control
BL_PIN = 10  # Change to your actual backlight pin
pwm = PWM(Pin(BL_PIN))
pwm.freq(1000)  # 1 kHz frequency

def set_brightness(level):
    """
    level: int from 0 (off) to 1023 (max brightness)
    """
    if level < 0:
        level = 0
    elif level > 1023:
        level = 1023
    # Scale 0-1023 to 0-65535 for 16-bit PWM duty cycle
    pwm.duty_u16(level * 64)

# Draw shapes
def draw_rectangles():
    for x in range(0, 225, 15):
        display.fill_rectangle(x, 0, 15, 227, RECT_COLOR)

def draw_polygons():
    display.fill_polygon(7, 120, 120, 100, POLY_COLOR)
    sleep(1)
    display.draw_polygon(3, 120, 286, 30, POLY_COLOR, rotate=15)
    sleep(3)

def draw_circles():s
    display.fill_circle(132, 132, 70, CIRC_COLOR)
    sleep(1)
    display.draw_circle(132, 96, 70, color565(0, 0, 255))
    sleep(1)

def draw_ellipses():
    display.fill_ellipse(96, 96, 30, 16, ELLP_COLOR)
    sleep(1)
    display.draw_ellipse(96, 256, 16, 30, color565(255, 255, 0))

# Infinite animation loop with brightness adjustment
brightness = 0
direction = 1  # 1 to increase, -1 to decrease

while True:
    set_brightness(brightness)

    display.clear(BACK_COLOR)
    draw_rectangles()
    sleep(1)

    display.clear(BACK_COLOR)
    draw_polygons()
    sleep(1)

    display.clear(BACK_COLOR)
    draw_circles()
    sleep(1)

    display.clear(BACK_COLOR)
    draw_ellipses()
    sleep(1)

    brightness += direction * 100  
    if brightness >= 5000:
        brightness = 1023
        direction = -1
    elif brightness <= 0:
        brightness = 0
        direction = 1
