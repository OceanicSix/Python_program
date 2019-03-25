def linear_search(data, target):


    matched_record = None
    position = -1  # not found position


    for record in data:
        if record == target:  # If x is matched with key
            matched_record = record
            position = data.index(record)  # Get the index of x
            return position, matched_record


    return position, matched_record

if __name__ == '__main__':
    D = [55, 30, 68, 39, 1,
         4, 49, 90, 34, 76,
         82, 56, 31, 25, 78,
         56, 38, 32, 88, 9,
         44, 98, 11, 70, 66,
         89, 99, 22, 23, 26]
    print(linear_search(D,30))