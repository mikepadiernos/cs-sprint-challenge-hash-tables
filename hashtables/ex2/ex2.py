#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # print(tickets, length)
    cache = {}

    # loop through the tickets
    # then cache the source as key and destination as value
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
        # print(cache[ticket.source])
        # print(cache)

    # list out the cache as route
    # starting with the key / value of NONE / LAX
    route = [cache["NONE"]]
    # print(route)

    # return the values that do not have the "NONE" as source
    # then add them to the cache
    while route[-1] != "NONE":
        # print(route[-1])
        route.append(cache[route[-1]])
    # print(route)

    return route
