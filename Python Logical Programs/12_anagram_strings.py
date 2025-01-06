def isAnagramString(str1, str2):
    # Trims the string and converts them to lower case...
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Checks if the sorted characters of both the strings match...
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

s1 = "abc"
s2 = "bca"
print(f"Are both strings Anagram? {isAnagramString(s1, s2)}")