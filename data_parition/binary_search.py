# Binary search function
def binary_search(data, target):

    matched_record = None
    position = -1  # not found position

    lower = 0
    middle = 0
    upper = len(data) - 1

    ### START CODE HERE ###
    while (lower <= upper):
        # calculate middle: the half of lower and upper
        middle = int((lower + upper) / 2)
        if data[middle]==target:
            matched_record=target
            position=middle
            return position,matched_record
        elif data[middle]<target:
            lower = middle + 1
        else:
            upper=middle-1

        ### END CODE HERE ###

    return position, matched_record


if __name__ == '__main__':
    D = [55, 30, 68, 39, 1,
         4, 49, 90, 34, 76,
         82, 56, 31, 25, 78,
         56, 38, 32, 88, 9,
         44, 98, 11, 70, 66,
         89, 99, 22, 23, 26]
    sortD=D[:]
    sortD.sort()
    print(binary_search(sortD,31))