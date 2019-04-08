# The first step in the merge-all groupby method

import multiprocessing as mp
def local_groupby(dataset):


    dict = {}
    for index, record in enumerate(dataset):
        key = record[0]
        val = record[1]
        if key not in dict:
            dict[key] = 0
        dict[key] += val
    return dict





def parallel_merge_all_groupby(dataset):
    """
    Perform a parallel merge_all groupby method

    Arguments:
    dataset -- entire record set to be merged

    Return:
    result -- the aggregated record dictionary according to the group_by attribute index
    """

    result = {}

    ### START CODE HERE ###

    # Define the number of parallel processors: the number of sub-datasets.
    n_processor = len(dataset)

    # Pool: a Python method enabling parallel processing.
    pool = mp.Pool(processes=n_processor)

    # ----- Local aggregation step -----
    local_result = []
    for data in dataset:
        # call the local aggregation method
        local_result.append(pool.apply(local_groupby, [data]))
    pool.close()
    print(local_result)

    # ---- Global aggregation step ----
    # Let's assume that the global operator is sum.
    # Implement here
    for subset in local_result:
        for key,value in subset.items():
            if key not in result:
                result[key]=value
            else:
                result[key]+=value

    ### END CODE HERE ###

    return result


if __name__ == '__main__':
    data1 = [('A', 1), ('B', 2), ('C', 3), ('A', 10), ('B', 20), ('C', 30)]
    data2 = [('A', 4), ('B', 5), ('C', 6), ('A', 40), ('B', 50), ('C', 60)]
    # result = local_groupby(data1)
    # print(result)
    # result = local_groupby(data2)
    # print(result)
    E = [data1, data2]
    result = parallel_merge_all_groupby(E)
    print(result)

