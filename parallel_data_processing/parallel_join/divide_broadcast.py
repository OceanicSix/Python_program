from parallel_data_processing.data_parition.round_robin import rr_partition
from parallel_data_processing.parallel_join.hash_join import hash_join

import multiprocessing as mp


def divide_broadcast(table_1, table_2, processor_num):



    results = []

    ### START CODE HERE ###

    # Partition T1 into sub-tables using rr_partition().
    # The number of the sub-tables must be the equal to the n_processor
    T1_subsets = rr_partition(table_1, processor_num)

    # Pool: a Python method enabling parallel processing.
    pool = mp.Pool(processes=processor_num)

        # Apply a join on each processor

        # Note that as we assume a shared-memory architecture, no replication
        # of the broadcast table (in this case: table T2 (smaller table) occurs.
    parallel_result = [pool.apply_async(hash_join, [data_set, table_2]) for data_set in T1_subsets]
    for processor in parallel_result:
        output = processor.get()
        results.append(output)

    ### END CODE HERE ###

    return results


if __name__ == '__main__':
    table_r = [('Adele', 8), ('Bob', 22), ('Clement', 16), ('Dave', 23), ('Ed', 11),
               ('Fung', 25), ('Goel', 3), ('Harry', 17), ('Irene', 14), ('Joanna', 2),
               ('Kelly', 6), ('Lim', 20), ('Meng', 1), ('Noor', 5), ('Omar', 19)]

    table_s = [('Arts', 8), ('Business', 15), ('CompSc', 2), ('Dance', 12), ('Engineering', 7),
               ('Finance', 21), ('Geology', 10), ('Health', 11), ('IT', 18)]


    print(divide_broadcast(table_r,table_s,3))