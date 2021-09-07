from rpi_lcd import LCD
from gpiozero import Button
from src.main_menu import get_main_menu
from gpiozero import Button, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

main_menu = get_main_menu()
main_menu.first_item()

lcd = LCD()
btn_next = Button(26)
buzzer = TonalBuzzer(19)

def btn_next_press():
    main_menu.next_item()

    buzzer.play(Tone(550.0))
    sleep(0.1)
    buzzer.stop()

def btn_previous_press():
    main_menu.previous_item()

    buzzer.play(Tone(510.0))
    sleep(0.1)
    buzzer.stop()

def btn_confirm_press():
    main_menu.previous_item()

    buzzer.play(Tone(590.0))
    sleep(0.1)
    buzzer.stop()

btn_next.when_pressed = btn_next_press

while True:
    lines = main_menu.get_data()
    lcd.text(lines[0], 1)
    lcd.text(lines[1], 2)

