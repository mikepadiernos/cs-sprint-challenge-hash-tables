def has_negatives(a):
    # print(a)
    cache = {}
    result = []

    # loop through a for the numbers
    for n in a:
        # determine the negative values
        negative = 0 - n
        # print(diff)

        # determine if the negative values are in cache
        if negative in cache:
            # print(abs(negative))
            # append the negatives as positives to result list
            result.append(abs(negative))
        else:
            # otherwise, leave the positives in the cache
            cache[n] = n
    # print(cache)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
