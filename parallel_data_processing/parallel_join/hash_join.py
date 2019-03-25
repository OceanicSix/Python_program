def hash_attr(attr):

    digits_list = [int(num) for num in str(attr[1])]

    # Calulate the sum of elemenets in the digits
    return sum(digits_list)


def hash_join(table_1, table_2):

    result = []

    ### START CODE HERE ###
    dic = {}  # We will use a dictionary

    # For each record in table T2
    for entry_2 in table_2:
        # Hash the record based on join attribute value using hash function H into hash table
        index_2 = hash_attr(entry_2)
        if index_2 in dic:
            dic[index_2].add(entry_2)  # If there is an entry
        else:
            dic[index_2] = {entry_2}

    # For each record in table T1 (probing)
    for entry_1 in table_1:
        # Hash the record based on join attribute value using H
        index_1= hash_attr(entry_1)
        if index_1 in dic:
            for set_element in dic[index_1]:
                if entry_1[1]==set_element[1]:
                    result.append({",".join([entry_1[0],str(entry_1[1]),set_element[0]])})


        # If an index entry is found Then
        # #---Implemente here: You need to
        # Compare each record on this index entry with the record of table T1
        # If the key is the same then put the result

        ### END CODE HERE ###

    return result



if __name__ == '__main__':
    table_r = [('Adele', 8), ('Bob', 22), ('Clement', 16), ('Dave', 23), ('Ed', 11),
               ('Fung', 25), ('Goel', 3), ('Harry', 17), ('Irene', 14), ('Joanna', 2),
               ('Kelly', 6), ('Lim', 20), ('Meng', 1), ('Noor', 5), ('Omar', 19)]

    table_s = [('Arts', 8), ('Business', 15), ('CompSc', 2), ('Dance', 12), ('Engineering', 7),
               ('Finance', 21), ('Geology', 10), ('Health', 11), ('IT', 18)]

    print(hash_join(table_r,table_s))