def s_hash(x, n):
    """
    Define a simple hash function for demonstration

    Arguments:
    x -- an input record
    n -- the number of processors

    Return:
    result -- the hash value of x
    """

    ### START CODE HERE ###
    result = x % n
    ### END CODE HERE ###

    return result


def h_partition(data, n):
    """
    Perform hash data partitioning on data

    Arguments:
    data -- an input dataset which is a list
    n -- the number of processors

    Return:
    result -- the paritioned subsets of D
    """

    ### START CODE HERE ###
    dic = {}  # We will use a dictionary
    for x in data:  # For each data record, perform the following
        h = s_hash(x, n)  # Get the hash key of the input
        if (h in dic.keys()):  # If the key exists
            s = dic[h]
            s.add(x)
            dic[h] = s  # Add the new input to the value set of the key
        else:  # If the key does not exist
            s = set()  # Create an empty value set
            #s.update({x})
            s.add(x)
            dic[h] = s  # Add the value set to the key
    ### END CODE HERE ###

    return dic

if __name__ == '__main__':
    D = [55, 30, 68, 39, 1,
         4, 49, 90, 34, 76,
         82, 56, 31, 25, 78,
         56, 38, 32, 88, 9,
         44, 98, 11, 70, 66,
         89, 99, 22, 23, 26]
    print(h_partition(D, 3))