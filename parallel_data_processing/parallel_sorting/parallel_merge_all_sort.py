from parallel_data_processing.data_parition.round_robin import rr_partition

# Include this package for parallel processing
import multiprocessing as mp
from parallel_data_processing.parallel_sorting.k_way_merging import k_way_merge
from parallel_data_processing.parallel_sorting.sort_merge import serial_sorting

def parallel_merge_all_sorting(dataset, n_processor, buffer_size):

    if (buffer_size <= 2):
        print("Error: buffer size should be greater than 2")
        return

    result = []

    ### START CODE HERE ###

    # Pre-requisite: Perform data partitioning using round-robin partitioning
    subsets = rr_partition(dataset, n_processor)

    # Pool: a Python method enabling parallel processing.
    pool = mp.Pool(processes=n_processor)


    # ----- Sort phase -----
    parallel_result=[]
    sorted_set = []
    for data in subsets:
        parallel_result.append(pool.apply_async(serial_sorting, [data, buffer_size]))
    for processor in parallel_result:
        sorted_set+=processor.get()
    pool.close()

    # ---- Final merge phase ----
    print("sorted entire set:" + str(sorted_set))
    result = k_way_merge(sorted_set)
    ### END CODE HERE ###

    return result

if __name__ == '__main__':
    data = [8, 12, 16, 4, 11, 15, 3, 7, 14, 2, 6, 10, 1, 5, 9, 13]
    result = parallel_merge_all_sorting(data, 4, 4)
    print("final result:" + str(result))