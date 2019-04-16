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
        left_arr = [x for x in arr[1:] if x[1] < pivot[1]]  # Edit is required here
        right_arr = [x for x in arr[1:] if x[1] >= pivot[1]]  # Edit is required here
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
        if (records[i][1] < m[1]):  # Edit is required here
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
                merged_result.append(("place_filler",sys.maxsize))  # Edit is required here
            else:
                merged_result.append(record_sets[i][indexes[i]])

                # find the smallest record
        smallest = find_min(merged_result)

        # if we only have sys.maxsize on the tuple, we reached the end of every record set
        if (merged_result[smallest][1] == sys.maxsize):  # Edit is required here
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

# Include this package for parallel processing


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

    #perform round robin partition
    partition_result=rr_partition(dataset,n_processor)

    # ---------------------------sorting phase-----------------------
    pool = mp.Pool(processes=n_processor)
    sorted_lists = []    # a list to store all sorted data_set
    parallel_result = [] # a list to store all the multi-processing object

    #each processor sort their own partition in parallel, then add the result into sorted_lists
    for data_set in partition_result:
        parallel_result.append(pool.apply_async(serial_sorting, [data_set, buffer_size]))
    for processor in parallel_result:
        sorted_lists.append(processor.get()[0])
    pool.close()


 # ---------------------------merging phase-----------------------
    while (len(sorted_lists) != 1):  # loop ends when there is only one data_set left, in other words, the merging is finished
        merging_result = []             # used to stored the result of merging
        if len(sorted_lists) % 2 == 1:
            merging_result.append(sorted_lists.pop())  # first check if the number of data_set is an even number
                                                    # if yes, the last dataset will be added into merging result directly

        start_pos = 0
        num_of_merge = int(len(sorted_lists) / 2)   #As every two data_set is merged togerther, then the number of merge
                                                    #can be calculated in this way

        pool = mp.Pool(processes=num_of_merge) # each merge require one processor
        parallel_result = []
        for i in range(num_of_merge):
            merged_list = pool.apply_async(k_way_merge, [sorted_lists[start_pos:start_pos + 2]])#each process works on two different data_set
            start_pos += 2
            parallel_result.append(merged_list)
        for processor in parallel_result:
            merging_result.append(processor.get())
        sorted_lists = merging_result # the result of merging become the input of next iteration
        pool.close()
        result=sorted_lists[0]


    ### END CODE HERE ###

    return result
    ### END CODE HERE ###








if __name__ == '__main__':

    R = [('Adele', 8), ('Bob', 22), ('Clement', 16), ('Dave', 23), ('Ed', 11),
             ('Fung', 25), ('Goel', 3), ('Harry', 17), ('Irene', 14), ('Joanna', 2),
             ('Kelly', 6), ('Lim', 20), ('Meng', 1), ('Noor', 5), ('Omar', 19)]

        # S consists of 8 pairs, each comprising two attributes (nominal and numeric)
    S = [('Arts', 8), ('Business', 15), ('CompSc', 2), ('Dance', 12), ('Engineering', 7),
             ('Finance', 21), ('Geology', 10), ('Health', 11), ('IT', 18)]
    result = parallel_binary_merge_sorting(R,10,20)
    print("Final Result:" + str(result))