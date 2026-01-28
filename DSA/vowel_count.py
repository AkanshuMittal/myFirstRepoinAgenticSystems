# def vowel_count(str):
#     count = 0
#     vowels = "aeiouAEIOU"
    
#     for ch in str:
#         if ch in vowels:
#             count += 1
            
#     return count
    
# str = "helloU"
# res = vowel_count(str)

# print(res)


def vowel_count(str):
    vowel_list = []
    vowels = "aeiouAEIOU"
    
    for ch in str:
        if ch in vowels:
            vowel_list.append(ch)
            
    return vowel_list
            
str = "helloU"
res = vowel_count(str)

count = len(res)

print(count)

print(res[1])
