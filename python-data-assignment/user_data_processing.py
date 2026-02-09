def user_details(users):
    for user in users:
        scores = user["scores"]
        average = sum(scores)/len(scores)
        
    return average

def user_roles(roles):
    if "admin" in roles:
        return True
    else:
        return False
    
def main():
    users = [
    {
        "name": "Abhay",
        "scores": [43, 56, 12, 67],
        "roles": {"adimn", "editor", "viewer"}
    },
    {
        "name": "Mukul",
        "scores": [13, 96, 42, 47],
        "roles": {"adimn", "editor", "viewer"}
    }
]
        
    
    average_score = user_details(users)
    print(f"Average Score: {average_score}")
    
    result = user_roles("roles")
    print(f"Admin Access: {result}")