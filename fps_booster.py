import time
import random

num = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0 ,1, 2, 3, 4, 5, 6, 7, 8, 9]
run = [10, 15, 20, 25, 30]
rrun = random.choice(run)

def write_to_file(log):
     with open('logs.txt', 'a', encoding='utf-8') as file:
           file.write(f"\n[{time.strftime('%H:%M')}]: {log}!")

print("Ultimate FPS Booster by legovovus")

while True:
    print("=== Menu ===")
    a = input(" 1. Start \n 2. Description \n 3. Logs \n 4. Exit \n")

    if a == '1':
        print("Welcome to the Booster")
        game = input("Game name: ").title()

        # GAME ERRORS
        if random.random() < 0.1:
            print("UNKNOWN ERROR 104!")
            log = "UNKNOWN ERROR 104"
            write_to_file(log)
            time.sleep(0.5)
            break

        if random.random() < 0.1:
            print("UNKNOWN ERROR 0!")
            log = "UNKNOWN ERROR 0"
            write_to_file(log)
            time.sleep(0.5)
            break
                    
        fps = int(input("FPS: "))

        # FPS ERRORS
        if fps >= 2 ** 15:
            print("UNKNOWN ERROR 103!")
            log = "UNKNOWN ERROR 103"
            write_to_file(log)
            time.sleep(0.5)
            break
        elif fps <= 2 ** 4:
            print("UNKNOWN ERROR 102!")
            log = "UNKNOWN ERROR 102"
            write_to_file(log)
            time.sleep(0.5)
            break

        time.sleep(1)
        print("Finding the game process...")
        time.sleep(2)
        print("Processing RAM...")
        time.sleep(2)
        print("Boosting FPS...")
        time.sleep(2)
        print("The Booster is ready for using! Wait for 10 sec")
        time.sleep(10)
        print(f"The Booster will be running for {rrun}m")
        time.sleep(1)
        for counter in range(1, rrun * 60 + 1):
            print(f"{counter}m: {game}.exe BOOSTED | {fps - random.choice(num)} FPS")
            time.sleep(60)
            # RANDOM ERROR)
            if random.random() == 0.1:
                print("UNKNOWN ERROR 0!")
                log = "UNKNOWN ERROR 0"
                write_to_file(log)
                break
        print("Booster have done his job!")
        time.sleep(2)
            
    elif a == '2':
        print("=== FPS Booster Description ===")
        print("This is a simple FPS Booster for your games.\n" \
        "By using this app you can boost your FPS even if you have a bad PC.\n" \
        "It uses more RAM than you have bypassing the limits.\n" \
        "Every minute it sends a log with all information\n" \
        "All error responses you can see in 'Error Responses.txt'" \
        "Do not put a very big number of FPS! App can crash itself and your PC. Less than 2^15: 32768 and more than 2^4: 16")
        print("Created by legovovus")
        time.sleep(2)
    elif a == '3':
        print("\n=== Current Logs ===")
        try:
            with open('logs.txt', 'r', encoding='utf-8') as file:
                print(file.read())
        except FileNotFoundError:
            print("No logs found yet.")
        input("\nPress Enter to return to menu...")
    elif a == '4':
        break
    else:
        print("Error! Try again")
