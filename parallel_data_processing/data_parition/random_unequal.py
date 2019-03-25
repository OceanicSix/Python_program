import random
def ran_unequal(data,processor_num):
    result=[]
    for i in range(processor_num):
        result.append([])

    for record in data:
        random_index=random.randint(0,processor_num-1)
        result[random_index].append(record)

    return result

if __name__ == '__main__':
    D = [55, 30, 68, 39, 1,
         4, 49, 90, 34, 76,
         82, 56, 31, 25, 78,
         56, 38, 32, 88, 9,
         44, 98, 11, 70, 66,
         89, 99, 22, 23, 26]
    print(ran_unequal(D, 3))