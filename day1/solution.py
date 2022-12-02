'''happy linter'''


def solution():
    '''gets largest sum of stuff from input'''
    with open('input.txt', 'r', encoding="utf8") as f:
        lines = f.readlines()
    max_num = 0
    num = 0
    array_of_stuff = []
    for l in lines:
        if l != '\n':
            num += int(float(l))
        if l == '\n':
            array_of_stuff.append(num)
            if num > max_num:
                max_num = num
            num = 0
    array_of_stuff.sort()
    print(array_of_stuff[len(array_of_stuff)-3:])
    top_three = sum(array_of_stuff[len(array_of_stuff)-3:])
    print(top_three)

solution()
