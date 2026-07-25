

#  Example of Head Recursion


count=0
def func():
    global count
    if count==4:
     return
    print("arpit")
    count +=1
    func()
func()