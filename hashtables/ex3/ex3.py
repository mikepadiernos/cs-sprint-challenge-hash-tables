def intersection(arrays):

    cache = {}
    result = []

    # list out array in arrays
    for array in arrays:

        # list out integers in array
        for integer in array:
            # find out if an integer is in cache
            if integer not in cache:
                cache[integer] = 1
            # increment if integer is in cache
            else:
                cache[integer] += 1

    length = len(arrays)

    # loop over cache
    for item in list(cache.items()):
        # see if value is equal length of the array
        if item[1] == length:
            # add each item into list
            result.append(item[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
