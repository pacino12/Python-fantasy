# def add(arg1, arg2):
#     total = arg1 + arg2
#     return total


# out = add(2, 3)
# print(out)

def summ(arg):
    x = 0
    for i in arg:
        x = x+i
    return x


out = summ([10, 12, 30])
print(out)
