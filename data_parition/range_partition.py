def range_partition(data, range_indices):

    result = []

    new_data = data[:]
    new_data.sort()

    # Calculate the number of bins
    range_index = len(range_indices)

    # For each bin, perform the following
    for i in range(range_index):
        # Find elements to be belonging to each range
        lower_part = [x for x in new_data if x < range_indices[i]]
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

if __name__ == '__main__':
    D = [55, 30, 68, 39, 1,
         4, 49, 90, 34, 76,
         82, 56, 31, 25, 78,
         56, 38, 32, 88, 9,
         44, 98, 11, 70, 66,
         89, 99, 22, 23, 26]
    print(range_partition(D, [40, 80]))