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

if __name__ == '__main__':
    D = [55, 30, 68, 39, 1,
         4, 49, 90, 34, 76,
         82, 56, 31, 25, 78,
         56, 38, 32, 88, 9,
         44, 98, 11, 70, 66,
         89, 99, 22, 23, 26]
    print(rr_partition(D, 3))