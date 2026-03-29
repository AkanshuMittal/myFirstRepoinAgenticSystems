import json 

data = '''
{
    "User": {
        "id": 1,
        "roles": ["admin", "editor"]
    }
}
'''

print(type(data))

parsed = json.loads(data)

print(type(parsed))

print(parsed)

role = parsed["User"]["roles"]

print(type(role))

for i in role:
    print(i)
    
# val = parsed.get("User").get("abc")
val = parsed.get("User").get("abc")
print(val)