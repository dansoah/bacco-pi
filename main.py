from rpi_lcd import LCD
from gpiozero import Button
from src.main_menu.get_menu import get_main_menu
from gpiozero import Button, TonalBuzzer, DigitalOutputDevice
from gpiozero.tones import Tone
from time import sleep
from signal import signal, SIGTERM, SIGHUP, pause
import sys, traceback

main_menu = get_main_menu()
main_menu.first_item()

lcd = LCD()
lcd_display_transistor = DigitalOutputDevice(12)
lcd_display_transistor.on()

btn_next = Button(16, pull_up = True, bounce_time = 0.8)
btn_previous = Button(20, pull_up = True, bounce_time = 0.8)
btn_confirm = Button(21, pull_up = True, bounce_time = 0.8)
buzzer = TonalBuzzer(19)

def btn_next_press():
    main_menu.next_item()

    buzzer.play(Tone(550.0))
    sleep(0.1)
    buzzer.stop()
    sleep(0.2)

def btn_previous_press():
    main_menu.previous_item()

    buzzer.play(Tone(510.0))
    sleep(0.1)
    buzzer.stop()
    sleep(0.2)

def btn_confirm_press():
    main_menu.select_item()

    buzzer.play(Tone(590.0))
    sleep(0.1)
    buzzer.stop()
    sleep(0.2)

def hello():
    lcd.clear()
    sleep(0.6)
    lcd.display_enabled = True
    lcd.backlight_enabled = True

def goodbye():
    lcd.clear()
    lcd_display_transistor.off()
    sleep(0.6)
    lcd.display_enabled = False
    lcd.backlight_enabled = False
    sys.exit(1)

signal(SIGTERM, goodbye)
signal(SIGHUP, goodbye)

btn_next.when_pressed = btn_next_press
btn_previous.when_pressed = btn_previous_press
btn_confirm.when_pressed = btn_confirm_press

def main():
    while True:
        lines = main_menu.get_data()
        lcd.text(lines[0], 1)
        lcd.text(lines[1], 2)

if __name__ == "__main__":
    try:
        hello()
        main()
    except KeyboardInterrupt:
        print("Stopping due to keyboard iterruption")
    except Exception:
        print("Stopping due to an unhandled exception")
        traceback.print_exc(file=sys.stdout)
    goodbye()

    


    

