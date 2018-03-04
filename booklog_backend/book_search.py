import heapq
import numpy

class SearchDevice:
    def __init__(self, connections, read):
        self.connections = connections
        self.read = read

    def has_read(self, book):
        return (book in read)

    def get_connections(self, book):
        return self.connections[book]

    def search(self, count = 2):
        massive_heap = []
        arr = numpy.full(len(connections), False)

        for c in self.read:
            heapq.heappush(massive_heap, (-1, c))
            arr[c] = True

        books = []

        while len(books) < count and len(massive_heap) > 0:
            q = heapq.heappop(massive_heap)
            if q[0] > -1:
                books.append((-q[0], q[1]))

            for c in self.get_connections(q[1]):
                if not arr[c[0]]:
                    worth = q[0] * c[1]
                    heapq.heappush(massive_heap, (worth, c[0]))
                    arr[c[0]] = True

        return books

if __name__ == "__main__":
    connections = [[(2, 0.9), (3, 0.2)],  # 0
                   [(2, 0.3), (4, 0.5)],  # 1
                   [(0, 0.9), (1, 0.3), (5, 0.8)],  # 2
                   [(0, 0.2)],  # 3
                   [(1, 0.5)],  # 4
                   [(2, 0.8)]]  # 5

    # Make sure connections are good
    for i, l in enumerate(connections):
        for i_l, k in enumerate(l):
            happy = False
            for p in connections[k[0]]:
                if p[0] == i and p[1] == k[1]:
                    happy = True
                    break
            if not happy:
                raise AssertionError("Tree is fake news at %s, %s" % (i, i_l))

    read = [0, 1]

    device = SearchDevice(connections, read)

    print device.search(3)