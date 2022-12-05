'''Happy Linter'''
from string import ascii_lowercase as alc
def solution():
    '''happy linter'''
    this_dict={}
    sum_of_priorities=0
    for ind, c in enumerate(alc):
        this_dict[c] = ind+1
        this_dict[c.upper()] = ind+27
    with open('input.txt', 'r', encoding="utf8") as f:
        lines = f.readlines()
        res = []
    for sub in lines:
        res.append(sub.replace("\n", ""))

    result_of = []
    count= 0
    l_iter = iter(res)
    while True:
        item = next(l_iter, "end")
        if item == "end":
            break
        print(item, count)
        result_of.append(item)
        count+=1
        if count ==3:
            print("got 3 items")
            print(result_of)
            set_string1 = set(result_of[0])
            set_string2 = set(result_of[1])
            set_string3 = set(result_of[2])
            matched_character = set_string1 & set_string2 & set_string3
            print("the matched character is: ", matched_character)
            for key, value in this_dict.items():
                if list(matched_character)[0] == key:
                    sum_of_priorities+=value
            count=0
            result_of.clear()
    print(sum_of_priorities)
solution()

    