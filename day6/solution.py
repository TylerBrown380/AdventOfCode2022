'''For day 6 of Advent of Code'''
def solution():
    '''this method prints the solution to advent of code problem 6'''
    with open('input.txt', 'r', encoding="utf8") as f:
        lines = f.readlines()
    res = []
    for sub in lines:
        res.append(sub.replace("\n", ""))
    input_string = res[0]
    cache_arr = []
    for ind,i in enumerate(input_string):
        #part 1 solution, just change 14 to 4
        if len(cache_arr) < 14:
            cache_arr.append(i)
            #print(cache_arr)
        #part 1 solution, just change 14 to 4
        if len(cache_arr) == 14:
            if check_for_dupes(cache_arr):
                cache_arr.pop(0)
                cache_arr.append(i)
                #print(cache_arr)
            else:
                print(cache_arr, "index is:", ind)
                return
def check_for_dupes(list_of_elems):
    ''' Check if given list contains any duplicates '''
    set_of_elems = set()
    for elem in list_of_elems:
        if elem in set_of_elems:
            return True
        else:
            set_of_elems.add(elem)
    return False
solution()
