def strStr(haystack,needle):
    len1 = len(haystack)
    len2 = len(needle)
    if len1 < len2:
        return -1
    for i in range(len1 - len2 +1):
        if haystack[i:i + len2] == needle:
            return i
    return -1
hay = input("Enter the haystack: ")
print(hay)
needl = input("Enter the needle: ")
print(needl)
result = strStr(hay,needl)
print(result)