import platform
import getpass
import os
import json
import importlib
from colorama import Fore, Back, Style
from colorama import init as colorama_init
from art import tprint

colorama_init(True)

config = {
    "paths": {
        "/": "."
    },
    "commands_path": f"{os.getcwd()}/commands",
    "path_structure": [
        ''
    ],
    "help_text": """cd: changes directory
del: deletes stuff
dir: lists directories and files
help: does this
mkdir: makes a directory"""
}

def get_current_path():
    return '/'.join(config['path_structure'])

config['device_name'] = platform.node()
if config['device_name'] == "":
    config['device_name'] = "machine"

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def login(username=None, password=None, use_env=True):
    users = os.listdir("users")
    
    username = username or input("Username: ")
    password = password or getpass.getpass("Password: ")

    if username in users:
        print(f"Found user {username}")

        user_json = {}
        with open(os.path.join("users", username, "user.json")) as f:
            user_json = json.load(f)

        if password == user_json["password"]:
            print("Logged in!")
            if use_env:
                if platform.system() == "Windows":
                    os.system(f"set PYDOS_USER_ID={user_json['id']}")
                else:
                    os.system(f"export PYDOS_USER_ID={user_json['id']}")

            return {
                "status": "success",
                "error": None,
                "user_json": user_json
            }
        return {
            "status": "fail",
            "error": "Password incorrect"
        }
    return {
        "status": "fail",
        "error": "User not found"
    }

def run_command(command, args=None, kwargs=None):
    if command.endswith(".py") and command in os.listdir():
        command = importlib.import_module(command[:-3])
        command.command(os=os, config=config, args=args if args else [], kwargs=kwargs if kwargs else {})
    elif command in os.listdir(config["commands_path"]):
        command = importlib.import_module("commands." + command)
        command.command(os=os, config=config, args=args if args else [], kwargs=kwargs if kwargs else {})
    else:
        print("Command not found")

def main():
    clear()
    tprint("Welcome  to  PyDOS")
    print("")
    is_logged_in = False
    if 'current_user.json' in os.listdir():
        with open('current_user.json', 'r') as f:
            current_user = json.load(f)

        logged_in = login(current_user['username'], current_user['password'])
        if logged_in['status'] == 'success':
            is_logged_in = True

            run_command(f'cd', ['users'])
            run_command(f'cd', [current_user['username']])

    current_user = {}
    while not is_logged_in:
        logged_in = login()
        if logged_in['status'] == "success":
            with open('current_user.json', 'w') as f:
                json.dump({
                    "username": logged_in['user_json']['username'],
                    "password": logged_in['user_json']['password'],
                }, f, indent=4)
            
            current_user = logged_in['user_json']
            run_command(f'cd', ['users'])
            run_command(f'cd', [current_user['username']])
            is_logged_in = True
            break
        else:
            print("Unable to login:", logged_in['error'])
    
    print("")

    running = True
    while running:
        command = input(f"{Fore.BLUE}{config['device_name']}{Fore.GREEN}@pydos{Fore.YELLOW}{get_current_path()}~{Fore.WHITE} ")
        print(Style.RESET_ALL, end="")
        if command == "exit":
            running = False
            break
        
        args = command.split(' ')
        new_command = args[0]
        del args[0]
        run_command(new_command, args)

if __name__ == "__main__":
    main()
