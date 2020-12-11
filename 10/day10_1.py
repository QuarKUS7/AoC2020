from itertools import groupby, count


def compute_coeficient(groups):
    combinations = 1
    for group in groups:
        if len(group) == 3:
            combinations *= 7
        elif len(group) == 2:
            combinations *= 4
        elif len(group) == 1:
            combinations *= 2
    return combinations

if __name__ == '__main__':

    with open("day10.txt", "r") as f:
        entry_list =  f.read().splitlines()

    entry_list = [int(entry) for entry in entry_list]
    entry_list = [0] + sorted(entry_list, reverse=False)
    entry_list.append( entry_list[-1] + 3)

    spravne = []
    for i in range(1,len(entry_list)-1):
        diff = entry_list[i] - entry_list[i-1]
        diff2 = entry_list[i] - entry_list[i+1]
        if diff == 1 and diff2 == -1:
            spravne.append(entry_list[i])


    ano = ([list(g) for k, g in groupby(spravne, key=lambda i,j=count(): i-next(j))])
    out = compute_coeficient(ano)




    print(out == 3947645370368)
