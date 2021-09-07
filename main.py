from rpi_lcd import LCD
from gpiozero import Button
from src.main_menu import get_main_menu
from gpiozero import Button
from time import sleep

main_menu = get_main_menu()
main_menu.first_item()

lcd = LCD()
button = Button(26)

while True:
    lines = main_menu.get_data()
    lcd.text(lines[0], 1)
    lcd.text(lines[1], 2)
    
    button.wait_for_press()
    main_menu.next_item()

