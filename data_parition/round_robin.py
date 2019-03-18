def rr_partition(data, n):
    """
    Perform data partitioning on data

    Arguments:
    data -- an input dataset which is a list
    n -- the number of processors

    Return:
    result -- the paritioned subsets of D
    """

    result = []
    for i in range(n):
        result.append([])

    ### START CODE HERE ###
    # For each bin, perform the following
    for index, element in enumerate(data):
        # Calculate the index of the bin that the current data point will be assigned
        index_bin = (int)(index % n)
        # print(str(index) + ":" + str(element))
        result[index_bin].append(element)
    ### END CODE HERE ###

    return result