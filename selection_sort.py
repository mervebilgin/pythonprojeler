def selection_sort(list):
    for i in range(len(list)):
        minimum = i
        for j in range(i+1,len(list)):
            if list[minimum] > list[j]:
                minimum = j
            list[i],list[minimum] = list[minimum],list[i]

list = [19,2,34,76,13,65,121,49]
selection_sort(list)
print(list)

