def recursive_addition(number):
    if number==1:
        return 1
    else:
        return recursive_addition(number-1)+number

print(recursive_addition(4))


def recursive_multiplication(n,i):
    if n==i:
        return i
    else:
        return recursive_multiplication(n-1,i)*n


print(recursive_multiplication(5,2))