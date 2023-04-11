#program to list Sort by Number value in String
def num_sort(str):
    cn=[ele for ele in str.split() if ele.isdigit()]
    if len(cn) > 0:
        return int(cn[0])
    return -1
lst=["gfg is", "all no 7", "geeks over seas", "and planets 5"]
lst.sort(key=num_sort)
print(str(lst))