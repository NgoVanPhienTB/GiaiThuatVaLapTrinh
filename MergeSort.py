

def mergeSort(leff,right):

    arr = []
    i,j =0,0

    while i < len(leff) or j < len(right) :
        if leff[i] < right[j]:
            arr.append(leff[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
        if i==len(leff) or j==len(right):
            arr.append(right[i:] or leff[j:])
            break
    return arr


def merge(array):

    if len(array) < 2:
        return array
    mid = (len(array)-1)//2
    left = merge(array[:mid])
    right = merge(array[mid:])
    return merge(left,right)
