logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

import string

def process(shift_num, msg, encode = True):
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    ret = []
    for i in msg:
        if not i in upper and not i in lower:
            ret.append(i)
            continue
        lists = upper if i in upper else lower
        idx = lists.index(i)
        if encode == True:
            idx = (idx + shift_num) % len(lists)
        else:
            idx = (idx - shift_num + len(lists)) % len(lists)
        ret.append(lists[idx])

    return ''.join(ret)

print(logo)

while True:
    command = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if command == 'encode':
        msg = input('Type your message\n')
        num = int(input('Type the shift number:\n'))
        encode = process(num, msg, True)
        print(f"Here's your encoded result: {encode}")

    elif command == 'decode':
        msg = input('Type your message\n')
        num = int(input('Type the shift number:\n'))
        decode = process(num, msg, False)
        print(f"Here's your decoded result: {decode}")

    else:
        continue

    con = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if con != 'yes':
        break
