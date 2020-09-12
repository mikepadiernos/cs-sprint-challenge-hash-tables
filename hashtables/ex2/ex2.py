#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    cache = {}

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # list for route
    route = [cache["NONE"]]

    while route[-1] != "NONE":
        route.append(cache[route[-1]])

    return route
