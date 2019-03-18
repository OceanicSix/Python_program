def s_hash(record_value, process_num):

    hash_value = record_value % process_num

    return hash_value


def h_partition(data, processor_num):

    dic = {}  # We will use a dictionary
    for record in data:  # For each data record, perform the following
        hash_result = s_hash(record, processor_num)  # Get the hash key of the input
        if (hash_result in dic.keys()):  # If the key exists
             dic[hash_result].add(record)
        else:  # If the key does not exist
            dic[hash_result] = {record}  # Add the value set to the key


    return dic

if __name__ == '__main__':
    D = [55, 30, 68, 39, 1,
         4, 49, 90, 34, 76,
         82, 56, 31, 25, 78,
         56, 38, 32, 88, 9,
         44, 98, 11, 70, 66,
         89, 99, 22, 23, 26]
    print(h_partition(D, 3))