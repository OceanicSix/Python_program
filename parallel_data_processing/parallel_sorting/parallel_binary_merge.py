from parallel_data_processing.parallel_sorting.parallel_merge_all_sort import parallel_merge_all_sorting
from parallel_data_processing.data_parition.round_robin import rr_partition
from parallel_data_processing.parallel_sorting.sort_merge import serial_sorting
from parallel_data_processing.parallel_sorting.k_way_merging import k_way_merge
import multiprocessing as mp
def parallel_binary_merge(data,n_processor,buffer_size):
    data_sets=rr_partition(data,n_processor)
    pool=mp.Pool(processes=n_processor)
    sorted_lists=[]
    parallel_result=[]
    for data_set in data_sets:
        parallel_result.append(pool.apply_async(serial_sorting,[data_set,buffer_size]))
    for processor in parallel_result:
        sorted_lists.append(processor.get())
    pool.close()
    print(sorted_lists)

    while(len(sorted_lists)!=1):
        merged_set=[]
        if len(sorted_lists)%2==1:
            merged_set.append(sorted_lists.pop())

        start_pos=0
        num_of_merge=int(len(sorted_lists)/2)
        pool=mp.Pool(processes=num_of_merge)
        parallel_result=[]
        for i in range(num_of_merge):
            result=pool.apply_async(k_way_merge,[sorted_lists[start_pos:start_pos+2]])
            start_pos+=2
            parallel_result.append(result)
        for processor in parallel_result:
            merged_set.append(processor.get())
        sorted_lists=merged_set
        print(sorted_lists)

    return sorted_lists[0]




if __name__ == '__main__':
    data = [8, 12, 16, 4, 11, 15, 3, 7, 14, 2, 6, 10, 1, 5, 9, 13]
    result = parallel_binary_merge(data, 5, 4)
    print(result)
