with open("day8.txt", "r") as f:
    entry_list =  f.read().splitlines()

print(entry_list)

acu = 0
index = 0

def process_boot_code(entry_list):
    boot_code = []
    for entry in entry_list:
        parsed = entry.split(' ')
        code = {}
        code['instruction'] = parsed[0]
        code['amount'] = int(parsed[1])
        code['visited'] = False
        boot_code.append(code)
    return boot_code

def acc(code):
    global acu
    acu += code['amount']



def jmp(code):
    global index
    index += code['amount'] -1

def nop():
    pass

boot_code = process_boot_code(entry_list)
print(boot_code)

while True:
    code = boot_code[index]
    index += 1
    print(index)
    print(len(boot_code)-1)
    print('----')
    if code['instruction'] == 'acc':
        if not code['visited']:
             acc(code)
             code['visited'] = True
        else:
            print(acu)
            print(code)
            break
    elif code['instruction'] == 'jmp':
        if not code['visited']:
            jmp(code)
            code['visited'] = True
        else:
            print(acu)
            print(code)
            break
    else:
        if not code['visited']:
            nop()
            code['visited'] = True
        else:
            print(acu)
            print(code)
            break
