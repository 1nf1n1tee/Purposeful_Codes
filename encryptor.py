def nBase(num,base):
    if num == 0:
        return
    else:
        nBase(int(num/base),base)
        if num % base < 10:
            print(int(num%base),end='')
        else:
            print(chr(ord('A') + int(num%base) - 10),end='')
def encodeScripture(script_line, target_base):
    for i in script_line:
        # print(ord(i))
        nBase(ord(i), target_base)
        print(' ',end='')
    print()
encodeScripture("CAT is a domestic",16)