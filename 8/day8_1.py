with open("day8.txt", "r") as f:
    entry_list =  f.read().splitlines()


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
def run(boot_code):

    global index
    global acu
    while True:
        if index > len(boot_code)-1:
            print("ACU %i", acu)
            return
        code = boot_code[index]
        index += 1
        if code['instruction'] == 'acc':
            if not code['visited']:
                 acc(code)
                 code['visited'] = True
            else:
#                print(acu)
                #print(code)
                break
        elif code['instruction'] == 'jmp':
            if not code['visited']:
                jmp(code)
                code['visited'] = True
            else:
               # print(acu)
                #print(code)
                break
        else:
            if not code['visited']:
                nop()
                code['visited'] = True
            else:
#                print(acu)
                #print(code)
                break

#run(boot_code)
import copy
for i in range(len(boot_code)):
    acu = 0
    index = 0
    if boot_code[i]['instruction'] == 'jmp':
        tmp = copy.deepcopy(boot_code)
        tmp[i]['instruction'] = 'nop'
        run(tmp)
for i in range(len(boot_code)):
    acu = 0
    index = 0
    if boot_code[i]['instruction'] == 'nop':
        tmp = copy.deepcopy(boot_code)
        tmp[i]['instruction'] = 'jmp'
        run(tmp)
