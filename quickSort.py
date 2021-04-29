def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        left = [array[i] for i in range(1,len(array)) if array[i] <= pivot]
        right = [array[i] for i in range(1,len(array)) if array[i] > pivot]
        return quickSort(left) + [pivot] + quickSort(right)

