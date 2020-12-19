from day18 import process_entry

def compute_bracket(braket):
    parts = []
    parts.append(int(braket[0]))
    for i in range(1, len(braket), 2):
        sign = braket[i]
        num = int(braket[i+1])
        if sign == '+':
            last_num = parts.pop()
            parts.append(last_num + num)
        if sign == '*':
            parts.append(num)
    total_sum = 1
    for part in parts:
        total_sum *= part
    return total_sum

def compute_expresion(expresion):
    parts = []
    stack = []
    for i,val in enumerate(expresion):
        if val == '(':
            stack.append(i)
        elif val == ')':
            start = stack.pop()
            if stack == []:
                parts.append(compute_expresion(expresion[start+1:i]))
        else:
            if not stack:
                parts.append(val)

    return compute_bracket(parts)

def solve(entry_list):
    suma = []
    for entry in entry_list:
        suma.append((compute_expresion(entry)))

    return sum(suma)

if __name__ == '__main__':
    with open("day18.txt", "r") as f:
        entry_list =  f.readlines()
    entry_list = process_entry(entry_list)
    print(solve(entry_list))

