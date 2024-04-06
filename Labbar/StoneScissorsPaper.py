#===========================================================
# Stone, Paper, Scissors game - The first straight on simple version
import random  #importera slumtalsfunktion

#======== Funktion: Slumpa datorns val, jämför och skriv ut resultat av en omgång ===================================================
def gameround(choice):
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

    # Förtydliga att nu är denna rundan slut och nedanför kommer en ny runda om man vill.
    print("\n============ ANOTHER ROUND BELOW ================")

#============ HUVUDPROGRAMMET ===============================================
# The user plays/select
users_choice = ""

# Slingan med omgångar så länge användaren vill
while users_choice != int(0): # and questiongame == "y":    
    print("\nChoose Stone, Scissors or Paper ! ")
    print("1. Stone")
    print("2. Scissors")
    print("3. Paper")
    print("\n0. End this, I need a coffee")

    # Användarens val
    #users_choice = int(input("\nChoose 1, 2, 3 or 0  - then Enter: "))
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
        gameround(users_choice)
    else:
        break
        
print("\nThank you for playing.\n")

#===========================================================






