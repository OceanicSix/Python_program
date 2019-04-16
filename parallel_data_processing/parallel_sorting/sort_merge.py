from parallel_data_processing.parallel_sorting.k_way_merging import k_way_merge
from parallel_data_processing.parallel_sorting.quick_sort import quick_sort

def serial_sorting(dataset, buffer_size): # assume main memory can only hold to buffer_size number of records


    if (buffer_size <= 2):
        print("Error: buffer size should be greater than 2")
        return

    result = []

    ### START CODE HERE ###

    # --- Sort Phase ---divide into multiple subfile and sort them locally
    sorted_set = []

    start_pos = 0
    N = len(dataset)
    while True:
        if ((N - start_pos) > buffer_size):
            # read buffer_size number of record each time
            subset = dataset[start_pos:start_pos + buffer_size]
            # sort the subset (using qucksort defined above)
            sorted_subset = quick_sort(subset)
            sorted_set.append(sorted_subset)
            start_pos += buffer_size
        else:
            # read the last B-records from the input, where B is less than buffer_size
            subset = dataset[start_pos:]
            # sort the subset (using qucksort defined above)
            sorted_subset = quick_sort(subset)
            sorted_set.append(sorted_subset)
            break

    # --- Merge Phase ---
    merge_buffer_size = buffer_size - 1
    dataset = sorted_set
    while True:
        merged_set = [] # to store the set of record that is merged from 1 pass

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

    return result[0]

if __name__ == '__main__':
    data = [8, 12, 16, 4, 11, 15, 3, 7, 14, 2, 6, 10, 1, 5, 9, 13]
    result = serial_sorting(data, 4)
    print("final sorting result:" + str(result))