def anagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    if len(s1) != len(s2):
        return False
    char_count = {}
    for char in s1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False  
    for count in char_count.values():
        if count != 0:
            return False

    return True
# Input
s1 = input().strip()
s2 = input().strip()
# Check anagram
print(anagrams(s1, s2))