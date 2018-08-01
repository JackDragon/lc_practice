// register
book
purchase
// get
best
sellers

from collections import defaultdict


class Store:
    def __init__(self):
        self.book_purchases = defaultdict(int)
        self.bestsellers = None  # top 10 bestselling books in it

    def buyBook(self, id):
        self.book_purchases[id] += 1
        self.bestsellers = sorted(self.book_purchases.items(), key=lambda (k, v): v)

    def getBestsellers(self, n):
        return self.bestsellers[:n]


class Store:
    def __init__(self):
        self.book_purchases = {}
        self.bestsellers = PriorityQueue()

    def buyBook(self, id):
        if id in self.book_purchases:
            self.bestsellers.remove((self.book_purchases[id], id))
            self.book_purchases[id] += 1
            self.bestsellers.add((self.book_purchsases[id], id))
        else:
            self.book_purchases[id] = 1
            self.bestsellers.add((self.book_purchsases[id], id))

    def getBestsellers(self, n):
        return self.


class Store:
    def __init__(self):
        self.book_purchases = {}
        self.bestsellers = PriorityQueue()

    def buyBook(self, id):
        if id in self.book_purchases:
            self.book_purchases[id] += 1
        else:
            self.book_purchases[id] = 1
        if len(self.bestsellers) < 10:
            # we add to it
            self.bestsellers.add((self.book_purchases[id], id))
        else:
            least = self.bestsellers.pop()
            # (times bought, id)
            if self.bestsellers[id] > least[0]:
                self.bestsellers.add((self.book_purchases[id], id))
            else:
                self.bestsellers.add(least)

    def getBestsellers(self, n):
        n_smallest = [self.bestsellers.pop() for _ in n]