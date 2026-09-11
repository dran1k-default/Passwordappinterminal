
import random
import string
main_password_base = {}
password_symbols = string.ascii_letters + string.digits + string.punctuation
def start_screen():
    print("[1]Generate a random password (recommended)")
    print("[2]Create a password")
    print("[3]View passwords")
    print("[4]View passwords added in this session ")
    print("[5]Exit")
    user_input = int(input("select an option please: "))
    return user_input

def random_password_generation ():
    service_name = input("Enter the service or website name for this password: ")
    password = ''
    for i in range (12):
        random_symbol =random.choice(password_symbols)
        password += random_symbol

    main_password_base[service_name] = password
    with open("passwords.txt","a") as file:
        file.write(f"{service_name}:{password}\n")
    print(main_password_base)

def create_password_manualy():
    service_name = input("Enter the service or website name for this password: ")
    password = input("Enter your password: ")
    main_password_base[service_name] = password
    with open("passwords.txt","a") as file:
        file.write(f"{service_name}:{password}\n")
    print(main_password_base)

def session_password_viewer():
    print("-"*50)
    for key,value in main_password_base.items():
        print(f"{key}:{value}")
    print("-"*50)
    input("\nPress Enter to go to the main menu...")

