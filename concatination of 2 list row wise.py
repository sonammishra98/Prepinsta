test_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
test_list2 = [[1, 3], [9, 3, 5, 7], [8]]
res=list(sub1+ sub2 for sub1,sub2 in zip(test_list1,test_list2))
print(str(res))