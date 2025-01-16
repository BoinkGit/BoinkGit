#replace w/ school code
while True:
    code = input()
    bits = [0,0,0,0,0,0,0,0]
    pointer = 0
    print(bits)
    for i in code:
        if i == '>':
            pointer += 1
            pointer %= 8
        if i == '<':
            pointer -= 1
            pointer %= 8
        if i == '1':
            bits[pointer] = 1
        if i == '0':
            bits[pointer] = 0
        if i == '?':
            bits[pointer] = int(input('1/0\n'))
        if i == '~':
            pass
        if i == '&':
            pass
        if i == '|':
            pass
        if i == '=':
            pass
        print(bits)
