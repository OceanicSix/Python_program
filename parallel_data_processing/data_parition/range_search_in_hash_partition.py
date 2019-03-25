from time import time
from multiprocessing import Pool
from parallel_data_processing.data_parition.hash_partition import h_partition
from parallel_data_processing.data_parition.hash_partition import s_hash

from parallel_data_processing.data_parition.linear_search import linear_search

# Parallel searching algorithm for range selection
def parallel_search_range(data, query_range, processor_num):



    results = []

    pool = Pool(processes=processor_num)

    ### START CODE HERE ###

    # Perform data partitioning first
    partition_result = h_partition(data, processor_num)


    #------------------------------------------solution provided---------------------------------

    # for query in range(query_range[0], query_range[1], 1):
    #     # Each element in DD has a pair (hash key: records)
    #     query_hash =s_hash(query, processor_num)
    #     data_set = list(partition_result[query_hash])
    #     result = pool.apply(linear_search, [data_set, query])
    #     results.append(result)

    #---------------------------------My way of parallel processing---------------------------


    hash_list=[]
    for query in range(query_range[0], query_range[1], 1):
        hash_list.append([query,s_hash(query, processor_num)])
    parallel_result=[pool.apply_async(linear_search,[list(partition_result[hash_list[index][1]]),hash_list[index][0]])
                     for index in range(len(hash_list))]

    for processor in parallel_result:
        output=processor.get()
        results.append(output)


    ### END CODE HERE ###

    return results

if __name__ == '__main__':
    D = [55, 30, 68, 39, 1,
         4, 49, 90, 34, 76,
         82, 56, 31, 25, 78,
         56, 38, 32, 88, 9,
         44, 98, 11, 70, 66,
         89, 99, 22, 23, 26]
    time_beg = time()
    results = parallel_search_range(D, [30, 40], 5)
    time_end=time()
    print(results)
    print(time_end-time_beg)