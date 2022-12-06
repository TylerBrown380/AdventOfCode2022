'''Happy Linter'''
def solution():
    '''happy linter'''
    with open('input.txt', 'r', encoding="utf8") as f:
        lines = f.readlines()
    res = []
    count = 0
    overlap_count=0
    for sub in lines:
        res.append(sub.replace("\n", ""))
    for sub in res:
        substring_split = sub.split(',')
        second_split = substring_split[0].split('-')
        third_split = substring_split[1].split('-')
        #part 1
        if (int(second_split[0]) >= int(third_split[0]) and int(second_split[1]) <= int(third_split[1])) or (int(third_split[0]) >= int(second_split[0]) and int(third_split[1]) <= int(second_split[1])):
            #print("the numbers",second_split[0], "-",second_split[1], "is within", third_split[0],"-",third_split[1])
            count+=1
        #part 2
        if ((int(second_split[0]) >= int(third_split[0]) and int(second_split[0]) <= int(third_split[1])) 
        or (int(second_split[1]) >= int(third_split[0]) and int(second_split[1]) <= int(third_split[1]))
        or (int(third_split[0]) >= int(second_split[0]) and int(third_split[0]) <= int(second_split[1]))
        or (int(third_split[1]) >= int(second_split[0]) and int(third_split[1]) <= int(second_split[1]))):
            overlap_count+=1
    print("There are",count, "number of contained pairs")
    print("There are",overlap_count, "number of overlapping pairs")
solution()
