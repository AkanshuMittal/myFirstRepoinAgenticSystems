def access_control(age, has_ID_card):
    if age >= 18 and has_ID_card:
        print("Entry allowed")
    else:
        print("Entry restricted")
        
age = int(input("Enter your age: "))
has_ID_card = input("Are you have an ID card ? True or False: ").strip().lower()

#Convert string input to boolean safely
if has_ID_card == "true":
    has_ID_card = True
elif has_ID_card == "false":
    has_ID_card = False
else:
    print("Invalid input for ID card. Please enter True or False.")
    exit()
    
access_control(age, has_ID_card)



