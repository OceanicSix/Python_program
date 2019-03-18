def linear_search(data, key):
    """
    Perform linear search on data for the given key

    Arguments:
    data -- an input dataset which is a list or a numpy array
    key -- an query record

    Return:
    result -- the position of searched record
    """

    matched_record = None
    position = -1  # not found position

    ### START CODE HERE ###
    for x in data:
        if x == key:  # If x is matched with key
            matched_record = x
            position = data.index(x)  # Get the index of x
            break
    ### END CODE HERE ###

    return position, matched_record