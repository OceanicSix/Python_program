# You will have to edit qsort(arr) to make it work.
def qsort(arr):
    """
    Quicksort a list

    Arguments:
    arr -- the input list to be sorted

    Return:
    result -- the sorted arr
    """
    if len(arr) <= 1:
        return arr
    else:
        # take the first element as the pivot
        pivot = arr[0]
        left_arr = [x for x in arr[1:] if x < pivot]  # Edit is required here
        right_arr = [x for x in arr[1:] if x >= pivot]  # Edit is required here
        # uncomment this to see what to print
        # print("Left:" + str(left_arr)+" Pivot : "+ str(pivot)+" Right: " + str(right_arr))
        value = qsort(left_arr) + [pivot] + qsort(right_arr)

        return value


# You will have to edit find_min(records) and k_way_merge(record_sets) to make it work.
import sys


# Find the smallest record
def find_min(records):
    """
    Find the smallest record

    Arguments:
    records -- the input record set

    Return:
    result -- the smallest record's index
    """
    m = records[0]
    index = 0
    for i in range(len(records)):
        if (records[i] < m):  # Edit is required here
            index = i
            m = records[i]
    return index


def k_way_merge(record_sets):
    """
    K-way merging algorithm

    Arguments:
    record_sets -- the set of mulitple sorted sub-record sets

    Return:
    result -- the sorted and merged record set
    """

    # indexes will keep the indexes of sorted records in the given buffers
    indexes = []
    for x in record_sets:
        indexes.append(0)  # initialisation with 0

    # final result will be stored in this variable
    result = []

    while (True):
        merged_result = []  # the merging unit (i.e. # of the given buffers)

        # This loop gets the current position of every buffer
        for i in range(len(record_sets)):
            if (indexes[i] >= len(record_sets[i])):
                merged_result.append(sys.maxsize)  # Edit is required here
            else:
                merged_result.append(record_sets[i][indexes[i]])

                # find the smallest record
        smallest = find_min(merged_result)

        # if we only have sys.maxsize on the tuple, we reached the end of every record set
        if (merged_result[smallest] == sys.maxsize):  # Edit is required here
            break

        # This record is the next on the merged list
        result.append(record_sets[smallest][indexes[smallest]])
        indexes[smallest] += 1

    return result


def serial_sorting(dataset, buffer_size):
    """
    Perform a serial external sorting method based on sort-merge
    The buffer size determines the size of eac sub-record set

    Arguments:
    dataset -- the entire record set to be sorted
    buffer_size -- the buffer size determining the size of each sub-record set

    Return:
    result -- the sorted record set
    """

    if (buffer_size <= 2):
        print("Error: buffer size should be greater than 2")
        return

    result = []

    ### START CODE HERE ###

    # --- Sort Phase ---
    sorted_set = []

    # Read buffer_size pages at a time into memory and
    # sort them, and write out a sub-record set (i.e. variable: subset)
    start_pos = 0
    N = len(dataset)
    while True:
        if ((N - start_pos) > buffer_size):
            # read B-records from the input, where B = buffer_size
            subset = dataset[start_pos:start_pos + buffer_size]
            # sort the subset (using qucksort defined above)
            sorted_subset = qsort(subset)
            sorted_set.append(sorted_subset)
            start_pos += buffer_size
        else:
            # read the last B-records from the input, where B is less than buffer_size
            subset = dataset[start_pos:]
            # sort the subset (using qucksort defined above)
            sorted_subset = qsort(subset)
            sorted_set.append(sorted_subset)
            break

    # --- Merge Phase ---
    merge_buffer_size = buffer_size - 1
    dataset = sorted_set
    while True:
        merged_set = []

        N = len(dataset)
        start_pos = 0
        while True:
            if ((N - start_pos) > merge_buffer_size):
                # read C-record sets from the merged record sets, where C = merge_buffer_size
                subset = dataset[start_pos:start_pos + merge_buffer_size]
                merged_set.append(k_way_merge(subset))  # merge lists in subset
                start_pos += merge_buffer_size
            else:
                # read C-record sets from the merged sets, where C is less than merge_buffer_size
                subset = dataset[start_pos:]
                merged_set.append(k_way_merge(subset))  # merge lists in subset
                break

        dataset = merged_set
        if (len(dataset) <= 1):  # if the size of merged record set is 1, then stop
            result = merged_set
            break
    ### END CODE HERE ###

    return result


# Include this package for parallel processing
import multiprocessing as mp

def rr_partition(data, processor_num):

    result = []
    for i in range(processor_num):
        result.append([])

    for index, element in enumerate(data):
        # Calculate the index of the bin that the current data point will be assigned
        index_in_result = index % processor_num
        # print(str(index) + ":" + str(element))
        result[index_in_result].append(element)


    return result

def parallel_binary_merge_sorting(dataset, n_processor, buffer_size):
    """
    Perform a parallel binary-merge sorting method

    Arguments:
    dataset -- entire record set to be sorted
    n_processor -- number of parallel processors
    buffer_size -- buffer size determining the size of each sub-record set

    Return:
    result -- the merged record set
    """

    if (buffer_size <= 2):
        print("Error: buffer size should be greater than 2")
        return

    result = []

    ### START CODE HERE ###
    partition_result=rr_partition(dataset,n_processor)


    ### END CODE HERE ###

    return result


# def parallel_binary_merge_sorting1(dataset,buffer_size):
#     result=[]
#     num_of_dataset=len(dataset)
#     if num_of_dataset==1:
#         return result
#     pool = mp.Pool(processes=2)
#     parallel_result = []
#     sorted_set = []
#     for data in dataset:
#         parallel_result.append(pool.apply_async(serial_sorting, [data, buffer_size]))
#     for processor in parallel_result:
#         sorted_set += processor.get()
#     pool.close()
#     print("sorted entire set:" + str(sorted_set))
#     result = k_way_merge(sorted_set)

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

    R = [('Adele', 8), ('Bob', 22), ('Clement', 16), ('Dave', 23), ('Ed', 11),
             ('Fung', 25), ('Goel', 3), ('Harry', 17), ('Irene', 14), ('Joanna', 2),
             ('Kelly', 6), ('Lim', 20), ('Meng', 1), ('Noor', 5), ('Omar', 19)]

        # S consists of 8 pairs, each comprising two attributes (nominal and numeric)
    S = [('Arts', 8), ('Business', 15), ('CompSc', 2), ('Dance', 12), ('Engineering', 7),
             ('Finance', 21), ('Geology', 10), ('Health', 11), ('IT', 18)]
    result = parallel_merge_all_sorting(R, 10, 20)
    print("Final Result:" + str(result))