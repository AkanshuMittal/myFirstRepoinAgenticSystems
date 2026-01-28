def are_dicts_same(d1, d2):
    if d1 == d2:
        return True
    else:
        return False


# Input dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}

# Function call
result = are_dicts_same(d1, d2)

# Output
if result:
    print("Both dictionaries are the same")
else:
    print("Dictionaries are different")
