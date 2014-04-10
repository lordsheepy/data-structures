from math import log, floor


def radix_sort(unsorted, base):
    result = unsorted
    if not result:
        return []

    length = int(floor(log(abs(max(unsorted)), base))) + 1
    mini = int(floor(log(abs(min(unsorted)), base))) + 1
    if mini > length:
        length = mini

    for i in xrange(1, length + 1):
        buckets = [[] for x in range(base)]
        for j in result:
            digit = j % (base ** i) // (base ** (i-1))
            buckets[digit].append(j)
        result = [item for bucket in buckets for item in bucket]

    if min(result) < 0:
        buckets = [[], []]
        for j in result:
            if j <= 0:
                buckets[0].append(j)
            else:
                buckets[1].append(j)
        result = [item for bucket in buckets for item in bucket]
    return result
