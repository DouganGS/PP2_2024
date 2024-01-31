def pal(s):
    rev = s[::-1]
    if rev == s:
        return True
    else:
        return False
    

s = input()
print(pal(s))