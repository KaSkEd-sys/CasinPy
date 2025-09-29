from colorama import *
import random
import time
import os
balance = 200  #Our starter balance ($)

init(autoreset=True)

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = Fore.BLUE + "CasinPy"
    chances = Fore.RED + "Chances"
    print(f"Welcome to {logo} ! What Is your name?")
    name = input("name: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Okay, {name} In this game you must open cases and loot money to buy more cases ;) \nAlso... You can buy a NFT! but this coming soon ;)")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Okay, I think you're ready now, right? (y/n)")
    ready = input("(y/n): ")
    if ready == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Lets Start! {name}!')
        cases()
    elif ready == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Try next time ;)")
        time.sleep(2)
        


def cases():
    pass

main_menu()