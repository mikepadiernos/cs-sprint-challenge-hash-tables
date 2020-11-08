def get_indices_of_item_weights(weights, length, limit):
    # print(weights, length, limit)
    cache = {}
    # loop through the array to get the indices using length
    for i in range(length):
        # print(i)
        # see if an index is in cache
        if weights[i] not in cache:
            # get the key by subtracting the weights index from the limit
            # and use the index as value
            cache[limit - weights[i]] = i
            # print(cache)
        else:
            # arrange the indexes where the higher to lower keys are visible
            # otherwise, arrange by the indices
            if cache[weights[i]] > i:
                return cache[weights[i]], i
            else:
                return i, cache[weights[i]]
        print(i)

    return None
