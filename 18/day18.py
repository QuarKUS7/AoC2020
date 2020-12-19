def process_entry(entry_list):
    processed = []
    for entry in entry_list:
        entry = [ch for ch in list(entry.rstrip()) if ch != ' ']
        processed.append(entry)
    return processed


def compute_bracket(braket):
    total_sum = int(braket[0])
    for z,i in zip(braket[1:], braket[2:]):
        if z == '+':
            total_sum += int(i)
        if z == '*':
            total_sum *= int(i)
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
