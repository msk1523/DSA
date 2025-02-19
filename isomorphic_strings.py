""" 
Coding Exercise: Isomorphic Strings
Question:

Isomorphic Strings - Given two strings s and t, determine if they are isomorphic. 
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself. s and t consist of any valid ascii character.

"""

def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False
    isomorphic = {}
    for i in range(len(s)):
        if s[i] in isomorphic:
            if isomorphic.get(s[i]) == t[i]:
                continue
            else:
                return False
        else:
            isomorphic[s[i]]=t[i]
    return True

print(isomorphic_strings("egg","add"))
print(isomorphic_strings("foo","bar"))
        
            