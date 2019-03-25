import multiprocessing as mp
from parallel_data_processing.parallel_join.hash_join import hash_join
def range_partition(data, range_indices):

    result = []

    new_data = data[:]
    new_data=sorted(new_data,key=lambda new_data:new_data[1])

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

    #append the remeaning list
    result.append(new_data)

    return result




def disjoint_join(table_1, table_2, processor_num):


    result = []

    ### START CODE HERE ###

    # --- Implement the algorithm

    # Partition T1 & T2 into sub-tables using range_partition().
    partition_result_1=range_partition(table_1,[10,20])
    partition_result_2=range_partition(table_2,[10,20])
    data_size=len(partition_result_1)
    assert (data_size==processor_num), "The number of the sub-tables must be the equal to the n_processor"
    pool = mp.Pool(processes=processor_num)


    parallel_result=[pool.apply_async(hash_join,[partition_result_1[index],partition_result_2[index]])
                     for index in range(data_size)]

    for processor in parallel_result:
        output=processor.get()
        result.append(output)


    ### END CODE HERE ###

    return result

if __name__ == '__main__':
    table_r = [('Adele', 8), ('Bob', 22), ('Clement', 16), ('Dave', 23), ('Ed', 11),
               ('Fung', 25), ('Goel', 3), ('Harry', 17), ('Irene', 14), ('Joanna', 2),
               ('Kelly', 6), ('Lim', 20), ('Meng', 1), ('Noor', 5), ('Omar', 19)]

    table_s = [('Arts', 8), ('Business', 15), ('CompSc', 2), ('Dance', 12), ('Engineering', 7),
               ('Finance', 21), ('Geology', 10), ('Health', 11), ('IT', 18)]

    print(disjoint_join(table_r,table_s,3))