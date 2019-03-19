import random
def ran_int(start_value,end_value):
    length=end_value-start_value+1
    value_list=range(start_value,end_value+1)
    ran_number=random.random()
    #devide value 1 into $length part, e.g devide 1 into 10 part, if the 0/10=<ran_number<=
    #1/10, then return the first value in the value_list.
    for i in range(0,length):
        if ran_number>=i/length and ran_number<(i+1)/length:
            return value_list[i]


if __name__ == '__main__':
    for i in range(20):
        b=ran_int(14,21)
        print(b)

