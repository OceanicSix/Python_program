def recursive_addition(number):
    if number==1:
        return 1
    else:
        return recursive_addition(number-1)+number

print(recursive_addition(4))