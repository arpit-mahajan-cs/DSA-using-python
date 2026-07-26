

# Example of recursion using parameters [1 to N] [tail]


def func(i,n):
    if i>n:
        return
    func (1+i,n)
    print(i)
func(1,4)