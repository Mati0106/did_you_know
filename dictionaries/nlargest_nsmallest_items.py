"""
1.4 finding the largest or smallest n items

"""
import heapq

nums = [1, 6, 8, 23, 24, -1, 2 - 3]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 25},
    {'name': 'IBM', 'shares': 100, 'price': 235},
    {'name': 'AA', 'shares': 50, 'price': 225},
    {'name': 'IBM', 'shares': 400, 'price': 215},
    {'name': 'AA', 'shares': 30, 'price': 205},
    {'name': 'IBM', 'shares': 20, 'price': 15},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda x: x['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda x: x['price'])

### Implementing a Priority Queue

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 3)
q.push(Item('grok'), 4)

q.pop()

# Mapping Keys to Multiple Values in Dictionary
from collections import defaultdict

# list
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(1)
d['c'].append(1)
d['b'].append(2)
d['b'].append(1)

for key in d:
    print(key, d[key])
# set
s = defaultdict(set)
s['a'].add(1)
s['a'].add(2)
s['a'].add(1)

# Ordered dic

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 3
d['spam'] = 2
d['grok'] = 4

for key in d:
    print(key, d[key])

# min/max for dictionaries

prices = {
    'XX': 45,
    'YY': 23,
    'ZZ': 1,
    'KK': 46,
    'HF': 25
}

min_value, min_key = min(zip(prices.values(), prices.keys()))
max_value, max_key = max(zip(prices.values(), prices.keys()))

sorted(zip(prices.values(), prices.keys()))

# to get key corespond to min value
min(prices, key=lambda x: prices[x])


# 1.09 Common keys/values
a = {'z':10, 'y':20, 'h':30}
b = {'z':10, 'w':11, 'h':25}

# and
a.keys() & b.keys()

# a - b
a.keys() - b.keys()

# common items
a.items() & b.items()


# 1.10 Removing duplicates from a sequence
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a))