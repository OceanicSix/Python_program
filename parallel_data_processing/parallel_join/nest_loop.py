def nest_loop_join(table_1, table_2):

    result = []

    ### START CODE HERE ###

    # For each record of R
    for entry_1 in table_1:
        # For each record of S
        for entry_2 in table_2:
            # If matched Then
            if (entry_1[1] == entry_2[1]):
                # Store the record into the result list
                result.append({", ".join([entry_1[0], str(entry_1[1]), entry_2[0]])})

    ### END CODE HERE ###

    return result





if __name__ == '__main__':
    table_r = [('Adele', 8), ('Bob', 22), ('Clement', 16), ('Dave', 23), ('Ed', 11),
               ('Fung', 25), ('Goel', 3), ('Harry', 17), ('Irene', 14), ('Joanna', 2),
               ('Kelly', 6), ('Lim', 20), ('Meng', 1), ('Noor', 5), ('Omar', 19)]

    table_s = [('Arts', 8), ('Business', 15), ('CompSc', 2), ('Dance', 12), ('Engineering', 7),
               ('Finance', 21), ('Geology', 10), ('Health', 11), ('IT', 18)]

    print(nest_loop_join(table_r,table_s))