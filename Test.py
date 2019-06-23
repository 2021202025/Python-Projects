from pprint import pprint

def program():
    # d = {"a": 1, "b": 2, "c": 3}
    # d["d"] = 4
    # d = dict((k,v) for k, v in d.items() if v <= 1)
    # l = list(x for x in d.values() if x <= 1)
    # print(d)
    # print(l)

    # d = dict(a=list(range(1,11)), b=list(range(11,21)), c=list(range(21,31)))
    # # pprint(list(d.values())[1][2])
    # for k,v in d.items():
    #     print(k,"has value",v)
    return

def string_count():
    file = open("words2.txt", "r")
    lines = file.read()
    print(lines)
    lines.replace(',', ' ')
    lines = lines.split(' ')
    count = len(lines)
    for i in lines:
        if "," in i:
            count += 1
    print(count)
    # count = 1
    # for i in lines:
    #     if i==" " or i==",":
    #         count += 1
    # print(count)


string_count()

import time
start_time = time.time()
program()
print("--- %s seconds ---" % (time.time() - start_time))