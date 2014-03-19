#!usr/bin/env python


def insertion_sort(unsort):
    # if len(unsort) <= 1:
    #     return unsort
    # sort = []
    # sort.append(unsort.pop(0))
    # for i in range(len(unsort)-1):
    #     current = unsort.pop([i])
    #     for i in range(len(unsort)-1):
    #         if current <= i:
    #             sort.insert(i, current)
    #             break

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
    pass
