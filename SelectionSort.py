
def selection_sort(array):
    global dem
    dem = 0
    for i in range(0,len(array)):
        index = i
        for j in range(i + 1, len(array)):
            dem += 1
            if array[index] > array[j]:
                index = j

        if index != i:
            array[i], array[index] = array[index], array[i]


