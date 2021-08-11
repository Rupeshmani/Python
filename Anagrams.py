from collections import Counter 

def is_anagram(txt1, txt2):
    
    return Counter(txt1) == Counter(txt2)

print(is_anagram(input(),input()))
print(is_anagram(input(),input()))