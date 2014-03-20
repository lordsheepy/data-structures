
def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    left, right = [], []
    middle = len(unsorted) // 2

    for i in unsorted[:middle]:
        left.append(i)
    for i in unsorted[middle:]:
        right.append(i)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif left:
            result.extend(left)
            left = []
        elif right:
            result.extend(right)
            right = []
    return result


if __name__ == '__main__':
    best_case, worst_case = [], []
    for i in xrange(65336):
        best_case.append(i)
        worst_case.append((32768 + i * 32768 + (i / 2)) % 65336)
    import time
    t1 = time.time()
    merge_sort(best_case)
    t2 = time.time()
    print "Best case: %f seconds" % (t2 - t1)
    t3 = time.time()
    merge_sort(worst_case)
    t4 = time.time()
    print "Worst case: %f seconds" % (t4 - t3)
