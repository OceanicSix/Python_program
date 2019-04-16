# Range data partitionining function (Need to modify as instructed above)
def range_partition(data, range_indices):
    """
    Perform range data partitioning on data based on the join attribute

    Arguments:
    data -- an input dataset which is a list
    range_indices -- the index list of ranges to be s:plit

    Return:
    result -- the paritioned subsets of D
    """
    result = []

    ### START CODE HERE ###
    new_data = data[:]
    new_data.sort(key=lambda pair: pair[1])
    # Calculate the number of bins
    range_index = len(range_indices)

    # For each bin, perform the following
    for i in range(range_index):
        # Find elements to be belonging to each range
        lower_part = [x for x in new_data if x[1] < range_indices[i]]
        # Add the partitioned list to the result
        result.append(lower_part)
        # Find the last element in the previous partition
        last_element = lower_part[-1]
        # Find the index of of the last element
        last = new_data.index(last_element)
        # Remove the partitioned list from the dataset
        new_data = new_data[last + 1:]

    # append the remeaning list
    result.append(new_data)


    ### END CODE HERE ###

    return result


def H(r):
    """
    We define a hash function 'H' that is used in the hashing process works
    by summing the first and second digits of the hashed attribute, which
    in this case is the join attribute.

    Arguments:
    r -- a record where hashing will be applied on its join attribute

    Return:
    result -- the hash index of the record r
    """

    # Convert the value of the join attribute into the digits
    digits = [int(d) for d in str(r[1])]

    # Calulate the sum of elemenets in the digits
    return sum(digits)


def HB_join(T1, T2):
    """
    Perform the hash-based join algorithm.
    The join attribute is the numeric attribute in the input tables T1 & T2

    Arguments:
    T1 & T2 -- Tables to be joined

    Return:
    result -- the joined table
    """

    result = []

    dic = {}  # We will use a dictionary

    # For each record in table T2
    for s in T2:
        # Hash the record based on join attribute value using hash function H into hash table
        s_key = H(s)
        if s_key in dic:
            dic[s_key].add(s)  # If there is an entry
        else:
            dic[s_key] = {s}

    # For each record in table T1 (probing)
    for r in T1:
        # Hash the record based on join attribute value using H
        r_key = H(r)

        # If an index entry is found Then
        if r_key in dic:
            # Compare each record on this index entry with the record of table T1
            for item in dic[r_key]:
                if item[1] == r[1]:
                    # Put the rsult
                    result.append({", ".join([r[0], str(r[1]), item[0]])})

    return result


# Include this package for parallel processing
import multiprocessing as mp


def DPBP_join(T1, T2, n_processor):
    """
    Perform a disjoint partitioning-based parallel join algorithm.
    The join attribute is the numeric attribute in the input tables T1 & T2

    Arguments:
    T1 & T2 -- Tables to be joined
    n_processor -- the number of parallel processors

    Return:
    result -- the joined table
    """

    results = []

    ### START CODE HERE ###

    # Partition T1 & T2 into sub-tables using range_partition().
    # The number of the sub-tables must be the equal to the n_processor
    T1_subsets = range_partition(T1, [10, 20])
    T2_subsets = range_partition(T2, [10, 20])

    data_size = len(T1_subsets)
    assert (data_size == n_processor), "The number of the sub-tables must be the equal to the n_processor"
    pool = mp.Pool(processes=n_processor)

    parallel_result = [pool.apply_async(HB_join, [T1_subsets[index], T2_subsets[index]])
                       for index in range(data_size)]

    for processor in parallel_result:
        output = processor.get()
        results.append(output)
    ### END CODE HERE ###

    return results

if __name__ == '__main__':
    R = [('Adele', 8), ('Bob', 22), ('Clement', 16), ('Dave', 23), ('Ed', 11),
         ('Fung', 25), ('Goel', 3), ('Harry', 17), ('Irene', 14), ('Joanna', 2),
         ('Kelly', 6), ('Lim', 20), ('Meng', 1), ('Noor', 5), ('Omar', 19)]

    # S consists of 8 pairs, each comprising two attributes (nominal and numeric)
    S = [('Arts', 8), ('Business', 15), ('CompSc', 2), ('Dance', 12), ('Engineering', 7),
         ('Finance', 21), ('Geology', 10), ('Health', 11), ('IT', 18)]
    n_processor = 3
    print(DPBP_join(R, S, n_processor))