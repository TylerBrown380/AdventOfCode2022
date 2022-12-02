'''happy linter'''


def solution():
    '''gets largest sum of stuff from input'''
    with open('input.txt', 'r', encoding="utf8") as f:
        lines = f.readlines()
    max_num = 0
    num = 0
    for l in lines:
        if l != '\n':
            num += int(float(l))
        if l == '\n':
            if num > max_num:
                max_num = num
            num = 0
    print(max_num)


solution()
