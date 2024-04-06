
#============= Funktion studentregistret ==============================================
def registrera_students():
    students = {}
    # Fråga användaren om studentens information
    fraga = input('Vill du registrera elev? (y/n): ')
    while fraga == "y":
        namn = input("Ange studentens namn: ")
        age = input("Ange studentens ålder: ")
        kurser_input = input("Ange de kurser studenten är registrerad för (separera med kommatecken): ")
        
        # Konvertera kurslistan från en sträng till en lista
        kurser = kurser_input.split(',')

        # Trimma bort eventuella blanksteg från kursnamnen
        kurser = [kurs.strip() for kurs in kurser]

        students[namn] = {'age': age, 'kurser': kurser}

        fraga = input('Vill du registrera en elev till? (y/n): ')

    return students

#============== Funktion uppdatera registret med fler kurser =============================================
def uppdatera_student_kurser(studentreg):
    # Print existing students to choose from
    print("Existing students:")
    for name in studentreg:
        print(name)
    studentedit = input("Ange namn på studenten du vill editera kurser för: ")
    if studentedit in studentreg:
        nya_kurser_input = input("Ange de nya kurser studenten är registrerad för (separera med kommatecken): ")
        nya_kurser = nya_kurser_input.split(',')
        nya_kurser = [kurs.strip() for kurs in nya_kurser]
        
        studentreg[studentedit]['kurser'].extend(nya_kurser)

    return studentreg

#============= Funktion skriva ut ==============================================
def print_students_info(students):
    for name, details in students.items():
        print(f"\nName: {name}")
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")

#=========== HUVUDPROGRAMMET ================================================

# Vad vill användaren göra?
anv_val = ""
while anv_val != "x":    
    print("\nVälj ett av följande alternativ:")
    print("1. Skriva in ny student i studentregistret")
    print("2. Skriva ut aktuell studentregistret")
    print("3. Uppdatera kurser för student i studentregistret")
    print("x. Avsluta och gå och ta en kopp kaffe")

    # Användarens val
    anv_val = input("Skriv 1, 2, 3 eller x  - tryck sedan Enter: ")

    # Skicka användaren rätt
    if anv_val == '1':
        studentreg = registrera_students()
    elif anv_val == '2':
        print_students_info(studentreg)
    elif anv_val == '3': 
        studentreg = uppdatera_student_kurser(studentreg)
    else:
        print("\nTack. \n")
