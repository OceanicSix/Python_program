from multiprocessing import Pool  # For multiprocessing
from data_parition.range_partition import range_partition
from data_parition.hash_partition import h_partition
from data_parition.hash_partition import s_hash
from data_parition.linear_search import linear_search
from data_parition.round_robin import rr_partition
# Parallel searching algorithm for exact match
def parallel_search_exact(data, query, n_processor, m_partition, m_search):
    """
    Perform parallel search for exact match on data for the given key

    Arguments:
    data -- an input dataset which is a list
    query -- a query record
    n_processor -- the number of parallel processors
    m_partition -- a data partitioning method
    m_search -- a search method

    Return:
    results -- the matched record information
    """

    results = []

    # Pool: a Python method enabling parallel processing.
    # We need to set the number of processes to n_processor,
    # which means that the Pool class will only allow 'n_processor' processes
    # running at the same time.
    pool = Pool(processes=n_processor)

    ### START CODE HERE ###

    print("data partitioning:" + str(m_partition.__name__))
    print("searching method:" + str(m_search.__name__))

    if m_partition == range_partition:  # for range partitioning method
        # Perform data partitioning:
        # 2nd parameter is a list of maximum range values (3 ranges)
        range_indices = [40, 80]  # ideally pass this into the function as a variable
        DD = m_partition(data, range_indices)
        for index, element in enumerate(range_indices):
            if query < element:
                m = DD[index]
                break
            else:
                m = DD[-1]
        result = pool.apply(m_search, [m, query])
        results.append(result)

    elif m_partition == h_partition:  # for hash partitioning method
        # Perform data partitioning first
        DD = m_partition(data, n_processor)
        # Each element in DD has a pair (hash key: records)
        query_hash = s_hash(query, n_processor)
        d = list(DD[query_hash])
        result = pool.apply(m_search, [d, query])
        results.append(result)

    else:  # for round-robin or random-unequal partitioning method
        # Perform data partitioning first
        DD = m_partition(data, n_processor)
        for d in DD:  # Perform parallel search on all data partitions
            print(d)
            result = pool.apply_async(m_search, [d, query])
            output = result.get()  # if you use pool.apply_sync(), uncomment this.
            results.append(output)  # if you use pool.apply_sync(), uncomment this.
            # results.append(result) # if you use pool.apply_sync(), comment out this.

    """ 
    The method 'pool.apply()' will lock the function call until the function call is finished. 
    The method 'pool.apply_sync()' will not lock the function call,the call results will return immediately instead 
    of waiting for the result, and each method call will be alloacted to a different process. 
    So in this case,pool.apply_async() is processing the search in parallel,
    while the pool.apply() is not. 
    The reason we can use pool.apply() to do search for range_partition and hash_partition data 
    is that as long as we know which partition to do search，we don't need to search in parallel.


    """
    ### END CODE HERE ###

    return results

if __name__ == '__main__':
    data = [55, 30, 68, 39, 1,
         4, 49, 90, 34, 76,
         82, 56, 31, 25, 78,
         56, 38, 32, 88, 9,
         44, 98, 11, 70, 66,
         89, 99, 22, 23, 26]  # input data
    sortD = list(data)
    sortD.sort()
    query = 31  # query term
    n_processor = 3  # number of parallel processors

    ### parallel searching for exact match

    # round-robin partition, linear_search
    results = parallel_search_exact(data, query, n_processor, rr_partition, linear_search)
    print(results)