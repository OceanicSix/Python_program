def quick_sort(arr):
    """
    Quicksort a list

    Arguments:
    arr -- the input list to be sorted

    Return:
    result -- the sorted arr
    """
    if len(arr) <= 1:
        return arr
    else:
        # take the first element as the pivot
        pivot = arr[0]
        left_arr = [x for x in arr[1:] if x < pivot]
        right_arr = [x for x in arr[1:] if x >= pivot]
        # uncomment this to see what to print
        # print("Left:" + str(left_arr)+" Pivot : "+ str(pivot)+" Right: " + str(right_arr))
        value = quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

        return value


if __name__ == '__main__':
    data = [8, 12, 16, 4, 11, 15, 3, 7, 14, 2, 6, 10, 1, 5, 9, 13]
    print(quick_sort(data))