def idk(steps=True):
    repeat = []
    bits = [0,0,0]
    code = input()
    ind = 0
    spot = 0
    print(bits)
    while ind < len(code):
        if code[ind] == '+':
            bits[spot] += 1
        elif code[ind] == '-':
            bits[spot] -= 1
        elif code[ind] == '>':
            spot += 1
            spot %= 3
        elif code[ind] == '<':
            spot -= 1
            spot %= 3
        elif code[ind] == '[':
            repeat.append(ind)
        elif code[ind] == ']':
            ind = repeat[0]
            repeat.remove(repeat[0])
            code = code.replace(']','',1)
        elif code[ind] == ',':
            bits[spot] += int(f'{input("?")}1')
        ind += 1
        if steps:
            print(bits)
    if not steps:
        print(bits)
idk()
