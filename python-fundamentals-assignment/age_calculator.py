birth_year = int(input("Enter the Birth Year: "))

def age_calculator(birth_year):
    age = 2026 - birth_year
    
    return age

result = age_calculator(birth_year)

print(f"You are {result} years old")