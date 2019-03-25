from multiprocessing import Pool  # For multiprocessing

from parallel_data_processing.data_parition.hash_partition import h_partition
from parallel_data_processing.data_parition.hash_partition import s_hash
from parallel_data_processing.data_parition.linear_search import linear_search
from parallel_data_processing.data_parition.range_partition import range_partition

from parallel_data_processing.data_parition.round_robin import rr_partition


# Parallel searching algorithm for exact match
def parallel_search_exact(data, target, processor_num, partition_method, search_method):

    results = []

    # We need to set the number of processes to n_processor,
    # which means that the Pool class will only allow 'n_processor' processes
    # running at the same time.
    pool = Pool(processes=processor_num)

    ### START CODE HERE ###

    print("data partitioning:" + str(partition_method.__name__))
    print("searching method:" + str(search_method.__name__))

    if partition_method == range_partition:  # for range partitioning method
        # Perform data partitioning:
        # 2nd parameter is a list of maximum range values (3 ranges)
        range_indices = [40, 80]  # ideally pass this into the function as a variable
        partition_result = partition_method(data, range_indices)
        for index, element in enumerate(range_indices):
            if target < element:
                data_set = partition_result[index]
                break
            else:
                data_set = partition_result[-1]
        print(data_set)
        result = pool.apply(search_method, [data_set, target])
        results.append(result)

    elif partition_method == h_partition:  # for hash partitioning method
        # Perform data partitioning first
        partition_result = partition_method(data, processor_num)
        # Each element in DD has a pair (hash key: records)
        query_hash = s_hash(target, processor_num)
        data_set = list(partition_result[query_hash])
        print(data_set)
        result = pool.apply(search_method, [data_set, target])
        results.append(result)

    else:  # for round-robin or random-unequal partitioning method
        # Perform data partitioning first
        partition_result = partition_method(data, processor_num)
        parallel_result=[pool.apply_async(linear_search,[data_set,target])for data_set in partition_result]

        for process in parallel_result:
            output = process.get()
            results.append(output)


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
    results = parallel_search_exact(data, query, n_processor,rr_partition, linear_search)
    print(results)