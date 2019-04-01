#Assume there is no duplicate values;
def sort_merge_join(table_1, table_2):
    result = []

    # sort T1 based on the join attribute
    sorted_table_1 = list(table_1)
    sorted_table_1 = sorted(sorted_table_1, key=lambda sorted_table_1: sorted_table_1[1])

    # sort T2 based on the join attribute
    sorted_table_2 = list(table_2)
    sorted_table_2 = sorted(sorted_table_2, key=lambda sorted_table_2: sorted_table_2[1])

    ### START CODE HERE ###
    index_1 = index_2 = 0
    while True:
        join_attr_1 = sorted_table_1[index_1][1]
        join_attr_2 = sorted_table_2[index_2][1]

        # If join attribute s_T1(i) < join attribute s_T2(i)
        if join_attr_1 < join_attr_2:
            index_1 += 1

        # else
        elif join_attr_1 > join_attr_2:
            # if join attribute s_T1(1) > join attribute s_T2(1)
            # #---Implement here
            index_2 += 1
            # else
        else:
            result.append(
                {",".join([sorted_table_1[index_1][0], str(sorted_table_1[index_1][1]), sorted_table_2[index_2][0]])})
            index_1 += 1
            index_2 += 1  # assume there is no duplicated value


        # if either s_T1(i) or s_T2(j) is EOF Then break
        if (index_1 == len(sorted_table_1)) or (index_2 == len(sorted_table_2)):
            break
            ### END CODE HERE ###
    return result


if __name__ == '__main__':
    table_r = [('Adele', 8), ('Bob', 22), ('Clement', 16), ('Dave', 23), ('Ed', 11),
               ('Fung', 25), ('Goel', 3), ('Harry', 17), ('Irene', 14), ('Joanna', 2),
               ('Kelly', 6), ('Lim', 20), ('Meng', 1), ('Noor', 5), ('Omar', 19)]

    table_s = [('Arts', 8), ('Business', 15), ('CompSc', 2), ('Dance', 12), ('Engineering', 7),
               ('Finance', 21), ('Geology', 10), ('Health', 11), ('IT', 18)]

    print(sort_merge_join(table_r, table_s))
