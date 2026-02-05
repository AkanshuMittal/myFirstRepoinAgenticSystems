def transaction_validator(balance, withdrawal_amount, is_verified):
    if is_verified and withdrawal_amount <= balance:
        print("Withdrawal successful")
        
    else:
        print("Transaction denied")
        

balance = int(input("Enter the account balance: "))
withdrawal_amount =  int(input("Enter the withdrawal amount: "))
is_verified = input("Are you verified? True/False: ").strip().lower()

#Convert string input to boolean safely
if is_verified == "true":
    is_verified = True
elif is_verified == "false":
    is_verified = False
else:
    print("Invalid input for verification status. Please enter True or False.")
    exit()
    
transaction_validator(balance, withdrawal_amount, is_verified)