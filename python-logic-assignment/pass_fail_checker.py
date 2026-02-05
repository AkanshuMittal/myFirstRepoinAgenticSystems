def pass_fail_checker(score):
    
    if score >= 50:
        print("Pass")
    else:
        print("Fail")
        

score = int(input("Enter the score: "))

pass_fail_checker(score) 
