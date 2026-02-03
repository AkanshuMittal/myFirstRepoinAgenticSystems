def profile_builder(name, age, is_active_user):
    return name, age, is_active_user

name = input("Enter your name: ")
age = (int(input("Enter your age: ")))
is_active_user  = input("Are you active user ? True/False: ")

name,age,is_active_user = profile_builder(name,age,is_active_user)

print(f"User {name} is {age} years old. Active status: {is_active_user}")



