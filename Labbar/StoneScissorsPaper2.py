#===========================================================
# Stone, Paper, Scissors game - The second a bit more advanced version
import random  #importera slumtalsfunktion

#======== Funktion: Slumpa datorns val, jämför och skicka tebax resultatet ===================================================
def gameround(users_choice):
    result = 0
    computers_choice = random.randint(1,3) #Slumpar enbart talen 1, 2, 3

    # Gör resultatet mer begripligt för användaren än siffror.
    if users_choice==1: users_choice_string = "STONE" 
    elif users_choice==2: users_choice_string = "SCISSORS" 
    elif users_choice==3: users_choice_string = "PAPER"

    if computers_choice==1: computers_choice_string = "STONE" 
    elif computers_choice==2: computers_choice_string = "SCISSORS" 
    elif computers_choice==3: computers_choice_string = "PAPER"

    # Skriv ut vad användaren och datorn har valt
    print("\nThis is the choices:   User:",users_choice_string, "- Computer:", computers_choice_string)


    # Jämför valen och skriva ut resultatet. (Variabeln "result" ska jag använda i nästa version.)
    # 1 Sten-Stone / 2 Sax-Scissors / 3 Påse-Paper
    if users_choice==computers_choice: #Same
        result = 0 ; print("   << Even Steven - try again ! >>")
    elif users_choice==1 and computers_choice==2: #User==Sten and Computer==Sax: UserVinst
        result += 1 ; print("   << Stone beats Scissors - you win ! >>") #user_result += 1 ; computer_result -= 1
    elif users_choice==1 and computers_choice==3: #User==Sten and Computer==Påse: UserFörlust
        result -= 1 ; print("   << Stone does not beat Paper - you lose ! >>") #user_result -= 1 ; computer_result += 1
    elif users_choice==2 and computers_choice==1: #User==Sax and Computer==Sten: UserFörlust
        result -= 1 ; print("   << Scissors does not beat Stone - you lose ! >>") #user_result -= 1 ; computer_result += 1
    elif users_choice==2 and computers_choice==3: #User==Sax and Computer==Påse: UserVinst
        result += 1 ; print("   << Scissors beats Paper - you win ! >>") #user_result += 1 ; computer_result -= 1
    elif users_choice==3 and computers_choice==1: #User==Påse and Computer==Sten: UserVinst
        result += 1 ; print("   << Paper beats Stone - you win ! >>") #user_result += 1 ; computer_result -= 1
    else:  #users_choice==3 and computers_choice==2  #User==Påse and Computer==Sax: UserFörlust
        result -= 1 ; print("   << Paper does not beat Scissors - you lose ! >>") #user_result -= 1 ; computer_result += 1

    #print(result)
    return result

#======== Funktion: Ställningen i serien av rundor ===================================================
def totalstanding(result):
    global global_standing
    if result > 0:
        global_standing[1] += 1
    elif result < 0:
        global_standing[2] += 1
    else:
        print("Tie - no change in overall standings ! This round goes around...")
        global_standing[0] -= 1
        
#============= Funktion skriva ut ==============================================
def print_result(standing):
    # print(f"\nAndraOmgång: {roundnu} , You: {user_result} , Computer: {computer_result}")
    # print(global_standing)
    print(f"\nResultat efter omgång {global_standing[0]}: You: {global_standing[1]} , Computer: {global_standing[2]}")
    print("===================================")

#============ HUVUDPROGRAMMET ===============================================
# The user plays/select

# Initiering
users_choice = "" # Valet Stone, Sciccors or Paper
rounds = int(5) # Antalet /rounds i kampen. Default 5, först till tre vinner
roundnu = int(1) # Aktuell runda
user_result = int(0)
computer_result = int(0)
global_standing = [roundnu, user_result, computer_result]

# Fråga användaren hur många rundor
try:
    rounds = int(input("\nChoose best of 1, 3, 5 or 7 games - then Enter: "))
except ValueError:
    rounds = int(input("\nChoose best of 1, 3, 5 or 7 games - then Enter: "))

print("")

    # Slingan med omgångar
while users_choice != int(0) and global_standing[0] <= rounds:    
    print(f"Omgång {global_standing[0]}: Choose Stone, Scissors or Paper ! ")
    print("1. Stone   /   2. Scissors   /   3. Paper    /    0. End this, I need a coffee")

    # Användarens val
    try:
        users_choice = int(input("\nChoose 1, 2, 3 or 0  - then Enter: "))
    except ValueError:
        continue

    # Kolla att valet är ok
    if users_choice not in [0, 1, 2, 3]:
        print(f"\nHey hey hey... {users_choice} is not a valid option !")
        print("\nPlease choose a valid option: 1, 2, 3 or 0.")
        #continue
        check = input("\nDid you get that ? (y/n) ")
        if check == "y":
            try:
                users_choice = int(input("\nChoose 1, 2, 3 or 0  - then Enter: "))
            except ValueError:
                continue
            #gameround(users_choice)
        else:
            break

    #Spela en omgång
    if users_choice != 0:
        result = gameround(users_choice)
        #print(result)
    else:
        break

    totalstanding(result)

    print_result(global_standing)

    roundnu += 1
    global_standing[0] += 1
        
print("\nThank you for playing.\n")

#===========================================================






