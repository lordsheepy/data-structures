#!usr/bin/env python


def insertion_sort(unsort):

    for i in range(len(unsort)):
        # import pdb; pdb.set_trace()
        current = unsort[i]
        itercount = i
        while current < unsort[itercount - 1] and itercount > 0:
            unsort[itercount] = unsort[itercount - 1]
            itercount -= 1
        unsort[itercount] = current
    return unsort


if __name__ == '__main__':
    best_case, worst_case = [], []
    for i in xrange(16384):
        best_case.append(i)
        worst_case.append(16383 - i)
    import time
    t1 = time.time()
    insertion_sort(best_case)
    t2 = time.time()
    print "Best case: %f seconds" % (t2 - t1)
    t3 = time.time()
    insertion_sort(worst_case)
    t4 = time.time()
    print "Worst case: %f seconds" % (t4 - t3)
