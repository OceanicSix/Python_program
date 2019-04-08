# Let's first look at 'k-way merging algorithm' that will be used
# to merge sub-record sets in our external sorting algorithm.
import sys


# Find the smallest record
def find_min(records):
    smallest = records[0]
    index = 0
    for i in range(len(records)):
        if (records[i] < smallest):
            index = i
            smallest = records[i]
    return index


def k_way_merge(record_sets):


    # indexes will keep the indexes of record that is to be sorted in next round
    indexes = []
    for x in range(len(record_sets)):
        indexes.append(0)  # initialisation index with 0

    # final result will be stored in this variable
    result = []




    #for first iteration, put
    while (True):
        buffer = []  # initialise buffer to store the input record

        # This loop gets the current position of every buffer
        for i in range(len(record_sets)):
            if (indexes[i] >= len(record_sets[i])):
                buffer.append(sys.maxsize)
                # to generate the largest number, so it can't be found as smallest in find_min function
                # because this list has been reached to the end , so it should not be considered anymore.
                # then in later iteration, for the first set of record, a largest number will always be append
            else:
                buffer.append(record_sets[i][indexes[i]])
                # indexes[i] only store the current index for this set of record, and indexes list
                # and record_sets 's index are corresponded ( i.e. indexes[i] represent the index
                # of record for record_set [i]


                # find the smallest record
        smallest = find_min(buffer)

        # when all three subset are exhausted, then the previous for loop will generate 3 largest
        #number, then the smallest one will also be the largest number
        if (buffer[smallest] == sys.maxsize):
            break

        # smallest record is append in the final result.
        result.append(record_sets[smallest][indexes[smallest]])
        indexes[smallest] += 1

    return result


if __name__ == '__main__':
    buffers = [[1, 2, 3, 4, 8, 13], [5, 6, 7, 11, 12], [9, 10, 14, 15, 16]]
    result = k_way_merge(buffers)
    print(result)