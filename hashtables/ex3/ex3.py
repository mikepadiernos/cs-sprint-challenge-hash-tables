def intersection(arrays):
    # print(arrays)
    cache = {}
    result = []

    # loop through the arrays
    for array in arrays:
        # print(array)

        # loop through an individual array for integers
        for integer in array:

            # determine if an integer is in the cache
            if integer in cache:
                cache[integer] += 1
            else:
                cache[integer] = 1

    # loop through the cache for the integers
    for i in list(cache.items()):
        # determine if an item is equal to the length of the array
        if i[1] == len(arrays):
            # append the item to the result
            result.append(i[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
