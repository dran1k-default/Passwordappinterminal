import random
from turtledemo.penrose import start

from main_func import start_screen, random_password_generation, create_password_manualy, session_password_viewer,main_password_base,all_passwords_viewer,password_delete

while True:

    start_screen_result = start_screen()
    if start_screen_result == 1:
        random_password_generation()

    if start_screen_result == 2:
        create_password_manualy()

    if start_screen_result == 3:
        all_passwords_viewer()



    if start_screen_result == 4:
        session_password_viewer()

    if start_screen_result == 5:
        password_delete()


    if start_screen_result == 6:
        break




