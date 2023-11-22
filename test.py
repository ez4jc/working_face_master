list1 = [1, 2, 3, 4, 5]
list2 = [3, 4]

result = [x - y for x, y in zip(list1, list2)]
print(result)
