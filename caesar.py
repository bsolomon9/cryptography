#30-126 are printable, negative shift to decode
inp = list(input("input string: "))
shift = int(input("input number shift: "))


for i in range(len(inp)):
    new = ord(inp[i]) + shift

    while new > 126:
        new -= (126-30)

    while new < 30:
        new += (126-30)
    
    
    inp[i] = chr(new)


print(''.join(inp))