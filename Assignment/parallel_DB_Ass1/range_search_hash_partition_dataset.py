def linear_search(data, key):
    """
    Perform linear search on data for the given key

    Arguments:
    data -- an input dataset which is a list or a numpy array
    key -- an query record

    Return:
    result -- the position of searched record
    """

    matched_records = []

    ### START CODE HERE ###
    for record in data:
        if record[1]==key:
            matched_records.append(data.index(record))#append the position of matched recrod to result

    ### END CODE HERE ###

    return matched_records


# Define a simple hash function.
def s_hash(x, n):
    """
    Define a simple hash function for demonstration

    Arguments:
    x -- an input record
    n -- the number of processors

    Return:
    result -- the hash value of x
    """
    result = x % n

    return result


# Hash data partitionining function.
# We will use the "s_hash" function defined above to realise this partitioning
def h_partition(data, n):
    """
    Perform hash data partitioning on data

    Arguments:
    data -- an input dataset which is a list
    n -- the number of processors

    Return:
    result -- the paritioned subsets of D
    """
    partitions = {}

    ### START CODE HERE ###
    for record in data:
        hash_value=s_hash(record[1],n)
        if hash_value not in partitions:
            partitions[hash_value]=[record]
        else:
            partitions[hash_value].append(record)
    ### END CODE HERE ###

    return partitions


from multiprocessing import Pool


# Parallel searching algorithm for range selection
def parallel_search_range(data, query_range, n_processor):
    """
    Perform parallel search for range selection on data for the given key

    Arguments:
    data -- the input dataset which is a list
    query_range -- a query record in the form of a range (e.g. [30, 50])
    n_processor -- the number of parallel processors

    Return:
    results -- the matched record information
    """

    results = []

    pool = Pool(processes=n_processor)

    ### START CODE HERE ###

    # Perform data partitioning first

    partition_result=h_partition(data,n_processor)
    for query in range(query_range[0],query_range[1]+1):
        hash_value=s_hash(query,n_processor)
        working_dataset=partition_result[hash_value]
        indices=pool.apply(linear_search,[working_dataset,query])
        for index in indices:
            results.append(working_dataset[index])



    ### END CODE HERE ###

    return results

if __name__ == '__main__':
    R = [('Adele', 8), ('Bob', 22), ('Clement', 16), ('Dave', 23), ('Ed', 11),
         ('Fung', 25), ('Goel', 3), ('Harry', 17), ('Irene', 14), ('Joanna', 2),
         ('Kelly', 6), ('Lim', 20), ('Meng', 1), ('Noor', 5), ('Omar', 19)]

    # S consists of 8 pairs, each comprising two attributes (nominal and numeric)
    S = [('Arts', 8), ('Business', 15), ('CompSc', 2), ('Dance', 12), ('Engineering', 7),
         ('Finance', 21), ('Geology', 10), ('Health', 11), ('IT', 18)]

    # print(linear_search(R,16))
    # print(h_partition(R,3))
    # print(parallel_search_range(R,[0,10],4))
    n_processor = 3
    # Range partition, linear_search
    results = parallel_search_range(R, [5, 20], n_processor)
    print(results) 