def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    # loop through i as index in the array
    # using the value of length
    for i in range(length):
        # see if an index is in the dict
        if weights[i] not in cache:
            # add limit minus weight to the dict as the key
            # with the index as value
            cache[limit - weights[i]] = i
        else:
            # arrange the indexes where it returns
            # the higher number
            if cache[weights[i]] > i:
                return cache[weights[i]], i
            else:
                return i, cache[weights[i]]

    return None
