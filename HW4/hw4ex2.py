lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst_1 = [el for el in lst[1:] if el > lst[lst.index(el) - 1]]
print(lst_1)