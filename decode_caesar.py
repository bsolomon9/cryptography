#30-126 are printable
inp = list(input("input string: "))
shift = int(input("input number shift: "))


for i in range(len(inp)):
    new = ord(inp[i]) - shift
    while new < 30:
        new += (126-30)
    
    inp[i] = chr(new)


print(''.join(inp))
    