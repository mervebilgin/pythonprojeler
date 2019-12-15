"""
Buble sort:
Her döngüde yanyana iki eleman üzerinde karşılaştırma yapılır.
İlk döngü bittiğinde en büyük eleman dizinin en sonuna atılır.
Bir sonraki döngü dizinin (n-1) elemanı için yapılır.
"""
def bubble_sort(list):
    for i in range(0,len(list)):
        for j in range(0,len(list)-i-1):
            if (list[j] > list[j+1]):

                list[j],list[j+1] = list[j+1],list[j]

list = [19,2,34,76,13,65,121,49]
bubble_sort(list)
print(list)
