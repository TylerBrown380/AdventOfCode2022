'''Happy Linter'''
def solution():
    '''happy linter'''
    with open('input.txt', 'r', encoding="utf8") as f:
        lines = f.readlines()
    res = []
    for sub in lines:
        res.append(sub.replace("\n", ""))
    sum_of_points = 0
    for sub in res:
        substring_split = sub.split()
        if substring_split[0] == 'A' and substring_split[1] == 'X':
            sum_of_points+=3
        if substring_split[0] == 'A' and substring_split[1] == 'Y':
            sum_of_points+=4
        if substring_split[0] == 'A' and substring_split[1] == 'Z':
            sum_of_points+=8
        if substring_split[0] == 'B' and substring_split[1] == 'X':
            sum_of_points+=1
        if substring_split[0] == 'B' and substring_split[1] == 'Y':
            sum_of_points+=5
        if substring_split[0] == 'B' and substring_split[1] == 'Z':
            sum_of_points+=9
        if substring_split[0] == 'C' and substring_split[1] == 'X':
            sum_of_points+=2
        if substring_split[0] == 'C' and substring_split[1] == 'Y':
            sum_of_points+=6
        if substring_split[0] == 'C' and substring_split[1] == 'Z':
            sum_of_points+=7
    print(sum_of_points)
solution()
