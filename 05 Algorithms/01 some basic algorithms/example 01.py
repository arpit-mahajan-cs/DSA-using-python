

# WPP to read a string and convert all even indexed values into upper case.

def myfun(s):
    l = list(s.lower())
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = l[i].upper()
    return ''.join(l)

s = "arpit mahajan"
print(s)
print(myfun(s))