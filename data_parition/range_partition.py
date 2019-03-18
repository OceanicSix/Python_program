def range_partition(data, range_indices):
    """
    Perform range data partitioning on data

    Arguments:
    data -- an input dataset which is a list
    range_indices -- the index list of ranges to be split

    Return:
    result -- the paritioned subsets of D
    """

    result = []

    ### START CODE HERE ###
    # First, we sort the dataset according their values
    new_data = list(data)
    new_data.sort()

    # Calculate the number of bins
    n_bin = len(range_indices)

    # For each bin, perform the following
    for i in range(n_bin):
        # Find elements to be belonging to each range
        s = [x for x in new_data if x < range_indices[i]]
        # Add the partitioned list to the result
        result.append(s)
        # Find the last element in the previous partition
        last_element = s[len(s) - 1]
        # Find the index of of the last element
        last = new_data.index(last_element)
        # Remove the partitioned list from the dataset
        new_data = new_data[int(last) + 1:]

        # Append the last remaining data list
    result.append([x for x in new_data if x >= range_indices[n_bin - 1]])
    ### END CODE HERE ###

    return result

if __name__ == '__main__':
    D = [55, 30, 68, 39, 1,
         4, 49, 90, 34, 76,
         82, 56, 31, 25, 78,
         56, 38, 32, 88, 9,
         44, 98, 11, 70, 66,
         89, 99, 22, 23, 26]
    print(range_partition(D, [40, 80]))