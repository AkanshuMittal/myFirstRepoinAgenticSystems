def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    freq = {}
    
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1 
        
    for ch in s2:
        if ch not in freq:
            return False
        
        freq[ch] -=1
        
        if freq[ch] == 0:
            del freq[ch]
            
    return len(freq) == 0

s1 = "listen"
s2 = "silent"

res = is_anagram(s1, s2)

if res:
    print("Both string are anagranm of each other.")
    
else:
    print("Not Anagram")