

# WPP to find max of two number 


def maxfun_version1(a,b):
    return max (a,b)
def maxfun_version2(a,b):
    return a if a>b else b
def maxfun_version3(a,b):
    if a>b:
        return a
    else:
        return b
def maxfun_version4(a,b):
    call = lambda a,b : a if a>b else b
    return call(a,b)
def maxfun_version5(a,b):
    L=[]
    L.append(a)
    L.append(b)
    return max (L)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("max value by using verion 1:",maxfun_version1(a,b))
print("max value by using verion 2:",maxfun_version2(a,b))
print("max value by using verion 3:",maxfun_version3(a,b))
print("max value by using verion 4:",maxfun_version4(a,b))
print("max value by using verion 5:",maxfun_version5(a,b))