from collections.abc import Set


def isArrayUnique(array):
    print(len(set(array)))

    return len(set(array)) == len(array)


print(isArrayUnique([3, 3,4,5]))