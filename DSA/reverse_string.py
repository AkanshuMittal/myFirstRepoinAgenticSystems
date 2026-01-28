def reverse_string(s):
    if s == "":
        return s 
    
    return reverse_string(s[1:]) + s[0]

s = "hello"

print(reverse_string(s))


# O(n)

# O(n)

